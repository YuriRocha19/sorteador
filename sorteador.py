import streamlit as st
import random
import time
import io

st.set_page_config(page_title="Sorteio de Folhas", page_icon="📄")

st.title("📄 Sorteador de Folhas e Números com Emoção!")

if st.button("🎲 Iniciar Sorteio"):
    st.warning("Sorteio iniciado! Aguarde o suspense e a revelação dos resultados...")

    resultados = []

    for i in range(10):
        st.subheader(f"Sorteio {i+1}/10")

        efeito = st.empty()  # Espaço reservado para efeito visual

        # Efeito visual em etapas
        efeito.markdown("🔄 Preparando sorteio...")
        time.sleep(5)

        folha = random.randint(1, 80)
        numero = random.randint(1, 20)
        resultados.append((folha, numero))

        efeito.markdown(f"🎉 **Resultado:** Folha: **{folha}**, Número: **{numero}**")
        time.sleep(2)  # Pequena pausa antes do próximo sorteio

    # Gerar conteúdo do .txt
    conteudo_txt = "\n".join([f"{i+1}. Folha: {folha}, Número: {numero}" for i, (folha, numero) in enumerate(resultados)])
    arquivo_txt = io.BytesIO()
    arquivo_txt.write(conteudo_txt.encode())
    arquivo_txt.seek(0)

    st.download_button(
        label="📄 Baixar resultado como .txt",
        data=arquivo_txt,
        file_name="sorteio_resultados.txt",
        mime="text/plain"
    )
