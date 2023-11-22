from django.shortcuts import render

# Create your views here.
def bablu(request):
    return render(request,'bablu.html')

def hansi(request):
    return render(request,'hansi.html')



def bablu2(request):
    return render(request,'bablu2.html')