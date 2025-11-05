import re
import textwrap
from typing import List
from graphviz import Digraph


# Helpers: extração simples de passos e sumarização heurística
def _extract_steps_from_md(md_text: str, max_steps: int = 20) -> List[str]:
    """Extrai headings e itens de lista de um Markdown como passos.

    Simples e determinístico — suficiente para transformar roteiros em fluxograma.
    """
    lines = md_text.splitlines()
    steps: List[str] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            steps.append(m.group(2).strip())
            continue
        m = re.match(r'^(?:- |\* |\d+\.\s+)(.*)', line)
        if m:
            steps.append(m.group(1).strip())
            continue

    if not steps:
        paras = [p.strip() for p in md_text.split('\n\n') if p.strip()]
        steps = paras

    steps = [textwrap.shorten(s, width=300, placeholder='...') for s in steps]
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


def criar_fluxograma(md_text: str, horizontal: bool = False, max_nodes: int = 20) -> Digraph:
    """Cria um graphviz.Digraph a partir do Markdown fornecido.

    - Extrai passos/headings/listas do Markdown
    - Gera rótulos curtos para nós
    - Coloca o texto completo em `tooltip` (útil em SVG)
    """
    steps = _extract_steps_from_md(md_text, max_steps=max_nodes)

    dot = Digraph("fluxograma")
    dot.attr(rankdir=("LR" if horizontal else "TB"), splines="ortho")

    prev_id = None
    for i, step in enumerate(steps):
        node_id = f"n{i}"
        full_text = step
        short = _summarize_text(full_text, max_words=6)
        label = short.replace('"', "'")
        dot.node(node_id, label, shape="box", style="rounded,filled", fillcolor="lightgrey", tooltip=full_text)
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