from django.urls import path
from . import views
from .views import StudentCreate


urlpatterns = [

    # path('', views.index , name='index'),
    path('', views.get_data, name='get_data' ),
    path('create',  StudentCreate.as_view()),
]