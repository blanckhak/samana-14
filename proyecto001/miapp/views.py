from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def saludo(request):
    mensaje ="""" <h1>Bienvenidos al curso</h1>
<h2>Mg. Flor Elizabeth Cerdán León</h2>
<h3>Todo lo puedo en Cristo que me fortalece</h3> """
def saludo(request):
    return render(request,'saludo.html')