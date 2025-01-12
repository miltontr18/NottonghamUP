from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


#Creating a Flask instance
app = Flask(__name__)
#app.config[]
#Create a Form class
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

#Creating a route decorator
@app.route('/')
def index():
    first_name = "John"
    stuff = "This is bold text"

    favourite_pizza = ["pepperoni", "cheese", "hawaiian", "mushroom", 41, 22]
    return render_template('index.html',
                           first_name = first_name,
                           stuff = stuff,
                           favourite_pizza = favourite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

#Creating name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    #Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('name.html', name=name, form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)