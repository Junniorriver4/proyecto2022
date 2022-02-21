from django.urls import path, include
from streamapp import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.index, name='index'),
    path('Camara', views.callCamara, name='callCamara'),
    path('Entrenamiento', views.callEntrenamiento, name='callEntrenamiento'),
    path('RegistroF', views.RegistroF, name='RegistroF'),
    
    path('Mascotas', views.callMascotas, name='callMascotas'),
    path('Ayuda', views.callAyuda, name='callAyuda'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('mask_feed', views.mask_feed, name='mask_feed'),


    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
