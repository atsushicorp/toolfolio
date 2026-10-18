# CSV集計整形ツール

## 概要

 このツールは、売上データ及び商品マスタデータの２つのcsvファイルを読み込み、
 月別及び商品別に売上データを集計するpythonプログラムです。

## 主な機能

- 各商品について同月内の売上データの集計
- 商品マスタ内の重複登録チェック
- 売上データにおける商品マスタに存在しないデータのチェック
- 年月・商品IDによる昇順ソート
- CSVファイルへの保存 

## 動作環境

- Python 3.13
- pandas

## サンプルデータについて

本リポジトリに含まれるsales.csv及びproducts.csvの売上データや商品名その他のデータは、
動作確認のために作成した架空の情報です。

本ツールは学習及びポートフォリオ公開を目的として作成しています。

## セットアップ・実行方法

Python 3.13をインストールした環境で、以下の手順を実行してください。

### 1. 仮想環境の作成

リポジトリのルートディレクトリ（`toolfolio`）に移動し、仮想環境を作成します。

```powershell
python -m venv .venv
```

### 2. 仮想環境の有効化

```powershell
.\.venv\Scripts\Activate.ps1
```

有効化されると、ターミナルの先頭に `(.venv)` が表示されます。

### 3. 必要なライブラリのインストール

```powershell
python -m pip install -r python/requirements.txt
```

### 4. プログラムの実行

```powershell
cd python/sales-summary
python main.py
```

実行すると、`sales.csv` と `products.csv` を読み込み、月別・商品別に集計した結果を `monthly_sales.csv` に保存します。

※ `monthly_sales.csv` が既に存在する場合は、上書きせずにエラー終了します。

### 5. 仮想環境の終了

作業終了後は、以下のコマンドで仮想環境を終了できます。

```powershell
deactivate
```

## 注意事項

- `monthly_sales.csv`が既に存在する場合は、上書きせずに終了します。
- 再実行するには、既存の`monthly_sales.csv`を移動または削除してください。
- お手元で`sales.csv`及び`products.csv`を編集してサンプルコードを実行及びテストを行いたい場合は、以下の入力データに関する注意事項をご確認ください。
- `sales.csv`(売上データ)において`products.csv`（商品マスタ）に存在しない商品コード`product_id`が存在した場合はデータ不整合エラーが発生します。
- `products.csv`に商品コードが重複した場合はエラーが発生します。
- 入力CSVはUTF-8形式を想定しています。
- 本リポジトリのコードの利用及びテスト実行に関し、一切の責任は負いかねます。何卒ご了承ください。

## CSVファイル仕様

### 入力：sales.csv（売上データ）

| 列名 | 内容 |
|---|---|
| `date` | 売上日（YYYY-MM-DD） |
| `product_id` | 商品ID |
| `quantity` | 販売数量 |

### 入力：products.csv（商品マスタ）

| 列名 | 内容 |
|---|---|
| `product_id` | 商品ID |
| `product_name` | 商品名 |
| `price` | 商品単価 |

### 出力：monthly_sales.csv（月別売上集計）

| 列名 | 内容 |
|---|---|
| `month` | 年月（YYYY-MM） |
| `product_id` | 商品ID |
| `product_name` | 商品名 |
| `total_quantity` | 月別販売数量の合計 |
| `total_sales` | 月別売上金額の合計 |