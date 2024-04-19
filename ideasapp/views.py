from django.shortcuts import render, HttpResponse
from .models import Feedback

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def feedback(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        # title=request.POST["title"]
        feedback=request.POST["feedback"]
        obj=Feedback(name=name, email=email, feedback=feedback)
        obj.save()
        return HttpResponse("<h1> Idea has been submitted </h1>")
        
        # print(f"Name: {name}, Email: {email}, Feedback: {feedback}")
        
    return render(request,'feedback.html')