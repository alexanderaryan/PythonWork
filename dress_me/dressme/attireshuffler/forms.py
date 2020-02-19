from dress_me.dressme import StringField,FlaskForm,DataRequired,SubmitField,\
    FormField, FieldList, Form, SelectMultipleField
from datetime import datetime


def present_or_future_date(value):

    if value < datetime.date.today():
        raise FlaskForm.ValidationError("The date cannot be in the past!")
    return value

"""class MaleForm(FlaskForm):

    shirt = StringField("Shirt",validators=[DataRequired()])
    pants = StringField("Pants", validators=[DataRequired()])
    submit = SubmitField("I am done!")"""


class ShuffleForm(FlaskForm):

    #from_date = DateField('From', format='%Y-%m-%d', validators=[present_or_future_date])
    #to_date = DateField('To', format='%Y-%m-%d',validators=[present_or_future_date])
    from_date = StringField('From')
    to_date = StringField('To' )
    weekends = SelectMultipleField("Your Weekends",\
                                   choices=[(0, 'Monday'), (1,'Tuesday'), ( 2,'Wednesday'),\
                                                             ( 3,'Thursday'),(4,'Friday'),(5,'Saturday'),\
                                                             (6,'Sunday')])
    submit = SubmitField('Remove')


class MaleForm(Form):

    shirt = StringField("Shirt")
    pants = StringField("Pants")


class MainMaleForm(FlaskForm):

    attires = FieldList(
        FormField(MaleForm),
        min_entries=1,
        max_entries=100
    )
    submit = SubmitField("I am done!")


class FemaleForm(Form):

    attire = StringField("Attire",validators=[DataRequired()])
    from_date = StringField("From")
    to_date = StringField("To")


class MainFemaleForm(FlaskForm):

    attires = FieldList(
        FormField(FemaleForm),
        min_entries=1,
        max_entries=100
    )
    submit = SubmitField("I am done!")

