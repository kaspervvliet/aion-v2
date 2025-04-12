
import pandas as pd
import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def get_latest_data(symbol, interval='15m', limit=100):
    try:
        # Placeholder: hier zou je een echte API call doen
        logging.info(f"[{datetime.utcnow()}] Ophalen van data voor {symbol}, interval={interval}")
        
        # Simulatie van een externe call (dummy data)
        df = pd.DataFrame({
            'timestamp': pd.date_range(end=datetime.utcnow(), periods=limit, freq='15T'),
            'open': [100 + i for i in range(limit)],
            'high': [101 + i for i in range(limit)],
            'low': [99 + i for i in range(limit)],
            'close': [100 + i + 0.5 for i in range(limit)]
        })

        # Validatie
        if df.isnull().values.any():
            raise ValueError("Ophalen van data bevat lege waarden.")

        required_columns = {'timestamp', 'open', 'high', 'low', 'close'}
        if not required_columns.issubset(df.columns):
            raise ValueError("Dataset mist verplichte kolommen.")

        return df.to_dict(orient='records')

    except Exception as e:
        logging.error(f"Fout bij het ophalen van data: {e}")
        return []
