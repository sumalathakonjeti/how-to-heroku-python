from flask import Flask

pagehtml = """
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The Schooner</title>
  <meta name="description" content="The Schooner">
  <meta name="author" content="Kristofer">

<style>
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  line-height: 1.6;
  color: #303030;
  max-width: 40rem;
  padding: 2rem;
  margin: auto;
  background: #FEF4FF;
}
img {
  max-width: 100%;
}
a {
  color: #2ECC40;
}
h1, h2, strong {
  color: #303030;
}
</style>
</head>

<body>
  <h2>The Python</h2>
  <p><img src="https://image.shutterstock.com/image-vector/vector-illustration-icon-python-programming-260nw-1397241389.jpg"</p>
<p>This is a Python.</p>


</body>
</html>
"""
app = Flask(__name__)

@app.route("/")
def hello():
    return pagehtml
