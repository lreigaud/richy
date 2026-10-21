# src/config.py

# Paramètres généraux du marché
TICKER = "SPY"              # S&P 500 ETF (idéal pour du swing long terme)
START_DATE = "2016-01-01"   # Début du backtest (10 ans d'historique)
END_DATE = "2026-01-01"     # Fin du backtest

# Paramètres du capital et des frais
INITIAL_CASH = 10000        # Capital de départ en dollars
COMMISSION = 0.001          # 0.1% de frais par transaction (simule les frais réels d'un courtier)

# Paramètres de la stratégie technique
SMA_FAST = 20               # Période de la moyenne mobile rapide (en jours)
SMA_SLOW = 50               # Période de la moyenne mobile lente (en jours)

# Gestion du risque (Money Management)
# 0.03 = 3% de baisse maximum autorisée | 0.09 = 9% de hausse visée
STOP_LOSS_PCT = 0.03        
TAKE_PROFIT_PCT = 0.09      
