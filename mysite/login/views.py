from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login/")
def view_upload(request):
    return render(request, 'upload.html')
