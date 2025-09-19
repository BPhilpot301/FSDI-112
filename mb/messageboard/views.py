from django.shortcuts import render, ListView
from .models import Message

class MessgeListView(ListView):
    model = Messagetemplate_name = "messageboard/message_list.html"
    context_object_name = "messages"
# Create your views here.
