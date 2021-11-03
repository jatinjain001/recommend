from django.shortcuts import render
import cv2
from django.http import StreamingHttpResponse
from . import camera
# Create your views here.


def home(request):
    return render(request,"index.html")

def index(request):
    return render(request, 'home.html')

#Every time you call the phone and laptop camera method gets frame
#More info found in camera.py
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#Method for laptop camera
def video_feed(request):
	return StreamingHttpResponse(gen(camera.VideoCamera()),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')

#Method for phone camera
def webcam_feed(request):
	return StreamingHttpResponse(gen(camera.IPWebCam()),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')




