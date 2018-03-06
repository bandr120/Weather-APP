import sqlite3
from geopy.geocoders import Nominatim
import urllib.request
import json
import datetime
import sqlite3
import hashlib


def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%a %d %b %Y %I:%M %p')
    # ).strftime('%D %I:%M %p')
    return converted_time

def createweathernowtable():
    conn= sqlite3.connect('data.db')
    curs = conn.cursor()
    curs.execute('create table weathernow(city_id smallint,city_name varchar(20),country varchar(10),time datetime,temp real,visibility real,humidity real,pressure real,condition varchar(15),description varchar(25),cloud_cover real,wind_speed real,wind_direction real);')
    conn.commit()
    curs.close()


def createweatherforecasttable():
    conn= sqlite3.connect('data.db')
    curs = conn.cursor()
    curs.execute('create table weatherforecast(city_id smallint,city_name varchar(20),country varchar(10),time datetime,temp real,humidity real,pressure real,condition varchar(15),description varchar(25),cloud_cover real,wind_speed real,wind_direction real,rain real);')
    conn.commit()
    curs.close()

def insertweathernow(wd):
    cid=wd.get('id')
    cname=wd.get("name")
    cntry=wd.get("sys").get("country")
    time=wd.get('dt')
    temp=wd.get('main').get('temp')
    vsblty=wd.get('visibility')
    humid=wd.get('main').get('humidity')
    press=wd.get('main').get('pressure')
    cond=wd['weather'][0]['main']
    desc=wd['weather'][0]['description']
    cloud=wd.get('clouds').get('all')
    winds=wd.get('wind').get('speed')
    windd=wd.get('wind').get('deg')
    sqlvalues =str(cid) + ",'" + cname + "','"+  cntry + "','"+ str(time) + "',"+ str(temp) + ","+ str(vsblty) + ","+ str(humid) + ","+ str(press) + ",'" + cond + "','"+ desc + "',"+ str(cloud) + "," + str(winds) + ","+ str(windd) 
    conn= sqlite3.connect('data.db')
    curs = conn.cursor()
    #print ('insert into weathernow values(' + sqlvalues + ');')
    curs.execute('insert into weathernow values(' + sqlvalues + ');')
    conn.commit()
    curs.close()


def insertweatherforecast(wd):
    conn= sqlite3.connect('data.db')
    curs = conn.cursor()
    for wlist in range (0,wd.get("cnt")):
        cid=wd.get("city").get('id')
        cname=wd.get("city").get("name")
        cntry=wd.get("city").get("country")
        time=wd['list'][wlist].get('dt')
        temp=wd['list'][wlist].get('main').get('temp')
        humid=wd['list'][wlist].get('main').get('humidity')
        press=wd['list'][wlist].get('main').get('pressure')
        cond=wd['list'][wlist]['weather'][0]['main']
        desc=wd['list'][wlist]['weather'][0]['description']
        cloud=wd['list'][wlist].get('clouds').get('all')
        winds=wd['list'][wlist].get('wind').get('speed')
        windd=wd['list'][wlist].get('wind').get('deg')
        rain=wd['list'][wlist].get('rain').get('3h')
        if rain == None:
             rain=0.0
        sqlvalues =str(cid) + ",'" + cname + "','"+  cntry + "','"+ str(time) + "',"+ str(temp) + "," + str(humid) + ","+ str(press) + ",'" + cond + "','"+ desc + "',"+ str(cloud) + "," + str(winds) + ","+ str(windd) + "," + str(rain)
        curs.execute('insert into weatherforecast values(' + sqlvalues + ');')
        conn.commit()
    curs.close()
    
def addresstolatlon(adr):
    geo = Nominatim()
    location = geo.geocode(adr)
    print(location.raw)
    return location.latitude,location.longitude

    
#this function will call the online api and return dictionary called 'wdict' containing all retreived weather values
def getweathernow(lat,lon):
    user_api_key = '612ea5670775e78679efe28d9c00265e'
    unit = 'imperial'
    api = 'http://api.openweathermap.org/data/2.5/weather?'
    full_api_url = api + 'lat=' + str(lat) + '&lon=' +str(lon)+'&mode=json&units=' + unit + '&APPID=' + user_api_key
    print(full_api_url)
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    url.close()
    wdict = json.loads(output)
    wdict['dt'] = time_converter(wdict.get('dt'))
    return wdict


#this function will call the online api and return dictionary called 'wdict' containing all retreived weather values
def getweatherforecast(lat,lon):
    user_api_key = '612ea5670775e78679efe28d9c00265e'
    unit = 'imperial'
    api = 'http://api.openweathermap.org/data/2.5/forecast?'
    full_api_url = api + 'lat=' + str(lat) + '&lon=' +str(lon)+'&mode=json&units=' + unit + '&APPID=' + user_api_key
    print(full_api_url)
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    url.close()
    wdict = json.loads(output)
    for wlist in range (0,wdict.get("cnt")):
        wdict['list'][wlist]['dt']=time_converter( wdict['list'][wlist].get('dt'))
    return wdict 
   

def showforecast(wd):
    print("City Id: ",wd.get("city").get('id'))
    print("City Name: ",wd.get("city").get("name"))
    print("Country: ",wd.get("city").get("country"))
    print("...................................")
    for wlist in range (0,wd.get("cnt")):
        print("Time: ",wd['list'][wlist].get('dt'))
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
    print("Visibility: ",wd.get('visibility'))
    print("Humidity: ",wd.get('main').get('humidity'))
    print("Pressure: ",wd.get('main').get('pressure'))
    print("Condition: ",wd['weather'][0]['main'])
    print("Description: ",wd['weather'][0]['description'])
    print("Cloud Cover: ",wd.get('clouds').get('all'))
    print("Wind Speed: ",wd.get('wind').get('speed'))
    print("Wind Direction: ",wd.get('wind').get('deg'))



def searchweathernow(cid,time):
    sql="select * from weathernow where city_id='" + str(cid) + "' and time ='" + time + "';"
    conn= sqlite3.connect('data.db')
    curs = conn.cursor()
    curs.execute(sql)
    conn.commit()
    return curs.fetchone()
    curs.close()
    
    


#this function will create a table called 'weathernow' in db
#createweathernowtable()

#this function will create a table called 'weatherforecast' in db
#createweatherforecasttable()


#provide any testing address or city    
x="hamden,ct"


#storing the returned latitude & longitude from the function addresstolatlon(x)
y=addresstolatlon(x)
lat=y[0]
lon=y[1]


print("==========begin testing getweatherforecast,showforecast outputs   ===========")
forcst=getweatherforecast(lat,lon)
showforecast(forcst)
print("========== end of testing getweatherforecast,showforecast outputs   ===========")
print("\n\n\n")




print("==========begin testing getweathernow,showweathernow outputs   ===========")
wnow=getweathernow(lat,lon)
showweathernow(wnow)
print("========== end of testing getweathernow,showweathernow outputs   ===========")



print("==========begin testing if weather record exist in db   ===========")
print(searchweathernow(wnow.get('id'),wnow.get('dt')))
#insertweathernow(wnow)
#insertweatherforecast(forcst)

