#! /usr/bin/python3
import cgi
# cgiはcgiプログラムに使うモジュールだ。
import cgitb
# cgitbはcgiプログラムデバッグに関するモジュールだ。(エラーが発生すればphpみたいにエラーを画面に表示する。)
cgitb.enable()
# パラメータを取得するための関数
# get、post区分なしでデータを持ち込む。
form = cgi.FieldStorage()
# パラメータdataを取得する。
data = form.getvalue('data')
# パラメータのtestを取得する。
test = form.getvalue('test')
# 画面い応答するhtmlドキュメント
html = f"""
<!DOCTYPE html>
<html>
<head><title>python</title></head>
  <body>
    <form method='post'>
      <input type='text' name='test' value='hello'>
      <input type='submit'>
    </form>
    <br />
    data - {data} <br />
    test - {test} <br />
  </body>
</html>
""";
# ヘッダータイプ設定
print("Content-type:text/html")
# httpプロトコールでheaderとbodyの区分は改行なので必ず入れる。なければエラーに発生する。(bodyがないhttpファイルなので)
print('')
print(html)
