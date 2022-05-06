from django.shortcuts import render
from.models import Contact
# Create your views here.

def index (request):
    return render(request,'index.html')



def Leatherjournal(request):
    return render(request,'Handmade-Leather-journal.html')


def christmas(request):
    return render(request,'Handmade-christmas-ornament.html')


def Giftproducts(request):
    return render(request,'Handmade-Giftproducts.html')


def Lamp(request):
    return render(request,'Handmade-Lamp-star.html')



def Leatherbag(request):
    return render(request,'Handmade-Leather-bag.html')



def Handmadepapers(request):
    return render(request,'Handmade-papers.html')

def Papersbag(request):
    return render(request,'Handmade-papers-bag.html')



def Papersbox(request):
    return render(request,'Handmade-papers-box.html')


def Seedpapers(request):
    return render(request,'Handmade-plantable-papers.html')


def Vintagepapers(request):
    return render(request,'Vintage-papers.html')



def contact (request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})


def About(request):
    return render(request,'About.html')


def Factory(request):
    return render(request,'Factory-tour.html')

def Gallery(request):
    return render(request,'Gallery.html')


def Collaborate(request):
    return render(request,'Collaborate.html')



def How(request):
    return render(request,'How-it-works.html')




def Place(request):
    return render(request,'Place-order.html')