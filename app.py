from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world(language="de"):
    return render_template('de/index-de.html')

@app.route('/Einkehr/<language>')
def einkehr(language="de"):
    return render_template('de/einkehr-de.html')

@app.route('/Produkte/<language>')
def produkte(language="de"):
    return render_template('de/produkte-de.html')

@app.route('/Speißekarte/<language>')
def speißen(language="de"):
    return render_template('de/speiße-de.html')

@app.route('/QA/<language>')
def qa(language="de"):
    return render_template('de/qa-de.html')

@app.route('/Kontakt/<language>')
def kontakt(language="de"):
    return render_template('de/kontakt-de.html')

@app.route('/Impressum/<language>')
def impressum(language="de"):
    return render_template('de/impressum-de.html')

@app.route('/Datenschutz/<language>')
def datenschutz(language="de"):
    return render_template('de/datenschutz-de.html')


if __name__ == '__main__':
    app.run(debug=True)
