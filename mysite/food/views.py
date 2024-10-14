from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import ItemForm
from .models import Item


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    return render(request, "index.html", {"items": item_list})


def item(request):
    return HttpResponse("This is an item view")


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, "detail.html", {"item": item})


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("food:index")
    else:
        form = ItemForm()
    return render(request, "item-form.html", {"form": form})


def edit_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect("food:index")
    else:
        form = ItemForm(instance=item)
    return render(request, "item-form.html", {"form": form, "item": item})


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    return render(request, "delete.html", {"item": item})
