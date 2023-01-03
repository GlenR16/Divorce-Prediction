from django.shortcuts import render,redirect
from .models import Data
from django.views.decorators.csrf import csrf_exempt

# import the pickle model here 

def index(request):
    return render(request,"index.html")

def form(request):
    return render(request,"form.html",{"range":range(1,55)})

@csrf_exempt
def result(request):
    if request.method=="POST":
        data = dict(request.POST.items())
        #predict outcome variable
        outcome=True
        new_data = Data(prediction=outcome)
        new_data.set_data(data)
        new_data.save()
        return render(request,"result.html",{"outcome":outcome})
    else:
        return redirect("form")