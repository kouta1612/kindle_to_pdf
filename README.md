# kindle から PDF を作成するライブラリ

## 環境構築

```terminal
pip3 install -r requirements.txt
```

## スクリーンショット

### デフォルト版

```terminal
python3 ./screenshot.py
```

### オプション指定版

```terminal
python3 ./screenshot.py -d right -p 500 -t 1
```

### オプション一覧

```text
d: ページをめくる方向(left or right)
p: 全体で何ページ分のスクリーンショットを行うか
t: 何秒ごとにスクリーンショットを行うか
```

## PDF 作成

```terminal
python3 ./create_pdf.py
```
