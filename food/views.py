from django.shortcuts import render ,  redirect
from .models import Popular,Order

# Create your views here.
def index(request):
    return render(request, 'food/index.html')


def speciality(request):
    return render(request, 'food/speciality.html')

def popular(request):
    popular = Popular.objects.all()
    content = {'popular':popular}
    return render(request, 'food/popular.html', content)

def gallery(request):
    return render(request, 'food/gallery.html')

def cart(request):
    return render(request, 'food/cart.html')



def checkout(request):
    if request.method == "POST":
        items_json = request.POST['itemsJson']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']

        order = Order(items_json=items_json,username=username,email=email,address=address,phone=phone)
        order.save()
        return redirect('index')
    return render(request, 'food/checkout.html')



