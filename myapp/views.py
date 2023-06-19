from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Product,Project,ProjectImage,ProductCategory,CreateProduct,ProductImage

# Create your views here.

def index(request):
    project = Project.objects.all()
    product=None
    if project:
        product = Product.objects.distinct('product_name')
    
    context ={
        'project':project,
        'product':product   
    }
    return render(request, 'index.html', context)

def aboutus(request):
    #product = Product.objects.values()[:3]
    return render(request, 'about.html', {})

def product_categories(request,id):
    print(id)
    category = ProductCategory.objects.all()
    product = Product.objects.filter(product_name_id=id)
    context = {
        'product':product,
        'category':category
    }   
    return render(request, 'product-lists.html',context)

def product_details(request, id):
    product = get_object_or_404(Product,id=id)
    cats = Product.objects.filter(id=id)  
    photos = ProductImage.objects.filter(product_name_id=id)  
    context = {'product':product, 'photos':photos,'cats':cats}
    return render(request, 'product_details.html', context)


################################ project ###########

def project_details(request,project_name):
    project_name = get_object_or_404(Project,project_name=project_name)
    photos = ProjectImage.objects.filter(project_name=project_name)
    context ={'project':project_name,'photos':photos}
    
    return render(request, 'project_details.html', context )