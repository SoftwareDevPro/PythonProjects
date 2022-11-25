
from django.shortcuts import render
import uuid
from django.conf import settings
from qrcode import *

def index(request):
    if request.method == "POST":
        url = request.POST['url']
        img = make(url)
        img_name = f"qrimg_{uuid.uuid1().int}.png"
        img.save(settings.MEDIA_ROOT/img_name)
        return render(request, "index.html", { "img": img_name })
    return render(request, "index.html")
