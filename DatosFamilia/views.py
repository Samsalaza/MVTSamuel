from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import Template, loader

def mifamilia (request):
    familiar1=Familiares(nombre="Juan", apellido="Salazar", dni=95473163, fecha_nacimiento='1989-01-02')
    familiar2=Familiares(nombre="Marlyn", apellido="Jimenez", dni=95456163, fecha_nacimiento='1987-02-03')
    familiar3=Familiares(nombre="Alicia", apellido="Reinales", dni=90473167, fecha_nacimiento='1969-01-03')
    familiar1.save()
    familiar2.save()
    familiar3.save()

    diccionario={
        "nombre_familia1":familiar1.nombre, "apellido_familia1":familiar1.apellido, "dni_familia1":familiar1.dni, "fecha_nacimiento_familia1":familiar1.fecha_nacimiento,
        "nombre_familia2":familiar2.nombre, "apellido_familia2":familiar2.apellido, "dni_familia2":familiar2.dni, "fecha_nacimiento_familia2":familiar2.fecha_nacimiento,
        "nombre_familia3":familiar3.nombre, "apellido_familia3":familiar3.apellido, "dni_familia3":familiar3.dni, "fecha_nacimiento_familia3":familiar3.fecha_nacimiento,
    }
    
    plantilla=loader.get_template('mainTemplate.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)


    

    