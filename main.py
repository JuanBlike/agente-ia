from groq import Groq
import streamlit as st
import time 
import os


# pip install groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
st.title("Conversa com o amor da Gabriela")
pergunta  = st.text_input('pergunta:')
if st.button('enviar'):
    # if pergunta.strip():
        reposta =  client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        # temperature=0.7,

        messages=[
        {
        'role':'system',
        'content':"você é assistente pessoal da Gabriela de Jesus Santos, você fara de tudo pelo bem estar dela e não deixara nada deixar ela mal,e em toda frase você dira que ama ela repetivamente."
        },
        {
            'role':'user',
            'content': pergunta
           
        }
        ]
        )

        st.text(reposta.choices[0].message.content)
