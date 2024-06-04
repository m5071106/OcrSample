## OCR sample program with m3, macOS 14.5, Python 3.10.14

### 簡易版 (img_to_text.py をターミナルで実行する)

1. img_to_text.py 冒頭のコメントをもとに必要なモジュールを準備してください
2. sourceフォルダに画像ファイルを格納してください。対象拡張子はextensions.txtで制御します。
3. python3 img_to_text.py
   で変換を開始します。
4. resultフォルダに音声ファイル名+年月日時分秒のテキストが格納されます。

### Web版 (front_web.py をターミナルで実行後、Web Browser で http://[hostname]:5001/でアクセス)

1. img_to_text.py 冒頭のコメントをもとに必要なモジュールを準備してください
2. python3 front_web.py でwebを起動します。
3. http://[hostname]:5001/ でアクセスします。
4. ファイルをアップロードし、変換ボタン選択で処理が始まります。
5. 結果がWeb上に表記されます。./result/フォルダを別の静的webでディレクトリが見られるよう設定することで変換結果をダウンロードします。
