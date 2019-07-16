import folium
import pandas

data = pandas.read_csv("Places.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
type = list(data["TYPE"])

def color(name):
    if name == "National-Park" :
        return 'green'
    elif name == "Monument":
        return 'red'
    elif name == "Adventure-Sport":
        return 'darkblue'
    else:
        return 'orange'

map = folium.Map(location=[20,78], zoom_start=5)

fg = folium.FeatureGroup(name="India Map")

for lt,ln,nm,ty in zip(lat,lon,name,type):
    #fg.add_child(folium.Marker(location = [lt,ln], popup=nm, icon=folium.Icon(color=color(ty))))
    fg.add_child(folium.CircleMarker(location = [lt,ln],radius=6, popup=nm,fill_color=color(ty),color='grey',fill_opacity=0.7 ))



map.add_child(fg)

map.save("Map.html")
