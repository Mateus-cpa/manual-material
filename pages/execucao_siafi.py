import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
import os
from pathlib import Path

# Configuração inicial do Streamlit
st.set_page_config(
    page_title="Execução SIAFI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuração do tema
if 'tema_escuro' not in st.session_state:
    st.session_state.tema_escuro = False

# Sidebar com configurações
with st.sidebar:
    st.title("Configurações")
    st.session_state.tema_escuro = st.toggle("Modo Escuro", st.session_state.tema_escuro)
    if st.session_state.tema_escuro:
        st.markdown("""
        <style>
        .stApp {
            background-color: #262730;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

st.title("Gerenciamento de Execução SIAFI")

# Configuração do banco de dados
DB_PATH = Path('data/execucao_siafi.db')

# Função para criar a tabela se não existir
def criar_tabela():
    os.makedirs(DB_PATH.parent, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS execucao_siafi
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                area TEXT,
                tipo_dh TEXT,
                situacao TEXT,
                descricao_situacao TEXT,
                atividade_material TEXT,
                conta_contabil TEXT,
                conta_corrente TEXT,
                obs_sei TEXT,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Criar a tabela ao iniciar o aplicativo
criar_tabela()

# Função para adicionar um novo registro
def adicionar_registro(area, tipo_dh, situacao, descricao_situacao, 
                      atividade_material, conta_contabil, conta_corrente, obs_sei):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO execucao_siafi 
                (area, tipo_dh, situacao, descricao_situacao, 
                atividade_material, conta_contabil, conta_corrente, obs_sei)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (area, tipo_dh, situacao, descricao_situacao,
                atividade_material, conta_contabil, conta_corrente, obs_sei))
    conn.commit()
    conn.close()

# Função para carregar todos os registros
def carregar_registros():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM execucao_siafi", conn)
    conn.close()
    return df

# Função para atualizar um registro
def atualizar_registro(id, area, tipo_dh, situacao, descricao_situacao,
                      atividade_material, conta_contabil, conta_corrente, obs_sei):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''UPDATE execucao_siafi
                SET area=?, tipo_dh=?, situacao=?, descricao_situacao=?,
                    atividade_material=?, conta_contabil=?, conta_corrente=?, obs_sei=?
                WHERE id=?''',
                (area, tipo_dh, situacao, descricao_situacao,
                atividade_material, conta_contabil, conta_corrente, obs_sei, id))
    conn.commit()
    conn.close()

# Função para excluir um registro
def excluir_registro(id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM execucao_siafi WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Interface do usuário
tab1, tab2 = st.tabs(["Visualizar/Editar", "Adicionar Novo"])

with tab1:
    # Carregar e exibir dados existentes
    st.subheader("Registros Existentes")
    df = carregar_registros()
    
    if not df.empty:
        # Adicionar filtros
        col1, col2, col3 = st.columns(3)
        with col1:
            area_filter = st.selectbox(
                "Filtrar por Área",
                options=["Todos"] + list(df['area'].unique())
            )
        with col2:
            tipo_dh_filter = st.selectbox(
                "Filtrar por Tipo DH",
                options=["Todos"] + list(df['tipo_dh'].unique())
            )
        with col3:
            situacao_filter = st.selectbox(
                "Filtrar por Situação",
                options=["Todos"] + list(df['situacao'].unique())
            )

        # Aplicar filtros
        df_filtered = df.copy()
        if area_filter != "Todos":
            df_filtered = df_filtered[df_filtered['area'] == area_filter]
        if tipo_dh_filter != "Todos":
            df_filtered = df_filtered[df_filtered['tipo_dh'] == tipo_dh_filter]
        if situacao_filter != "Todos":
            df_filtered = df_filtered[df_filtered['situacao'] == situacao_filter]

        # Opções de exportação
        col1, col2 = st.columns([1, 5])
        with col1:
            formato = st.selectbox(
                "Formato de Exportação",
                options=["Excel", "CSV"]
            )
            if st.button("Exportar"):
                if formato == "Excel":
                    df_filtered.to_excel("data/execucao_siafi_export.xlsx", index=False)
                    st.success("Dados exportados para Excel com sucesso!")
                else:
                    df_filtered.to_csv("data/execucao_siafi_export.csv", index=False)
                    st.success("Dados exportados para CSV com sucesso!")

        # Adicionar botões de edição e exclusão
        df_filtered['Ações'] = None
        edited_df = st.data_editor(
            df,
            column_config={
                "Ações": st.column_config.Column(
                    "Ações",
                    help="Editar ou excluir registro",
                    width="small",
                )
            },
            hide_index=True,
        )
        
        # Tratar edições
        if edited_df is not None:
            for index, row in edited_df.iterrows():
                # Verificar se houve alterações
                original_row = df.loc[index]
                if not row.equals(original_row):
                    if st.session_state.get(f'confirmar_edicao_{row["id"]}', False):
                        atualizar_registro(
                            row['id'], row['area'], row['tipo_dh'],
                            row['situacao'], row['descricao_situacao'],
                            row['atividade_material'], row['conta_contabil'],
                            row['conta_corrente'], row['obs_sei']
                        )
                        st.success('Registro atualizado com sucesso!')
                        st.rerun()
                    else:
                        st.warning(f"Confirmar edição do registro {row['id']}?")
                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button("Confirmar", key=f"confirm_edit_{row['id']}"):
                                st.session_state[f'confirmar_edicao_{row["id"]}'] = True
                                st.rerun()
                        with col2:
                            if st.button("Cancelar", key=f"cancel_edit_{row['id']}"):
                                st.rerun()

with tab2:
    st.subheader("Adicionar Novo Registro")
    with st.form("novo_registro"):
        col1, col2 = st.columns(2)
        
        with col1:
            area = st.text_input("Área")
            tipo_dh = st.text_input("Tipo DH")
            situacao = st.text_input("Situação")
            descricao_situacao = st.text_area("Descrição Situação")
            
        with col2:
            atividade_material = st.text_input("Atividade Material")
            conta_contabil = st.text_input("Conta Contábil")
            conta_corrente = st.text_input("Conta Corrente")
            obs_sei = st.text_area("Obs SEI")
        
        if st.form_submit_button("Adicionar"):
            if area and tipo_dh and situacao:  # Validação básica
                adicionar_registro(
                    area, tipo_dh, situacao, descricao_situacao,
                    atividade_material, conta_contabil, conta_corrente, obs_sei
                )
                st.success("Registro adicionado com sucesso!")
                st.rerun()
            else:
                st.error("Por favor, preencha pelo menos os campos: Área, Tipo DH e Situação")