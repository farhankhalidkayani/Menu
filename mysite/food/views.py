from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import ItemForm
from .models import Item


# Create your views here.


class index(ListView):
    model = Item
    template_name = "index.html"
    context_object_name = "items"


class detail(DetailView):
    model = Item
    template_name = "detail.html"


class add_item(CreateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_img"]
    template_name = "item-form.html"
    success_url = reverse_lazy("food:index")

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


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
