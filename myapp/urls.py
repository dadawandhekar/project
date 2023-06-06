from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('about-us/',views.aboutus, name="about-us"),
    path('product-categories/<int:id>',views.product_categories, name="product_categories"),
    path('product-details/<int:id>',views.product_details, name="product_details"),
    path('project-details/<project_name>',views.project_details, name="project_details"),
]
