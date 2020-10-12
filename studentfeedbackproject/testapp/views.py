from django.shortcuts import render
from testapp.forms import StudentfeedbackForm
from testapp.models import Student
# Create your views here.
def thankyou_view(request):
    students=Student.objects.all()
    return render(request,'testapp/thankyou.html',{'students':students})

def feedback_view(request):
    form=StudentfeedbackForm()
    if request.method=="POST":
        form=StudentfeedbackForm(request.POST)
        #Implicit validation by using Django's inbuilt validators
        if form.is_valid():
            print("validation done successfully and printing the data")
            print("Student name:",form.cleaned_data['name'])   # cleaned_data is a dictionary, end user provided data is always available inside dictionary
            print("Student Rollno:",form.cleaned_data['rollno'])
            print("Student Email:",form.cleaned_data['email'])
            print("Student Feedback:",form.cleaned_data['feedback'])
            form.save(commit=True)
            return thankyou_view(request)
    return render(request,'testapp/feedback.html',{'form':form})
