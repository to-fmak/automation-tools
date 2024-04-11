# Overview
- Qiita Organizationの記事を一括でファボるスクリプト

# Usage
- Qiitaアカウントの設定画面でアクセストークンの取得する
- ライブラリをインストールする
```bash
$ pip3 install -r requirements.txt
```
- Qiita OrganizationとACCESS_TOKENの環境変数にセットする
```bash
$ export ORG_ID=xxx
$ export ACCESS_TOKEN=xxxxxxxx
```
- スクリプトを実行する
```bash
$ python3 main.py
```

- responseの例
```
5a60e7dc4b43654181f9
{"message":"Already liked","type":"already_liked"}
147ba578b83b8d7a8c93
{"message":"Already liked","type":"already_liked"}
2da21e6e3ee3bd542e92
ebae7787546716957ff0
6dfa48ee22c724f408c6
f4295840833156f0af29
16f1712580c2e7c81080
6638dea4521c8f50517f
...
...

```