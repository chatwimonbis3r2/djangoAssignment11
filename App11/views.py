from django.shortcuts import render, redirect

from App11.forms import ProductForm
from App11.models import Product

def Home(request):
    return render(request,'Home.html')

lstOurProduct = []

def listProduct(request):
    context = {'product':lstOurProduct}
    return render(request, 'listProduct.html',context)

def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            model = form.get('model')
            screen = form.get('screen')
            cpu = form.get('cpu')
            vga = form.get('vga')
            ram = form.get('ram')
            harddisk = form.get('harddisk')

            if model == 'Alienware':
                pModel = 19000
            elif model == 'XPS':
                pModel = 12000
            elif model == 'Vosto':
                pModel = 9000
            elif model == 'G Series':
                pModel = 7000
            else:  # Inspion
                pModel = 5000

            if screen == '17':
                pScreen = 1700
            elif screen == '15':
                pScreen = 1500
            elif screen == '14':
                pScreen = 1300
            else:  # 13
                pScreen = 1100

            if cpu == 'AMD' or 'Core-i3':
                pCpu = 3500
            elif cpu == 'Core-i5':
                pCpu = 4000
            elif cpu == 'Core-i7':
                pCpu = 4500
            else:  # Core-i9
                pCpu = 5000

            if vga == 'NVIDIA':
                pVga = 4200
            elif vga == 'Intel':
                pVga = 3800
            else:  # Redeon
                pVga = 3400

            if ram == '32':
                pRam = 1890
            elif ram == '16':
                pRam = 1590
            elif ram == '8':
                pRam = 1290
            else:  # 4
                pRam = 990

            if harddisk == 'SSD 1TB':
                pHarddisk = 2190
            elif harddisk == 'SDD 500GB':
                pHarddisk = 1890
            elif harddisk == 'HDD 1TB':
                pHarddisk = 1590
            else:  # HDD 500GB'
                pHarddisk = 1290

            pSum = pModel + pScreen + pCpu + pVga + pRam + pHarddisk

            if pSum < 20000:
                pDiscount = pSum * 5 / 100
            elif pSum < 30000:
                pDiscount = pSum * 15 / 100
            else:
                pDiscount = pSum * 10 / 100

            pTotal = pSum - pDiscount

            ProductList = Product(id,model,screen,cpu,vga,ram,harddisk)
            lstOurProduct.append(ProductList)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
        context = {'form':form}
        return render(request,'inputProduct.html',context)