
from django.shortcuts import render
from django.contrib import messages
from .forms import CaptchaForm

def index(request):
    if request.method == "POST":
        form = CaptchaForm(request.POST)
        if form.is_valid():
            messages.success(request, "Captcha successfully verified")
        else:
            messages.error(request, "Captcha Failed")
    
    form = CaptchaForm()
    return render(request, "index.html", { "form": form })