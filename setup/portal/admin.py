from django.contrib import admin
from .models import PortalInfor

admin.site.site_header = 'Portal de Noticias'

class ListandoInfoPortal(admin.ModelAdmin):
    list_display = ('id', 'titulo_portal', 'created_at')
    list_display_links = ('id', 'titulo_portal')
    search_fields = ('id',)

admin.site.register(PortalInfor, ListandoInfoPortal)