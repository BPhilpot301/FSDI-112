from django.shortcuts import render
from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
)
from .models import Post, Status
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin,
)

class PostListView(ListView):
    template_name = "posts/list.html"
    #model = Post
    context_object_name = "post_list"
    status = Status.objects.get(name="published")
    queryset = Post.objects.filter(status=status).order_by("created_on").reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return(context)

class PostDraftListView(LoginRequiredMixin, ListView):
    template_name = "posts/draft_list.html"
    context_object_name = "draft"
    status = Status.objects.get(name="draft")
    queryset = Post.objects.filter(status=status).order_by("created_on").reverse()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_posts = context['draft'].filter(author=self.request.user)
        context['draft'] = draft_posts
        return context


class PostArchivedListView(LoginRequiredMixin, ListView):
    template_name = "posts/archived_list.html"
    context_object_name = "archived"
    status = Status.objects.get(name="archived")
    queryset = Post.objects.filter(status=status).order_by("created_on").reverse()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_posts = context['archived'].filter(author=self.request.user)
        context['archived'] = draft_posts
        return context
# Create your views here.

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "posts/detail.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)