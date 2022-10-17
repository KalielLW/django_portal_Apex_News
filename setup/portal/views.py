from django.shortcuts import render
from .models import PortalInfor
from artigo.models import Artigo, Categoria


def create_context_base():
    info_portal = PortalInfor.objects.all().last()
    artigos = Artigo.objects.filter(ativo=True)

    return {
        'titulo': info_portal.titulo_portal,
        'contato': {
            'telefone': info_portal.telefone,
            'email': info_portal.email,
            'endereco': info_portal.endereco,
        },
        'midias_sociais': {
            'facebook': info_portal.facebook,
            'youtube': info_portal.youtube,
            'instagram': info_portal.instagram,
        },
        "lista_noticias_principais" : artigos[:4],
        "categorias": Categoria.objects.all(),
        "popular_news": artigos[:3],
        "lista_noticias": artigos,
    }

def index(request):

    context = create_context_base()

    return render(request, 'index/index.html', context)
