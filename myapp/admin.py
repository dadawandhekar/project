from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Product,CreateProduct,ProductCategory
from .models import Project,ProjectImage
from .models import Product,ProductImage


class CreateProductAdmin(admin.ModelAdmin): # new
     list_display = ['product_name']
     
class ProductCategoryAdmin(admin.ModelAdmin): # new
     list_display = ['product_category']
     
################################ project ####################################

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): # new
     list_display = ['product_name','product_category','product_description','product_img']
     inlines = [ProductImageAdmin]
     class Meta:
          model =Product
          
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
     list_display = ['product_name']

     
################################ project ####################################

     
class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]

    class Meta:
       model = Project

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    pass

#admin.site.register(ProductAdmin,ProjectAdmin) # new
admin.site.register(CreateProduct,CreateProductAdmin) 
admin.site.register(ProductCategory,ProductCategoryAdmin)

admin.site.unregister(Group) 