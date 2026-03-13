#!/usr/bin/env python

from yfinance import Ticker
import pandas as pd

from yfinance import Ticker
import pandas as pd
import os

def get_stock_data(ticker: str = "^GSPC", years: int = 5, path: str = "data/sp500_5y.csv"):
    """Descarga datos históricos de yfinance para el periodo especificado"""
    # Crear directorio si no existe
    if not os.path.exists('data'):
        os.makedirs('data')
        
    t = str(years) + "y"
    print(f"Descargando {t} de datos para {ticker}...")
    stock = Ticker(ticker).history(period=t)
    stock.to_csv(path, encoding='utf-8')

    print(f"Datos guardados en {path}")
    return stock

