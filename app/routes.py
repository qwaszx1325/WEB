from flask import render_template, flash

from app import app, bcrypt, db
from froms import RegisterForm
from models import User




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data)
        email = form.email.data
        phone = form.phone.data
        address = form.address.data
        user = User(username=username, email=email, password=password, phone=phone,)
        db.session.add(user)
        db.session.commit()
        flash('Congrats, registration success', category='success')

    return render_template('register.html', form=form)
