from Class_Definition import *
import json


class Logic_Service:
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
            
locat=['Hamden', 41.3745, -72.9396]            
ash=['Lincoln,New Hampshire',44.045648,-71.670685]
query_7="select * from weatherforecast limit 1"
i=Logic_Service()
print(i.exec_opt(2,*locat))
