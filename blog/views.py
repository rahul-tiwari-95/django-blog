from django.shortcuts import render

#we just defined post_list function which we have used in urls.py --> since this is the view --> we need to encode the template

def post_list(request):
    return render(request, 'blog/post_list.html', {})

# Create your views here.