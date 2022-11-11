
from django.urls import path
from .views import home ,post_Todo,getTodo,patch_todo,Todo
urlpatterns = [
    path('', home,name='home'),
    path('post-todo/', post_Todo,name='post_todo'),
    path('get-todo/', getTodo,name='get_todo'),
    path('patch-todo/', patch_todo,name='patch_todo'),

    path('todo/',Todo.as_view())
]
