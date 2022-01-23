from email import message 
from django.shortcuts import render
import requests
from .forms import CityForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1bc1a421d2e7819147764cb2f48b0bb6'
   
    if request.method=='POST':
        form=CityForm(request.POST)
        print(form)
        if form.is_valid():
            city =form.cleaned_data['name'] 
            r1= requests.get(url.format(city))
            if r1.status_code !=200:
                #return HttpResponse("City Not Found")
                return HttpResponseRedirect('/na/')
            else:
                pass
            r = requests.get(url.format(city)).json()
            
            city_weather={
                'City':city,
                'temp':r['main']['temp'],
                'description':r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                'feels_like':r['main']['feels_like'], 
                'temp_min':r['main']['temp_min'], 
                'temp_max':r['main']['temp_max'], 
                'humidity':r['main']['humidity'],   

             }
            return render(request,'weatherapp/home.html',{'form':form,'city_weather':city_weather})

    else:
        form=CityForm()
        return render(request,'weatherapp/home.html',{'form':form,})

#for citynot found
def notfound(request):
    return render(request,'weatherapp/notfound.html')



