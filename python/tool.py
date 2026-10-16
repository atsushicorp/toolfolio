import pandas as pd
import sys


df = pd.read_csv('./input_sample.csv', encoding='utf-8')
#列の削除
df = df.drop(columns=["memo"])
#条件データ値による抽出
df= df[df['status'] == "active"].copy()
#name列データの文字列操作
df['name'] = df['name'].str.strip()
#ageでsort
df = df.sort_values('age')

#ファイル保存ー上書き禁止
try:
    df.to_csv('./output.csv',encoding='utf-8',index=False, mode='x')
    #内容出力
    print(df)
except FileExistsError:
    print('要確認：output.csvは既に存在します。上書きは行いませんでした。')
    sys.exit(1)