# sample_serverless
sample project for serverless FaaS

1.githubから必要なファイルをダウンロード（lambda関数）

2.S3を1つ立てる
　設定は基本デフォルト
　バケット名:sample-serveless-s3
　フォルダ名input, output
3.lambdaを1つ立てる
　設定は基本デフォルト
　Lambda関数名：lambda_function
　role:lambda basic excution role
　トリガー:S3（input）create 
　　github からダウンロードしたコード（sample_filter
　　コンソールのinline editorにコピペ
　　環境変数:S3へのアップロード
    テスト
4.テスト
5.実行
・githubからサンプルデータ（csv）をダウンロードしS3にアップロード
・データが変換されているか確認
