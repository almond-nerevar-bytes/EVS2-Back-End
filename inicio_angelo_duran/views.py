from django.shortcuts import render

# Create your views here -- NO.
TEMAS = [
    {
        'id': 1, #algo divertido que quiero hacer
        'tema': 'tema1',
        'nombre': 'Zona Urbana PS1',
        'descripcion': 'Este estilo de arte poligonal me gusta mucho en general, bastante llamativo',
        'imagenes': [
            {'archivo': 'images/foto2.jpg', 'titulo': 'Me parece curioso esto, llamativo incluso'},
            {'archivo': 'images/foto3.jpg', 'titulo': 'Pequeño... pero atractivamente acogedor'},
        ]
    },
    {
        'id': 2,
        'tema': 'tema2',
        'nombre': 'Zona Rural PS1',
        'descripcion': 'Es curioso esto por que se parece mucho al lugar donde vivo',
        'imagenes': [
            {'archivo': 'images/foto1.jpg', 'titulo': 'Luce como si fuera un espacio miniminal'},
            {'archivo': 'images/foto4.jpg', 'titulo': 'Curioso por que esto tambien luce como el lugar donde vivo'},
        ]
    },
]