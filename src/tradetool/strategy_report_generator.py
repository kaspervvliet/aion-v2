
import openai
from datetime import datetime

# Vereist: OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

class StrategyReportGenerator:
    def __init__(self, trades, strategy_name="Strategy"):
        self.trades = trades
        self.strategy_name = strategy_name

    def generate_report(self):
        """
        Genereert een uitgebreid rapport voor de strategie, inclusief GPT-validatie.
        """
    st.markdown("Strategie rapport succesvol gegenereerd.")
".join([f"Trade {i+1}: {trade['result']} - PnL: {trade['balance']:.2f}" for i, trade in enumerate(self.trades)])
        report_prompt = f"""
        Strategie: {self.strategy_name}
        
        Hier zijn de trade details:
        {trade_details}
        
        Geef een samenvatting van de strategie, inclusief sterke en zwakke punten, en waar verbetering mogelijk is.
        """

        # GPT genereren rapport
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=report_prompt,
            temperature=0.7,
            max_tokens=300
        )

        return response.choices[0].text.strip()

    def save_report(self, report, filename="strategy_report.txt"):
        """
        Slaat het gegenereerde rapport op als tekstbestand.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if os.getenv("ENV") != "render":
            with open(filename, "w") as file:
            file.write(f"Strategy Report - {self.strategy_name}
")
            file.write(f"Generated at: {timestamp}

")
            file.write(report)
        print(f"Strategierapport opgeslagen als {filename}")
