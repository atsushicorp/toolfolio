import pandas as pd
import sys
import os
from pandas.errors import MergeError

#csvファイルの読み込み(対象ファイル：sales.csvとproduct.csvの場合)
#ファイル存在チェック
files = ["./sales.csv","./products.csv"]
#すべてのファイルが存在したら処理を行う
if all(os.path.exists(f) for f in files):
    #salesファイル
    df_sales = pd.read_csv('./sales.csv', encoding='utf-8')
    #productsファイル
    df_product = pd.read_csv('./products.csv', encoding='utf-8')
else:
    print('要確認：処理したいファイルが見つかりませんでした。')
    sys.exit(1)

try:
    #ファイルの統合
    df_merged = pd.merge(df_sales, df_product, on="product_id", how="left", indicator=True, validate="many_to_one")
    #sales.csv（売上データ）内にproducts.csv(商品マスタ)以外の商品コード（product_id）がないかチェック
    if (df_merged["_merge"] == "left_only").any():
        missing_keys = df_merged[df_merged["_merge"] == "left_only"]["product_id"].tolist()
        raise ValueError(f"要確認：sales.csv（売上データ）にproducts.csv(商品マスタ)に存在しないキーが含まれています。不一致product_id:{missing_keys}")
    
    #売上金額列の追加と計算
    df_merged["sales_amount"] = df_merged["price"] * df_merged["quantity"]
    #年月表示列を追加
    df_merged["month"] = pd.to_datetime(df_merged["date"])
    #表示形式を変換yyyy-mm-dd →　yyyy-mm
    df_merged["month"] = df_merged["month"].dt.strftime("%Y-%m")
    #重複する列データの統合
    df_summary = df_merged.groupby(["month","product_id","product_name"]).agg(
        total_quantity = ("quantity","sum"),
        total_sales = ("sales_amount", "sum")
    ).reset_index()
    #年月・商品IDの昇順を指定
    df_summary_sorted = df_summary.sort_values(
        by=["month","product_id"],
        ascending=[True,True],
    )

    #ファイル保存ー上書き禁止
    try:
        df_summary_sorted.to_csv('./monthly_sales.csv', encoding='utf-8',index=False, mode='x')
        #出力内容
        print("中間データ：",df_merged)
        print("ファイル保存内容：",df_summary_sorted)
    except FileExistsError:
        print('要確認：monthly_sales.csvは既に存在します。上書きは行いませんでした。')
        sys.exit(1)

except MergeError as me:
    print(f"商品マスターの重複エラー：{me}")
    sys.exit(1)
except ValueError as ve:
    print(f"データ不整合エラー:{ve}")
    sys.exit(1)
    