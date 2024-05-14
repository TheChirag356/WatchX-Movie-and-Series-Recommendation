from flask_wtf import FlaskForm

class LocationForm(FlaskForm):
    movies = ('Movies', allow_blank = True, get_label = 'Title')