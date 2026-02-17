import requests
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from .models import Moto, Resena

def lista_motos(request):
    motos = Moto.objects.all()
    return render(request, 'motos/lista_motos.html', {'motos': motos})

def detalle_moto(request, id):
    moto = get_object_or_404(Moto, id=id)
    return render(request, 'motos/detalle_moto.html', {'moto': moto})

def tasa_cambio(request):
    url = "https://api.exchangerate-api.com/v4/latest/COP"
    response = requests.get(url)
    data = response.json()
    tasa_usd = data["rates"]["USD"]
    return JsonResponse({"usd": tasa_usd})

@login_required
def agregar_resena(request, id):
    moto = get_object_or_404(Moto, id=id)

    if request.method == "POST":
        comentario = request.POST.get('comentario')
        estrellas = request.POST.get('estrellas')
        imagen = request.FILES.get('imagen')

        Resena.objects.create(
            moto=moto,
            usuario=request.user,
            comentario=comentario,
            estrellas=estrellas,
            imagen=imagen
        )

    return redirect('detalle_moto', id=moto.id)


from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('lista_motos')
    else:
        form = RegistroForm()

    return render(request, 'registration/registro.html', {'form': form})

