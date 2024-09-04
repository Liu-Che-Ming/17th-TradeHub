from django.shortcuts import get_object_or_404, redirect, render

from .forms.product_form import ProductForm
from .models import Product


def index(request):
    state = request.GET.get("select")
    order_by = request.GET.get("sort", "id")
    is_desc = request.GET.get("desc", True) == "False"
    state_match = {"often", "haply", "less"}

    products = Product.objects.all()

    if state in state_match:
        products = Product.objects.filter(state=state)
    order_by_field = f"{'-' if is_desc else ''}{order_by}"
    products = products.order_by(order_by_field)

    content = {
        "products": products,
        "selected_state": state,
        "order_by": order_by,
        "is_desc": is_desc,
    }

    return render(request, "pages/index.html", content)


def new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:index")
        return render(request, "pages/new.html", {"form": form})
    form = ProductForm()
    return render(request, "pages/new.html", {"form": form})


# def show(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == "POST":
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect("products:show", id=id)
#         return render(request, "pages/edit.html", {"product": product, "form": form})
#     return render(request, "pages/show.html", {"product": product})


def edit(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products:index")
        return render(request, "pages/edit.html", {"product": product, "form": form})
    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)
    return render(request, "pages/edit.html", {"product": product, "form": form})


def delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect("products:index")
