from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, curdoc
from datetime import datetime
from bokeh.io import export_png
import random

source = ColumnDataSource(dict(time = [datetime.now()], value = [random.randint(5, 10)]))
plot = figure(plot_width = 1200, x_axis_type = 'datetime', tools = 'pan,box_select,crosshair,reset,save,wheel_zoom')
plot.line(x = 'time', y = 'value', line_color = 'black', source = source)

counter = 0
def update():
    global counter
    new_source_data = dict(time = [datetime.now()], value = [random.randint(5, 10)])
    source.stream(new_source_data)
    counter = counter + 1
    export_png(plot, filename = "plot_" + str(counter) + ".png")

curdoc().add_root(plot)
curdoc().add_periodic_callback(update, 1000)