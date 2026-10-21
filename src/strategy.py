# src/strategy.py
from backtesting import Strategy
from backtesting.lib import crossover
import pandas as pd
from src.config import SMA_FAST, SMA_SLOW, STOP_LOSS_PCT, TAKE_PROFIT_PCT

def SMA(values, n):
    """Calcule la Moyenne Mobile Simple (Simple Moving Average)"""
    return pd.Series(values).rolling(n).mean()

class SwingSmaCross(Strategy):
    # Attribution des paramètres depuis la configuration
    n1 = SMA_FAST
    n2 = SMA_SLOW

    def init(self):
        # Pré-calcul des indicateurs sur l'ensemble de l'historique
        self.sma_fast = self.I(SMA, self.data.Close, self.n1)
        self.sma_slow = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        # Prix de clôture de la bougie actuelle
        current_price = self.data.Close[-1]

        # RÈGLE D'ACHAT : Si la MM rapide croise au-dessus de la MM lente (et qu'on n'est pas déjà positionné)
        if crossover(self.sma_fast, self.sma_slow) and not self.position:
            # Calcul des prix cibles pour sécuriser le trade
            sl_price = current_price * (1 - STOP_LOSS_PCT)
            tp_price = current_price * (1 + TAKE_PROFIT_PCT)
            
            # Exécution de l'ordre d'achat avec limites automatiques
            self.buy(sl=sl_price, tp=tp_price)
            
        # RÈGLE DE SORTIE ANTICIPÉE : Si les MM se croisent en sens inverse avant de toucher SL ou TP
        elif crossover(self.sma_slow, self.sma_fast) and self.position:
            self.position.close()
