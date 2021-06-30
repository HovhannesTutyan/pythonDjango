from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    # path('cats/<int:catid>/', categories), #http://127.0.0.1:8000/woman/cats/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('about/', about, name="about")

]