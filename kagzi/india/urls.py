from django.urls import path

from . import views

urlpatterns = [
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