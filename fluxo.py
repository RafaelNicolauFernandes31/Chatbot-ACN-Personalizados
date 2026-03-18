import streamlit as st
import urllib.parse

def gerenciar_fluxo(resposta_usuario, numero_whatsapp):
    # Inicializa o passo se não existir
    if "passo" not in st.session_state:
        st.session_state.passo = 1
        st.session_state.dados_orcamento = {}

    # Lógica de decisão (resumida para o exemplo)
    if st.session_state.passo == 1:
        st.session_state.dados_orcamento["nome"] = resposta_usuario
        proxima = f"Prazer, {resposta_usuario}! O que você deseja personalizar hoje?"
        st.session_state.passo = 2
    
    elif st.session_state.passo == 2:
        st.session_state.dados_orcamento["produto"] = resposta_usuario
        proxima = "Ótimo! E qual seria a quantidade?"
        st.session_state.passo = 3
        
    elif st.session_state.passo == 3:
        st.session_state.dados_orcamento["quantidade"] = resposta_usuario
        
        # Gera o link do WhatsApp
        msg = (f"Olá! Pedido ACN Personalizados:\n"
               f"Nome: {st.session_state.dados_orcamento['nome']}\n"
               f"Produto: {st.session_state.dados_orcamento['produto']}\n"
               f"Qtd: {resposta_usuario}")
        
        link = f"https://wa.me/{numero_whatsapp}?text={urllib.parse.quote(msg)}"
        st.session_state.link_whatsapp = link
        proxima = "Tudo pronto! Clique no botão abaixo para me enviar no WhatsApp."
        st.session_state.passo = 4 # Fim
        
    else:
        proxima = "Aguarde um instante que já vamos te atender!"

    return proxima