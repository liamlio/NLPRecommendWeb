from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class QueryForm(FlaskForm):
    query = TextAreaField('Query/Abstract',
    validators=[DataRequired(), Length(min=1)])

    top_k= IntegerField('Number of Recommended Papers',
    validators=[DataRequired(), NumberRange(min=1, max=10)])

    submit = SubmitField('Generate Recommendations')
