import folium
def make_map():
    start_coords = (28.3948574 ,84.1240082)
    folium_map = folium.Map(location=start_coords, zoom_start=10)
    folium_map.save('myapp/templates/map.html')
    #return folium_map._repr_html_()
