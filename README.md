# sample_serverless
sample project for serverless FaaS

# Features
* sample_serverless is a program for convert a csv file into json file
* sample_serverlessは   です

# Requirement 
* Python 3.7
* Environments under [Amazon Web Service]

# Usage
1. githubから必要なファイルをダウンロード（lambda関数）
    1. ローカルにsample_serverlessフォルダを作成
    2. \sample_serverlessにgit cloneする
        クローン元URL：https://github.com/nmotoki/sample_serverless.git

    ```
    git clone https://github.com/nmotoki/sample_serverless.git    
    ```
    3. ローカルリポジトリに下記ファイルがあることを確認
    - README.md
    - lambda_function.py
    - sample_data.csv

2. AWSマネジメントコンソールにログイン
* AWSアカウントの登録、MFA設定、IAMユーザーの登録はできていることを前提
* リージョンはアジアパシフィック（東京）

3. S3バケットの作成・設定
    1. AWSマネジメントコンソールからS3のコンソール画面を開く
    2. 「バケットを作成する」ボタンを押下
    3. バケット名を「sample-serverless-s3」
        リージョンを「アジアパシフィック（東京）」に設定
    4. 「オプションの設定」はデフォルトのまま「次へ」
    5. 「アクセス許可の設定」で「パブリックアクセスを全てブロック」のチェックボックスからチェックを外し「次へ」
        * 今回はあくまでサンプルとしての利用のためパブリックアクセスを許可していますが、基本的にはブロックしアクセス許可の設定を適切に行って下さい
        * サンプルで利用するデータは不特定多数の目に触れても問題ないものを使用してください
    6. 「確認」で問題無ければ「バケットを作成」を押下
    7. S3のコンソールから作成した「sample-serverless-s3」を選択
    8. バケットのコンソール画面で「フォルダの作成」を押下
    9. フォルダ名を「input」として後はデフォルト設定で「保存」
    10. 同様に「output」フォルダを作成

4. IAMロールの作成
    1. AWSマネジメントコンソールからIAMのコンソール画面を開く
    2. 「ダッシュボード」-「アクセス管理」-「ロール」タブを押下
    3. 「ロール」画面 -「ロールの作成」を押下
    4. 「ロールの作成」画面 -「信頼されたエンティティの種類を選択」
        「AWSサービス」を選択
    5. 「このロールを使用するサービスを選択」-「Lambda」を選択し「次のステップ：アクセス権限」を押下
    6. 「ロールの作成」画面 - 検索窓で「S3」を検索し「AmazonS3FullAccess」のチェックボックスにチェック
    7. 検索窓で「lambda」を検索し「AWSLambdaBasicExecutionRole」のチェックボックスにチェック
    8. 「次のステップ：タグ」を押下
    9. 「タグの追加（オプション）」はデフォルト設定のまま「次のステップ：確認」を押下
    10. 「確認」画面で「ロール名」を「sample-s3-lambda-role」に設定し「ロールの作成」を押下

5. Lambdaの作成
    1. AWSマネジメントコンソールからLambdaのコンソール画面 - 「設定」タブを開く
    2. 「関数の作成」ボタンを押下
    3. 「関数の作成」画面で「一から作成」オプションを選択
    4. 「基本的な情報」タブ「関数名」に「sample-serverless-lambda」と記入
    5. 「ランタイム」を「python 3.7」に設定
    6. 「アクセス権限」-「実行ロールの選択または作成」メニューを押下し
        「実行ロール」ラジオボタン - 「既存のロールを使用する」を選択
    7. 「既存のロール」メニューから、先ほど作成した「sample-s3-lambda-role」を選択し「関数の作成」を押下

6. テスト
    1. 「sample-serverless-lambda」のコンソール画面 - 「設定」タブの「テスト」ボタンを押下
    2. 「テストイベントの設定」モーダル-「イベント名」テキストボックスに「helloworld」と記入し「作成」
    3. 「テスト」ボタンの左隣のテキストぼっく（テストイベント名）が「helloworld」となっていることを確認し「テスト」ボタンを押下
    4. テスト結果が正常に返ってくることを確認

7. Lambdaの設定
    1. 「sample-serverless-lambda」のコンソール画面 - 「設定」タブの「関数コード」-「コードエントリタイプ」を「コードをインラインで編集」に設定
    2. 「ランタイム」を「Python 3.7」に設定
    3. 「ハンドラ」を「lambda_function.lambda_handler」に設定
    4. デフォルトで作成されている「lambda_function」のファイル名を「test_lambda_function.py」に変更する
    5. インラインエディターに新規ファイルを作成しファイル名を「lambda_function」とする
    6. Git Hubからダウンロードした「lambda_function.py」のコードをコピー＆ペーストし保存する
    7. 「Designer」メニューを開き「トリガーを追加」ボタンを押下
    8. 「トリガーを追加画面」-「トリガーの設定」-「トリガーを選択」メニューから「S3」を選択
    9. 「バケット」に「sample-serverless-s3」を設定
    10. 「イベントタイプ」に「全てのオブジェクト作成イベント」を設定
    11. 「プレフィックス」に「input/」を設定
    12. 「サフィックス」に「.csv」を設定
    13. 「トリガーの有効化」のチェックボックスにチェックをつける
    14. 「追加」ボタンを押下

8. 実行
    1. sample-serverless-s3のコンソール画面を開く
    2. 「input」フォルダ内に移動しGit Hubからダウンロードした「sample_data.csv」をアップロード
    3. 「output」フォルダ内に移動しjsonファイル（sample_data.json）が作成されているのを確認する
    4. 「sample_data.json」をダウンロードし正しく変換されていることを確認する

9. ログ確認
    1. CloudWatchLogsのコンソール画面を開く
    2. 「ダッシュボード」 - 「ログ」-「ロググループ」に移動し、検索窓で「/aws/lambda/sample-serverless-lambda」を検索
    3. ヒットしたロググループのコンソール画面に移動
    4. 該当するイベント時刻のログストリームを選択
    5. ログ画面右上にある日付メニュ－を押下し、「UTC」と書かれたプルダウンメニューを押下後「現地タイムゾーン」に設定し「適用」
    6. 実行した日付時刻のログを確認し、処理が正常に行われたことを確認する

# Author
* nmotoki
 
# License
 
"sample_serverless" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
 
