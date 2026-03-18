import streamlit as st
from fluxo import gerenciar_fluxo  # Aqui está a mágica!


st.set_page_config(page_title="ACN Personalizados", page_icon="avatar.png")

st.title("🚀 Chatbot ACN Personalizados")

# --- 1. PRIMEIRO: Inicializa (Cria a gaveta) ---
if "mensagens" not in st.session_state:
    # Começamos com a primeira mensagem da bonequinha
    st.session_state.mensagens = [{"role": "assistant", "content": "Olá! Sou a assistente da ACN Personalizados. Qual seu nome?"}]

# --- 2. DEPOIS: Exibe (Abre a gaveta) ---
for mensagem in st.session_state.mensagens:
    avatar_atual = "avatar.png" if mensagem["role"] == "assistant" else None
    with st.chat_message(mensagem["role"], avatar=avatar_atual):
        st.markdown(mensagem["content"])


# 2. Entrada do usuário
if pronto := st.chat_input("Como posso ajudar?"):
    st.session_state.mensagens.append({"role": "user", "content": pronto})
    with st.chat_message("user"):
        st.markdown(pronto)

    # Chamada do seu arquivo auxiliar
    resposta_bot = gerenciar_fluxo(pronto, "5521966420939")
    
    # 3. Resposta do robô usando a bonequinha como avatar
    with st.chat_message("assistant", avatar="avatar.png"):
        st.write(resposta_bot)
        if st.session_state.get("passo") == 4:
            st.link_button("🟢 Finalizar no WhatsApp", st.session_state.link_whatsapp)
            
    st.session_state.mensagens.append({"role": "assistant", "content": resposta_bot})




        




    