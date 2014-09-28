from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, abort

from flask_bootstrap import Bootstrap


import json

import time
import random
import pickle

DEBUG = True
def create_app():
	app = Flask(__name__)
	Bootstrap(app)


	@app.route('/')
	def home():

		return render_template('home.html')

	@app.route('/events')
	def events():
		print "events"
		return render_template('index.html')

	@app.route('/organizations')
	def organizations():
		print "organizations"
		return render_template('index.html')

	@app.route('/businesses')
	def businesses():
		print "businesses"
		return render_template('index.html')

	@app.route('/about')
	def about():
		print "about"
		return render_template('index.html')


	@app.route('/history')
	def history():
		print "history"
		return render_template('index.html')

	return app




if __name__ == '__main__':

    # app.run(debug=True)
    create_app().run(debug=True)