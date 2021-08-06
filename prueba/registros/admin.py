from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto
from .models import AlumnoRegistro

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('matricula','nombre','carrera','turno')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')
    #verifica que si existen los campos los muestra
    list_per_page=2
    #muestra los registros de 2 por pagina
    list_display_links=('matricula','nombre')
    #hace que nos lleve al formulario desde nombre y matricula
    list_editable=('turno',)
    #permite que no tengamos que entrar al formulario, editamos de tabla de consulta

    def get_readonly_fields(self, request, obj=None):
         #si el usuario pertenece el grupo usuario
        if request.user.groups.filter(name="Usuarios").exists():
        #bloquea los campos
            return ('matricula','carrera','turno')
        #Cualquier otro usuario que no pertenece al grupo usuario
        else:
            #bloquea los campos
            return ('created','updated')

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id','coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created','id')
    #verifica que si existen los campos los muestr

admin.site.register(Comentario, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id','mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created','id')
    #verifica que si existen los campos los muestr

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)


class AdministrarMatricula(admin.ModelAdmin):
    list_display = ('nombre','matricula','nombre')
    #como enlista en el administrador
    search_fields = ('nombre','matricula','created')
    date_hierarchy = 'created'
    readonly_fields = ('created','updated')
    #no deja editar el campo

admin.site.register(AlumnoRegistro, AdministrarMatricula)

