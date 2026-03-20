import streamlit as st

# URL ou caminho da imagem da sua bonequinha
AVATAR_URL = "avatar.png" # Coloque o link da imagem aqui

PRODUTOS_VALIDOS = [
    "Topo de bolos","Kits festas", "Adesivos personalizados", "Cadernos personalizados", 
    "Materiais personalizados", "Chaveiros personalizados", "Toalhas personalizadas"
]

# Inicialização do estado
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"role": "assistant", "content": "Olá! Sou a assistente da ACN Personalizados. Qual seu nome?"}
    ]
    st.session_state.passo = "nome"

# Exibe o histórico de mensagens com o avatar
for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"], avatar=AVATAR_URL if msg["role"] == "assistant" else None):
        st.write(msg["content"])

# Entrada do usuário
if prompt := st.chat_input("Como posso ajudar?"):
    # Adiciona fala do usuário ao histórico
    st.session_state.mensagens.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Lógica de Resposta da Assistente
    with st.chat_message("assistant", avatar=AVATAR_URL):
        if st.session_state.passo == "nome":
            if len(prompt.strip()) > 2:
                nome = prompt.strip()
                resposta = f"Prazer, {nome}! O que você deseja personalizar hoje?"
                st.session_state.passo = "produto"
                # Exibe as opções para facilitar
                st.write(resposta)
                st.info("Escolha: " + " | ".join(PRODUTOS_VALIDOS))
            else:
                resposta = "Por favor, digite um nome válido para continuarmos."
                st.write(resposta)

        elif st.session_state.passo == "produto":
            item_escolhido = next((item for item in PRODUTOS_VALIDOS if item.lower() == prompt.lower()), None)
            
            if item_escolhido:
                resposta = f"Ótimo! E qual seria a quantidade de {item_escolhido}?"
                st.session_state.passo = "quantidade"
                st.write(resposta)
            else:
                resposta = "Ainda não trabalhamos com esse item. Por favor, escolha uma das opções da nossa lista."
                st.write(resposta)
                st.warning("Opções: " + ", ".join(PRODUTOS_VALIDOS))

        # Adiciona a resposta da assistente ao histórico
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})




        




    
