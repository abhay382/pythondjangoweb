"""kagzi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from india import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('india/', include('india.urls')),
    path('', views.index, name='index'),
     path('Handmade-Leather-journal/', views.Leatherjournal, name='Handmade-Leather-journal'),
     path('Handmade-christmas-ornament/', views.christmas, name='Handmade-christmas-ornament'),
     path('Handmade-Giftproducts/', views.Giftproducts, name='Handmade-Giftproducts'),
     path('Handmade-Lamp-star/', views.Lamp, name='Handmade-Lamp-star'),
     path('Handmade-Leather-bag/', views.Leatherbag, name='Handmade-Leather-bag'),
     path('Handmade-papers/', views.Handmadepapers, name='Handmade-papers'),
     path('Handmade-papers-bag/', views.Papersbag, name='Handmade-papers-bag'),
     path('Handmade-papers-box/', views.Papersbox, name='Handmade-papers-box'),
     path('Handmade-plantable-papers/', views.Seedpapers, name='Handmade-plantable-papers'),
     path('Vintage-papers/', views.Vintagepapers, name='Vintage-papers'),
     path('contact/', views.contact, name='Contact'),
     path('About/', views.About, name='About'),
     path('Factory-tour/', views.Factory, name='Factory-tour'),
     path('Gallery/', views.Gallery, name='Gallery'),
     path('Handmade-Leather-journal/', views.Leatherjournal, name='Handmade-Leather-journal'),
 path('Let-Collaborate/', views.Collaborate, name='Handmade-Leather-journal'),
 path('How-it-works/', views.How, name='How-it-works'),
 path('Place-order/', views.Place, name='Place-order'),
]
