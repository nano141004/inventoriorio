from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Mariano Gerardus Senduk',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)