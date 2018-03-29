import unittest
import os.path
from  Class_Definition import  *



class test_View(unittest.TestCase):

    def test_Convert_Nested_Dictionary_To_Flat(self):
        try:
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            dictionary= {'cod': '200', 'message': 0.0052, 'cnt': 40, 'list': [{'dt': 1521655200, 'main': {'temp': 34.83, 'temp_min': 34.3, 'temp_max': 34.83, 'pressure': 1002.49, 'sea_level': 1018.25, 'grnd_level': 1002.49, 'humidity': 88, 'temp_kf': 0.29}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 92}, 'wind': {'speed': 10.6, 'deg': 39.5017}, 'rain': {'3h': 0.015}, 'snow': {'3h': 3.953}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-21 18:00:00'}, {'dt': 1521666000, 'main': {'temp': 34.25, 'temp_min': 33.87, 'temp_max': 34.25, 'pressure': 1001.65, 'sea_level': 1017.43, 'grnd_level': 1001.65, 'humidity': 90, 'temp_kf': 0.22}, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}], 'clouds': {'all': 92}, 'wind': {'speed': 11.01, 'deg': 29.5009}, 'rain': {}, 'snow': {'3h': 4.774}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-21 21:00:00'}, {'dt': 1521676800, 'main': {'temp': 33.17, 'temp_min': 32.91, 'temp_max': 33.17, 'pressure': 1002.71, 'sea_level': 1018.45, 'grnd_level': 1002.71, 'humidity': 88, 'temp_kf': 0.14}, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13n'}], 'clouds': {'all': 92}, 'wind': {'speed': 11.12, 'deg': 28.5023}, 'rain': {}, 'snow': {'3h': 4.061}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-22 00:00:00'}, {'dt': 1521687600, 'main': {'temp': 32.63, 'temp_min': 32.51, 'temp_max': 32.63, 'pressure': 1003.13, 'sea_level': 1018.85, 'grnd_level': 1003.13, 'humidity': 90, 'temp_kf': 0.07}, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13n'}], 'clouds': {'all': 92}, 'wind': {'speed': 11.45, 'deg': 22.5002}, 'rain': {}, 'snow': {'3h': 4.417}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-22 03:00:00'}, {'dt': 1521698400, 'main': {'temp': 33.09, 'temp_min': 33.09, 'temp_max': 33.09, 'pressure': 1002.12, 'sea_level': 1017.88, 'grnd_level': 1002.12, 'humidity': 88, 'temp_kf': 0}, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13n'}], 'clouds': {'all': 92}, 'wind': {'speed': 11.77, 'deg': 11.0036}, 'rain': {}, 'snow': {'3h': 1.768}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-22 06:00:00'}, {'dt': 1521709200, 'main': {'temp': 33.69, 'temp_min': 33.69, 'temp_max': 33.69, 'pressure': 1002.4, 'sea_level': 1018.24, 'grnd_level': 1002.4, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 92}, 'wind': {'speed': 10.54, 'deg': 3}, 'rain': {'3h': 0.045}, 'snow': {'3h': 0.975}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-22 09:00:00'}, {'dt': 1521720000, 'main': {'temp': 34.31, 'temp_min': 34.31, 'temp_max': 34.31, 'pressure': 1004.64, 'sea_level': 1020.37, 'grnd_level': 1004.64, 'humidity': 84, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 92}, 'wind': {'speed': 8.97, 'deg': 352.001}, 'rain': {'3h': 0.07}, 'snow': {'3h': 0.489}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-22 12:00:00'}, {'dt': 1521730800, 'main': {'temp': 37.77, 'temp_min': 37.77, 'temp_max': 37.77, 'pressure': 1005.76, 'sea_level': 1021.58, 'grnd_level': 1005.76, 'humidity': 75, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 80}, 'wind': {'speed': 8.84, 'deg': 341.003}, 'rain': {'3h': 0.04}, 'snow': {'3h': 0.022000000000002}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-22 15:00:00'}, {'dt': 1521741600, 'main': {'temp': 40.22, 'temp_min': 40.22, 'temp_max': 40.22, 'pressure': 1006.28, 'sea_level': 1021.94, 'grnd_level': 1006.28, 'humidity': 70, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 88}, 'wind': {'speed': 8.97, 'deg': 334.503}, 'rain': {}, 'snow': {'3h': 0.00019999999999953}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-22 18:00:00'}, {'dt': 1521752400, 'main': {'temp': 40.87, 'temp_min': 40.87, 'temp_max': 40.87, 'pressure': 1007.33, 'sea_level': 1022.97, 'grnd_level': 1007.33, 'humidity': 69, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 88}, 'wind': {'speed': 8.1, 'deg': 337.506}, 'rain': {'3h': 0.01}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-22 21:00:00'}, {'dt': 1521763200, 'main': {'temp': 38.7, 'temp_min': 38.7, 'temp_max': 38.7, 'pressure': 1009.41, 'sea_level': 1025.23, 'grnd_level': 1009.41, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 76}, 'wind': {'speed': 7, 'deg': 337.001}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-23 00:00:00'}, {'dt': 1521774000, 'main': {'temp': 35.48, 'temp_min': 35.48, 'temp_max': 35.48, 'pressure': 1011.58, 'sea_level': 1027.38, 'grnd_level': 1011.58, 'humidity': 78, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 68}, 'wind': {'speed': 6.73, 'deg': 335.5}, 'rain': {}, 'snow': {'3h': 0.0013000000000005}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-23 03:00:00'}, {'dt': 1521784800, 'main': {'temp': 32.33, 'temp_min': 32.33, 'temp_max': 32.33, 'pressure': 1012.53, 'sea_level': 1028.46, 'grnd_level': 1012.53, 'humidity': 84, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 80}, 'wind': {'speed': 6.08, 'deg': 339.002}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-23 06:00:00'}, {'dt': 1521795600, 'main': {'temp': 30.59, 'temp_min': 30.59, 'temp_max': 30.59, 'pressure': 1012.78, 'sea_level': 1028.81, 'grnd_level': 1012.78, 'humidity': 90, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 76}, 'wind': {'speed': 4.97, 'deg': 325.002}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-23 09:00:00'}, {'dt': 1521806400, 'main': {'temp': 32.02, 'temp_min': 32.02, 'temp_max': 32.02, 'pressure': 1013.77, 'sea_level': 1029.71, 'grnd_level': 1013.77, 'humidity': 87, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 76}, 'wind': {'speed': 4.94, 'deg': 320.501}, 'rain': {}, 'snow': {'3h': 0.0075000000000003}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-23 12:00:00'}, {'dt': 1521817200, 'main': {'temp': 38.61, 'temp_min': 38.61, 'temp_max': 38.61, 'pressure': 1013.53, 'sea_level': 1029.39, 'grnd_level': 1013.53, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 44}, 'wind': {'speed': 4.94, 'deg': 331.004}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-23 15:00:00'}, {'dt': 1521828000, 'main': {'temp': 40.54, 'temp_min': 40.54, 'temp_max': 40.54, 'pressure': 1012.73, 'sea_level': 1028.45, 'grnd_level': 1012.73, 'humidity': 66, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 88}, 'wind': {'speed': 5.75, 'deg': 331.006}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-23 18:00:00'}, {'dt': 1521838800, 'main': {'temp': 39.58, 'temp_min': 39.58, 'temp_max': 39.58, 'pressure': 1012.82, 'sea_level': 1028.63, 'grnd_level': 1012.82, 'humidity': 67, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 76}, 'wind': {'speed': 6.73, 'deg': 338}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-23 21:00:00'}, {'dt': 1521849600, 'main': {'temp': 35.21, 'temp_min': 35.21, 'temp_max': 35.21, 'pressure': 1014.88, 'sea_level': 1030.77, 'grnd_level': 1014.88, 'humidity': 75, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 64}, 'wind': {'speed': 7.29, 'deg': 345.001}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-24 00:00:00'}, {'dt': 1521860400, 'main': {'temp': 31.81, 'temp_min': 31.81, 'temp_max': 31.81, 'pressure': 1016.71, 'sea_level': 1032.67, 'grnd_level': 1016.71, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'clouds': {'all': 12}, 'wind': {'speed': 6.67, 'deg': 347.002}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-24 03:00:00'}, {'dt': 1521871200, 'main': {'temp': 28.57, 'temp_min': 28.57, 'temp_max': 28.57, 'pressure': 1017.45, 'sea_level': 1033.57, 'grnd_level': 1017.45, 'humidity': 89, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'clouds': {'all': 20}, 'wind': {'speed': 6.17, 'deg': 344.501}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-24 06:00:00'}, {'dt': 1521882000, 'main': {'temp': 27.21, 'temp_min': 27.21, 'temp_max': 27.21, 'pressure': 1017.72, 'sea_level': 1033.9, 'grnd_level': 1017.72, 'humidity': 91, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'clouds': {'all': 12}, 'wind': {'speed': 6.17, 'deg': 338.5}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-24 09:00:00'}, {'dt': 1521892800, 'main': {'temp': 28.05, 'temp_min': 28.05, 'temp_max': 28.05, 'pressure': 1018.67, 'sea_level': 1034.89, 'grnd_level': 1018.67, 'humidity': 88, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'clouds': {'all': 24}, 'wind': {'speed': 6.17, 'deg': 336.502}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-24 12:00:00'}, {'dt': 1521903600, 'main': {'temp': 36.11, 'temp_min': 36.11, 'temp_max': 36.11, 'pressure': 1018.9, 'sea_level': 1034.88, 'grnd_level': 1018.9, 'humidity': 70, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 44}, 'wind': {'speed': 5.06, 'deg': 349.002}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-24 15:00:00'}, {'dt': 1521914400, 'main': {'temp': 40.07, 'temp_min': 40.07, 'temp_max': 40.07, 'pressure': 1018.19, 'sea_level': 1034.12, 'grnd_level': 1018.19, 'humidity': 62, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 44}, 'wind': {'speed': 3.4, 'deg': 312.5}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-24 18:00:00'}, {'dt': 1521925200, 'main': {'temp': 40.34, 'temp_min': 40.34, 'temp_max': 40.34, 'pressure': 1016.68, 'sea_level': 1032.65, 'grnd_level': 1016.68, 'humidity': 61, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 64}, 'wind': {'speed': 3.04, 'deg': 343.001}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-24 21:00:00'}, {'dt': 1521936000, 'main': {'temp': 34.58, 'temp_min': 34.58, 'temp_max': 34.58, 'pressure': 1017.96, 'sea_level': 1033.97, 'grnd_level': 1017.96, 'humidity': 74, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 76}, 'wind': {'speed': 2.26, 'deg': 6.50348}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-25 00:00:00'}, {'dt': 1521946800, 'main': {'temp': 31.03, 'temp_min': 31.03, 'temp_max': 31.03, 'pressure': 1018.96, 'sea_level': 1035.08, 'grnd_level': 1018.96, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 68}, 'wind': {'speed': 1.57, 'deg': 22.5013}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-25 03:00:00'}, {'dt': 1521957600, 'main': {'temp': 29.32, 'temp_min': 29.32, 'temp_max': 29.32, 'pressure': 1019.39, 'sea_level': 1035.56, 'grnd_level': 1019.39, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 88}, 'wind': {'speed': 2.93, 'deg': 358.501}, 'rain': {}, 'snow': {'3h': 0.014999999999997}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-25 06:00:00'}, {'dt': 1521968400, 'main': {'temp': 26.53, 'temp_min': 26.53, 'temp_max': 26.53, 'pressure': 1019.47, 'sea_level': 1035.68, 'grnd_level': 1019.47, 'humidity': 100, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 12}, 'wind': {'speed': 4.94, 'deg': 33.5}, 'rain': {}, 'snow': {'3h': 0.015000000000001}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-25 09:00:00'}, {'dt': 1521979200, 'main': {'temp': 29.36, 'temp_min': 29.36, 'temp_max': 29.36, 'pressure': 1021.8, 'sea_level': 1037.9, 'grnd_level': 1021.8, 'humidity': 100, 'temp_kf': 0}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'clouds': {'all': 64}, 'wind': {'speed': 5.84, 'deg': 48.0035}, 'rain': {}, 'snow': {'3h': 0.09}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-25 12:00:00'}, {'dt': 1521990000, 'main': {'temp': 36.47, 'temp_min': 36.47, 'temp_max': 36.47, 'pressure': 1023.34, 'sea_level': 1039.36, 'grnd_level': 1023.34, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'clouds': {'all': 64}, 'wind': {'speed': 6.96, 'deg': 42.5003}, 'rain': {}, 'snow': {'3h': 0.030000000000001}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-25 15:00:00'}, {'dt': 1522000800, 'main': {'temp': 35.16, 'temp_min': 35.16, 'temp_max': 35.16, 'pressure': 1024.93, 'sea_level': 1040.91, 'grnd_level': 1024.93, 'humidity': 87, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 88}, 'wind': {'speed': 7.78, 'deg': 52.0013}, 'rain': {'3h': 0.08}, 'snow': {'3h': 0.95}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-25 18:00:00'}, {'dt': 1522011600, 'main': {'temp': 37.09, 'temp_min': 37.09, 'temp_max': 37.09, 'pressure': 1026.38, 'sea_level': 1042.34, 'grnd_level': 1026.38, 'humidity': 72, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 64}, 'wind': {'speed': 8.61, 'deg': 40.0036}, 'rain': {'3h': 0.01}, 'snow': {'3h': 0.080000000000002}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-25 21:00:00'}, {'dt': 1522022400, 'main': {'temp': 32.72, 'temp_min': 32.72, 'temp_max': 32.72, 'pressure': 1029.21, 'sea_level': 1045.32, 'grnd_level': 1029.21, 'humidity': 81, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'clouds': {'all': 24}, 'wind': {'speed': 8.32, 'deg': 37.0011}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-26 00:00:00'}, {'dt': 1522033200, 'main': {'temp': 29.09, 'temp_min': 29.09, 'temp_max': 29.09, 'pressure': 1031.3, 'sea_level': 1047.61, 'grnd_level': 1031.3, 'humidity': 88, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 7.67, 'deg': 37.0033}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-26 03:00:00'}, {'dt': 1522044000, 'main': {'temp': 26.59, 'temp_min': 26.59, 'temp_max': 26.59, 'pressure': 1032.47, 'sea_level': 1048.75, 'grnd_level': 1032.47, 'humidity': 91, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 7.99, 'deg': 30.0015}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-26 06:00:00'}, {'dt': 1522054800, 'main': {'temp': 25.18, 'temp_min': 25.18, 'temp_max': 25.18, 'pressure': 1032.94, 'sea_level': 1049.42, 'grnd_level': 1032.94, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 8.63, 'deg': 26.007}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-26 09:00:00'}, {'dt': 1522065600, 'main': {'temp': 25.49, 'temp_min': 25.49, 'temp_max': 25.49, 'pressure': 1034.74, 'sea_level': 1051.27, 'grnd_level': 1034.74, 'humidity': 85, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 8.88, 'deg': 24.006}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-26 12:00:00'}, {'dt': 1522076400, 'main': {'temp': 31.94, 'temp_min': 31.94, 'temp_max': 31.94, 'pressure': 1035.52, 'sea_level': 1051.86, 'grnd_level': 1035.52, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 8.97, 'deg': 25.5096}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-26 15:00:00'}], 'city': {'id': 4839373, 'name': 'New Haven County', 'coord': {'lat': 41.4001, 'lon': -72.9329}, 'country': 'US', 'population': 862477}}
            v=View()
            cv=v.get_flatten(dictionary)
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))
        
    def test_Validating_Converted_Dictionary(self):
        try:
            dictionary= {'cod': '200', 'message': 0.0052, 'cnt': 40, 'list': [{'dt': 1521655200, 'main': {'temp': 34.83, 'temp_min': 34.3, 'temp_max': 34.83, 'pressure': 1002.49, 'sea_level': 1018.25, 'grnd_level': 1002.49, 'humidity': 88, 'temp_kf': 0.29}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 92}, 'wind': {'speed': 10.6, 'deg': 39.5017}, 'rain': {'3h': 0.015}, 'snow': {'3h': 3.953}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-21 18:00:00'}, {'dt': 1521666000, 'main': {'temp': 34.25, 'temp_min': 33.87, 'temp_max': 34.25, 'pressure': 1001.65, 'sea_level': 1017.43, 'grnd_level': 1001.65, 'humidity': 90, 'temp_kf': 0.22}, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13d'}], 'clouds': {'all': 92}, 'wind': {'speed': 11.01, 'deg': 29.5009}, 'rain': {}, 'snow': {'3h': 4.774}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-21 21:00:00'}, {'dt': 1521676800, 'main': {'temp': 33.17, 'temp_min': 32.91, 'temp_max': 33.17, 'pressure': 1002.71, 'sea_level': 1018.45, 'grnd_level': 1002.71, 'humidity': 88, 'temp_kf': 0.14}, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13n'}], 'clouds': {'all': 92}, 'wind': {'speed': 11.12, 'deg': 28.5023}, 'rain': {}, 'snow': {'3h': 4.061}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-22 00:00:00'}, {'dt': 1521687600, 'main': {'temp': 32.63, 'temp_min': 32.51, 'temp_max': 32.63, 'pressure': 1003.13, 'sea_level': 1018.85, 'grnd_level': 1003.13, 'humidity': 90, 'temp_kf': 0.07}, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13n'}], 'clouds': {'all': 92}, 'wind': {'speed': 11.45, 'deg': 22.5002}, 'rain': {}, 'snow': {'3h': 4.417}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-22 03:00:00'}, {'dt': 1521698400, 'main': {'temp': 33.09, 'temp_min': 33.09, 'temp_max': 33.09, 'pressure': 1002.12, 'sea_level': 1017.88, 'grnd_level': 1002.12, 'humidity': 88, 'temp_kf': 0}, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13n'}], 'clouds': {'all': 92}, 'wind': {'speed': 11.77, 'deg': 11.0036}, 'rain': {}, 'snow': {'3h': 1.768}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-22 06:00:00'}, {'dt': 1521709200, 'main': {'temp': 33.69, 'temp_min': 33.69, 'temp_max': 33.69, 'pressure': 1002.4, 'sea_level': 1018.24, 'grnd_level': 1002.4, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 92}, 'wind': {'speed': 10.54, 'deg': 3}, 'rain': {'3h': 0.045}, 'snow': {'3h': 0.975}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-22 09:00:00'}, {'dt': 1521720000, 'main': {'temp': 34.31, 'temp_min': 34.31, 'temp_max': 34.31, 'pressure': 1004.64, 'sea_level': 1020.37, 'grnd_level': 1004.64, 'humidity': 84, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 92}, 'wind': {'speed': 8.97, 'deg': 352.001}, 'rain': {'3h': 0.07}, 'snow': {'3h': 0.489}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-22 12:00:00'}, {'dt': 1521730800, 'main': {'temp': 37.77, 'temp_min': 37.77, 'temp_max': 37.77, 'pressure': 1005.76, 'sea_level': 1021.58, 'grnd_level': 1005.76, 'humidity': 75, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 80}, 'wind': {'speed': 8.84, 'deg': 341.003}, 'rain': {'3h': 0.04}, 'snow': {'3h': 0.022000000000002}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-22 15:00:00'}, {'dt': 1521741600, 'main': {'temp': 40.22, 'temp_min': 40.22, 'temp_max': 40.22, 'pressure': 1006.28, 'sea_level': 1021.94, 'grnd_level': 1006.28, 'humidity': 70, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 88}, 'wind': {'speed': 8.97, 'deg': 334.503}, 'rain': {}, 'snow': {'3h': 0.00019999999999953}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-22 18:00:00'}, {'dt': 1521752400, 'main': {'temp': 40.87, 'temp_min': 40.87, 'temp_max': 40.87, 'pressure': 1007.33, 'sea_level': 1022.97, 'grnd_level': 1007.33, 'humidity': 69, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 88}, 'wind': {'speed': 8.1, 'deg': 337.506}, 'rain': {'3h': 0.01}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-22 21:00:00'}, {'dt': 1521763200, 'main': {'temp': 38.7, 'temp_min': 38.7, 'temp_max': 38.7, 'pressure': 1009.41, 'sea_level': 1025.23, 'grnd_level': 1009.41, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 76}, 'wind': {'speed': 7, 'deg': 337.001}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-23 00:00:00'}, {'dt': 1521774000, 'main': {'temp': 35.48, 'temp_min': 35.48, 'temp_max': 35.48, 'pressure': 1011.58, 'sea_level': 1027.38, 'grnd_level': 1011.58, 'humidity': 78, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 68}, 'wind': {'speed': 6.73, 'deg': 335.5}, 'rain': {}, 'snow': {'3h': 0.0013000000000005}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-23 03:00:00'}, {'dt': 1521784800, 'main': {'temp': 32.33, 'temp_min': 32.33, 'temp_max': 32.33, 'pressure': 1012.53, 'sea_level': 1028.46, 'grnd_level': 1012.53, 'humidity': 84, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 80}, 'wind': {'speed': 6.08, 'deg': 339.002}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-23 06:00:00'}, {'dt': 1521795600, 'main': {'temp': 30.59, 'temp_min': 30.59, 'temp_max': 30.59, 'pressure': 1012.78, 'sea_level': 1028.81, 'grnd_level': 1012.78, 'humidity': 90, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 76}, 'wind': {'speed': 4.97, 'deg': 325.002}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-23 09:00:00'}, {'dt': 1521806400, 'main': {'temp': 32.02, 'temp_min': 32.02, 'temp_max': 32.02, 'pressure': 1013.77, 'sea_level': 1029.71, 'grnd_level': 1013.77, 'humidity': 87, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 76}, 'wind': {'speed': 4.94, 'deg': 320.501}, 'rain': {}, 'snow': {'3h': 0.0075000000000003}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-23 12:00:00'}, {'dt': 1521817200, 'main': {'temp': 38.61, 'temp_min': 38.61, 'temp_max': 38.61, 'pressure': 1013.53, 'sea_level': 1029.39, 'grnd_level': 1013.53, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 44}, 'wind': {'speed': 4.94, 'deg': 331.004}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-23 15:00:00'}, {'dt': 1521828000, 'main': {'temp': 40.54, 'temp_min': 40.54, 'temp_max': 40.54, 'pressure': 1012.73, 'sea_level': 1028.45, 'grnd_level': 1012.73, 'humidity': 66, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 88}, 'wind': {'speed': 5.75, 'deg': 331.006}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-23 18:00:00'}, {'dt': 1521838800, 'main': {'temp': 39.58, 'temp_min': 39.58, 'temp_max': 39.58, 'pressure': 1012.82, 'sea_level': 1028.63, 'grnd_level': 1012.82, 'humidity': 67, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 76}, 'wind': {'speed': 6.73, 'deg': 338}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-23 21:00:00'}, {'dt': 1521849600, 'main': {'temp': 35.21, 'temp_min': 35.21, 'temp_max': 35.21, 'pressure': 1014.88, 'sea_level': 1030.77, 'grnd_level': 1014.88, 'humidity': 75, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 64}, 'wind': {'speed': 7.29, 'deg': 345.001}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-24 00:00:00'}, {'dt': 1521860400, 'main': {'temp': 31.81, 'temp_min': 31.81, 'temp_max': 31.81, 'pressure': 1016.71, 'sea_level': 1032.67, 'grnd_level': 1016.71, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'clouds': {'all': 12}, 'wind': {'speed': 6.67, 'deg': 347.002}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-24 03:00:00'}, {'dt': 1521871200, 'main': {'temp': 28.57, 'temp_min': 28.57, 'temp_max': 28.57, 'pressure': 1017.45, 'sea_level': 1033.57, 'grnd_level': 1017.45, 'humidity': 89, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'clouds': {'all': 20}, 'wind': {'speed': 6.17, 'deg': 344.501}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-24 06:00:00'}, {'dt': 1521882000, 'main': {'temp': 27.21, 'temp_min': 27.21, 'temp_max': 27.21, 'pressure': 1017.72, 'sea_level': 1033.9, 'grnd_level': 1017.72, 'humidity': 91, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'clouds': {'all': 12}, 'wind': {'speed': 6.17, 'deg': 338.5}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-24 09:00:00'}, {'dt': 1521892800, 'main': {'temp': 28.05, 'temp_min': 28.05, 'temp_max': 28.05, 'pressure': 1018.67, 'sea_level': 1034.89, 'grnd_level': 1018.67, 'humidity': 88, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'clouds': {'all': 24}, 'wind': {'speed': 6.17, 'deg': 336.502}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-24 12:00:00'}, {'dt': 1521903600, 'main': {'temp': 36.11, 'temp_min': 36.11, 'temp_max': 36.11, 'pressure': 1018.9, 'sea_level': 1034.88, 'grnd_level': 1018.9, 'humidity': 70, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 44}, 'wind': {'speed': 5.06, 'deg': 349.002}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-24 15:00:00'}, {'dt': 1521914400, 'main': {'temp': 40.07, 'temp_min': 40.07, 'temp_max': 40.07, 'pressure': 1018.19, 'sea_level': 1034.12, 'grnd_level': 1018.19, 'humidity': 62, 'temp_kf': 0}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 44}, 'wind': {'speed': 3.4, 'deg': 312.5}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-24 18:00:00'}, {'dt': 1521925200, 'main': {'temp': 40.34, 'temp_min': 40.34, 'temp_max': 40.34, 'pressure': 1016.68, 'sea_level': 1032.65, 'grnd_level': 1016.68, 'humidity': 61, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 64}, 'wind': {'speed': 3.04, 'deg': 343.001}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-24 21:00:00'}, {'dt': 1521936000, 'main': {'temp': 34.58, 'temp_min': 34.58, 'temp_max': 34.58, 'pressure': 1017.96, 'sea_level': 1033.97, 'grnd_level': 1017.96, 'humidity': 74, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 76}, 'wind': {'speed': 2.26, 'deg': 6.50348}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-25 00:00:00'}, {'dt': 1521946800, 'main': {'temp': 31.03, 'temp_min': 31.03, 'temp_max': 31.03, 'pressure': 1018.96, 'sea_level': 1035.08, 'grnd_level': 1018.96, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 68}, 'wind': {'speed': 1.57, 'deg': 22.5013}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-25 03:00:00'}, {'dt': 1521957600, 'main': {'temp': 29.32, 'temp_min': 29.32, 'temp_max': 29.32, 'pressure': 1019.39, 'sea_level': 1035.56, 'grnd_level': 1019.39, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 88}, 'wind': {'speed': 2.93, 'deg': 358.501}, 'rain': {}, 'snow': {'3h': 0.014999999999997}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-25 06:00:00'}, {'dt': 1521968400, 'main': {'temp': 26.53, 'temp_min': 26.53, 'temp_max': 26.53, 'pressure': 1019.47, 'sea_level': 1035.68, 'grnd_level': 1019.47, 'humidity': 100, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 12}, 'wind': {'speed': 4.94, 'deg': 33.5}, 'rain': {}, 'snow': {'3h': 0.015000000000001}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-25 09:00:00'}, {'dt': 1521979200, 'main': {'temp': 29.36, 'temp_min': 29.36, 'temp_max': 29.36, 'pressure': 1021.8, 'sea_level': 1037.9, 'grnd_level': 1021.8, 'humidity': 100, 'temp_kf': 0}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'clouds': {'all': 64}, 'wind': {'speed': 5.84, 'deg': 48.0035}, 'rain': {}, 'snow': {'3h': 0.09}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-25 12:00:00'}, {'dt': 1521990000, 'main': {'temp': 36.47, 'temp_min': 36.47, 'temp_max': 36.47, 'pressure': 1023.34, 'sea_level': 1039.36, 'grnd_level': 1023.34, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 600, 'main': 'Snow', 'description': 'light snow', 'icon': '13d'}], 'clouds': {'all': 64}, 'wind': {'speed': 6.96, 'deg': 42.5003}, 'rain': {}, 'snow': {'3h': 0.030000000000001}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-25 15:00:00'}, {'dt': 1522000800, 'main': {'temp': 35.16, 'temp_min': 35.16, 'temp_max': 35.16, 'pressure': 1024.93, 'sea_level': 1040.91, 'grnd_level': 1024.93, 'humidity': 87, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 88}, 'wind': {'speed': 7.78, 'deg': 52.0013}, 'rain': {'3h': 0.08}, 'snow': {'3h': 0.95}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-25 18:00:00'}, {'dt': 1522011600, 'main': {'temp': 37.09, 'temp_min': 37.09, 'temp_max': 37.09, 'pressure': 1026.38, 'sea_level': 1042.34, 'grnd_level': 1026.38, 'humidity': 72, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 64}, 'wind': {'speed': 8.61, 'deg': 40.0036}, 'rain': {'3h': 0.01}, 'snow': {'3h': 0.080000000000002}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-25 21:00:00'}, {'dt': 1522022400, 'main': {'temp': 32.72, 'temp_min': 32.72, 'temp_max': 32.72, 'pressure': 1029.21, 'sea_level': 1045.32, 'grnd_level': 1029.21, 'humidity': 81, 'temp_kf': 0}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'clouds': {'all': 24}, 'wind': {'speed': 8.32, 'deg': 37.0011}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-26 00:00:00'}, {'dt': 1522033200, 'main': {'temp': 29.09, 'temp_min': 29.09, 'temp_max': 29.09, 'pressure': 1031.3, 'sea_level': 1047.61, 'grnd_level': 1031.3, 'humidity': 88, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 7.67, 'deg': 37.0033}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-26 03:00:00'}, {'dt': 1522044000, 'main': {'temp': 26.59, 'temp_min': 26.59, 'temp_max': 26.59, 'pressure': 1032.47, 'sea_level': 1048.75, 'grnd_level': 1032.47, 'humidity': 91, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 7.99, 'deg': 30.0015}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-26 06:00:00'}, {'dt': 1522054800, 'main': {'temp': 25.18, 'temp_min': 25.18, 'temp_max': 25.18, 'pressure': 1032.94, 'sea_level': 1049.42, 'grnd_level': 1032.94, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 8.63, 'deg': 26.007}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'n'}, 'dt_txt': '2018-03-26 09:00:00'}, {'dt': 1522065600, 'main': {'temp': 25.49, 'temp_min': 25.49, 'temp_max': 25.49, 'pressure': 1034.74, 'sea_level': 1051.27, 'grnd_level': 1034.74, 'humidity': 85, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 8.88, 'deg': 24.006}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-26 12:00:00'}, {'dt': 1522076400, 'main': {'temp': 31.94, 'temp_min': 31.94, 'temp_max': 31.94, 'pressure': 1035.52, 'sea_level': 1051.86, 'grnd_level': 1035.52, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 8.97, 'deg': 25.5096}, 'rain': {}, 'snow': {}, 'sys': {'pod': 'd'}, 'dt_txt': '2018-03-26 15:00:00'}], 'city': {'id': 4839373, 'name': 'New Haven County', 'coord': {'lat': 41.4001, 'lon': -72.9329}, 'country': 'US', 'population': 862477}}
            v=View()
            cv=v.get_flatten(dictionary)
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            self.assertNotEqual(len(cv),len(dictionary),"\n\n----------------------------Returned Dictionary Length Don't Match")
            self.assertTrue(type(cv) is dict,"\n\n----------------------------Returned Value Type  Don't Match")
            self.assertTrue(len(cv) ==778,"\n\n----------------------------Returned Number Of Records Don't Match")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))

class test_Locations(unittest.TestCase):
    
    def setUp(self):
        try:
            self.assertTrue((os.path.isfile('conf.cfg')),"\n\n ----------------------------Configuration File 'conf.cfg' Does Not Excist ,,Will write Defaults,Try Test Again'")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))


    def test_Setting_Location(self):
        try:
            
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            city= 'Abdoul'
            lat = '999999'
            lon = '888888'
            loc=Locations()
            loc.set_location(city,lat,lon)
            c=Configs()
            conf=c.get_section('user_setting')
            self.assertEqual(conf['city_name'],'Abdoul',"\n\n----------------------------Test Writing City Name Failed")
            self.assertEqual(conf['lat'],'999999',"\n\n----------------------------Test Writing City Name Failed")
            self.assertEqual(conf['lon'],'888888',"\n\n----------------------------Test Writing City Name Failed")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))
        
    def test_Detecting_Location(self):
        try:
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            city= 'Abdoul'
            lat = '999999'
            lon = '888888'
            loc=Locations()
            loc.set_location(city,lat,lon)
            dc=loc.detect_location()
            self.assertTrue(type(dc) is tuple,"----------------Test Writing City Name Failed - Returned Type Don't Match")
            self.assertEqual(len(dc),3,"----------------Test Writing City Name Failed - Returned Length Don't Match")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))
               


class test_Database(unittest.TestCase):
    
    def setUp(self):
        try:
            self.assertTrue((os.path.isfile('conf.cfg')),"\n\n ----------------------------Configuration File 'conf.cfg' Does Not Excist ,,Will write Defaults,Try Test Again'")
            self.assertTrue((os.path.isfile('data.db')),"\n\n ----------------------------File 'data.db' Does Not Excist ")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))


    def test_Running_Read_Write_Queries(self):
        try:
            test_dict=m1={'test_field': -72.94, 'lat': 41.37, 'weather':'light snow','temp': 33.8, 'pressure': 1004, 'humidity': 80, 'temp_min': 32, 'temp_max': 35.6, 'visibility': 3219}
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            db=Database('db_1')
            sel_qur=db.exec("select * from cities limit 30")
            self.assertEqual(len(sel_qur),30,"\n\n----------------------------Length of Select Query Doesn't Match Expected Results")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))





class test_ApiGateway(unittest.TestCase):
    
    def setUp(self):
        try:
            self.assertTrue((os.path.isfile('conf.cfg')),"\n\n ----------------------------Configuration File 'conf.cfg' Does Not Excist ,,Will write Defaults,Try Test Again'")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))


    def test_Calling_Online_API(self):
        try:
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            a=ApiGateway('api_1')
            self.assertIn('http',a.url,"\n\n----------------------------Bad API - URL")
            self.assertEqual(None,a.json,"\n\n----------------------------Should Be Empty , Something Went Wrong")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))
        



class test_Configs(unittest.TestCase):
    
    def setUp(self):
        try:
            self.assertTrue((os.path.isfile('conf.cfg')),"\n\n ----------------------------Configuration File 'conf.cfg' Does Not Excist ,,Will write Defaults,Try Test Again'")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))


    def test_Configuration_File(self):

        
        try:
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            self.conf=Configs()
            self.assertNotEqual(self.conf.dc,{},"\n\n----------------------------Error initializing Config Class")
            self.assertIn('user_setting',self.conf.dc.keys(),"\n\n----------------------------Invalid Config --No User Setting Section\n")
            self.assertIn('db_1',self.conf.dc.keys(),"\n\n ----------------------------Invalid Config --No Database Section")
            self.assertIn('api_1',self.conf.dc.keys(),"\n\n ----------------------------Invalid Config --No Api-1 Section")
            self.assertIn('api_2',self.conf.dc.keys(),"\n\n ----------------------------Invalid Config --No Api-2 Section")
            self.assertIn('api_3',self.conf.dc.keys(),"\n\n ----------------------------Invalid Config --No Api-3 Section")
            self.assertIn('api_4',self.conf.dc.keys(),"\n\n ----------------------------Invalid Config --No Api-4 Section")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))            
              


    def test_Reading_sections_From_Config_File(self):
        try:
            self.conf=Configs()
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            dictionary=self.conf.get_section('user_setting')
            a=list(dictionary.keys())
            self.assertEqual(['city_name','lat','lon'],a,"\n\n-----------------------------Bad 'user_setting' configuration in 'conf.cfg'")
            dictionary=self.conf.get_section('db_1')
            a=list(dictionary.keys())
            self.assertIn('database',a,"\n\n-----------------------------Bad 'Database' configuration in 'conf.cfg'")
            dictionary=self.conf.get_section('api_1')
            a=list(dictionary.keys())
            self.assertIn('url',a,"\n\n-----------------------------Bad 'Api_1' configuration in 'conf.cfg'")
            dictionary=self.conf.get_section('api_2')
            a=list(dictionary.keys())
            self.assertIn('url',a,"\n\n-----------------------------Bad 'Api_2' configuration in 'conf.cfg'")
            dictionary=self.conf.get_section('api_3')
            a=list(dictionary.keys())
            self.assertIn('url',a,"\n\n-----------------------------Bad 'Api_3' configuration in 'conf.cfg'")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))
                        
    def test_Write_Config_To_File(self):
        try:
            self.co=Configs()
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            self.co.write('test','key','hello world')
            c=self.co.get_all()
            self.assertEqual('hello world',c['test']['key'],"\n\n-----------------------------Test Writing to 'conf.cfg' Failed")
            
            
        
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))
         


class test_Main_Service(unittest.TestCase):


    def test_DB_Save_Weather_forecast(self):
        try:
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            ms=Main_Service()
            ms.db.exec('delete from weatherforecast_dict')
            dic={'coord': {'lon': -71.47, 'lat': 42.77}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'base': 'stations', 'main': {'temp': 37.38, 'pressure': 1017, 'humidity': 64, 'temp_min': 35.6, 'temp_max': 39.2}, 'visibility': 16093, 'wind': {'speed': 3.27, 'deg': 227.505}, 'clouds': {'all': 40}, 'dt': 1522241760, 'sys': {'type': 1, 'id': 1951, 'message': 0.0055, 'country': 'US', 'sunrise': 1522233246, 'sunset': 1522278484}, 'id': 5090046, 'name': 'Nashua', 'cod': 200}
            st=ms.db.write(dic,'weatherforecast_dict')
            t=ms.db.exec('select f0 from weatherforecast_dict')
            self.assertTrue(len(t)==26,"---------------------------Returned Number of Written Records Don't Match")
            self.assertTrue(st==None,"---------------------------Returned Write Status Don't Match")
            ms.db.exec('delete from weatherforecast_dict')
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))



    def test_DB_Save_Weather_Now(self):
        try:
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            #write(self,dic,tab)
            ms=Main_Service()
            ms.db.exec('delete from weathernow_dict')
            dic={'coord': {'lon': -71.47, 'lat': 42.77}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'base': 'stations', 'main': {'temp': 37.38, 'pressure': 1017, 'humidity': 64, 'temp_min': 35.6, 'temp_max': 39.2}, 'visibility': 16093, 'wind': {'speed': 3.27, 'deg': 227.505}, 'clouds': {'all': 40}, 'dt': 1522241760, 'sys': {'type': 1, 'id': 1951, 'message': 0.0055, 'country': 'US', 'sunrise': 1522233246, 'sunset': 1522278484}, 'id': 5090046, 'name': 'Nashua', 'cod': 200}
            st=ms.db.write(dic,'weathernow_dict')
            t=ms.db.exec('select f0 from weathernow_dict')
            self.assertTrue(len(t)==26,"---------------------------Returned Number of Written Records Don't Match")
            self.assertTrue(st==None,"---------------------------Returned Write Status Don't Match")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))


    def test_Check_Address_Information(self):
        try:
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            ms=Main_Service()
            result=ms.loc.search_nominatim('nashua,nh')
            self.assertTrue(type(result) is list,"---------------------------Returned Value Type  Don't Match")
            self.assertTrue(len(result) >0,"---------------------------Returned Value Length  Don't Match")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))

    def test_Auto_Detect_Location(self):
        try:
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            ms=Main_Service()
            result=ms.loc.detect_location()
            self.assertTrue(type(result) is tuple,"---------------------------Returned Value Type  Don't Match")
            self.assertTrue(len(result) ==3,"---------------------------Returned Value Length  Don't Match")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))
      

    def test_Set_Default_Location(self):
        try:
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            ms=Main_Service()
            #('Nashua','42.7653662','-71.467566'
            ms.loc.set_location('Nashua','42.7653662','-71.467566')
            ms.__init__()
            self.assertTrue(ms.city=='Nashua',"---------------------------Setting City Name Failed")
            self.assertTrue(ms.lat=='42.7653662',"---------------------------Setting Latitude Failed")
            self.assertTrue(ms.lon=='-71.467566',"---------------------------Setting Longitude Failed")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))

    def test_Show_Weather_Now(self):
        try:
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            ms=Main_Service()
            result=ms.w.get_weather_now()
            self.assertTrue(type(result) is dict,"---------------------------Returned Value Type  Don't Match")
            self.assertTrue(len(result)>0,"---------------------------Returned Value Length  Don't Match")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))

    def test_Show_Weather_Forecast(self):
        try:
            print ("Testing Method--------[{0}]".format( self.id().split('.')[-1]))
            ms=Main_Service()
            result=ms.w.get_weather_forecast()
            self.assertTrue(type(result) is dict,"---------------------------Returned Value Type  Don't Match")
            self.assertTrue(len(result)>0,"---------------------------Returned Value Length  Don't Match")
        except Exception as e:
            print ("Error---------[{0}]--------IN Method----------[{1}]".format( e,self.id().split('.')[-1]))


      
       
if __name__ == '__main__':
    unittest.main()


