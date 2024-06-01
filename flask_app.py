

from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def homepage():
    return render_template('pages/index.html')


@app.route('/projects')
def projectspage():
    return render_template('pages/projects.html')


@app.route('/about')
def aboutpage():
    return render_template('pages/about.html')


@app.route('/contact')
def contactpage():
    return render_template('pages/contact.html')


@app.route('/projects/epimetheus')
def epimetheus():
    return render_template('pages/epimetheus.html')


@app.route('/projects/intesavincente')
def intesavincente():
    return render_template('pages/intesavincente.html')


@app.route('/projects/dardos')
def dardos():
    return render_template('pages/dardos.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


if __name__ == '__main__':
    app.run(debug=True)
