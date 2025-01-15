from django.db import models

class Alumno(models.Model):
    # Convertimos `idChat` en la llave primaria y eliminamos el campo `codigo`
    idChat = models.CharField(max_length=50, primary_key=True)  # Ahora idChat es la clave primaria
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    rol = models.CharField(max_length=50, blank=True, null=True)
    horasTotales = models.CharField(max_length=50, blank=True, null=True)  # Almacenado como cadena
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)

    class Meta:
        db_table = 'alumno'

    def __str__(self):
        return self.nombre


class Checadas(models.Model):
    # Modificamos `identificador` para que sea una clave foránea a `Alumno` usando `idChat`
    identificador = models.ForeignKey(Alumno, on_delete=models.CASCADE, db_column='identificador')  # Hace referencia al `idChat` de Alumno
    horaEntrada = models.TimeField()
    fechaEntrada = models.CharField(max_length=20)
    horaSalida = models.TimeField(blank=True, null=True)
    fechaSalida = models.CharField(max_length=20, blank=True, null=True)
    horas = models.TimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'checadas'

    def __str__(self):
        return f"Checada de {self.identificador.nombre} el {self.fechaEntrada}"
