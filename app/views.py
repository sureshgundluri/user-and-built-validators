from django.shortcuts import render
from django.http import HttpResponse

from app.forms import *

def user_defined_validators(request):
    FO=Nameform()
    d={'form':FO}
    if request.method=='POST':
        FFO=Nameform(request.POST)
        if FFO.is_valid():
            return HttpResponse(str(FFO.cleaned_data))
    return render(request,'user_defined_validators.html',d)
