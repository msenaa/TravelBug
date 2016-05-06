from flask import Flask, render_template
import os


app = Flask(__name__);


@app.route('/')
@app.route('/home')
@app.route('/home')
def home():
   return render_template('/home.html')

@app.route('/AboutMe')
@app.route('/AboutMe')
def AboutMe():
   return render_template('/AboutMe.html')

   
@app.route('/Places')
@app.route('/Places')
def Places():
   return render_template('/Places.html')

@app.route('/comment')
@app.route('/comment')
def comment():
   return render_template('/comment.html')
   

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)