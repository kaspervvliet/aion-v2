
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_hero_stats(stats):
    st.markdown("## 📈 Hero Stats Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Winrate", f"{stats.get('winrate', 0):.1f}%")
    col2.metric("Gemiddelde RR", f"{stats.get('rr', 0):.2f}")
    col3.metric("Bias", stats.get('bias', 'Onbekend'))

    st.markdown("### 🔍 Equity Curve")
    pnl = stats.get("equity_curve", np.cumsum(np.random.randn(30)))
    fig, ax = plt.subplots()
    ax.plot(pnl, label="PnL")
    ax.set_ylabel("Equity")
    ax.set_xlabel("Trades")
    ax.legend()
    st.pyplot(fig)
