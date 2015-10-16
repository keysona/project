from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
# Create your views here.
from .handle import handle_upload_file
from django.http import HttpResponse
from django.http import JsonResponse


def test(request):
    #form = UploadFileForm(request.POST, request.FILES)
    #return render(request,'upload.html',{'image_urls':result})
    form = UploadFileForm()
    return render(request,'start.html', {'modelform_filefield':form})

def upload(request):
    if request.is_ajax():
        form = UploadFileForm(request.POST, files=request.FILES)
        if form.is_valid():
            result = handle_upload_file(request.FILES['file'])
            return JsonResponse(result)
        else:
            return HttpResponse("form invalid")
    return HttpResponse("not a ajax request")
     
    
