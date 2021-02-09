from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ml.models import Image
from ml.ml_service import ML


from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  

def image_upload_view(request): 
  
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('image_list') 
    else: 
        form = ImageForm() 
    return render(request, 'image_upload.html', {'form' : form}) 
  
class ImageDetailView(DetailView):
    model = Image
    template_name = 'image_detail.html'

class ImageList(ListView):
    model = Image
    context_object_name = 'images_model'
    template_name = 'image_list.html'

