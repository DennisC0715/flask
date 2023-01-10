from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, ValidationError
from flask_bootstrap import Bootstrap

def validate_email(form, field):
    if len(field.data) < 4:
        raise ValidationError('Name must be more than 4 characters')


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), validate_email])
    password = PasswordField(label='Password', validators=[DataRequired(), InputRequired()])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "dennis"




@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "chensuyuan1989@hotmail.com" and login_form.password.data == "123456":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=login_form)




if __name__ == '__main__':
    app.run(debug=True)
