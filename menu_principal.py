"""streamlit_markmap.py
Streamlit app que mostra arquivos Markdown da pasta raiz e roteiros/ 
e transforma em fluxograma em imagem.

Uso:
  poetry run streamlit run menu_principal.py

Features:
- lista todos os arquivos .md da pasta conteudo/
- mostra o conteúdo original do arquivo selecionado
- converte e exibe como mapa mental interativo
- permite baixar o mapa mental como HTML standalone
"""
import html
import os
import glob

#bibliotecas importadas
#import streamlit.components.v1 as components
import streamlit as st
import graphviz

#bibliotecas locais
from src.gerar_fluxograma import criar_fluxograma as fluxograma

ST_REPO_CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "roteiros")


def list_local_root_md_files():
    pattern = os.path.join(os.path.dirname(os.path.abspath(__file__)), "*.md")
    return sorted(glob.glob(pattern))

def list_local_md_files():
    if not os.path.exists(ST_REPO_CONTENT_DIR):
        return []
    pattern = os.path.join(ST_REPO_CONTENT_DIR, "**", "*.md")
    return sorted(glob.glob(pattern, recursive=True))

def read_md_from_path(filepath: str) -> str:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        st.error(f"Erro ao ler {filepath}: {e}")
        return ""

    
# -- FUNÇÃO PRINCIPAL --
def main():
    st.set_page_config(page_title="Material de Estudos", layout="wide")
    st.title("📚 Manuais de execução patrimonial")

    # Lista de arquivos .md disponíveis
    local_root_md_files = list_local_root_md_files()
    local_files = list_local_md_files()
    local_files = local_root_md_files + local_files
    
    if not local_files:
        st.error("Nenhum arquivo .md encontrado na pasta `roteiros/`")
        return

    # Seleção do arquivo na barra lateral
    with st.sidebar:
        
        st.markdown("### Seleção de roteiros")

        selected_file_roteiro = st.selectbox(
            "Selecione um roteiro:",
            options=local_files,
            index=0,
            format_func=lambda x: os.path.splitext(os.path.basename(x))[0].replace('_', ' ').title()
        )

        st.markdown("### Configurações do Fluxograma")
        orientation = st.checkbox("Orientação Horizontal", value=False)
        nos_maximos = st.slider("Número máximo de nós", 
                                min_value=4, 
                                max_value=20, 
                                value=10, 
                                step=1,
                                key="max_nodes_slider")
        max_words = st.slider("Número máximo de palavras no rótulo", 
                              min_value=3, 
                              max_value=15, 
                              value=8, 
                              step=1, 
                              key="label_word_limit")
        
        st.markdown("---")
        st.markdown("### Sobre")
        st.markdown("Este app converte arquivos Markdown da pasta `roteiros/`.")

    # Carregar e exibir o conteúdo do arquivo selecionado
    if selected_file_roteiro == 'Selecione um arquivo':
        st.info("Por favor, selecione um arquivo na barra lateral.")
        # Mostrar Readme como introdução
        readme_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")
        readme_text = read_md_from_path(readme_path)
        st.markdown(readme_text)
        return
    filepath = os.path.abspath(selected_file_roteiro)
    md_text = read_md_from_path(filepath)
    
    if md_text:
        # Exibir o conteúdo original do Markdown
        st.markdown("### Conteúdo Original")
        with st.expander("Ver conteúdo Markdown", expanded=True):
            st.markdown(md_text)
        st.markdown('### Fluxograma')
        
        
        imagem_fluxograma = fluxograma(md_text, horizontal=orientation, 
                                       max_nodes=nos_maximos, 
                                       max_words=max_words)
        st.graphviz_chart(imagem_fluxograma)

        st.download_button(
           label="Baixar Fluxograma",
           data=imagem_fluxograma.source,
           file_name=f"{selected_file_roteiro}.png",
           mime="image/png")
        

if __name__ == "__main__":
    main()