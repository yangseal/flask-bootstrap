#coding:utf8
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return u"hello world"

@app.route("/test")
def test():
    return "Hello Flask"

@app.route("/test/<name>")
def test02(name):
    return  "Hello : " + name


@app.route("/templa")
def testTemp():
    title = "测试模版"
    name  = "tom"
    pages = {"page":'10', 'total':'20'}
    return  render_template('template1.html', title=title, name=name, pages=pages)



if __name__=='__main__':
    app.run(debug=True)