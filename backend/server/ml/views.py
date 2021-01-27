from django.shortcuts import render

from ml.ml_service import ML


from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  
# Create your views here. 
def image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = HotelForm() 
    return render(request, 'image_upload.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 