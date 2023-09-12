from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Mariano Gerardus Senduk',
        'class': 'PBP F',
        'item1' : 'laptop',
        'item2' : 'charger',
        'item3' : 'tumbler',
        'item4' : 'book', 
        'item5' : 'ballpoint',
        'item6' : 'handphone'
    }

    return render(request, "main.html", context)