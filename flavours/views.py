from django.shortcuts import render

# Create your views here.
def flavours(request):
    return render(request, "flavours.html")