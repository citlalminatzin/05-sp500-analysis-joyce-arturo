#!/usr/bin/env python

import matplotlib.pyplot as plt
from models import calc_error, modelo_geom, modelo_circ
from data import get_stock_data

def main():
    df = get_stock_data(years=5)
    print(df.head())

    # Precios
    df['Close'].plot(title="Precio S&P 500 (Dependencia temporal alta)")
    plt.savefig('grafica_precios.png')

    # Rendimientos
    rendimientos = df['Close'].pct_change()
    rendimientos.plot(title="Rendimientos S&P 500 (Cercano a ruido blanco)")
    plt.savefig('grafica_rendimientos.png')

if __name__ == "__main__":
    main()
