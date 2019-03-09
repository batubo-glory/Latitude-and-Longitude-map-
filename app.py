import folium

lat = input("Please enter latitude: ")
long = input("Please enter longitude: ")
map = folium.Map(location=[float(long), float(lat)])
map.save("map1.html")

