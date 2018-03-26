from urllib.request import urlopen
import json
from backports import configparser
import sqlite3
from geopy.geocoders import Nominatim



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

