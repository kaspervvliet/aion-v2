
import streamlit as st

def show_whynot(reason_list):
    st.markdown("### ❌ Waarom deze entry niet is uitgevoerd:")
    for reason in reason_list:
        st.markdown(f"- {json.dumps(reason, indent=2)}")
