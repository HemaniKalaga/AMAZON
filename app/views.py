from django.shortcuts import render

# Create your views here.
def dummy(request):
    return render(request,'dummy.html')
