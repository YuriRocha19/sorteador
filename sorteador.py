import streamlit as st
import random
import io

st.set_page_config(page_title="Sorteio Interativo", page_icon="🎲")

st.title("📄 Sorteador de Folhas e Números (Interativo)")

# Inicializar variáveis na sessão
if "resultados" not in st.session_state:
    st.session_state.resultados = []
if "contador" not in st.session_state:
    st.session_state.contador = 0

# Sorteio passo a passo
if st.session_state.contador < 10:
    if st.button("🎯 Sortear Próximo"):
        folha = random.randint(1, 80)
        numero = random.randint(1, 20)
        st.session_state.resultados.append((folha, numero))
        st.session_state.contador += 1

# Mostrar sorteios feitos até agora
if st.session_state.resultados:
    st.subheader("📝 Resultados até agora:")
    for i, (folha, numero) in enumerate(st.session_state.resultados, start=1):
        st.markdown(f"**{i}.** Folha: **{folha}**, Número: **{numero}**")

# Quando completar 10 sorteios, habilitar download
if st.session_state.contador == 10:
    st.success("🎉 Todos os 10 sorteios foram feitos!")

    conteudo_txt = "\n".join([
        f"{i+1}. Folha: {folha}, Número: {numero}"
        for i, (folha, numero) in enumerate(st.session_state.resultados)
    ])

    arquivo_txt = io.BytesIO()
    arquivo_txt.write(conteudo_txt.encode())
    arquivo_txt.seek(0)

    st.download_button(
        label="📄 Baixar resultado como .txt",
        data=arquivo_txt,
        file_name="sorteio_resultados.txt",
        mime="text/plain"
    )

    if st.button("🔁 Reiniciar Sorteio"):
        st.session_state.resultados = []
        st.session_state.contador = 0
