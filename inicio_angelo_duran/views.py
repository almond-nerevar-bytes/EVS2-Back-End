from django.shortcuts import render

# Create your views here -- NO.
TEMAS = [
    {
        'id': 1,
        'tema': 'urbano',
        'nombre': 'Zona Urbana PS1',
        'descripcion': 'Este estilo de arte poligonal me gusta mucho en general, bastante llamativo',
        'imagenes': [
            {'archivo': 'images/foto2.jpg', 'titulo': 'Me parece curioso esto, llamativo incluso'},
            {'archivo': 'images/foto3.jpg', 'titulo': 'Pequeño... pero atractivamente acogedor'},
        ]
    },
    {
        'id': 2,
        'tema': 'paisajes',
        'nombre': 'Zona Rural PS1',
        'descripcion': 'Es curioso esto por que se parece mucho al lugar donde vivo',
        'imagenes': [
            {'archivo': 'images/foto1.jpg', 'titulo': 'Luce como si fuera un espacio miniminal'},
            {'archivo': 'images/foto4.jpg', 'titulo': 'Curioso por que esto tambien luce como el lugar donde vivo'},
        ]
    },
]

#tenia pensado este metodo mas que nada por que queria implementar un estilo parecido como si fuera un JSON o algo asi 
#ademas me parecia mejor en vez de escribir "{'id': 1, 'nombre': 'Escenario PS1', 'categoria': 'Paisajes', 'precio': 15000, 'imagen': 'images/foto1.jpg'}," you know...

def index(request):
    return render(request, 'inicio.html', {'temas': TEMAS})

def tema_urbano(request):
    return render(request, 'detalle.html', {'tema': TEMAS[0]})

def tema_paisajes(request):
    return render(request, 'detalle.html', {'tema': TEMAS[1]})