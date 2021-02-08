from flask import Flask, render_template, request, url_for, redirect,after_this_request
from image import MemeCreator
import requests
import os


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST' and request.form['meme']:
		text_meme = request.form['meme'].replace('\r','').replace('\n','')
		MemeCreator.draw_meme_with_text(output_file_name=text_meme, text=text_meme,center_x=True,center_y=True)
		return render_template('index.html',meme=text_meme + '.jpg')
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
