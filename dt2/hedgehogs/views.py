from django.shortcuts import render

def home(request):
    return render(request, 'hedgehogs/home.html')

def about(request):
    return render(request, 'hedgehogs/about.html')

def gallery(request):
    return render(request, 'hedgehogs/gallery.html')

def contact(request):
    return render(request, 'hedgehogs/contact.html')
