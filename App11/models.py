from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=6, default='',primary_key=True)
    model = models.CharField(max_length=100,default='')
    screen = models.CharField(max_length=100,default='')
    cpu = models.CharField(max_length=100,default='')
    vga = models.CharField(max_length=100,default='')
    ram = models.CharField(max_length=100,default='')
    harddisk = models.CharField(max_length=100,default='')

    def pModel(self):
        if self.model == 'Alienware':
            pModel = 19000
        elif self.model == 'XPS':
            pModel = 12000
        elif self.model == 'Vosto':
            pModel = 9000
        elif self.model == 'G Series':
            pModel = 7000
        else:#Inspion
            pModel = 5000
        return pModel

    def pScreen(self):
        if self.screen == '17':
            pScreen = 1700
        elif self.screen == '15':
            pScreen = 1500
        elif self.screen == '14':
            pScreen = 1300
        else:#13
            pScreen = 1100
        return pScreen

    def pCpu(self):
        if self.cpu == 'AMD' or 'Core-i3':
            pCpu = 3500
        elif self.cpu == 'Core-i5':
            pCpu = 4000
        elif self.cpu == 'Core-i7':
            pCpu = 4500
        else:#Core-i9
            pCpu = 5000
        return pCpu

    def pVga(self):
        if self.vga == 'NVIDIA':
            pVga = 4200
        elif self.vga == 'Intel':
            pVga = 3800
        else:#Redeon
            pVga = 3400
        return pVga

    def pRam(self):
        if self.ram == '32':
            pRam = 1890
        elif self.ram == '16':
            pRam = 1590
        elif self.ram == '8':
            pRam = 1290
        else:#4
            pRam = 990
        return pRam

    def pHarddisk(self):
        if self.harddisk == 'SSD 1TB':
            pHarddisk = 2190
        elif self.harddisk == 'SDD 500GB':
            pHarddisk = 1890
        elif self.harddisk == 'HDD 1TB':
            pHarddisk = 1590
        else:#HDD 500GB'
            pHarddisk = 1290
        return pHarddisk

    def pSum(self):
        pSum = self.pModel()+ \
               self.pScreen()+ \
               self.pCpu()+ \
               self.pVga()+ \
               self.pRam()+ \
               self.pHarddisk()
        return pSum

    def pDiscount(self):
        if self.pSum() <20000:
            pDiscount = self.pSum()*5/100
        elif self.pSum() <30000:
            pDiscount = self.pSum()*10/100
        else:
            pDiscount = self.pSum()*15/100
        return  pDiscount

    def pTotal(self):
        pTotal = self.pSum() - self.pDiscount()
        return pTotal

    def __str__(self):
        text = str(self.id) + ' : ' \
               + str(self.model) + ',' \
               + str(self.screen) + ',' \
               + str(self.cpu) + ',' \
               + str(self.vga) + ',' \
               + str(self.ram) + ',' \
               + str(self.harddisk) + ',' \
               + str(self.pTotal())
        return text