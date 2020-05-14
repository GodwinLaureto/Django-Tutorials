from django.urls import path

import re


from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    #path('learn_now/<subject_name>/', views.learn_now, name = "learn_now"),
    path(r'^learn_now/(?P<subject_id>\d+)/$', views.learn_now, name = "learn_now")
    
]