from urllib.request import urlopen
import json
class ApiGateway:
    
    def __init__(self,formula,*args):
        try:
            self.formula=formula
            self.url=self.formula.format(*args)
        except Exception as ex:
            return ex
        

    def get(self):      #to call the online api and returns json dictionary
        try:
            response = urlopen(self.url)
            return json.load(response)

        except Exception as ex:
            return ex
    



"""
a = 'https://maps.googleapis.com/maps/api/place/textsearch'
mod="json"
ky='AIzaSyD5ksNiWdfsJik4Uh_v9o4M5OMluzcq3KY'
forma="{0}/{1}?query={2}&key={3}"
loc="06518"
ap = ApiGateway(forma,a,mod,loc,ky)
print(ap.get())

"""



"""
uuu='https://ipapi.co'
mmm='json'
fff="{0}/{1}"
a = 'http://api.openweathermap.org/data/2.5/weather?'
la="41.3745"
lo="-72.9396"
mod="json"
un='imperial'
ky='612ea5670775e78679efe28d9c00265e'
forma="{0}lat={1}&lon={2}&mode={3}&units={4}&APPID={5}"
u=forma.format(a,la,lo,mod,un,ky)
#ap = ApiGateway(forma,a,la,lo,mod,un,ky)
ap = ApiGateway('https://ipapi.co/json')
print(ap.get())
"""
