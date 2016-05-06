#this is calling flask and importing it
from flask import Flask, render_template
import os


app = Flask(__name__);

#routes to the home html page
@app.route('/')
@app.route('/home')
@app.route('/home')
def home():
   return render_template('/home.html')

#routes to the about me html page
@app.route('/AboutMe')
@app.route('/AboutMe')
def AboutMe():
   return render_template('/AboutMe.html')

#routes to the places html page   
@app.route('/Places')
@app.route('/Places')
def Places():
   return render_template('/Places.html')

#routes to the comment html page
@app.route('/comment')
@app.route('/comment')
def comment():
   return render_template('/comment.html')
   
#it executes all of the code found in it
if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)