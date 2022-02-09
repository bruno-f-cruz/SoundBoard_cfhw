from lib2to3.pgen2.token import ISNONTERMINAL
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mpl
from pathlib import Path


def load_xlsx_sheet(xlsxPath, sheetName, skiprows = 15, col1 = 0, col2 = 1):
    d = pd.read_excel(open(xlsxPath, 'rb'),
              sheet_name=sheetName, 
              skiprows=skiprows)  
    d = d.iloc[:, [col1,col2]]
    d.columns.values[0] = 'X'
    d.columns.values[1] = 'Y'
    return d

def load_trc_file(Path, skiprows = 15, col1 = 0, col2 = 1):
    d = pd.read_csv(Path, skiprows=skiprows, sep = '\t')
    d = d.iloc[:, [col1,col2]]
    d.columns.values[0] = 'X'
    d.columns.values[1] = 'Y'
    return d


def plot_quick_XY(d, figsize = (6,4), c = 'k', title = "x_y_plot", xlabel = "Frequency[kHz]", ylabel = "Magnitude[dB]", xlim = None, label = 'THD = ?', linewidth = 0.5):

    fig = plt.figure(figsize=figsize, tight_layout=True)
    ax = fig.add_subplot(1,1,1)
    plt.plot(d["X"]/1000, d["Y"],
    linewidth = linewidth,
    c = c, label = label)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if (xlim is None):
        plt.xlim([0,np.max(d["X"]/1000)])
    else:
        plt.xlim(xlim)
    return fig, ax