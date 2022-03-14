import pandas as pd 

class statistical_describe:

    def __init__(self,df : pd.DataFrame(),seg1 : str, seg2 : str):
        self.df = df 
        self.seg1 = seg1 
        self.seg2 = seg2 
    
    def main(self):
        print("{}과 {} 사이의 공분산 값은 {:.4f}".format(self.seg1,self.seg2 ,self.df[self.seg1].cov(self.df[self.seg2])))
        print("{}과 {} 사이의 상관 계수 값은 {:.4f}".format(self.seg1,self.seg2 ,self.df[self.seg1].corr(self.df[self.seg2])))


