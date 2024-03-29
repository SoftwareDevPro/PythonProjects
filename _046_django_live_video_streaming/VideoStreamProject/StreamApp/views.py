
from django.shortcuts import render
from django.http.response import StreamingHttpResponse

from StreamApp.camera import VideoCamera

def index(request):
    return render(request, "index.html")

def generate_image(camera):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")

def video_stream(request):
    return StreamingHttpResponse(generate_image(VideoCamera()),
           content_type="multipart/x-mixed-replace; boundary=frame")