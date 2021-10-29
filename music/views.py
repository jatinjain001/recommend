from django.shortcuts import render
import cv2
# Create your views here.


def home(request):
    return render(request,"index.html")


