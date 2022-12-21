from django.urls import path
from . import views
from main.views import VoditeljList, AktivnostList, ProstorijaList, RacunaloList
app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('voditelj/', VoditeljList.as_view()),
    path('aktivnost/', AktivnostList.as_view()),
    path('prostorija/', ProstorijaList.as_view()),
    path('racunalo/', RacunaloList.as_view()),
]