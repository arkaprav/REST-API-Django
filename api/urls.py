from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.drink_list, name='home'),
    path('<int:id>/', views.drink_details, name='details')
]

urlpatterns = format_suffix_patterns(urlpatterns)