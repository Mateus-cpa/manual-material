import re
import matplotlib.pyplot as plt
import networkx as nx
from anytree import Node


def wrap_label(texto, largura=25):
    """Quebra o texto em várias linhas para caber melhor no nó."""
    palavras = texto.split()
    linhas, atual = [], []
    tamanho = 0
    for p in palavras:
        if tamanho + len(p) + 1 > largura:
            linhas.append(" ".join(atual))
            atual = [p]
            tamanho = len(p)
        else:
            atual.append(p)
            tamanho += len(p) + 1
    if atual:
        linhas.append(" ".join(atual))
    return "\n".join(linhas)


def parse_listagem(texto):
    """
    Converte a listagem numerada em uma árvore de nós.
    Cada linha precisa começar com 1., 1.1., 1.1.2. etc.
    """
    linhas = texto.strip().splitlines()
    raiz = None
    nos = {}

    for linha in linhas:
        if not linha.strip():
            continue

        # separa índice (1.1.2) do restante
        match = re.match(r"^([\d\.]+)\s+(.*)$", linha.strip())
        if not match:
            continue

        indice, conteudo = match.groups()
        conteudo = conteudo.strip()

        # nó pai = remover o último nível da numeração
        niveis = indice.strip(".").split(".")
        chave = ".".join(niveis)

        # monta label com quebra de linha automática
        label = wrap_label(conteudo, largura=25)

        # cria nó
        if len(niveis) == 1:
            nos[chave] = Node(label)
            raiz = nos[chave]
        else:
            pai_chave = ".".join(niveis[:-1])
            nos[chave] = Node(label, parent=nos[pai_chave])

    return raiz


def desenhar_arvore_por_nivel(root, output="img/organograma.png"):
    edges = []
    nodes = {}
    levels = {}

    def traverse(node, level=0):
        nodes[node] = str(node.name)
        levels.setdefault(level, []).append(node)
        for child in node.children:
            edges.append((node, child))
            traverse(child, level + 1)

    traverse(root)

    G = nx.DiGraph()
    for n in nodes:
        G.add_node(n, label=nodes[n])
    G.add_edges_from(edges)

    # posição dos nós: distribuídos por nível (y = nível, x = índice no nível)
    pos = {}
    for level, ns in levels.items():
        step = 0.15  # <-- diminui espaço horizontal
        offset = -(len(ns) - 1) * step / 2
        for i, n in enumerate(ns):
            pos[n] = (offset + i * step, -level * 0.5)  # <-- diminui espaço vertical

    plt.figure(figsize=(30, 20))
    nx.draw(
        G,
        pos,
        with_labels=True,
        labels=nx.get_node_attributes(G, "label"),
        node_size=8000,
        node_color="lightblue",
        font_size=6,
        font_weight="bold",
        edge_color="gray",
        node_shape="s",  # <-- quadrados
    )

    plt.tight_layout()
    plt.savefig(output, dpi=300)
    plt.close()
    print(f"✅ Organograma em camadas gerado em {output}")


if __name__ == "__main__":
    with open("raw/unidades_pr.txt", encoding="utf-8") as f:
        texto = f.read()

    raiz = parse_listagem(texto)
    desenhar_arvore_por_nivel(raiz, output="img/organograma.png")
