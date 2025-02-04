from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from .forms import ProductForm

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, "Vous n'êtes pas autorisé à ajouter des produits.")
        return redirect('product_list')
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit ajouté avec succès!")
            return redirect('product_list')
    else:
        form = ProductForm()
    
    return render(request, 'products/add_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Vous n'êtes pas autorisé à modifier ce produit.")
        return redirect('product_list')
    
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit modifié avec succès!")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/edit_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Vous n'êtes pas autorisé à supprimer ce produit.")
        return redirect('product_list')
    
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "Produit supprimé avec succès!")
    return redirect('product_list')


@login_required
def dashboard(request):
    total_products = Product.objects.count()
    latest_products = Product.objects.all().order_by('-created_at')[:5] 
    return render(request, 'products/dashboard.html', {
        'total_products': total_products,
        'latest_products': latest_products,
    })

def search(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.none() 
    return render(request, 'products/search_results.html', {'products': products, 'query': query})
