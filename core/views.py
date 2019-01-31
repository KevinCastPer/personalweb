from django.shortcuts import render, HttpResponse

# Create your views here.
html_base = """
<h1>Mi Web Personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</></li>
</ul>
"""

def home(request):
    return HttpResponse(html_base + """
        <h2>Portada</h2>
        <p>Esto es la portada</p>
    """)

def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Me llamo Kevin y soy programador</p>
    """)
