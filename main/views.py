from django.shortcuts import render
from main.models import Post
from django.utils. import timezone

# Create your views here.
def post_ist (request):

	posts = Post.objects.filter(published_date__lte=timezone.now()).orderby('published_date')

	return render(request,"post_ist.html",context{})

