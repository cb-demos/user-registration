import os

from flask_wtf import FlaskForm
from python_freeipa import ClientMeta
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError

INVITE_CODE_ENV = os.environ.get("INVITE_CODE", "")
ELEVATED_INVITE_CODE_ENV = os.environ.get("ELEVATED_INVITE_CODE", "")

client = ClientMeta(os.environ.get("LDAP_SERVER"), verify_ssl=False)
client.login(os.environ.get("LDAP_ADMIN"), os.environ.get("LDAP_PASSWORD"))


class SignupForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    first_name = StringField("First name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    if INVITE_CODE_ENV:
        invite_code = StringField("Invite code", validators=[DataRequired()])

    def validate_email(self, email):
        if "@cloudbees.com" not in email.data:
            raise ValidationError(
                "You must sign up with your CloudBees email account."
            )

    def validate_username(self, username):
        user = client.user_find(username.data)
        if user["count"] != 0:
            raise ValidationError(
                f"Username {username.data} already exists, please use another."
            )
        if "@" in username.data:
            raise ValidationError(
                f"Invalid symbol in username {username.data}. Special characters like @ aren't allowed in the username. You "
                f"can use the part before the @ in your email as your username. "
            )

    def validate_invite_code(self, invite_code):
        if invite_code.data == INVITE_CODE_ENV:
            return
        if invite_code.data == ELEVATED_INVITE_CODE_ENV:
            return
        else:
            raise ValidationError("Invite code is incorrect!")
