from django.shortcuts import render, get_object_or_404
from .forms import searchForm, addForm
from .models import Product
from django.utils.text import slugify
from cart.forms import CartAddProductForm



#To render searched products
def productView(request):
    #we wearch inside available products
    products = Product.objects.filter(available=True)
    nameProduct = None
    codeProduct = None
 
    if request.method == 'POST':
        # Form was submitted
        form = searchForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            if cd['name']:
                nameProduct = cd['name']
                products = products.filter(name__icontains = nameProduct)
            elif cd['code']:
                codeProduct = cd['code']
                products = products.filter(code__icontains = codeProduct)
            else:
                products = products                       
 
    else:
        form = searchForm()
    return render(request, 'shops/search.html', {'products': products, 'form': form})


#To get detail of product
def productDetail(request, id, slug):
    #we included the id and slug in the product's urls, so we will look by id and slug inside available products 
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    #to add product to the cart
    cart_product_form = CartAddProductForm()

    return render(request, 'shops/detail.html', {'product': product,'cart_product_form': cart_product_form})  


#To add a new product into the database
def productAdd(request):
    newProduct = None
    sent = False
    if request.method == 'POST':
       
        productForm = addForm(request.POST, request.FILES)
        if productForm.is_valid():
            cd = productForm.cleaned_data
            newProduct = Product(
                name = cd['name'],
                image = cd['image'],
                description = cd['description'],
                price = cd['price'],
                code = cd['code'],
            )
            newProduct.slug = slugify(newProduct.name)
            newProduct.save()
            sent = True
    else:
        productForm = addForm()
    return render(request, 'shops/add.html', {'productForm': productForm, 'sent': sent})
