# app.py

import streamlit as st
import random

st.set_page_config(page_title="Sorteio de Folha", page_icon="📄")

st.title("📄 Sorteador de Folhas e Números")

st.write("Clique no botão abaixo para sortear uma folha (1 a 80) e um número dentro da folha (1 a 20).")

if st.button("🎲 Sortear"):
    folha = random.randint(1, 80)
    numero = random.randint(1, 20)
    
    st.success(f"🟢 Folha sorteada: **{folha}**")
    st.success(f"🔢 Número sorteado na folha: **{numero}**")
