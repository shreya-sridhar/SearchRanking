import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('data/reviews.csv')

def datatypeInfo():
    df1.info()

def viewDataSample():
    print(df1.head())

def centralTendency():
    print("Ratings")
    print(df1.rating.describe())
    print("Dogs")
    print(df1.dogs.describe())
    print("Sitter")
    print(df1.sitter.describe())

datatypeInfo()
viewDataSample()
centralTendency()


