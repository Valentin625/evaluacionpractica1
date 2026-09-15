from django.http import HttpResponse

def vista1(request):
    return HttpResponse("Hola desde vista 1 de app1")

def vista2(request):
    return HttpResponse("Hola desde vista 2 de app1")
