
import streamlit as st

def show_machine_personality(bias, strategy, confidence):
    st.markdown("### 🤖 Machine Gedrag")
    st.write(f"**Bias:** {bias}")
    st.write(f"**Strategie:** {strategy}")
    st.write(f"**Confidence:** {confidence}")
