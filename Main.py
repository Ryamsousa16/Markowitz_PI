import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('Acoes_ibov.csv')
df = df.dropna()

carteira = ['KLBN11.SA', 'ABEV3.SA', 'RENT3.SA', 'B3SA3.SA', 'CIEL3.SA', 'ELET3.SA',
            'LREN3.SA', 'BBDC3.SA', 'MGLU3.SA', 'BBDC4.SA', 'ELET6.SA', 'SANB11.SA',
            'MRFG3.SA', 'BRAP4.SA', 'MRVE3.SA', 'BBAS3.SA', 'MULT3.SA', 'CSAN3.SA',
            'BRKM5.SA', 'PCAR3.SA', 'CCRO3.SA', 'PETR3.SA', 'PETR4.SA', 'QUAL3.SA',
            'CVCB3.SA', 'RADL3.SA', 'CYRE3.SA', 'RAIL3.SA', 'ECOR3.SA', 'SBSP3.SA',
            'SUZB3.SA', 'EGIE3.SA', 'TAEE11.SA', 'EQTL3.SA', 'VIVT3.SA', 'CSNA3.SA',
            'FLRY3.SA', 'GGBR4.SA', 'GOLL4.SA', 'GOAU4.SA', 'UGPA3.SA', 'USIM5.SA',
            'VALE3.SA', 'HYPE3.SA', 'ITSA4.SA', 'WEGE3.SA', 'EMBR3.SA']

df_log = np.log(df[carteira] / df[carteira].shift(1))
print(df_log[0:5])
