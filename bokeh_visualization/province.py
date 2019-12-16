from bokeh.io import curdoc
from bokeh.models.widgets import Tabs,Select
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Panel,HoverTool,Range,Legend
from bokeh.transform import dodge
from bokeh.layouts import column, row, WidgetBox

def province_plot(data):
	
	''' given data source, plots various graph '''
	
	def make_data_source(province_name):
		
		''' Given data source and specific provinice name, makes and return column data source '''
		
		data_province = data[data.Province==province_name]
		new_source = ColumnDataSource(data=data_province)
		districts =  data_province['District'].tolist()
		y_max = max(data_province[['Percentage of active female accounts','Percentage of active male accounts' ]].max().values)

		return  new_source, districts, y_max+5
		
	
	def plot_active_accounts(source, districts, y_max):

		# https://stackoverflow.com/questions/50937462/add-hover-to-plot-with-multiple-vertical-bars-bokeh 
		p = figure(x_range=districts, y_range=(0, y_max), 
		   plot_height=250, title="Percentage of active accounts",
		   tools='save, box_zoom, wheel_zoom,reset', tooltips='$name:@$name')
		
		m=p.vbar(x=dodge('District', -0.25, range=p.x_range), top='Percentage of active male accounts', width=0.2, source=source,
		 color="#718dbf", name = 'Total number of active male accounts')

		f=p.vbar(x=dodge('District',  0.0,  range=p.x_range), top='Percentage of active female accounts', width=0.2, source=source,
		color="#e84d60", name = 'Total number of active female accounts')

		#p.x_range.range_padding = 0.1
		p.xgrid.grid_line_color = None
		#p.legend.location = "top_right"
		p.xaxis.major_label_orientation = 1.2
		#p.legend.orientation = "vertical"
		#

		legend = Legend(items=[('Male', [m]), ('Female',[f])], location=(0, 30))
		legend.click_policy="hide"
		p.add_layout(legend, 'right')
		
		return p
		 
		
	def plot_literacy_rate(source, districts):

		lit_rate = figure(x_range=districts, y_range=(0, 100), 
		   					plot_height=250, title="Literacy rate",
		   					tools='save, box_zoom, wheel_zoom,reset')
		
		m = lit_rate.vbar(x=dodge('District', -0.25, range=lit_rate.x_range), top='Literacy_Rate_Male', width=0.2, source=source,
		 		color="#718dbf")

		f = lit_rate.vbar(x=dodge('District',  0.0,  range=lit_rate.x_range), top='Literacy_Rate_Female', width=0.2, source=source,
		   		color="#e84d60")

		
		#p.x_range.range_padding = 0.1
		lit_rate.xgrid.grid_line_color = None
		lit_rate.legend.location = "top_left"
		lit_rate.xaxis.major_label_orientation = 1.2
		lit_rate.legend.orientation = "horizontal"

		legend = Legend(items=[('Male', [m]), ('Female',[f])], location=(0, 30))
		legend.click_policy="hide"
		lit_rate.add_layout(legend, 'right')
		return lit_rate 
		
	def update_data_source(attr, old, new):
		
		selected_province = province_select.value
		new_source, districts, y_max  = make_data_source(selected_province)
		source.data.update(new_source.data)
		#p.x_range = districts
		p.x_range.factors = (districts)
		p.y_range.end = y_max

		lit_rate.x_range.factors=(districts)
		
		
	
	#### make selection widget to select province for interactivity 
	provinces = list(set(data.Province))
	province_select = Select(title = 'Provinces', value = 'Gandaki', options = provinces)
	controls = WidgetBox(province_select)
	
	## update data select on click 
	province_select.on_change('value', update_data_source)
	
	# initial values from select widget 
	first_province = province_select.value
	
	source, districts, y_max = make_data_source(first_province)
	p = plot_active_accounts(source, districts, y_max)
	lit_rate = plot_literacy_rate(source, districts)
	layout = column(controls,p,lit_rate)
	tab = Panel(child=layout, title="Provinces")
	
	return  tab