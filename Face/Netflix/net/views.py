from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, 'net/index.html')

@csrf_exempt
def example(request):  
    if request.method=='POST':
        userLoginId = request.POST['userLoginId']
        password = request.POST['password']
    return render(request, 'net/hola.html', {"userLoginId" : userLoginId, "password" : password})

#def forming(request):
 #   if request.method == "POST":
  #      Usuario = Usuario(request.POST)
   #     userLoginId = Usuario.cleaned_data['userLoginId']
    #return render(request, 'net/hola.html', {"userLoginId" : userLoginId})
