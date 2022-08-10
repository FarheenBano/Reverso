from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    return render(request,'index.html')

def job(request):
    # return HttpResponse("Hello")
    return render(request,'job.html')

def testing(request):
    # return HttpResponse("Hello")
    return render(request,'testing.html')


def fee(request):
    # return HttpResponse("Hello")
    return render(request,'fee.html')

def about(request):
    # return HttpResponse("Hello")
    return render(request,'about.html')


def contact(request):
    # return HttpResponse("Hello")
    return render(request,'contact.html')

def free(request):
    # return HttpResponse("Hello")
    return render(request,'free.html')