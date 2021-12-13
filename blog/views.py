from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
           
def main_page(request):
    posts = Post.objects.all().order_by('publisheg_date')
    context = {
        'posts': posts, 
    }
    return render(request, 'main_page.html', 'isus.css',  context)
