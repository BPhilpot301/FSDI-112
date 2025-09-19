from django.urls import path, include 
from .views import MessageListView


urlpatterns = [
    path ("", MessageListView.as_view(), name="message-list"),
    path("messages/", include("messageboard.urls")),
]