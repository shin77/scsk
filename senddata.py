#!/usr/bin/python3

#SQL操作モジュール読み込む
import SQLlib
import numpy as np
import cgi
#import cgitb
##cgitb.enable()

#よく使う個人情報の名称をリストとして定義しておく
info_list= [ ['name',             '姓名'],
             ['year/month/day',   '生年月日'],
             ['gender',           '性別'],
             ['phone1',           '電話番号'],
             ['phone2',           '電話番号'],
             ['email',            'E-mail'],
             ['pref_id',          '住所都道府県'],
             ['town',             '市区町村']]

web_list=   [ ['website',          'provider_name'],
            ['url',              'URL']]
#             ['user_id',          'user_code'],
#             ['password',         'password'],

#POSTメソッド送られてきたデータを受け取る
form = cgi.FieldStorage()
#ユーザ情報を受け取る
user_code=form.getfirst('user_id')
password=form.getfirst('password')
#個人情報を受け取る
info_data={}
for i in range(len(info_list)):
    if info_list[i][0] == 'year/month/day':
        if form.getfirst('year') is not None:
            info_data[info_list[i][1]] = form.getfirst('year') \
                    + "/" + form.getfirst('month') \
                    + "/" + form.getfirst('day')
    elif info_list[i][0] == 'phone1':
        if form.getfirst('phone1-1') is not None: 
            info_data[info_list[i][1]] = form.getfirst('phone1-1') \
                    + form.getfirst('phone1-2') \
                    + form.getfirst('phone1-3')
    elif info_list[i][0] == 'phone2':
        if form.getfirst('phone2-1') is not None: 
            info_data[info_list[i][1]] = form.getfirst('phone2-1') \
                    + form.getfirst('phone2-2') \
                    + form.getfirst('phone2-3')
    elif info_list[i][0] == 'email':
        if form.getfirst('email') is not None:
            info_data[info_list[i][1]] = form.getfirst('email') \
                    + "@" + form.getfirst('domain') 
    else:
        data = form.getfirst(info_list[i][0])
        if data is None:
            continue
        else:
            info_data[info_list[i][1]] = data
#企業データを受け取る
provider_name = form.getfirst('website')
URL = form.getfirst('url')

#DBに接続
conn = SQLlib.connect_personalDB()
cursor = conn.cursor()
#個人情報をデータベースに追加
test = []
for i in range(len(info_list)):
    #個人情報をデータベースに追加
    if info_list[i][1] in info_data:
        data = info_data[info_list[i][1]]
        test.append([user_code, info_list[i][1],data])
        per_id = SQLlib.insert_info(cursor, user_code, info_list[i][1], data)
        #個人情報を企業と結び付ける
        SQLlib.provide(cursor, user_code, per_id, provider_name, URL)
#コミットして更新を反映する
conn.commit()
#DBから切断
SQLlib.close_DB(conn)
#
##HTML生成
html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>完了</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="save.css" />
    </head>
    
    <body>
		<header>
			<div class="container">
				<div class="icon">
					<img src="images/icon1.png" width="150" alt="toro's picture">
				</div>
				<div class="info">
					<h1>Viewformation</h1><br>
					<h2>いつでもどこでもあなたに情報を。</h2><br>
					<h2>データ管理にお困りのあなたに寄り添います</h2>
				</div>
			</div>
			
		</header>
    
		<main>
		<div class="textbody">
			<div class="returnbutton"><a href="home.html">HOMEへ</a></div>
		</div>
		</main>
    </body>
</html>
"""
print("Content-Type: text/html")
print("")
print(html)
