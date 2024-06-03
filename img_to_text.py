# 事前準備
# pip install pyocr
from PIL import Image

import cv2
import datetime
import numpy as np
import os
import pyocr
import sys

# 画像からテキストに変換する関数
def img_to_text():

    # 変数の初期化
    resultfilename = None
    result = None

    # 対象拡張子の読み込み
    with open('extensions.txt', 'r') as file:
        extensions = file.read().splitlines()

    # 入出力ディレクトリのパス
    source_dir = './source'
    result_dir = './result'
    backup_dir = './backup'
    temporary_dir = './temporary'
    # sourceディレクトリ内のファイル一覧を取得
    file_list = os.listdir(source_dir)

    # tempoary_dir 内のファイルを削除
    for filename in os.listdir(temporary_dir):
        os.remove(f'{temporary_dir}/{filename}')

    # 認識対象の拡張子のファイルのみを抽出し、変換を行う
    for filename in file_list:
        if any(extension in filename for extension in extensions):
            print(f'{filename}の画像変換を開始')
            # 変換時刻を取得
            datetimenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            # 入力
            img = cv2.imread(source_dir + "/" + filename)
            # グレースケール
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 2値化
            threshold = 140
            img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)[1]
            # 反転
            img = cv2.bitwise_not(img)
            cv2.imwrite(temporary_dir + "/" + filename, img)
            # OCR
            tools = pyocr.get_available_tools()
            result = tools[0].image_to_string(
                Image.open(temporary_dir + "/" + filename)
                ,lang="eng")

            # 変換後のファイル名を作成
            converted_filename = filename
            for extension in extensions:
                converted_filename = converted_filename.replace('.' + extension, '')
            # 結果出力配列に変換後のファイル名を追加
            resultfilename = f'{converted_filename}_{datetimenow}.txt'
            # 処理したファイルをバックアップディレクトリに移動
            os.rename(f'{source_dir}/{filename}', f'{backup_dir}/{filename}')
            # バックアップディレクトリに移動したファイルに年月日時分秒をつけてリネーム
            os.rename(f'{backup_dir}/{filename}', f'{backup_dir}/{filename}.{datetimenow}')
            # resultフォルダ内にファイルを作成し、結果を書き込む
            with open(f'{result_dir}/{resultfilename}', mode='w+') as f:
                f.write(result)

    # tempoary_dir 内のファイルを削除
    for filename in os.listdir(temporary_dir):
        os.remove(f'{temporary_dir}/{filename}')

    return resultfilename, result

# メイン処理
if __name__ == "__main__":
    # unpacking
    resultfilename, result = img_to_text()
    print(resultfilename, result)
