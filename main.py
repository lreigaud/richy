# main.py
from backtesting import Backtest
import pandas as pd
from src.data_loader import get_historical_data
from src.strategy import SwingSmaCross
from src.config import TICKER, START_DATE, END_DATE, INITIAL_CASH, COMMISSION

def main():
    print("=== INITIALISATION DU BACKTEST SUR 10 ANS ===")
    
    # 1. Chargement des données
    data = get_historical_data(ticker=TICKER, start=START_DATE, end=END_DATE)
    
    # CORRECTION COMPATIBILITÉ PYTHON 3.14 / PANDAS :
    # On s'assure que l'index est bien un DatetimeIndex propre pour éviter le bug '.is_numeric()'
    data.index = pd.to_datetime(data.index)
    
    # 2. Configuration du moteur de backtest
    bt = Backtest(
        data, 
        SwingSmaCross, 
        cash=INITIAL_CASH, 
        commission=COMMISSION, 
        hedging=False
    )
    
    # 3. Exécution de la simulation
    print(f"--> Simulation en cours pour {TICKER}...")
    stats = bt.run()
    
    # 4. Affichage des résultats clés dans la console
    print("\n" + "="*40)
    print("               RÉSULTATS DU BOT               ")
    print("="*40)
    print(f"Rendement Total [%]       : {stats['Return [%]']:.2f}%")
    print(f"Rendement du Marché [%]   : {stats['Buy & Hold Return [%]']:.2f}%")
    print(f"Taux de réussite (Win Rate): {stats['Win Rate [%]']:.2f}%")
    print(f"Nombre total de trades    : {stats['# Trades']}")
    print(f"Perte Maximale (Drawdown) : {stats['Max. Drawdown [%]']:.2f}%")
    print(f"Ratio de Sharpe           : {stats['Sharpe Ratio']:.2f}")
    print("="*40 + "\n")
    
    # 5. Lancement du graphique interactif HTML
    print("--> Ouverture du graphique interactif dans votre navigateur...")
    bt.plot()

if __name__ == "__main__":
    main()
