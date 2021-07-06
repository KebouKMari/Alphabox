from django.urls import path, include
from . import views 
urlpatterns = [
    path('', views.index,name='learn'),
    path('modules/', views.modules, name='modules'),
    path('play/', views.play, name='play'),
    path('setting/',views.index_setting, name='settings'),
    path('session/create/', views.create_session, name="create_session" ),
    path('session/get/', views.get_session, name="get_session"),
    path('validateword/', views.validate_word, name='validateword')
]