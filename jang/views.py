from django.shortcuts import redirect, render
from jang.models import productdetails

# Create your views here.

#load addproduct.html page
def load_addproducts(request):
   return render(request,'addproducts.html')

#enter product details
def add_product_details(request):
   if request.method=='POST':
      pname=request.POST['product_name']
      des=request.POST['description']
      qty=request.POST['quantity']
      price=request.POST['price']
      product=productdetails(product_name=pname,
                             description=des,
                             quantity=qty,
                             Price=price)
      product.save()
      print("hi")
      return redirect('showproducts')
      
   return render(request,'addproducts.html')
       

#show product details
def showproducts(request):
   products=productdetails.objects.all()
   return render(request,'showproduct.html',{'product':products})


 #Load Edit Page....
def editpage(request,pk):
    products=productdetails.objects.get(id=pk) #.....select * from tablename where id = 56;
    return render(request,'edit.html',{'products':products})

#Editing..
def edit_productdetails(request,pk):
   if request.method=='POST':
        products = productdetails.objects.get(id=pk)
        products.product_name = request.POST.get('product_name')
        products.description = request.POST.get('description')
        products.quantity = request.POST.get('quantity')
        products.Price = request.POST.get('price')
        products.save()
        return redirect('showproducts')
   return render(request,'edit.html',)


#Load delete Page...
def deletepage(request,pk):
    products=productdetails.objects.get(id=pk)
    return render(request,'delete.html',{'products':products})

#Deleting Product Element..
def delete_product(request,pk):
    products=productdetails.objects.get(id=pk)
    products.delete()
    return redirect('showproducts')