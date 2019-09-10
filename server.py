from flask import Flask, render_template, request, redirect, session
from random import randint

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        print(session['gold'])  
        session['activities'] = []

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_money():
    print(request.form) 
    gold = 0
    structure = ''
    # session['gold'] = 0
    if request.form['structure'] == 'farm':
        # random number between 10-20
        gold = randint(10, 20)
        structure = 'farm'
        session['gold'] += gold
        print(randint(10, 20))
    elif request.form['structure'] == 'cave':
        # random number between 5-10
        gold = randint(5, 10)
        structure = 'cave'
        session['gold'] += gold
        print(randint(5, 10))
    elif request.form['structure'] == 'house':
        # random number between 2-5
        gold = randint(2, 5)
        structure = 'house'
        session['gold'] += gold
        print(randint(2, 5))
    elif request.form['structure'] == 'casino':
        # random number betwwen 0-50 plus or minus
        gold = randint(-50, 50)
        structure = 'casino'
        session['gold'] += gold
        print(randint(-50, 50))

        # Print out a string and have it logged to the text area in green or red
        # Set the reset
      
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)