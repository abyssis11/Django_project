from django.urls import path
from . import views
from main.views import VoditeljList, ProstorijaList, RacunaloList
app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aktivnosti/', views.aktivnosti, name='aktivnosti'),
    path('voditelj/', VoditeljList.as_view()),
    path('prostorija/', ProstorijaList.as_view()),
    path('racunalo/', RacunaloList.as_view()),
]