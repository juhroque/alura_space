from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicar=True)
    return render(request, "galeria/index.html", {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) # puxar objeto ou dar não encontrado
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})