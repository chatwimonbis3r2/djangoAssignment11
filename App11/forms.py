from django import forms
from App11.models import *

model_choice = [('Alienware', 'Alienware'),
                ('XPS', 'XPS'),
                ('Vosto', 'Vosto'),
                ('G Series', 'G Series'),
                ('Inspion', 'Inspion')]

screen_Choice = [('17', '17'),
                 ('15', '15'),
                 ('14', '14'),
                 ('13', '13')]

cpu_Choice = [('AMD', 'AMD'),
              ('Core-i3', 'Core-i3'),
              ('Core-i5', 'Core-i5'),
              ('Core-i7', 'Core-i7'),
              ('Core-i9', 'Core-i9'),]

vga_Choice = [('NVIDIA', 'NVIDIA'),
              ('Intel', 'Intel'),
              ('Redeon', 'Redeon')]

ram_Choice = [('32', '32'),
              ('16', '16'),
              ('8', '8'),
              ('4', '4')]

harddisk_Choice = [('SSD 1TB', 'SSD 1TB'),
              ('SDD 500GB', 'SDD 500GB'),
              ('HDD 1TB', 'HDD 1TB'),
              ('HDD 500GB', 'HDD 500GB')]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id','model', 'screen', 'cpu', 'vga', 'ram', 'harddisk')
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=model_choice),
            'screen': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=screen_Choice),
            'cpu': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=cpu_Choice),
            'vga': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=vga_Choice),
            'ram': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=ram_Choice),
            'harddisk': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=harddisk_Choice),
        }
        labels = {
            'id': 'ID',
            'model': 'Model',
            'screen': 'Screen',
            'cpu': 'Cpu',
            'vga': 'Vga',
            'ram': 'Ram',
            'harddisk': 'Harddisk',
        }