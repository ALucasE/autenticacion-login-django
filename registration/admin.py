from django.contrib import admin
from .models import Usuario
# Register your models here.

#Default: Administracion de Django
admin.site.site_header = 'Administracion de Usuarios'

#Default: Sitio administrativo
admin.site.index_title = 'Panel de control'

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('date_joined', 'last_login', 'updated') 
    list_display = ('username','is_active','is_staff')
    ordering = ('-date_joined',)
    search_fields = ('username',) 

admin.site.register(Usuario, UsuarioAdmin)