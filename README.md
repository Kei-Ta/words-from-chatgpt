# words-from-chatgpt

このプロジェクトはChatGPTから帰ってくる言葉をRaspberryPIと接続したe-Paperに表示するプログラムです。

# フォルダ構成
/src 実行プログラムが入っているライブラリ\n
/pic フォント等が入っているライブラリ\n
/lib e-paperに表示するためのライブラリ\n

# 実行方法
1. srcフォルダへ移動
```
cd src
```

2. APIキーを環境変数に設定
```
export OPENAI_API_KEY="*****************************"
```
※各自取得したAPIキーを設定すること

2. プログラムの実行
```
python3 epaper.py 
```
e-PaperにChatGPTから受け取ったメッセージが表示される
