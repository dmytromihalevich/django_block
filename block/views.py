from django.shortcuts import render
from models import *
# Create your views here.

def post_list(request):
    posts = Post.objects.all()

    return render(request, template_name="index.html")

