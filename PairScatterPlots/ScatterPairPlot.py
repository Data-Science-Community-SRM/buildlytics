import pandas as pd
import seaborn as sns
class CNPairPlot:
    continuous=[]
    categorical=[]
    def get_cn_pp(self,data):
        self.data=data
        for i in self.data.columns:
             if (self.data[i].nunique()/self.data.shape[0])*100 > 20 : ##unique nos in a column are more than 20% then it is a continuous variable
                self.continuous.append(i)
             else:
                self.categorical.append(i)
        cn=self.data.drop(columns=self.categorical,axis=1)
        return sns.pairplot(cn,corner=True,kind="scatter")


