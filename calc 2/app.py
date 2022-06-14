# importing modules
from flask import Flask, render_template , request

# creating app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return render_template('index.html')

# /kimtomi route
@app.route('/kimtomi',methods=['GET','POST'])
def kimtomi():
    # if the POST reuest is made then this block is executed
    if request.method == 'POST':
        # getting value of the input field
        number = float(request.form.get('kilometer'))
        #  converting the kilometer to miles
        result = number * 0.5293160546162113
        # sending result to template
        return render_template('kimtomi.html',result=round(result,5))
    # This run if the get request is made
    return render_template('kimtomi.html')

# /mitokim route
@app.route('/mitokim',methods=['GET','POST'])
def mitokim():
    # if the POST reuest is made then this block is executed
    if request.method == 'POST':
        # getting value of the input field
        number = float(request.form.get('miles'))
        #  converting the miles to kilometer 
        result = number * 1.8892304347826088
        # sending result to template
        return render_template('mitokim.html',result=round(result,5))
    # This run if the get request is made
    return render_template('mitokim.html')


if __name__ == '__main__':
    app.run(debug=True)
