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
  session['name'] = name.title()

  if name == '':
      name = 'bitcoin'.title()

  url = "https://coinmarketcap.com/currencies/" + name

  print(url)

  r = requests.get(url)  

  soup = BeautifulSoup(r.text, 'html.parser')  

  cryptoname = soup.find('p', {
      'class': 'sc-AxhUy ghbWav converter-item-name'
  }).text
  

  cryptoval = soup.find('div', {'class':   'priceValue___11gHJ'}).text  

  cryptostrip = cryptoval[1:]  

  print(cryptoname + ': ' + cryptostrip + ' USD')

  name.title()

  return render_template('index.html', data=cryptostrip, name=name)
  
if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5000)