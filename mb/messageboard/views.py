from django.urls import reverse_lazy
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        DeleteView,
        UpdateView,
)
from .models import Post
from django.contrib.auth.models import User
#CRUD -> create, read, update and delete app 
#The generic classes are ListView, CreateView, UpdateView, DeleteView and DetailView

# Create your views here.

#"""
#PostListView is going to retrieve all the object from the Post table in the db
#"""

class PostListView(ListView):
    #template_name attribute is going to render a specific html file
    template_name = "posts/list.html"
    #model is going to be from which table we want to retrieve the data
    model = Post 
    #queryset is used to define the model used for the view

    #queryset = Post.objects.all()

    #context is a python dictionary that holds the data for the generic views
    #and this context travels to the htmls
    #by defaul is the context name of ListView and DetailView is "object" or "object_list"

    #context_object_name would allow us to modifu the name and how to call it in the htmls
    context_object_name = "post_list"

#"""
#PostDetailView is going to retrieve a single element from the Post table in the db
#"""
class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post   
    context_object_name = "single_post"

#"""
#PostCreateView is going to allow us to create a new post and add it to the db
#"""
class PostCreateView(CreateView):
        template_name = "posts/new.html"
        model = Post
        fields = ["title","subtitle","body"]

        def form_valid(self, form):
            print(form)
            form.instance.author = User.objects.filter(is_superuser=True).first()
            return super().form_valid(form)
        
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/edit.html'
    fields = ['title', 'subtitle', 'body']