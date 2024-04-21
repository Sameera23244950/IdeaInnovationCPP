from django.shortcuts import render, HttpResponse
from .models import Feedback
from numbers_properties_pkg import numbers_properties


# Create your views here.
def index(request):
    app_name = "ideasapp"  # Your Django app name
    model_name = "Feedback"  # The model name within your app
 
    count = numbers_properties.FeedbackCounter.count_titles(app_name,model_name)
    return render(request, 'index.html', {'feedback_count': count})


def feedback(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        title=request.POST["title"]
        feedback=request.POST["feedback"]
        
        obj=Feedback(name=name, email=email, title=title, feedback=feedback)
        obj.save()
        return HttpResponse("<h1> Idea has been submitted </h1>")

    return render(request,'feedback.html')