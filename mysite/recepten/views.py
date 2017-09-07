from django.shortcuts import render

# Create your views here.
def index(request):
    # https://github.com/andymccurdy/redis-py


    return render(request, 'recepten/index.html')