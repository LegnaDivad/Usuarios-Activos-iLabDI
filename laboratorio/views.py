from django.shortcuts import render
from .models import Checadas

def checadas_view(request):
    # Obtiene todas las checadas relacionadas con los alumnos
    checadas = Checadas.objects.all().select_related('identificador')  # Optimiza la consulta a los alumnos relacionados
    
    # Depuración
    print(checadas)  # Esto te ayudará a ver los objetos que se están cargando
    
    # Pasa los datos al template
    return render(request, 'laboratorio/usuarios.html', {'checadas': checadas})
