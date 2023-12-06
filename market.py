
from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about/<username>')
def about_page(username):
     return f'<h1> This is the abot page of {username} </h1>'

@app.route('/market')
def market_page():
     items = [
{'id':1 ,'name':'phone','barcode':2345345,'price':500},
{'id':2 ,'name':'laptop','barcode':243573647,'price':900},
{'id':3 ,'name':'keyboard','barcode':3568737,'price':150}]
     return render_template('market.html',items=items)

if __name__ == "__main__":
     app.run(debug=True)