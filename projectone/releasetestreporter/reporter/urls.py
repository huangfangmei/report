from django.urls import re_path
from . import views
urlpatterns = [
    re_path('all/', views.get),  # all/是前端get对应路由   views.get是views中对应函数
    re_path('reportlist/', views.get_reporter_list)
]
