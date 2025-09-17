import os
from graphviz import Digraph

def fluxograma_baixa():
    # Garantir que a pasta existe
    output_dir = "img/alienacao"
    os.makedirs(output_dir, exist_ok=True)

    # Criar o fluxograma
    fluxo = Digraph("Fluxograma", format="png")
    fluxo.attr(rankdir="TB", size="8")

    # Nós
    fluxo.node("A", "Unidade Patrimonial\npreenche planilha do MCom\ne anexa ao processo", shape="box", style="rounded,filled", fillcolor="lightblue")
    fluxo.node("B", "Núcleo de Tecnologia\nanalisa interesse em manter\nmateriais no acervo", shape="box", style="rounded,filled", fillcolor="lightgreen")
    fluxo.node("C", "Materiais com HD ou memória:\nabertura de chamado para\nlimpeza de dados", shape="box", style="rounded,filled", fillcolor="lightyellow")
    fluxo.node("D", "Comissão classifica os bens\n(Decreto 9.373/2018)", shape="box", style="rounded,filled", fillcolor="orange")
    fluxo.node("E", "Recolhimento dos\nmateriais inservíveis", shape="box", style="rounded,filled", fillcolor="lightcoral")

    # Conexões
    fluxo.edge("A", "B")
    fluxo.edge("B", "C")
    fluxo.edge("C", "D")
    fluxo.edge("D", "E")

    # Caminho do arquivo de saída
    output_path = os.path.join(output_dir, "fluxograma_baixa")
    
    # Renderizar (gera fluxograma_baixa.png)
    fluxo.render(output_path, cleanup=True)

    print(f"Fluxograma gerado em: {output_path}.png")

# Executar
fluxograma_baixa()
