from django.shortcuts import render, HttpResponse

def about(request):
    # return HttpResponse('Hello guys: about')
    return render(request, 'about.html')

def home(request):
    # return HttpResponse('Hello boys: home')
    return render(request, 'Home.html')

