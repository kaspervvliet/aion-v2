
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def plot_interactive_candlechart(candles: pd.DataFrame, entry_price: float, tp: float, sl: float, confidence: float):
    st.markdown("## 🕯️ Interactieve Setup Visualisatie")

    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=candles['timestamp'],
        open=candles['open'],
        high=candles['high'],
        low=candles['low'],
        close=candles['close'],
        name="Candles",
        increasing_line_color='green',
        decreasing_line_color='red',
        showlegend=False
    ))

    fig.add_hline(y=entry_price, line=dict(color="blue", dash="dash"), annotation_text="ENTRY", annotation_position="top left")
    fig.add_hline(y=tp, line=dict(color="green", dash="dash"), annotation_text="TP", annotation_position="top left")
    fig.add_hline(y=sl, line=dict(color="red", dash="dash"), annotation_text="SL", annotation_position="top left")

    fig.update_layout(
        xaxis_rangeslider_visible=False,
        plot_bgcolor="#ffffff",
        margin=dict(l=0, r=0, t=30, b=0),
        height=500,
        title=dict(
            text=f"Confidence: {confidence:.2f}",
            x=0.02,
            xanchor='left',
            font=dict(size=14)
        )
    )

    st.plotly_chart(fig, use_container_width=True)
