from django.contrib import admin
from .models import Autor, Categoria, Artigo

class ListandoAutor(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('id',)

admin.site.register(Autor, ListandoAutor)

class ListandoCategoria(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('id',)

admin.site.register(Categoria, ListandoCategoria)

class ListandoArtigo(admin.ModelAdmin):
    list_display = ('id', 'titulo' ,'created_at', 'ativo')
    list_display_links = ('id', 'titulo')
    search_fields = ('id', 'autor')

admin.site.register(Artigo, ListandoArtigo)



