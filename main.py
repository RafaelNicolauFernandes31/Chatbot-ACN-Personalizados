import streamlit as st

# URL ou caminho da imagem da sua bonequinha
AVATAR_URL = "avatar.png" # Coloque o link da imagem aqui


st.title("🚀 Chatbot ACN Personalizados")

# 1. Exibe as mensagens do histórico com o avatar personalizado
for mensagem in st.session_state.mensagens:
    # Se a mensagem for do assistente, usa a imagem da bonequinha
    avatar_atual = "avatar.jpg" if mensagem["role"] == "assistant" else None
    
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
    with st.chat_message("assistant", avatar="avatar.jpg"):
        st.write(resposta_bot)
        if st.session_state.get("passo") == 4:
            st.link_button("🟢 Finalizar no WhatsApp", st.session_state.link_whatsapp)
            
    st.session_state.mensagens.append({"role": "assistant", "content": resposta_bot})




    
