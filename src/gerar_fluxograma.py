import re
import textwrap
from typing import List, Dict, Optional
from graphviz import Digraph
import streamlit as st

# Helpers: extração simples de passos e sumarização heurística
def _extract_steps_from_md(md_text: str, max_steps: int = 20, max_words: int = 8) -> List[Dict]:
    """Extrai elementos do Markdown como passos com metadados.

    Retorna uma lista de dicionários com chaves: 'text', 'kind' ('heading'|'list'|'paragraph') e
    'level' (int para headings, None caso contrário).
    """
    lines = md_text.splitlines()
    steps: List[Dict] = []
    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue
        m = re.match(r'^(#{1,6})\s+(.*)', line.strip())
        if m:
            steps.append({
                'text': m.group(2).strip(),
                'kind': 'heading',
                'level': len(m.group(1))
            })
            continue
        m = re.match(r'^(?:- |\* |\d+\.\s+)(.*)', line.strip())
        if m:
            steps.append({
                'text': m.group(1).strip(),
                'kind': 'list',
                'level': None
            })
            continue

    # Se não achou nada estruturado, tratar parágrafos como passos
    if not steps:
        paras = [p.strip() for p in md_text.split('\n\n') if p.strip()]
        for p in paras:
            steps.append({'text': p, 'kind': 'paragraph', 'level': None})

    # Limita e encurta o texto armazenado
    for s in steps:
        s['text'] = textwrap.shorten(s['text'], width=300, placeholder='...')

    return steps[:max_steps]


def _summarize_text(text: str, max_words: int = 8) -> str:
    """Gera rótulo curto para nós usando heurística simples.

    (Transformers pode ser integrado se você quiser sumarização mais potente.)
    """
    text = text.strip()
    if not text:
        return ""
    first_sentence = re.split(r'(?<=[.!?])\s+', text)[0]
    words = first_sentence.split()
    if len(words) <= max_words:
        return first_sentence
    return " ".join(words[:max_words]) + "..."


def criar_fluxograma(
    md_text: str,
    horizontal: bool = False,
    max_nodes: int = 20,
    max_words: int = 8,
    color_map: Optional[Dict[int, str]] = None,
    shape_map: Optional[Dict[str, str]] = None,
) -> Digraph:
    """Cria um graphviz.Digraph a partir do Markdown fornecido.

    - Extrai passos/headings/listas do Markdown
    - Gera rótulos curtos para nós
    - Coloca o texto completo em `tooltip` (útil em SVG)
    """
    steps = _extract_steps_from_md(md_text, max_steps=max_nodes, max_words=max_words)

    # valores padrão para cores e formas
    # Uso de cores hex mais perceptíveis para evitar aparência "branca" em alguns renderizadores
    default_color = "#cfe8ff"  # tom suave de azul
    if color_map is None:
        color_map = {1: "#a6d2ff", 2: "#b7f0c6", 3: "#fff3b0"}
    # Evitar 'note' como padrão (alguns renderizadores mostram fundo branco); usar 'box' por padrão
    if shape_map is None:
        shape_map = {"heading": "box", "list": "box", "paragraph": "ellipse"}

    dot = Digraph("fluxograma")
    dot.attr(rankdir=("LR" if horizontal else "TB"), splines="ortho")

    prev_id = None
    for i, step in enumerate(steps):
        node_id = f"n{i}"
        full_text = step['text']
        kind = step.get('kind', 'paragraph')
        level = step.get('level')

        short = _summarize_text(full_text, max_words=max_words)
        label = short.replace('"', "'")

        # cor por nível de heading — cai para default se não houver mapeamento
        fillcolor = default_color
        if kind == 'heading' and isinstance(level, int):
            fillcolor = color_map.get(level, default_color)
        elif kind in shape_map:
            # para outros tipos, podemos permitir cores específicas por tipo no futuro
            fillcolor = default_color

        shape = shape_map.get(kind, 'box')

        # Forçar cor da borda e da fonte para realçar o preenchimento
        dot.node(
            node_id,
            label,
            shape=shape,
            style="rounded,filled",
            fillcolor=fillcolor,
            color="#333333",
            fontcolor="#111111",
            tooltip=full_text,
        )
        if prev_id is not None:
            dot.edge(prev_id, node_id)
        prev_id = node_id

    return dot

if __name__ == "__main__":
    sample_md = """
    # Introdução
    Este é um exemplo de documento Markdown.

    ## Passo 1
    Descrição do passo 1.

    ## Passo 2
    Descrição do passo 2.

    ## Passo 3
    Descrição do passo 3.
    """
    fluxograma = criar_fluxograma(sample_md)
    fluxograma.render("fluxograma", format="png", cleanup=True)