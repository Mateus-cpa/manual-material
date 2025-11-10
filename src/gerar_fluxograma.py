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
        m = re.match(r'^(?:- |\* |(\d+)\.\s+)(.*)', line.strip())
        if m:
            ordered = bool(m.group(1))
            steps.append({
                'text': m.group(2).strip(),
                'kind': 'list',
                'level': None,
                'ordered': ordered,
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
    max_nodes: int = 30,
    max_words: int = 8,
    color_map: Optional[Dict[int, str]] = None,
    shape_map: Optional[Dict[str, str]] = None,
    show_side_nodes: bool = False,  # controla exibição das ramificações laterais
) -> Digraph:
    """Cria um graphviz.Digraph a partir do Markdown fornecido.

    - Extrai passos/headings/listas do Markdown
    - Gera rótulos curtos para nós
    - Coloca o texto completo em `tooltip` (útil em SVG)
    """
    steps = _extract_steps_from_md(md_text, max_steps=max_nodes, max_words=max_words)

    # Sequência de 10 cores padrão para cada Heading2 e seus subordinados
    default_group_colors = [
        "#bd6262", "#fab731", "#fbd80f", "#75ee35", "#57bcf3",
        "#5a60f8", "#c158fa", "#fe56b2", "#fa5579", "#ff2323",
    ]
    default_color = "#f0f0f0"
    # color_map pode ser fornecido por índice (1-based) para cada Heading2
    if color_map is None:
        color_map = {i + 1: c for i, c in enumerate(default_group_colors)}

    # Formas padrão: heading2 -> box, heading3 -> box (legível), lateral -> ellipse
    if shape_map is None:
        shape_map = {"h2": "box", "h3": "ellipse", "lateral": "parallelogram"}

    dot = Digraph("fluxograma")
    dot.attr(
        rankdir=("LR" if horizontal else "TB"),
        splines="ortho",
        nodesep="0.2",  # reduz espaço entre nós no mesmo rank
        ranksep="0.3",  # reduz espaço entre ranks diferentes
    )

    prev_main_id = None
    group_index = 0
    last_main_id = None

    # procurar título (first H1) e removê-lo do fluxo principal
    title = None
    for s in steps:
        if s.get('kind') == 'heading' and s.get('level') == 1:
            title = s['text']
            break
    if title:
        dot.attr(label=title, 
                 labelloc='t', 
                 fontsize='18', 
                 fontcolor="#0D05F3",
                 fontname='Helvetica-Bold')

    # construir nós: H2 e H3 no fluxo principal; H4 e listas como laterais; ignorar parágrafos
    for i, step in enumerate(steps):
        kind = step.get('kind')
        level = step.get('level')
        full_text = step['text']

        # pular H1 e parágrafos simples
        if kind == 'heading' and level == 1:
            continue
        if kind == 'paragraph':
            continue

        node_id = f"n{i}"
        short = _summarize_text(full_text, max_words=max_words)
        label = short.replace('"', "'")

        # Lógica de cor/grupo: quando encontramos H2, incrementamos o índice de grupo
        if kind == 'heading' and level == 2:
            group_index += 1
            group_color = color_map.get(group_index, default_color)
            shape = shape_map.get('h2', 'box')
            fillcolor = group_color
            # criar nó principal H2
            dot.node(node_id, label, shape=shape, style="rounded,filled", fillcolor=fillcolor, color="#333333", fontcolor="#111111", tooltip=full_text)
            # conectar no fluxo principal
            if last_main_id is not None:
                dot.edge(last_main_id, node_id)
            last_main_id = node_id

        elif kind == 'heading' and level == 3:
            # H3 participa do fluxo principal — usar shape configurável (padrão: box) e ajustar fonte/margem
            shape = shape_map.get('h3', 'box')
            fillcolor = color_map.get(group_index, default_color)
            dot.node(
                node_id,
                label,
                shape=shape,
                style="rounded,filled",
                fillcolor=fillcolor,
                color="#333333",
                fontcolor="#111111",
                fontsize='11',
                margin='0.08,0.05',
                tooltip=full_text,
            )
            if last_main_id is not None:
                dot.edge(last_main_id, node_id)
            last_main_id = node_id

        elif show_side_nodes and ((kind == 'heading' and level == 4) or (kind == 'list' and step.get('ordered'))):
            # H4 e itens numerados -> ramificação lateral, só mostrado se show_side_nodes=True
            shape = shape_map.get('lateral', 'ellipse')
            fillcolor = "#f7f7f7"
            
            # Criar nó lateral de forma simples, sem subgraph ou grupos
            dot.node(node_id, label,
                shape=shape,
                style="rounded,filled",
                fillcolor=fillcolor,
                color="#333333",
                fontcolor="#111111",
                tooltip=full_text,
                margin='0.02',  # margem reduzida
            )
            
            if last_main_id is not None:
                # Aresta lateral simples, sem tentar forçar alinhamento
                dot.edge(last_main_id, node_id,
                    constraint='false',
                    minlen='0.5',
                    weight='1'
                )

        else:
            # outros tipos (por exemplo: unordered lists) — atualmente ignorados ou tratados como laterais
            # aqui optamos por ignorar unordered lists e parágrafos
            continue

    return dot

if __name__ == "__main__":
    sample_md = """
    # Manual de Procedimentos
    Exemplo de documento com estrutura sugerida.

    ## Processo Principal
    Visão geral do processo.

    ### Etapa 1
    Detalhamento da primeira etapa.

    #### Observação importante
    Detalhe que deve aparecer como ramificação.

    1. Passo detalhado
    2. Outro passo importante

    ### Etapa 2
    Detalhamento da segunda etapa.

    ## Processo Secundário
    Outro processo relacionado.

    ### Etapa Final
    Conclusão do processo.
    """
    
    # Exemplo básico - sem ramificações laterais (padrão)
    fluxograma = criar_fluxograma(sample_md)
    fluxograma.render("fluxograma_simples", format="png", cleanup=True)
    
    # Exemplo com ramificações laterais ativadas
    fluxograma_completo = criar_fluxograma(
        sample_md,
        show_side_nodes=True,  # mostra H4 e listas numeradas
        horizontal=True,       # layout horizontal (opcional)
    )
    fluxograma_completo.render("fluxograma_completo", format="png", cleanup=True)