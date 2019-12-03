from bokeh.plotting import figure
from bokeh.models import Panel , ColumnDataSource
from bokeh.models.widgets import DataTable, TableColumn
import pandas as pd
def show_summary_stat(data):

    '''given data, this function shows the summary statistics of Nepal'''
    summary = data.describe()
    
    columns = [TableColumn(field=col, title=col) for col in summary.columns ]
    source = ColumnDataSource(data=summary)
    data_table = DataTable(source=source, columns=columns, width=1000, height=800,
    header_row=True, fit_columns=True,editable=False,scroll_to_selection=True)

    tab = Panel(child=data_table, title="Summary statistics")
    return tab

    #   show(data_table)




    #p2 = figure(plot_width=300, plot_height=300)
   # p2.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=3, color="navy", alpha=0.5)
    
