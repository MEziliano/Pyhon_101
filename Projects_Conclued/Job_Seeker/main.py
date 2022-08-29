from scraping import get_jobs
from flask import Flask, render_template, request, redirect, send_from_directory
from save import save_to_csv

app = Flask('MaratonaScraping')

@app.route('/')
def mymymymy():
    return redirect('/search')

@app.route('/search')
def search():
  return render_template('search.html')

@app.route('/result')
def result():
  keyword = request.args.get('keyword')
  keyword = keyword.lower()
  if keyword:
    search_result = get_jobs(keyword)
    save_to_csv(search_result)
  else:
    return redirect('/')
  return render_template('result.html', jobs=search_result, keyword=keyword)

@app.route('/download/<filename>')
def download_file(filename):
  try:
    return send_from_directory('/home/runner/scraping-3/static', filename=f"{filename}.csv", as_attachment=True)
  except:
    return redirect('/')

#inicia o flask server
app.run(host='0.0.0.0')