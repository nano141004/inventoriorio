import datetime
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from main.models import Item
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    items  = Item.objects.filter(user=request.user)
    amount_items = len(items)

    context = {
        'name': request.user.username,
        'class': 'PBP F',
        'item1' : 'laptop',
        'item2' : 'charger',
        'item3' : 'tumbler',
        'item4' : 'book', 
        'item5' : 'ballpoint',
        'item6' : 'handphone',
        'items' : items,
        'amount_items' : amount_items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def plus(request, id):
    data = Item.objects.get(pk=id)
    data.amount += 1
    data.save()
    return redirect('main:show_main')

def minus(request, id):
    data = Item.objects.get(pk=id)
    if (data.amount == 1):
        data.delete()
        return redirect('main:show_main')
    data.amount -= 1
    data.save()
    return redirect('main:show_main')

def remove(request, id):
    data = Item.objects.get(pk=id)
    data.delete()
    return redirect('main:show_main')

def get_item_json(request):
    items  = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()
        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def plus_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        data = Item.objects.get(pk=id)
        data.amount += 1
        data.save()
        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def minus_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        data = Item.objects.get(pk=id)
        data.amount -= 1
        data.save()
        if (data.amount == 0):
            data.delete()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()   

@csrf_exempt
def remove_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        data = Item.objects.get(pk=id)
        data.delete()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_item = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["amount"]),
            description = data["description"]
        )

        new_item.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)