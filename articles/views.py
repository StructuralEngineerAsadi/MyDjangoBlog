from django.shortcuts import render
from . import models
# Create your views here.
def articles_list(request):
    articles = models.Marticle.objects.all().order_by('date')
    args = {'articles':articles}
    return render(request , 'articles/articlesList.html',args)