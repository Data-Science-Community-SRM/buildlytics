import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class EDA:
    continuous=[]
    categorical=[]
    def viewtop(self ,data):
        self.data = data
        view = self.data.head()
        return view

    def viewbottom(self ,data):
        self.data = data
        view = self.data.tail()
        return view

    def viewstats(self ,data):
        self.data = data
        mean = self.data.mean()
        median = self.data.median()
        mode =self.data.mode()
        return mean, median, mode

    def viewnull(self ,data):
        self.data = data
        view = self.data.notnull()
        return view

    def PairPlot(self,data):
        self.data=data
        for i in self.data.columns:
             if (self.data[i].nunique()/self.data.shape[0])*100 > 20 : ##unique nos in a column are more than 20% then it is a continuous variable
                self.continuous.append(i)
             else:
                self.categorical.append(i)
        cn=self.data.drop(columns=self.categorical,axis=1)
        return sns.pairplot(cn,corner=True,kind="scatter")

    def HeatMaps(self,data,threshold=0.5):
        self.data=data
        self.threshold=threshold
        corr_matrix = self.data.corr().abs()
        filtered_corr_df = corr_matrix[(corr_matrix >= self.threshold) & (corr_matrix != 1.000)] 
        plt.figure(figsize=(30,10))
        plt.show()
        return sns.heatmap(filtered_corr_df, annot=True, cmap="Reds")

    def ScatterGrp(self,df,colx,coly,cols,color=['yellow','orange'],ratio=10,font='Helvetica',save=False,save_name='Default'):
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
            plt.ylim(ymin=-1,ymax=len(coly_encoded))

            if save:
                plt.savefig(save_name+".png")
            