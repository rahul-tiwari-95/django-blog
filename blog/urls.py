from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = "post_list")
]

# we will call the post_list function from views -- since we imported all the functions inside view by using the dot operator