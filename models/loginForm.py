from wtforms import Form, BooleanField, StringField, PasswordField, validators

class LoginForm(Form):
    email = StringField('Email', [
        validators.DataRequired("Email Address is Required."),
        validators.Length(min=4, max=254),
        validators.Email("Enter a Valid Email")
        ])
    password = PasswordField('Password', [
        validators.DataRequired("Password is Required."),
        validators.Length(min=8,message="Password should atleast be 8 characters long."),
        validators.Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",message="Password must contain a Uppercase letter, a Special Character and a Number.")
    ])