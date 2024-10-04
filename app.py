from flask import Flask,render_template,request
import requests
import os
from dotenv import load_dotenv

load_dotenv()  



app = Flask(__name__)

app.secret_key = "key"

@app.route('/')
def base():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={os.getenv('NEWS_API_KEY')}"
    r = requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('base.html', cases=case)

@app.route('/business')
def business():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={os.getenv('NEWS_API_KEY')}"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('business.html',cases = case)

@app.route('/entertainment')
def entertainment():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey={os.getenv('NEWS_API_KEY')}"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('entertainment.html',cases = case)

@app.route('/health')
def health():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey={os.getenv('NEWS_API_KEY')}"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('health.html',cases = case)

@app.route('/science')
def science():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey={os.getenv('NEWS_API_KEY')}"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('science.html',cases = case)

@app.route('/sports')
def sports():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey={os.getenv('NEWS_API_KEY')}"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('sports.html',cases = case)

@app.route('/technology')
def technology():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={os.getenv('NEWS_API_KEY')}"
    r= requests.get(url).json()
    case = {
        'articles': r['articles']
    }
    return render_template('technology.html',cases = case)

if __name__ == '__main__':
    app.run(debug=True)


 