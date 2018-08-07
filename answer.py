import pandas as pd

cols = ['NU_INSCRICAO','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO']

df = pd.read_csv('train.csv', usecols=cols)
df = df.dropna(thresh=5)
df['NU_NOTA_CN'] = df['NU_NOTA_CN'].apply(lambda x: x*2)
df['NU_NOTA_LC'] = df['NU_NOTA_LC'].apply(lambda x: x*1.5)
df['NU_NOTA_MT'] = df['NU_NOTA_MT'].apply(lambda x: x*3)
df['NU_NOTA_REDACAO'] = df['NU_NOTA_REDACAO'].apply(lambda x: x*3)
df['NOTA_FINAL'] = df['NU_NOTA_CN'] + df['NU_NOTA_LC'] + df['NU_NOTA_MT'] +df['NU_NOTA_REDACAO'] + df['NU_NOTA_CH']
df = df.sort_values('NOTA_FINAL', ascending = False)
df = df.head(20)
headerOutput = ['NU_INSCRICAO','NOTA_FINAL']
df.to_csv("answer.csv", columns=headerOutput, index=False)