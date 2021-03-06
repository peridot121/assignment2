#!/usr/bin/env python
import sys
import pandas as pd
import os
import matplotlib.pyplot as plt

if __name__=="__main__":
    target = sys.argv[1]
    if target == 'time':
        f = './time.csv'
        scatter = False
        lines = True
        title = 'Knapsack Time Elapsed'
    elif target == 'functions':
        f = './functions.csv'
        scatter = False
        lines = True
        title = 'Knapsack Function Calls'
    elif target == 'global':
        f = './global.csv'
        scatter = False
        lines = True
        title = 'Knapsack Global Optima'
    else:
        f = './optimal.csv'
        scatter = False
        lines = True
        title = 'Knapsack Fitness'

    pd.set_option('display.max_row', 1000)
    pd.set_option('display.max_columns', 50)
    df = pd.read_csv(f)
    plt.figure(figsize=(10, 8))
    algos = { 'RHC': { 'marker': 'x', 'color': 'Red'},
              'GAHighPop': { 'marker': '1', 'color': 'Orchid'},
              'GALowPop': { 'marker': '1', 'color': 'Purple'},
              'MIMIC200': { 'marker': '*', 'color': 'Lime'},
              'MIMIC50': { 'marker': '+', 'color': 'OliveDrab'},
              'SA55': { 'marker': '^', 'color': 'Turquoise'},
              'SA75': { 'marker': 'v', 'color': 'LightSteelBlue'},
              'SA95': { 'marker': '>', 'color': 'Blue'},
            }
    xval = 'iterations'
    yval = target
    for algorithm in ['RHC', 'GAHighPop', 'GALowPop', 'MIMIC200', 'MIMIC50', 'SA55', 'SA75', 'SA95']:
        for iter in df['iterations'].unique():
            df.ix[(df.algorithm == algorithm) & (df.iterations == iter), target] = df.ix[(df.algorithm == algorithm) & (df.iterations == iter)][target].mean()

        if lines is True:
            plt.plot(df[xval][df['algorithm'] == algorithm],
                     df[yval][df['algorithm'] == algorithm],
                     color=algos[algorithm]['color'],
                     label=algorithm)
        if scatter is True:
            plt.scatter(df[xval][df['algorithm'] == algorithm],
                        df[yval][df['algorithm'] == algorithm],
                        marker=algos[algorithm]['marker'],
                        color=algos[algorithm]['color'],
                        alpha=0.7,
                        s=50,
                        label=algorithm)
    plt.title(title)
    plt.ylabel(yval)
    plt.xlabel(xval)
    plt.legend(loc='auto',prop={'size':10})
    plt.xlim([0, max(df[xval])+10])
    plt.ylim([0, max(df[yval])+10])
    plt.show()
