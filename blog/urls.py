from  django.url import path
from . import views

urlpatters = [
    path('', views.post_list, name = 'post_list'),
]