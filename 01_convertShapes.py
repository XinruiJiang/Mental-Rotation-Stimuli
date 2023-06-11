import pandas as pd

df=pd.read_csv('Shapes.csv',skiprows=1)
df=df.drop('Shape',axis=1)

for colName in df:
    ps=df[colName].dropna()
    ps=ps.tolist()
    nestedL=[[0]]*len(ps)
    n=0
    for p in ps:
        p=p[:-1]
        p=p.split('  ')[-1]
        p=tuple(map(int,p.split(' ')))
        nestedL[n]=p
        n=n+1
    print(nestedL,',')
