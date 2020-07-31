from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView  # templateview
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):  # listviewは全体を表示できる
    template_name = 'list.html'
    model = TodoModel


class TodoDetail(DetailView):  # detailviewは１つずつ表示できる
    template_name = 'detail.html'
    model = TodoModel


class TodoCreate(CreateView):  # detailviewは１つずつ表示できる
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')  # どのを持ってくるか指定、modelに記載されいているもの
    success_url = reverse_lazy('list') # データの作成完了した時に飛ぶURL、classBaseはreverse_lazy(funcはreverse)

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list') 

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list') 
