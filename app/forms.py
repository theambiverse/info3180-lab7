from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class UploadForm(FlaskForm):
    photo=FileField(validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images only!')])

     description = StringField('Description', validators=[InputRequired()])