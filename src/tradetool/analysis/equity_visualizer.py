
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_equity_curve(journal_path="trade_journal.json"):
    try:
        df = pd.read_json(journal_path)
    except Exception:
        st.warning("Geen journalgegevens gevonden.")
        return

    if df.empty:
        st.info("Er zijn nog geen entries gelogd.")
        return

    df = df.sort_values("timestamp")
    df["pnl"] = df["rr"].apply(lambda rr: rr if rr >= 1 else -1)
    df["equity"] = df["pnl"].cumsum()

    max_drawdown = (df["equity"].cummax() - df["equity"]).max()
    winrate = (df["pnl"] > 0).mean() * 100
    expectancy = df["pnl"].mean()

    st.markdown("## 📊 Equity Visualizer")
    fig, ax = plt.subplots()
    ax.plot(df["timestamp"], df["equity"], label="Equity")
    ax.set_ylabel("PnL cumulatief")
    ax.set_xlabel("Tijd")
    ax.set_title("Equity Curve")
    ax.legend()
    st.pyplot(fig)

    st.markdown(
        f"### 📈 Statistieken\n"
        f"- **Max Drawdown:** {max_drawdown:.2f}\n"
        f"- **Winrate:** {winrate:.1f}%\n"
        f"- **Expectancy:** {expectancy:.2f} R"
    )
