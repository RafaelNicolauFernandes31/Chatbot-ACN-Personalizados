import streamlit as st
from fluxo import gerenciar_fluxo
import os

# --- 1. CONFIGURAÇÃO DA PÁGINA (ÍCONE NA ABA DO NAVEGADOR) ---
# O 'page_icon' usa o arquivo da bonequinha
st.set_page_config(
    page_title="ACN Personalizados - Chatbot", 
    page_icon="avatar.png", 
    layout="centered"
)

# --- 2. VALIDAÇÃO DO AVATAR ---
# Verifica se o arquivo existe para não dar erro no deploy
AVATAR_PATH = "avatar.png"
if not os.path.exists(AVATAR_PATH):
    # Se a imagem sumir, ele usa um ícone padrão de robô
    AVATAR_PATH = "assistant" 

# --- 3. LIMPEZA DE INTERFACE (REMOVE MENUS E BOTÕES) ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Chatbot ACN Personalizados")

# --- 4. INICIALIZAÇÃO DO HISTÓRICO (EVITA ERRO DE ATRIBUTO) ---
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"role": "assistant", "content": "Olá! Sou a assistente da ACN Personalizados. Qual seu nome?"}
    ]

# --- 5. EXIBIÇÃO DO HISTÓRICO ---
for mensagem in st.session_state.mensagens:
    # Define se usa a bonequinha ou o ícone de usuário
    avatar_atual = AVATAR_PATH if mensagem["role"] == "assistant" else None
    
    with st.chat_message(mensagem["role"], avatar=avatar_atual):
        st.markdown(mensagem["content"])

# --- 6. INTERAÇÃO DO USUÁRIO ---
if pronto := st.chat_input("Como posso ajudar?"):
    # Adiciona fala do usuário
    st.session_state.mensagens.append({"role": "user", "content": pronto})
    with st.chat_message("user"):
        st.markdown(pronto)

    # Chamada da lógica do seu chatbot
    resposta_bot = gerenciar_fluxo(pronto, "5521966420939")
    
    # Exibe resposta do robô com o avatar validado
    with st.chat_message("assistant", avatar=AVATAR_PATH):
        st.write(resposta_bot)
        if st.session_state.get("passo") == 4:
            st.link_button("🟢 Finalizar no WhatsApp", st.session_state.link_whatsapp)
            
    # Salva no histórico
    st.session_state.mensagens.append({"role": "assistant", "content": resposta_bot})
    
