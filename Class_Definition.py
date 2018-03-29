from urllib.request import urlopen
import json
from backports import configparser
import sqlite3
from geopy.geocoders import Nominatim


class User_Interface:
    
    def __init__(self):
        
        self.ms=Main_Service()
        self.printmain()
        
    def load_opt1(self):
        x=input('Enter Location Keyword to Search :')
        y=self.ms.loc.search_nominatim(x)
        print(y)
        input('')
        self.printmain()
        
    def load_opt2(self):
        y=self.ms.loc.detect_location()
        print(y)
        input('')
        self.printmain()

    def load_opt3(self):
        x=input('Enter City Name :')
        y=input('Enter Latitude :')
        z=input('Enter Longitude :')
        self.ms.loc.set_location(x,y,z)
        self.ms.__init__()
        input('')
        self.printmain()


    def load_opt4(self):
        x=self.ms.w.get_weather_now()
        print(x)
        input('')
        self.printmain()

    def load_opt5(self):
        x=self.ms.w.get_weather_forecast()
        print(x)
        input('')
        self.printmain()

        
    def load_opt6(self):
        x=self.ms.db.exec('select * from weathernow_dict')
        for i in x:
            print(*i)
        input('')
        self.printmain()

    def load_opt7(self):
        x=self.ms.db.exec('select * from weatherforecast_dict')
        for i in x:
            print(*i)
        input('')
        self.printmain()
    def load_opt8(self):
        self.ms.db.write(self.ms.wnow,'weathernow_dict')
        input('')
        self.printmain()        

    def load_opt9(self):
        self.ms.db.write(self.ms.wfor,'weatherforecast_dict')
        input('')
        self.printmain()
        
    def printmain(self):
        self.input=None
        print("\n\n\n")
        print(' M A I N  M E N U '.center(80,"="))
        print("|",' '.center(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",'                [ 1 ]-  Check Address Information.'.ljust(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",'                [ 2 ]-  Auto Detect Location.'.ljust(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",'                [ 3 ]-  Set Default Location.'.ljust(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",'                [ 4 ]-  Show Weather Now.'.ljust(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",'                [ 5 ]-  Show 36 Hours Weather.'.ljust(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",'                [ 6 ]-  DB.Show Weather Now.'.ljust(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",'                [ 7 ]-  DB.Show 36 Hours Weather.'.ljust(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",'                [ 8 ]-  DB.Save Weather Now.'.ljust(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",'                [ 9 ]-  DB.Save 36 Hours Weather.'.ljust(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",'                [10 ]-  Exit Application.'.ljust(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",' '.center(76," "),"|")
        print("|",''.center(76,"="),"|")
        self.input=input('Plese Enter Your Choice : ')
        if self.input =='1':self.load_opt1()                                             #[ 1 ]-  Check Address Information.
        elif self.input=='2':self.load_opt2()                                      #[ 2 ]-  Auto Detect Location.
        elif self.input=='3':self.load_opt3()                                      #[ 3 ]-  Set Default City.
        elif self.input=='4':self.load_opt4()                         #[ 4 ]-  Show Weather Now.
        elif self.input=='5':self.load_opt5()                    #[ 5 ]-  Show 36 Hours Weather.
        elif self.input=='6':self.load_opt6()                            #[ 6 ]-  DB.Show Offline Weather Now.(Last Saved Weather Record)
        elif self.input=='7':self.load_opt7()                            #[ 7 ]-  DB.Show Offline 36 Hours Weather.(Last Saved Weather Record)
        elif self.input=='8':self.load_opt8()                           #[ 8 ]-  DB.Save Weather Now.
        elif self.input=='9':self.load_opt9()                            #[ 9 ]-  DB.Save 36 Hours Weather.


class Weather:
    
    def __init__(self):      
        a=Configs()
        x=a.get_section('user_setting')
        self.city=x['city_name'].strip()
        self.lat=x['lat'].strip()
        self.lon=x['lon'].strip()
        self.status=self.is_wset()     
        self.weathernow_dict=None
        self.weatherforecast_dict=None
        self.get_weather_now()
        self.get_weather_forecast()

    def is_wset(self):
        if len(self.lat) !=0 and len(self.lon) !=0:
            return 1
        else:
            return 0
        

    def get_weather_now(self):
        if self.status==1:
            a=ApiGateway('api_1')
            self.weathernow_dict=a.get()
            return self.weathernow_dict
        else:
            return None

    def get_weather_forecast(self):
        if self.status==1:
            a=ApiGateway('api_4')
            self.weatherforecast_dict=a.get()
            return self.weatherforecast_dict
        else:
            return None
            

class View:
    def __init__(self):
        self.status=None
        self.cntr=0


    def get_flatten(self,ma,lst=[],parent='',tempd={}):
        self.lstp=lst
   
        if type(ma) is dict:
            for i in ma:
                self.get_flatten(ma[i],self.lstp,parent+ '.'+str(i))
        if type(ma) is list:
            for j in range(0,len(ma)):
                self.get_flatten(ma[j],self.lstp,parent+ '.'+str(j))
        else:          
            if type(ma) is list or type(ma) is dict:
                None
            else:
                self.cntr+=1
                parent=parent[1:]
                tempd[parent]=ma
        return tempd
                 

    def get_print(self,di):
        d1=self.get_flatten(di)
        cnt=1
        for k in d1:
            print(k.ljust(30,"-"),end=' | ')
            print(str(d1[k]).ljust(30,"-"))



class Locations:
    
    def __init__(self):
        self.conf=Configs()
        t=self.conf.get_section('user_setting')
        self.city=t['city_name']
        self.lat=t['lat']
        self.lon=t['lon']

    

    def set_location(self,city,lat,lon):
        self.conf.write('user_setting','city_name',str(city))
        self.conf.write('user_setting','lat',str(lat))
        self.conf.write('user_setting','lon',str(lon))
        t=self.conf.get_section('user_setting')
        self.city=t['city_name']
        self.lat=t['lat']
        self.lon=t['lon']



    def detect_location(self):
        a= ApiGateway('api_2')
        d=a.get()
        return str(d['city']),str(d['latitude']),str(d['longitude'])

    def search_location(self,text):
        a=ApiGateway('api_3')
        return a.get()
        
    def search_nominatim(self,adr):
        geo = Nominatim()
        loc = geo.geocode(adr, exactly_one=False, timeout=None)
        return loc


class ApiGateway:
    
    def __init__(self,api_no):
        self.url=None
        c = Configs()
        self.d = c.get_section(api_no)
        self.construct_api()
        self.json=None

        

    def get(self):
        try:
            response = urlopen(self.url)
            return json.load(response)

        except Exception as ex:
            return ex
    
    
    def construct_api(self):
        key_lst=[]
        value_lst=[]
        key_lst=list(self.d['keys'].split(','))
        for ff in key_lst:
            value_lst.append(self.d[ff])
        self.url=self.d['formula'].format(*value_lst)

 

class Configs:
    
    def __init__(self):
        self.conf=configparser.ConfigParser()
        self.conf._interpolation=configparser.ExtendedInterpolation()
        self.conf.read('conf.cfg')
        self.dc={}
        self.dc_sub={}
        self.load()


    def load(self):
        for sec in self.conf.sections():
            for opt in self.conf.options(sec):
                self.dc_sub[opt]=self.conf.get(sec,opt)
            self.dc.update({sec:self.dc_sub})
            self.dc_sub={}
            
    def get_section(self,sec):
        return self.dc[sec]
    
    def get_all(self):
        return self.dc

    def write(self,sec,key,value):
        cfgfile = open('conf.cfg','w')
        self.conf.set(sec,key,value)
        self.conf.write(cfgfile)
        cfgfile.close()
        self.__init__()
        return 'success'
        

class Database:
    
    def __init__(self, name):      
        self.name=name
        self.conn=None
        self.cursor=None
        c = Configs()
        self.d = c.get_section(name)['database']


    def open(self):
        self.conn = sqlite3.connect(self.d)
        self.cursor = self.conn.cursor()

    
    def close(self):        
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            self.conn=None
            self.cursor=None
            

    def exec(self,query):
        if self.conn==None:
            self.open()
        try:
            self.cursor.execute(query)
            if 'select' in query :
                rows = self.cursor.fetchall()
                return rows

        except Exception as ex: 
            return ex

        finally:
            self.close()

    def convert_flat_dict_tolist(self,ma):
        final_list=[]
        v=View()
        fdict=v.get_flatten(ma)
        for i in fdict:
            plst=[]
            t=i.split('.')
            for j in range (0,len(t)):
                plst.append(t[j])
            plst.append(fdict[i])
            final_list.append(plst)
        return final_list
                
            
    def write(self,dic,tab):
        lis=self.convert_flat_dict_tolist(dic)
        tem=['','','','','','','','']
        count=0
        for i in lis:
            tem=['','','','','','','','']
            for si in range (0,len(i)):tem[si]=i[si]
            qur="insert into {0} values {1}".format(tab,tuple(tem))
            self.exec(qur)




class Configs_Double:
    
    def __init__(self):
        self.dc={}
        self.load()


    def load(self):
        self.dc={'user_setting': {'city_name': 'Hamden', 'lat': '41.3745', 'lon': '-72.9396'}, 'db_1': {'database': 'data.db'}, 'show_1': {'return': 'main.temp_min,weather.[0].description'}, 'show_2': {'return': 'city,region_code,country_name'}, 'show_4': {'return': 'cnt,list.[0].dt'}, 'api_1': {'url': 'http://api.openweathermap.org/data/2.5/weather?', 'units': 'imperial', 'key': '612ea5670775e78679efe28d9c00265e', 'formula': '{0}lat={1}&lon={2}&mode={3}&units={4}&APPID={5}', 'keys': 'url,lat,lon,mode,units,key', 'lat': '41.3745', 'lon': '-72.9396', 'mode': 'json', 'return': 'main.temp_min,weather.[*].description'}, 'api_2': {'url': 'https://ipapi.co', 'mode': 'json', 'formula': '{0}/{1}', 'keys': 'url,mode', 'return': 'city,region_code,country_name'}, 'api_3': {'url': 'https://maps.googleapis.com/maps/api/place/textsearch', 'mode': 'json', 'city': 'Hamden', 'key': 'AIzaSyD5ksNiWdfsJik4Uh_v9o4M5OMluzcq3KY', 'formula': '{0}/{1}?query={2}&key={3}', 'keys': 'url,mode,city,key', 'return': 'results.0.location.lat,results.0.location.lng,results.0.name'}, 'api_4': {'url': 'http://api.openweathermap.org/data/2.5/forecast?', 'units': 'imperial', 'key': '612ea5670775e78679efe28d9c00265e', 'formula': '{0}lat={1}&lon={2}&mode={3}&units={4}&APPID={5}', 'keys': 'url,lat,lon,mode,units,key', 'lat': '41.3745', 'lon': '-72.9396', 'mode': 'json', 'return': 'weather.0.main,weather.main.temp'}, 'api_5': {'url': 'https://api.darksky.net/forecast', 'units': 'imperial', 'key': 'e28826d45c3a9316c946396a2c8f1a71', 'formula': '{0}/{1}/{2},{3}', 'keys': 'url,key,lat,lon', 'lat': '41.3745', 'lon': '-72.9396', 'return': 'latitude,longitude,currently.summary,currently.temperature,daily.data.[0]'}, 'test': {'key': 'hello world'}}
            
            
    def get_section(self,sec):
        return self.dc[sec]
    
    def get_all(self):
        return self.dc


class ApiGateway_Double:
    
    def __init__(self,api_no):
        self.url=None
        c = Configs_Double()
        self.d = c.get_section(api_no)
        self.construct_api()
        self.json=None

        

    def get(self):
        return {'coord': {'lon': -72.94, 'lat': 41.37}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}, {'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}], 'base': 'stations', 'main': {'temp': 38.55, 'pressure': 1019, 'humidity': 86, 'temp_min': 33.8, 'temp_max': 42.8}, 'visibility': 8047, 'wind': {'speed': 4.7}, 'clouds': {'all': 90}, 'dt': 1522228320, 'sys': {'type': 1, 'id': 627, 'message': 0.1648, 'country': 'US', 'sunrise': 1522233655, 'sunset': 1522278783}, 'id': 4839373, 'name': 'New Haven County', 'cod': 200}
    
    
    def construct_api(self):
        key_lst=[]
        value_lst=[]
        key_lst=list(self.d['keys'].split(','))
        for ff in key_lst:
            value_lst.append(self.d[ff])
        self.url=self.d['formula'].format(*value_lst)



class Main_Service:
    def __init__(self):
        self.loc=Locations()
        self.w=Weather()
        self.wnow=self.w.weathernow_dict
        self.wfor=self.w.weatherforecast_dict
        self.city=self.w.city
        self.lat=self.w.lat
        self.lon=self.w.lon
        self.db=Database('db_1')





    def exec_opt(self,opt,*args):
        if opt ==1:return self.loc.search_nominatim(args[0])                #[ 1 ]-  Check Address Information.
        elif opt==2:return self.loc.detect_location()                       #[ 2 ]-  Auto Detect Location.
        elif opt==3:return self.loc.set_location(args[0],args[1],args[2])   #[ 3 ]-  Set Default City.
        elif opt==4:return self.w.get_weather_now()                         #[ 4 ]-  Show Weather Now.
        elif opt==5:return self.w.get_weather_forecast()                    #[ 5 ]-  Show 36 Hours Weather.
        elif opt==6:return self.db.exec(args[0])                            #[ 6 ]-  DB.Show Offline Weather Now.(Last Saved Weather Record)
        elif opt==7:return self.db.exec(args[0])                            #[ 7 ]-  DB.Show Offline 36 Hours Weather.(Last Saved Weather Record)
        elif opt==8:return self.db.exec(args[0])                            #[ 8 ]-  DB.Save Weather Now.
        elif opt==9:return self.db.exec(args[0])                            #[ 9 ]-  DB.Save 36 Hours Weather.
            

