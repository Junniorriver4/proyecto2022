from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse
from .models import familia

from django.http.response import StreamingHttpResponse
from streamapp.camera import VideoCamera, MaskDetect
import streamapp
# Create your views here.



def index(request):
	return render(request, 'streamapp/home.html',)

def callCamara(request):
    	
    return render(request, 'streamapp/camaraEnVivo.html',)

def callEntrenamiento(request):
    	
    return render(request, 'streamapp/Entrenamiento.html',)


def RegistroF(request):
	RegistroF= familia.objects.all()
	return render(request, 'streamapp/RegistroF.html',{'RegistroF': RegistroF})

def crear(request):
	formulario= RegistarForm(request.POST or None)
	return render(request, 'streamapp/RegistroF.html',{'formulario': formulario})

    






def callMascotas(request):
    return render(request, 'streamapp/Mascotas.html')

def callAyuda(request):
    return render(request, 'streamapp/Ayuda.html')





def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')


def mask_feed(request):
	return StreamingHttpResponse(gen(MaskDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')
					