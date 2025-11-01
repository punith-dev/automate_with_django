from django.shortcuts import render, redirect
from .utils import get_all_custom_models
from uploads.models import Upload
from django.conf import settings
from pathlib import Path
from django.core.management import call_command
from django.contrib import messages

# Create your views here.

def import_data(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')

        # Create Upload instance and ensure the uploaded file is saved to storage
        upload = Upload(model_name=model_name)
        if uploaded_file:
            # save() on the FileField ensures the file gets a name and is written to MEDIA_ROOT
            upload.file.save(uploaded_file.name, uploaded_file, save=True)
        else:
            upload.save()

        file_path = Path(settings.MEDIA_ROOT) / upload.file.name

        try:
            call_command('importdata', file_path, model_name)
            messages.success(request, 'Data imported successfully')
        except Exception as e:
            messages.error(request, e)
        
        return redirect('import_data')
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models' : custom_models, 
        }
    
    return render(request, 'dataentry/importdata.html', context)