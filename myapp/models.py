from django.db import models
from django.utils.html import mark_safe


class CreateProduct(models.Model):
    product_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.product_name
        
    
class ProductCategory(models.Model):
    product_category = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.product_category
        
 
####################### Product Model #############################

class Product(models.Model):
    product_name =models.ForeignKey(CreateProduct, on_delete=models.CASCADE)
    product_category =models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_description = models.TextField()
    product_img = models.FileField(blank=True)
    
    def __str__(self):
        return str(self.product_name.product_name)
        
class ProductImage(models.Model):
    product_name = models.ForeignKey(Product,default=None, on_delete=models.CASCADE)
    product_img = models.FileField(upload_to="media/Product/images/")
    
    def __str__(self):
        return self.product_name.product_name.product_name
    
#######################  End Product Model #########################
########################### Project Model ##########################  
    
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description =models.CharField(max_length=500)
    project_img =models.FileField(blank=True)
    
    def __str__(self):
        return self.project_name
    
class ProjectImage(models.Model):
    project_name = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    project_img = models.FileField(upload_to = 'media/Project/images/')
    
    def __str__(self):
        return self.project_name.project_name
    
############################# End Project Model #######################333
