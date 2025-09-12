from django.shortcuts import render

# Create your views here.
import base64
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import classify_image
import re

from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'Waste_classifier/index.html')


@csrf_exempt
def classify_webcam_image(request):
    if request.method == 'POST':
        try:
            data = request.POST.get('image')
            # Data URL format: "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
            img_str = re.sub('^data:image/.+;base64,', '', data)
            image_bytes = base64.b64decode(img_str)
            label, confidence = classify_image(image_bytes)
            return JsonResponse({'class': label, 'confidence': confidence})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def classify_uploaded_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            image_file = request.FILES['image']
            image_bytes = image_file.read()
            label, confidence = classify_image(image_bytes)
            return JsonResponse({'class': label, 'confidence': confidence})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)