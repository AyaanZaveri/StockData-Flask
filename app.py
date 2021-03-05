from flask import Flask, render_template, session
from flask import request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = "asdf"

if __name__ == "__main__":
    app.run()

@app.route('/', methods=['GET','POST'])

def process():
  name = request.form.get('name','')
  session['name'] = name

  return render_template('index.html', name=name)
  
if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5000)