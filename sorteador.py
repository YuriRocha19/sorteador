# app.py

import streamlit as st
import random
import io

st.set_page_config(page_title="Sorteio de Folhas", page_icon="📄")

st.title("📄 Sorteador de Folhas e Números")
st.write("Clique no botão abaixo para sortear 10 pares de folha (1 a 80) e número (1 a 20).")

if st.button("🎲 Sortear 10 casos"):
    resultados = []
    for i in range(10):
        folha = random.randint(1, 80)
        numero = random.randint(1, 20)
        resultados.append((folha, numero))

    st.subheader("📝 Resultados dos Sorteios:")
    for i, (folha, numero) in enumerate(resultados, start=1):
        st.markdown(f"**{i}.** Folha: **{folha}**, Número: **{numero}**")

    # Gerar conteúdo do .txt
    conteudo_txt = "\n".join([f"{i+1}. Folha: {folha}, Número: {numero}" for i, (folha, numero) in enumerate(resultados)])

    # Criar arquivo em memória
    arquivo_txt = io.BytesIO()
    arquivo_txt.write(conteudo_txt.encode())
    arquivo_txt.seek(0)

    # Botão de download
    st.download_button(
        label="📄 Baixar resultado como .txt",
        data=arquivo_txt,
        file_name="sorteio_resultados.txt",
        mime="text/plain"
    )
