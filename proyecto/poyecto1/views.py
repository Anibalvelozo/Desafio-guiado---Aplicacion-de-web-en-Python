from django.shortcuts import render
from django.http import HttpResponse
from django.utils.lorem_ipsum import paragraph

# Create your views here.

def home(request):
    text = paragraph()
    return HttpResponse(
    f"""
    <h1>Pagina de inicio</h1>
    <p>{text}</p>
    """)

def about(request):
    text = paragraph()
    return HttpResponse(
    f"""
    <h1>Acerca de nosotros</h1>
    <p>{text}</p>
    """)

def contact(request):
    text = paragraph()
    return HttpResponse(
    f"""
    <h1>Contacto</h1>
 <form action="#" method="post">
    <label for="name">Nombre:</label><br>
    <input type="text" id="name" name="name"><br>
    <label for="email">Correo electrónico:</label><br>
    <input type="email" id="email" name="email"><br>
    <label for="message">Mensaje:</label><br>
    <textarea id="message" name="message"></textarea><br>
    <input type="submit" value="Enviar">
</form>
    """)
