from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import AutorForm, PostForm, ComentarioForm, BusquedaPostForm
from .models import Post

def home(request):
    return render(request, 'home.html')

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Crear Autor'})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Crear Post'})

def crear_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ComentarioForm()
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Crear Comentario'})

def buscar_post(request):
    resultados = []
    if request.method == "GET":
        form = BusquedaPostForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaPostForm()
    return render(request, 'buscar.html', {'form': form, 'resultados': resultados})

# Create your views here.


def inicio(request):
    return render(request, 'home.html')
    return render(request, 'inicio.html')