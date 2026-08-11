from groq import Groq
import streamlit as st
import os

# Configuração da página
st.set_page_config(
    page_title="Conversa com o amor da Gabriela",
    page_icon="❤️"
)

# Cliente Groq
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# Título
st.title("❤️ Conversa com o amor da Gabriela")

# Memória da conversa
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
Você é a assistente pessoal da Gabriela de Jesus Santos.

Sua prioridade é ajudar Gabriela de maneira amigável, respeitosa
e útil.

Você deve conversar de maneira natural e carinhosa.
Demonstre carinho por Gabriela frequentemente, mas não precisa
repetir exatamente a mesma frase em todas as respostas.

Nunca invente informações como se fossem fatos.
Se não souber alguma coisa, diga que não sabe.
"""
        }
    ]

# Mostrar histórico
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Campo de mensagem
pergunta = st.chat_input("Digite sua mensagem...")

if pergunta:

    # Mostrar mensagem do usuário
    with st.chat_message("user"):
        st.markdown(pergunta)

    # Adicionar pergunta à memória
    st.session_state.messages.append({
        "role": "user",
        "content": pergunta
    })

    # Gerar resposta
    with st.chat_message("assistant"):

        with st.spinner("Pensando... ❤️"):

            resposta = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages
            )

            texto_resposta = resposta.choices[0].message.content

            st.markdown(texto_resposta)

    # Salvar resposta na memória
    st.session_state.messages.append({
        "role": "assistant",
        "content": texto_resposta
    })


# Botão para limpar conversa
if st.sidebar.button("🗑️ Limpar conversa"):
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
Você é a assistente pessoal da Gabriela de Jesus Santos.
Seja carinhosa, amigável, útil e respeitosa.
"""
        }
    ]

    st.rerun()
