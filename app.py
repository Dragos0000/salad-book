import os
from flask import Flask, flash, render_template, redirect, request, url_for, session

app = Flask(__name__)

@app.route('/')
def index():
    return 'flask app test OK'
    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
    