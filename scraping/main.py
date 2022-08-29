from scraping import get_jobs
from flask import Flask, render_template, request, redirect

#Nota:
#No range do scraping (indeed.py) configurei para criar apenas 1 URL
#Isso para não demorar muitos os testes.
#Para pegar todos os resultados do indeed, basta mudar para 20 ;)

app = Flask('MaratonaScraping')

@app.route('/')
def mymymymy():
  return 'Olá Mundo'

@app.route('/search')
def search():
  return render_template('search.html')
  #https://tableless.github.io/iniciantes/manual/html/estruturabasica.html

@app.route('/result')
def result():
  keyword = request.args.get('keyword')
  keyword = keyword.lower()
  if keyword:
    search_result = get_jobs(keyword)
  else:
    return redirect('/')

  return render_template('result.html', jobs=search_result, keyword=keyword)

  
#inicia o flask server
app.run(host='0.0.0.0')