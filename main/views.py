# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import UploadFileForm
import audsigweb_common.testing

from io import BytesIO
from scipy.io.wavfile import read 

# Create your views here.
def index(request):
    return HttpResponse('WELL, UH, HI')

def test(request):
    return HttpResponse('TESTING')

@csrf_exempt
def samplerate(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('oops')
    
    form = UploadFileForm(request.POST, request.FILES)
    fs, x = read(BytesIO(request.FILES['file'].read()))
    return JsonResponse({'fs': fs, 'x': len(x)})

def testing(request):
    return HttpResponse(audsigweb_common.testing.what())