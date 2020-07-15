from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import os
# Create your views here.


def index(request):
    try:
        with open(os.path.join(settings.REACT_APP_DIR,'build','index.html')) as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        return HttpResponse(
            '''
                frontend is not build
            '''
            , status = 501
        )
