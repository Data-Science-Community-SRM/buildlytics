import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

# read you data into df
# put your code here
class heatmaps:
    def get_heatmap(self ,data):
        # create correlation matrix with abs values
        self.data=data
        corr_matrix = self.data.corr().abs()
        # change this value as needed, if 0.5 does not work for your scenario
        threshold = 0.5
        filtered_corr_df = corr_matrix[(corr_matrix >= threshold) & (corr_matrix != 1.000)] 
        plt.figure(figsize=(30,10))
        plt.show()
        return sn.heatmap(filtered_corr_df, annot=True, cmap="Reds")
        
