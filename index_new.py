#!/usr/bin/python3

import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Title</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!--<link rel="stylesheet" href="uikit2.css" /> -->
        <link rel="stylesheet" href="css/style.css" > <!--多分ない-->
        <script src="uikit.min.js"></script>
        <script src="uikit-icons.min.js"></script>
        
        
        <style>
            
html,body{
	font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
	font-size:16px;
	font-weight:400;
	line-height:1.5;   -webkit-text-size-adjust:100%;
	background:#fff;
	color: #800000;
	height: 100%;
	margin: 0px;
}

body{
	width: 100%;
	padding-top: 100px;
	padding-left: 30%;
	text-align: left;
	background-color: #e6e6fa;
	background-position: center center;
	background-size: cover;
	background-repeat: no-repeat;
	/*background-image: url("images/img1.jpg");*/
}

/*見出し*/
h1 {
  color: white;/*文字色*/
  padding: 0.5em;/*文字周りの余白*/
  display: inline-block;/*おまじない*/
  line-height: 1.3;/*行高*/
  background: #800000;/*背景色*/
  vertical-align: middle;
  border-radius: 25px 0px 0px 25px;/*左側の角を丸く*/
}
h1:before {
  content: '●';
  color: white;
  margin-right: 8px;
}


.m1{	margin-right: 50px;}
.m2{	margin-right: 85px;}
.m3{	margin-right: 35px;}
.m4{	margin-right: 35px;}
.m5{	margin-right: 83px;}
.m6{	margin-right: 50px;}
.m7{	margin-right: 88px;}
.m8{	margin-right: 50px;}
.m9{	margin-right: 50px;}
.m10{	margin-right: 5px;}
.m11{	margin-right: 83px;}
.m12{	margin-right: 130px;}

#save{
	margin-left: 200px;
}


        </style>
        
    </head>
    <body>
        
        <ul>
          <form method="POST" action="sample.cgi">
            
            <h1>あなたの情報を登録してください！</h1>
            
            <p><span class="m1">サイト名</span>：<input type="text" name="company"></p>
            <p><span class="m2">URL</span>：<input type="text" name="url" size="40"></p>
            <p><span class="m3">ユーザー名</span>：<input type="text" name="user" size="20"></p>
            <p><span class="m4">パスワード</span>：<input type="text" name="pwd"></p>
            <p><span class="m5">氏名</span>：<input type="text" name="name"></p>
            <p><span class="m6">生年月日</span>：
                <!--year-->
                <select name="year">
                    <option value="1980y">1970年</option>
                    <option value="1981y">1971年</option>
                    <option value="1982y">1972年</option>
                    <option value="1983y">1973年</option>
                    <option value="1984y">1974年</option>
                    <option value="1985y">1975年</option>
                    <option value="1986y">1976年</option>
                    <option value="1987y">1977年</option>
                    <option value="1988y">1978年</option>
                    <option value="1989y">1979年</option>
                    <option value="1980y">1980年</option>
                    <option value="1981y">1981年</option>
                    <option value="1982y">1982年</option>
                    <option value="1983y">1983年</option>
                    <option value="1984y">1984年</option>
                    <option value="1985y">1985年</option>
                    <option value="1986y">1986年</option>
                    <option value="1987y">1987年</option>
                    <option value="1988y">1988年</option>
                    <option value="1989y">1989年</option>
                    <option value="1990y">1990年</option>
                    <option value="1991y">1991年</option>
                    <option value="1992y">1992年</option>
                    <option value="1993y">1993年</option>
                    <option value="1994y">1994年</option>
                    <option value="1995y">1995年</option>
                    <option value="1996y">1996年</option>
                    <option value="1997y">1997年</option>
                    <option value="1998y">1998年</option>
                    <option value="1999y">1999年</option>
                    <option value="2000y">2000年</option>
                    <option value="2001y">2001年</option>
                    <option value="2002y">2002年</option>
                    <option value="2003y">2003年</option>
                    <option value="2004y">2004年</option>
                    <option value="2005y">2005年</option>
                    <option value="2006y">2006年</option>
                    <option value="2007y">2007年</option>
                    <option value="2008y">2008年</option>
                    <option value="2009y">2009年</option>
                    <option value="2010y">2010年</option>
                    <option value="2011y">2011年</option>
                    <option value="2012y">2012年</option>
                    <option value="2013y">2013年</option>
                    <option value="2014y">2014年</option>
                    <option value="2015y">2015年</option>
                    <option value="2016y">2016年</option>
                    <option value="2017y">2017年</option>
                    <option value="2018y">2018年</option>
                    <option value="2019y">2019年</option>
                    <option value="2020y">2020年</option>
                    <option value="2021y">2021年</option>
                    
                    </select>
                <!--month-->
                <select name="month">
                <option value="jan">1月</option>
                <option value="feb">2月</option>
                <option value="mar">3月</option>
                <option value="apr">4月</option>
                <option value="may">5月</option>
                <option value="jun">6月</option>
                <option value="jul">7月</option>
                <option value="aug">8月</option>
                <option value="sep">9月</option>
                <option value="oct">10月</option>
                <option value="nov">11月</option>
                <option value="dec">12月</option>
                </select>
                <select name="day">
                    <option value="d1">1日</option>
                    <option value="d2">2日</option>
                    <option value="d3">3日</option>
                    <option value="d4">4日</option>
                    <option value="d5">5日</option>
                    <option value="d6">6日</option>
                    <option value="d7">7日</option>
                    <option value="d8">8日</option>
                    <option value="d9">9日</option>
                    <option value="d10">10日</option>
                    <option value="d11">11日</option>
                    <option value="d12">12日</option>
                    <option value="d13">13日</option>
                    <option value="d14">14日</option>
                    <option value="d15">15日</option>
                    <option value="d16">16日</option>
                    <option value="d17">17日</option>
                    <option value="d18">18日</option>
                    <option value="d19">19日</option>
                    <option value="d20">20日</option>
                    <option value="d21">21日</option>
                    <option value="d22">22日</option>
                    <option value="d23">23日</option>
                    <option value="d24">24日</option>
                    <option value="d25">25日</option>
                    <option value="d26">26日</option>
                    <option value="d27">27日</option>
                    <option value="d28">28日</option>
                    <option value="d29">29日</option>
                    <option value="d30">30日</option>
                    <option value="d31">31日</option>
                    </select></p>
            
            <p><span class="m7">性別</span>:<input type="radio" name="gender" value="male" />男性
                <input type="radio" name="gender" value="female" checked/>女性
                <input type="radio" name="gender" value="other" checked/>その他</p>
            <p><span class="m8">電話番号</span>：<input type="text" name="tel" size="8">
                   - <input type="text" name="NAME" size="8">
                   - <input type="text" name="NAME" size="8"></p>
            <p><span class="m9">携帯番号</span>：<input type="text" name="tel2" size="8">
                   - <input type="text" name="NAME" size="8">
                   - <input type="text" name="NAME" size="8"></p>
            <p><span class="m10">メールアドレス</span>：<input type="text" name="email">@
                 <input list="emailadress" id="email" name="emailadress" />
                    <datalist id="emailadress">
                    <option value="ezweb.ne.jp">
                    <option value="softbank.ne.jp">
                    <option value="docomo.ne.jp">
                    <option value="gmail.com">
                    <option value="yahoo.co.jp">
                    </datalist>
            </p>
            <p><span class="m11">住所</span>：<select name="pref_id">
                <option value="" selected>都道府県</option>
                <option value="1">北海道</option>
                <option value="2">青森県</option>
                <option value="3">岩手県</option>
                <option value="4">宮城県</option>
                <option value="5">秋田県</option>
                <option value="6">山形県</option>
                <option value="7">福島県</option>
                <option value="8">茨城県</option>
                <option value="9">栃木県</option>
                <option value="10">群馬県</option>
                <option value="11">埼玉県</option>
                <option value="12">千葉県</option>
                <option value="13">東京都</option>
                <option value="14">神奈川県</option>
                <option value="15">新潟県</option>
                <option value="16">富山県</option>
                <option value="17">石川県</option>
                <option value="18">福井県</option>
                <option value="19">山梨県</option>
                <option value="20">長野県</option>
                <option value="21">岐阜県</option>
                <option value="22">静岡県</option>
                <option value="23">愛知県</option>
                <option value="24">三重県</option>
                <option value="25">滋賀県</option>
                <option value="26">京都府</option>
                <option value="27">大阪府</option>
                <option value="28">兵庫県</option>
                <option value="29">奈良県</option>
                <option value="30">和歌山県</option>
                <option value="31">鳥取県</option>
                <option value="32">島根県</option>
                <option value="33">岡山県</option>
                <option value="34">広島県</option>
                <option value="35">山口県</option>
                <option value="36">徳島県</option>
                <option value="37">香川県</option>
                <option value="38">愛媛県</option>
                <option value="39">高知県</option>
                <option value="40">福岡県</option>
                <option value="41">佐賀県</option>
                <option value="42">長崎県</option>
                <option value="43">熊本県</option>
                <option value="44">大分県</option>
                <option value="45">宮崎県</option>
                <option value="46">鹿児島県</option>
                <option value="47">沖縄県</option>
                </select><br>
                <span class="m12"></span><input type="text" name="email" placeholder="市区町村" size="60"></p><br>
            <p><input type="submit" value="保存" id="save"></p>
            <p> 
        </form>
    </body>
</html>
"""

print("Content-type:text/html")
print("")
print(html)