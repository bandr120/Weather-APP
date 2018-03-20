#openweathermap api default configuration
api_1={'url':'http://api.openweathermap.org/data/2.5/weather?',
     'units':'imperial',
     'key':'612ea5670775e78679efe28d9c00265e',
     'formula':"{0}lat={1}&lon={2}&mode={3}&units={4}&APPID={5}",
     }



#"ipapi" api default configuration
api_2={'url':'https://ipapi.co',
        'mode':'json',
        'formula':"{0}/{1}",
     }


#"google" api default configuration
api_3={'url':'https://maps.googleapis.com/maps/api/place/textsearch',
       'mode':'json',
       'key':'AIzaSyD5ksNiWdfsJik4Uh_v9o4M5OMluzcq3KY',
       'formula':"{0}/{1}?query={2}&key={3}",
     }


#Database Configuration
db_1={'database':'data.db',
      'formula_insert_weather':"insert into {0} values({1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12});",
      'formula_select':"select * from {0} where {1} LIMIT {3};"}
