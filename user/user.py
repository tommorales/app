__author__ = 'tmorales'


from src.controller import Controller

city = "Madrid"
idStation = "80678"

o = Controller()

o.current(city)
print( "*"*40 )

o.forecast_5_day(city)
print( "Plotted ..... ")
print( "*"*40 )

o.weather_stations(id=idStation)
print( "*"*40 )


# Estaciones que esta dentro de un rectangulo
rectangle=dict(bbox=[8.87,49.07,65.21,61.26, 6], cnt=200)
o.weather_stations(rectangularZone=rectangle)
print( "*"*40 )

# Estaciones que esta dentro de un circulo
circle=dict(lat=55, lon=37, cnt=30)
o.weather_stations(geoPoint=circle)
print( "*"*40 )