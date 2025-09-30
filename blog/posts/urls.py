from django.urls import path
from .views import (
    PostListView,
    PostDraftListView,
    PostArchivedListView,
    PostCreateView,
    PostDetailView,
 ) 

urlpatterns = [
        path('list/', PostListView.as_view(), name='posts'),
        path('drafts/list/', PostDraftListView.as_view(), name='draft_list'),
        path('archived/list/', PostArchivedListView.as_view(), name='archived_list'),
        path('new/', PostCreateView.as_view(), name='new'),
        path('<int:pk>/', PostDetailView.as_view(), name="post_detail"), 
]