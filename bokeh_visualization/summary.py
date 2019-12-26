from bokeh.plotting import figure
from bokeh.models import Panel , ColumnDataSource
from bokeh.models.widgets import DataTable, TableColumn
import pandas as pd
from bokeh.layouts import column, row, WidgetBox

def show_summary_stat(data):

	'''given data, this function shows the summary statistics of Nepal'''

	df = pd.DataFrame( data.describe())
	df.drop(['S.N.'], axis = 1, inplace= True)
	df.index = df.index.set_names(['stats'])
	df.reset_index(level=0, inplace=True)
	cols = list(df.columns)
	columns = [TableColumn(field=cols[i], title=str(i+1)) for i in range(len(cols)) ]
	source = ColumnDataSource(data=df.iloc[1:,:])
	data_table = DataTable(source=source, columns=columns, width=1000, height=800,
								header_row=True, fit_columns=True,editable=False,scroll_to_selection=True
						   )
	""" dd = pd.DataFrame(cols)
	dd = dd.T
	dd.columns = dd.columns.map(str)
	columns_one = [TableColumn(field=str(i), title=str(i+1)) for i in range(len(cols)) ]
	source_one = ColumnDataSource(data=dd)
	lookup_table = DataTable(source=source_one, columns=columns_one, width=1000, height=800,
							header_row=True, fit_columns=True,editable=False,scroll_to_selection=True
						   )
	layout = column( lookup_table, data_table)
	tab = Panel(child=layout,title= 'Summary statistics') """
	tab = Panel(child=data_table, title='Summary statistics')
	return tab
	
	
	

	



