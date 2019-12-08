import json
import pandas as pd
import geopandas as gpd
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool, Panel
from bokeh.palettes import brewer

def choloropath_map(data):

	# Read geojson file containing Nepali districts 
	nepal_geojson = '../myapp/static/nepal-districts-new.geojson'

	gdf = gpd.read_file(nepal_geojson)

	# rename column in data to match with field in geojson
	new_data = data.rename(columns={'District':'DIST_EN'})

	# replacing the district name in dataframe such that it matches with the name in geojson data
	new_data = new_data.replace('Makwanpur', 'Makawanpur')
	new_data = new_data.replace('Kavrepalanchok', 'Kabhrepalanchok')
	new_data = new_data.replace('Dhanusa', 'Dhanusha')

	merged = gdf.merge(new_data, how='left', on='DIST_EN') # merge data and geojson

	merged_json = json.loads(merged.to_json())  #Read data to json

	#Convert to String like object
	json_data = json.dumps(merged_json)

	#Input GeoJSON source that contains features for plotting.
	geosource = GeoJSONDataSource(geojson = json_data)
	palette = brewer['OrRd'][8]
	palette = palette[::-1]
	color_mapper = LinearColorMapper(palette = palette, low = 0, high = 100)

	#Create color bar
	color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20,
	border_line_color=None,location = (0,0), orientation='horizontal')

	#Create figure object.
	p = figure(title = 'Percantage of females with active bank account', plot_height = 600, 
		   plot_width = 700, toolbar_location = None)
	p.xgrid.grid_line_color = None
	p.ygrid.grid_line_color = None

	#Add patch renderer to figure. 
	p.patches('xs','ys', source = geosource,fill_color = {'field' :'Percentage of active female accounts', 'transform' : color_mapper},
		  line_color = 'black', line_width = 0.25, fill_alpha = 1)

	# add hover tool 
	p.add_tools(HoverTool(tooltips = [ ('District','@DIST_EN'),
							  ('Female literacy rate (%)', '@Literacy_Rate_Female'),
							  ('Male literacy rate (%)', '@Literacy_Rate_Male'),
							  
							  ]))
	
	
	p.add_layout(color_bar, 'below')
	
	tab = Panel(child=p, title='Choropleth map')
	return tab