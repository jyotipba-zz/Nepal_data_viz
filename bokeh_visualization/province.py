from bokeh.io import curdoc
from bokeh.models.widgets import Tabs,Select
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Panel,HoverTool
from bokeh.transform import dodge
from bokeh.layouts import column, row, WidgetBox

def province_plot(data):
	
	''' given data source, plots various graph '''
	
	def make_data_source(province_name):
		
		''' Given data source and specific provinice name, makes and return column data source '''
		
		data_province = data[data.Province==province_name]
		new_source = ColumnDataSource(data=data_province)
		districts =  data_province['District'].tolist()

		return  new_source, districts
		
	
	def plot_active_accounts(source, districts):

		p = figure(x_range=districts, y_range=(0, 100), 
		   plot_height=250, title="Percentage of active accounts",
		   toolbar_location=None,tooltips=[("Population", "@FCHV Distict wise")])
		
		p.vbar(x=dodge('District', -0.25, range=p.x_range), top='Percentage of active male accounts', width=0.2, source=source,
		legend_label="Male", color="#718dbf")

		p.vbar(x=dodge('District',  0.0,  range=p.x_range), top='Percentage of active female accounts', width=0.2, source=source,
		legend_label="Female",color="#e84d60")

		# add hover tool
		 
		hover = HoverTool(tooltips=[('# of active male accounts', '@name'), 
					('# of active female accounts', '@name')],
					mode='vline'
					)
		
		
		#p.x_range.range_padding = 0.1
		p.xgrid.grid_line_color = None
		p.legend.location = "top_left"
		p.xaxis.major_label_orientation = 1.2
		p.legend.orientation = "horizontal"
		p.add_tools(hover)
		return p 
		
	def plot_literacy_rate(source, districts):

		lit_rate = figure(x_range=districts, y_range=(0, 100), 
		   plot_height=250, title="Literacy rate",
		   toolbar_location=None)
		
		lit_rate.vbar(x=dodge('District', -0.25, range=lit_rate.x_range), top='Literacy_Rate_Male', width=0.2, source=source,
		legend_label="Male", color="#718dbf")

		lit_rate.vbar(x=dodge('District',  0.0,  range=lit_rate.x_range), top='Literacy_Rate_Female', width=0.2, source=source,
		legend_label="Female",color="#e84d60")

		
		#p.x_range.range_padding = 0.1
		lit_rate.xgrid.grid_line_color = None
		lit_rate.legend.location = "top_left"
		lit_rate.xaxis.major_label_orientation = 1.2
		lit_rate.legend.orientation = "horizontal"
		return lit_rate 
		
	def update_data_source(attr, old, new):
		
		selected_province = province_select.value
		new_source, districts  = make_data_source(selected_province)
		source.data.update(new_source.data)
		#p.x_range = districts
		p.x_range.factors=(districts)
		lit_rate.x_range.factors=(districts)
		
		
	
	#### make selection widget to select province for interactivity 
	provinces = list(set(data.Province))
	province_select = Select(title = 'Provinces', value = 'Gandaki', options = provinces)
	controls = WidgetBox(province_select)
	
	## update data select on click 
	province_select.on_change('value', update_data_source)
	
	# initial values from select widget 
	first_province = province_select.value
	
	source, districts = make_data_source(first_province)
	p = plot_active_accounts(source, districts)
	lit_rate = plot_literacy_rate(source, districts)
	layout = column(controls,p,lit_rate)
	tab = Panel(child=layout, title="Provinces")
	
	return  tab