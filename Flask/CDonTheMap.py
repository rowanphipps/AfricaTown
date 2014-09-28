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

	BUSINESSES = json.load(open('data/businesses.json'))
	HISTORY = json.load(open('data/historical_landmarks.json'))
	COMMUNITY = json.load(open('data/community_institutions.json'))


	

	@app.route('/')
	def home():

		return render_template('home.html')

	@app.route('/history')
	def history():
		print "history basic"
		return render_template('list.html', toList=HISTORY['results'], genre='history')

	@app.route('/community')
	def community():
		print "community"
		return render_template('list.html', toList=COMMUNITY['results'], genre='community')


	@app.route('/history/map')
	def historymap():
		print "historymap"
		return render_template('map.html', mode='history')


	@app.route('/community/map')
	def communitymap():
		print "orgmap"
		return render_template('map.html', mode='community')

	@app.route('/businesses')
	def businesses():
		print "businesses"
		return render_template('list.html', toList=BUSINESSES['results'], genre='business')

	@app.route('/businesses/map')
	def businessmap():
		print "businessmap"
		return render_template('map.html', mode='business')

	@app.route('/about')
	def about():
		print "about"
		return render_template('about.html')


	@app.route('/<Genre>/<ID>')
	def detail(Genre=None, ID=None):

		out = None
		
		res = []
		if Genre=='history':
			res = HISTORY['results']

		elif Genre=='community':
			res = COMMUNITY['results']

		elif Genre=='business':
			res = BUSINESSES['results']

		for i in res:

			if i['id'] == ID:
				out = i
				break

		return render_template('detail.html', place=out)







	return app




if __name__ == '__main__':

	# app.run(debug=True)
	create_app().run(debug=True)
