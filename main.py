from flask import Flask,render_template,request,url_for
import pandas as pd
import os

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
	if request.method == 'POST' and request.form['btn']=='Upload':
		print(request.form['btn'])
		f=request.files['file']
		filename = f.filename

		if filename.split('.')[1] == 'csv':
			df=pd.read_csv(f,encoding= 'utf-8')
		elif filename.split('.')[1] == 'xlsx':
			df=pd.read_excel(f,encoding='utf-8')
		else:
			return "please upload CSV or Excel"

	folder_files = os.listdir(os.curdir)	
	
	if request.method == 'POST' and request.form['btn']=='submit':
		print(request.form.getlist('mycheckbox'))
	return render_template("index.html",len=len(folder_files),folder_files=folder_files)


if __name__ == '__main__':
	app.run(host="127.0.0.1",port=8080,debug=True)