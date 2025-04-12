
import streamlit as st
from multi_asset_runner import MultiAssetRunner
from telegram_notifier import TelegramNotifier

st.set_page_config(page_title="📡 AI WatchMode", layout="wide")
st.title("📡 Real-Time Signal Monitor")

runner = MultiAssetRunner(config_dir="configs")
results = runner.run_all()

high_signals = {k: v for k, v in results.items() if v}

if not high_signals:
    st.success("✅ Geen actieve setups gevonden. Alles is rustig.")
else:
    for symbol, entries in high_signals.items():
        st.error(f"🚨 Signal detected on {json.dumps(symbol, indent=2)}")
        for e in entries:
            st.write(f"**{e['type'].upper()}** @ {e['price']} → RR: {e['rr']:.2f}")
            st.caption(e.get("gpt_explanation", "Geen uitleg beschikbaar"))
