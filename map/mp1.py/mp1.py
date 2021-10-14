import folium
mapa = folium.Map(location=[23.416419215610652, 77.65351376010518],zoom_start=36, tiles="Stamen terrain")
mapa.save("map1.html")