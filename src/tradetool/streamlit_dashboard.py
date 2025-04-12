
import streamlit as st
from tradetool.data import get_latest_data
from tradetool.strategy_config_loader import load_config
from entry_scorer import EntryScorer
from strategy_visualizer import StrategyVisualizer
from strategy_report import StrategyReportGenerator

st.set_page_config(page_title="AI Trading Dashboard", layout="wide")

st.title("📈 Self-Learning Trading Tool (Realtime AI Dashboard)")

config_file = "strategy_config.json"
data = get_latest_data("SOL/USD")
strategy, config = load_config(config_file, data)

# Analyse starten
with st.spinner("Analyseren..."):
    entries = strategy.find_entries()
    scorer = EntryScorer()
    scored = scorer.score_entries(entries)
    performance = strategy.calculate_performance(scored)

# UI output
st.subheader(f"Strategie: {config['strategy_name']}")
st.metric("Totale Trades", len(scored))
st.metric("Hitrate", f"{performance['hitrate'] * 100:.1f}%")
st.metric("Expectancy", performance['expectancy'])
st.metric("Profit Factor", performance['profit_factor'])

# Charts
vis = StrategyVisualizer()
equity_chart_path = vis.plot_equity_curve(scored, config["strategy_name"])
rr_chart_path = vis.plot_rr_distribution(scored, config["strategy_name"])

st.image(equity_chart_path, caption="📈 Equity Curve", use_column_width=True)
st.image(rr_chart_path, caption="📊 RR Distribution", use_column_width=True)

# Setup-table
st.subheader("🔍 Entry Details")
st.dataframe([{k: v for k, v in e.items() if k != 'rsi'} for e in scored])


st.info('Toelichting per entry is zichtbaar in de kolom `gpt_explanation`.')