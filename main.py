import streamlit as st
from fluxo import gerenciar_fluxo  # Aqui está a mágica!

#Customização do CSS
st.markdown("""
<style>
/* Esconde o rodapé 'Made with Streamlit' */
footer {visibility: hidden;}

/* Customiza a barra de entrada de texto */
.stChat Input textarea {

background-color: #ffffff !important; /* Cor de fundo branca*/
color: #333333 !important;  /*Cor de texto digitado*/
border: 1px solid #ddd !important; /*Borda sutil*/

/*Altera a cor do botão de enviar (setinha)*/

st.ChatInput button {
background-color: #FF4B4B !imnportant; /*Exemplo: Vermelho combinando com o foguete*/
color: white !important;
}
</style>
""",unsafe_allow_html=True)






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




        




    
