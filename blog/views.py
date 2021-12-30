from django.shortcuts import render
from .models import Post
from django.utils import timezone

#we just defined post_list function which we have used in urls.py --> since this is the view --> we need to encode the template

def post_list(request):

    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    allposts = Post.objects.all()

    #this function simply fetches all data of all posts and stores it into 'allposts'
    return render(request, 'blog/post_list.html', {'posts': allposts})


# Create your views here.
# we used {'posts' : posts} code to refrence it  we have learnt this in Angular and reactJS --> I am assuming that
# we will be using posts in the html file which we have created inside tempaltes --> blog --> post_list.html

