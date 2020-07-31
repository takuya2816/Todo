
from django.urls import path
from .views import TodoList
from .views import TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view() ,name='detail'),  # <int:pk>はkeyの定義
    path('create/', TodoCreate.as_view() ,name='create'),  # <int:pk>はkeyの定義
    path('delete/<int:pk>', TodoDelete.as_view() ,name='delete'),  # 消すデータ番号を指定
    path('update/<int:pk>', TodoUpdate.as_view() ,name='update'),
]
