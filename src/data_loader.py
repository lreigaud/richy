# src/data_loader.py
import os
import pandas as pd
import yfinance as yf

def get_historical_data(ticker="SPY", start="2016-01-01", end="2026-01-01"):
    """Télécharge et formate les données au format strict de backtesting.py"""
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{ticker}_10y.csv"
    
    if os.path.exists(file_path):
        print(f"--> Chargement des données locales pour {ticker}...")
        df = pd.read_csv(file_path, index_col=0, parse_dates=True)
    else:
        print(f"--> Téléchargement de 10 ans de données pour {ticker} depuis yfinance...")
        df = yf.download(ticker, start=start, end=end)
        
        # CORRECTION MULTIINDEX : Si yfinance renvoie des colonnes à plusieurs niveaux, on les aplatit
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.droplevel(1)  # Supprime le niveau contenant le nom du ticker
            
        # Nettoyage pour s'assurer d'avoir exactement les 5 colonnes requises
        df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
        df.to_csv(file_path)
        
    return df
