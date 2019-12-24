import json
import urllib.parse
import boto3
import csv
import traceback
import re
import os
import ast
from botocore.exceptions import ClientError


print('Loading function')

s3 = boto3.resource('s3')

# ハンドラー関数
# S3にCSVファイルがアップロードされたことをトリガーに起動
def lambda_handler(event, context):

    # CSVファイルがアップロードされたS3のバケットとキーを取得
    input_bucket = event['Records'][0]['s3']['bucket']['name']
    input_key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    input_filename = os.path.basename(input_key)

    # 出力先のバケットとキー、フォルダを指定
    output_bucket = input_bucket
    output_key = re.sub("^input", "output", input_key).replace(".csv", ".json")

    # CSVファイル読み込みのためのLambda内部のパスの指定
    tmp_path = "/tmp/" + input_filename
    print("success_read_key:"+input_key)
    print("success_read_bucket:"+input_bucket)

    # S3からアップロードされたCSVファイルをJSONファイルに変換
    json_list = modify_csv(s3, input_bucket, input_key, tmp_path)
    print(json_list)

    # JSONファイルをS3にアップロードする
    upload_file(output_bucket, output_key, bytes(json_list, 'UTF-8'))

# CSVファイルをJSONファイルに変換する関数
def modify_csv(s3, input_bucket, input_key, tmp_path):
    json_list = []
    try:
        s3.meta.client.download_file(input_bucket, input_key, tmp_path)
        # CSV ファイルの読み込み
        with open(tmp_path, 'r') as f:
            for row in csv.DictReader(f):
                json_list.append(row)

        # JSON ファイルへの書き込み
        with open('output.json', 'w') as f:
            json.dump(json_list, f)

    except Exception as e:
        print(e)        
    return json_list


# S3にJSONファイルをアップロードする関数
def upload_file(output_bucket, output_key, bytes):
    try:
        out_s3 = boto3.resource('s3')
        s3Obj = out_s3.Object(output_bucket, output_key)
        res = s3Obj.put(Body=bytes)
    except Exception as e:
        print(e)

    print("success upload")
    return res
