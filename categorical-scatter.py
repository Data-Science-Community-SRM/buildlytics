# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 12:32:54 2021

@author: LEGION
"""

import pandas as pd
import matplotlib.pyplot as plt

class Scatteratti:
    def scattergrp(df,colx,coly,cols,color=['yellow','orange'],ratio=10,font='Helvetica',save=False,save_name='Default'):
        colx_encoded=dict(zip(df[colx].sort_values().unique(),range(len(df[colx].unique()))))
        coly_encoded=dict(zip(df[coly].sort_values(ascending=False).unique(),range(len(df[coly].unique()))))
        
        # Apply the encoding
        df[colx]=df[colx].apply(lambda x: colx_codes[x])
        df[coly]=df[coly].apply(lambda x: coly_codes[x])
        
        # Prepare the aspect of the plot
        plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
        plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
        plt.rcParams['font.sans-serif']=font
        plt.rcParams['xtick.color']=color[-1]
        plt.rcParams['ytick.color']=color[-1]
        plt.box(False)
        
        # Plot all the lines for the background)
        for num in range(len(coly_encoded)):
            plt.hlines(num,-1,len(colx_encoded)+1,linestyle='dashed',linewidth=1,color=color[num%2],alpha=0.5)
        
        for num in range(len(colx_encoded)):
            plt.vlines(num,-1,len(coly_encoded)+1,linestyle='dashed',linewidth=1,color=color[num%2],alpha=0.5)
            
            # Plot the scatter plot with the numbers
            plt.scatter(df[colx], df[coly], s=df[cols]*ratio)
            
            # Change the ticks numbers to categories and limit them
            plt.xticks(ticks=list(colx_encoded.values()),labels=colx_encoded.keys(),rotation=90)
            plt.yticks(ticks=list(coly_encoded.values()),labels=coly_encoded.keys())
            plt.xlim(xmin=-1,xmax=len(colx_encoded))
            plt.ylim(ymin=-1,ymax=len(coly_encoded)
            
            # Save if wanted
            if save:
                plt.savefig(save_name+'.png')
                     