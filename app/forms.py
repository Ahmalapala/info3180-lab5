# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Regexp
from flask_wtf.file import FileField, FileAllowed, FileRequired

class MovieForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title.label = 'Movie Title'
        self.title.validators = [DataRequired(message='Please provide a movie title.')]
        self.description.label = 'Description'
        self.description.validators = [DataRequired(message='Please provide a description of the movie.')]
        self.poster.label = 'Movie Poster'
        self.poster.validators = [FileRequired(message='Poster is required'),
                                   FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')]
