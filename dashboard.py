#!/usr/bin/python3

import SQLlib

html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Database</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link rel="stylesheet" href="/html/css/home.css" />
        <link rel="stylesheet" href="/html/css/style.css" > <!--多分ない-->

    <!-- Bootstrap core CSS -->
<link href="../html/assets/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    <link href="../html/dashboard.css" rel="stylesheet">
  </head>
  <body>
		<header>
			<div class="container mx-auto">
                                <div class="mx-auto">
				<div class="icon">
					<img src="/html/images/icon1.png" width="150" alt="toro's picture">
				</div>
				<div class="info">
					<h1>ViewFormation</h1><br>
					<p>あなたの大切な個人情報を管理します</p>
                                </div>
                                </div>
			</div>
		</header>

<div class="container-fluid">
  <div class="row">
      <div class="table-responsive">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th>UserID</th>
              <th>Info Name</th>
              <th>Info Value</th>
              <th>Register Date</th>
              <th>Company</th>
              <th>URL</th>
              <th>Provided Date</th>
            </tr>
          </thead>
          <tbody>
"""
conn = SQLlib.connect_personalDB()
cursor = conn.cursor()
user_code='testuser'
rows = SQLlib.get_user_info(cursor, user_code)
rowsHTML = ""
for r in rows:
    #test = test + "a%s" % ("test")
    rowHTML = f"""
                <tr>
                  <td>{user_code}</td>
                  <td>{r['info_name']}</td>
                  <td>{r['info']}</td>
                  <td>{r['register_date']}</td>
                  <td>{r['provider_name']}</td>
                  <td>{r['URL']}</td>
                  <td>{r['provide_date']}</td>
                </tr>"""
    rowsHTML = rowsHTML + rowHTML
SQLlib.close_DB(conn)

endHTML="""
          </tbody>
      </div>
    </main>
  </div>
</div>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
      <script>window.jQuery || document.write('<script src="../assets/js/vendor/jquery.slim.min.js"><\/script>')</script><script src="../assets/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/feather-icons/4.9.0/feather.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.3/Chart.min.js"></script>
        <script src="dashboard.js"></script></body>
</html>
"""
print("Content-type:text/html")
print("")
print(html+rowsHTML+endHTML)
