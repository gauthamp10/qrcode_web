from flask import Flask, render_template, request, send_file
from flask_qrcode import QRcode

import gunicorn

app = Flask(__name__)
qrcode = QRcode(app)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404 
    
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/",methods=['GET','POST'])
def home_post():
    data = request.form['data']
    return render_template('index.html',text=data,appear='QRCode for: ')

@app.route("/about")
def about():
    return "Hi...there. Nothing special just a simple QRCode generator build for my convenience. Contact me @ gauthamp10@gmail.com"

   
    
if __name__ ==  '__main__':
    app.run(host='0.0.0.0',debug=True)