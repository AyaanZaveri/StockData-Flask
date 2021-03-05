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

  url = "https://ca.finance.yahoo.com/quote/" + name

  url2 = 'https://ca.finance.yahoo.com/quote/'+ name +'/key-statistics'

  r = requests.get(url)
  s = requests.get(url2)

  soup = BeautifulSoup(r.text, 'html.parser')
  soup2 = BeautifulSoup(s.text, 'html.parser')


  lossgain = soup.find('div', {'class': 'D(ib) Mend(20px)' }).find_all('span')[1].text

  print(lossgain)

  price = soup.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)' }).text

  print(price)

  marketcap = soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)' }).find_all('span')[1].text

  print(marketcap)

  volume = soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)' }).find_all('span')[11].text

  print(volume)

  enterpriseval = soup2.find('tr', {'class': 'Bxz(bb) H(36px) BdB Bdbc($seperatorColor) fi-row Bgc($hoverBgColor):h'}).find_all('td')[1].text

  print(enterpriseval)

  return render_template('index.html', price=price, name=name)
  
if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5000)