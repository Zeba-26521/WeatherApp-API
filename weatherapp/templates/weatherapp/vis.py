
from email import message
from django.shortcuts import render
import requests
from .forms import CityForm

# Create your views here.

def home(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1bc1a421d2e7819147764cb2f48b0bb6'
    #city='Agra'
   
    if request.method=='POST':
        form=CityForm(request.POST)
        print(form)
        if form.is_valid():
            city =form.cleaned_data['name'] 
            print(f"Name is:{city}")
            r = requests.get(url.format(city)).json()
            #print(r)
            #print(r['message']) 
            city_weather={
                'City':city,
                'temp':r['main']['temp'],
                'description':r['weather'][0]['description'],
                'icon': r['weather'][0]['icon']
             }
            #print(city_weather)
            return render(request,'weatherapp/home.html',{'form':form,'city_weather':city_weather})


    else:
        form=CityForm()
        return render(request,'weatherapp/home.html',{'form':form,})


