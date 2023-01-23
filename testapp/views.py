from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.files import File
from .models import Trip
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
import json
import cv2


def index(request):
    print(1)
    return HttpResponse("Europe Trips")

def my_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        my_model = Trip(origin=data['origin'], destination=data['destination'], price=data['price'], nights=data['nights'])
        my_model.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


def compare_images(request):
    if request.method == 'POST':
        folder='my_media_folder/' 
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        path = default_storage.save('path/to/image1.jpg', image1)
        image_path = default_storage.path(path)
        img1 = cv2.imread(image_path)
        path2 = default_storage.save('path/to/image2.jpg', image2)
        image_path2 = default_storage.path(path2)
        img2 = cv2.imread(image_path2)
        result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
        similarity = result[0][0]
        print(similarity)
        return JsonResponse({'status': 'success', 'similarity': str(similarity)})
    return JsonResponse({'status': 'error'})
