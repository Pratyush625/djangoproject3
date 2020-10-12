from django import forms
from testapp.models import Student
from django.core import validators #Implicit validator
'''
# creating your own validators
def starts_with_d(value):
    if value[0].lower() !='d': # if you dont want to consider case sensitive
        raise forms.ValidationError('Name should starts with small or capital d or D')

# Name contain alphabet symbol only
def contain_alphabet(value):
    if value.isalpha() != True:
        raise forms.ValidationError('Name should contain only alphabet symbol')

# Mail Id should be gmail
def gmail_verification(value):
    if value[len(value)-9:] !='gmail.com':
        raise forms.ValidationError('Must be gmail')

class StudentfeedbackForm(forms.Form):
    name=forms.CharField(validators=[contain_alphabet])
    rollno=forms.IntegerField()
    email=forms.EmailField(validators=[gmail_verification])
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(20),validators.MinLengthValidator(5)])

# Simultaneously using own validation method and clean method for email field
    def clean_email(self):
        inputemail=self.cleaned_data['email']
        print('validating email')
        return inputemail


    Explicit validation by User using clean method(clean_filledname())
    def clean_name(self):
        inputname=self.cleaned_data['name']
        print('validating name')
        if len(inputname)<4:
            raise forms.ValidationError('The length of name field should >=4')
        return inputname

    def clean_rollno(self):
        inputrollno=self.cleaned_data['rollno']
        print('validating rollno')
        return inputrollno

    def clean_email(self):
        inputemail=self.cleaned_data['email']
        print('validating email')
        return inputemail

    def clean_rollno(self):
        inputrollno=self.cleaned_data['rollno']
        print('validating rollno')
        return inputrollno

    def clean_feedback(self):
        inputfeedback=self.cleaned_data['feedback']
        print('validating feedback')
        return inputfeedback
'''
# Using Single clean method( all validation at one time)

class StudentfeedbackForm(forms.ModelForm):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Student
        fields='__all__'

    def clean(self):
        print('Total Validation....')
        cleaned_data=super().clean()

        inputpwd=cleaned_data['password']
        if len(inputpwd) <6:
            raise forms.ValidationError('Password should contain atleast 6 characters')

        inputpwd=cleaned_data['password']
        inputrpwd=cleaned_data['rpassword']
        if inputpwd !=inputrpwd:
            raise forms.ValidationError('Password not matched')

        inputname=cleaned_data['name']
        if len(inputname) <4:
            raise forms.ValidationError('Name should contain minimum 6 characters')

        inputrollno=cleaned_data['rollno']
        if len(str(inputrollno)) !=3:
            raise forms.ValidationError('Roll no should contain exactly 3 digits')

        inputemail=cleaned_data['email']
        if inputemail[len(inputemail)-9:] !='gmail.com':
            raise forms.ValidationError('Email must be gmail')

        inputfeedback=cleaned_data['feedback']
        if len(inputfeedback) <15:
            raise forms.ValidationError('The characters should >15')
