from geopy.geocoders import Nominatim
import urllib.request
import json
import datetime

def addresstolatlon(adr):
    geo = Nominatim()
    location = geo.geocode(adr)
    return location.latitude,location.longitude
    
def getweathernow(lat,lon):
    user_api_key = '612ea5670775e78679efe28d9c00265e'
    unit = 'imperial'
    api = 'http://api.openweathermap.org/data/2.5/weather?'
    full_api_url = api + 'lat=' + str(lat) + '&lon=' +str(lon)+'&mode=json&units=' + unit + '&APPID=' + user_api_key
    #print(full_api_url)
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    url.close()
    wdict = json.loads(output)
    return wdict

def getweatherforecast(lat,lon):
    user_api_key = '612ea5670775e78679efe28d9c00265e'
    unit = 'imperial'
    api = 'http://api.openweathermap.org/data/2.5/forecast?'
    full_api_url = api + 'lat=' + str(lat) + '&lon=' +str(lon)+'&mode=json&units=' + unit + '&APPID=' + user_api_key
    #print(full_api_url)
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    url.close()
    wdict = json.loads(output)
    return wdict 
   
def showforecast(wd):
    print("City Id: ",wd.get("city").get('id'))
    print("City Name: ",wd.get("city").get("name"))
    print("Country: ",wd.get("city").get("country"))
    print("...................................")
    for wlist in range (0,wd.get("cnt")):
        print("Time: ",wd['list'][wlist].get('dt_txt'))
        print("Temp: ",wd['list'][wlist].get('main').get('temp'))
        print("Humidity: ",wd['list'][wlist].get('main').get('humidity'))
        print("Pressure: ",wd['list'][wlist].get('main').get('pressure'))
        print("Condition: ",wd['list'][wlist]['weather'][0]['main'])
        print("Description: ",wd['list'][wlist]['weather'][0]['description'])
        print("Cloud Cover: ",wd['list'][wlist].get('clouds').get('all'))
        print("Wind Speed: ",wd['list'][wlist].get('wind').get('speed'))
        print("Wind Direction: ",wd['list'][wlist].get('wind').get('deg'))
        print("Rain 3 Hours: ",wd['list'][wlist].get('rain').get('3h'))
        print("...................................")


def showweathernow(wd):
    print("City Id: ",wd.get('id'))
    print("City Name: ",wd.get("name"))
    print("Country: ",wd.get("sys").get("country"))
    print("Time: ",wd.get('dt'))
    print("Temp: ",wd.get('main').get('temp'))
    print("Visibility: ",wd.get('main').get('visibility'))
    print("Humidity: ",wd.get('main').get('humidity'))
    print("Pressure: ",wd.get('main').get('pressure'))
    print("Condition: ",wd['weather'][0]['main'])
    print("Description: ",wd['weather'][0]['description'])
    print("Cloud Cover: ",wd.get('clouds').get('all'))
    print("Wind Speed: ",wd.get('wind').get('speed'))
    print("Wind Direction: ",wd.get('wind').get('deg'))




#testing the functions above    
x="hamden,ct"
y=addresstolatlon(x)
lat=y[0]
lon=y[1]
print("==========begin testing getweatherforecast,showforecast outputs   ===========")
forcst=getweatherforecast(lat,lon)
showforecast(forcst)
print("========== end of testing getweatherforecast,showforecast outputs   ===========")
print("\n\n\n")
print("==========begin testing getweathernow,showweathernow outputs   ===========")
forcst=getweathernow(lat,lon)
showweathernow(forcst)
print("========== end of testing getweathernow,showweathernow outputs   ===========")





