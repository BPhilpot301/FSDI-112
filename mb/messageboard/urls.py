from django.urls import path
from .views import PostListView #, PostDetailView

urlpatterns = [
        path('list/', PostListView.as_view(), name='posts'),
#        path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
#        path('new/', PostCreateView.as_view(), name="post_new")
]