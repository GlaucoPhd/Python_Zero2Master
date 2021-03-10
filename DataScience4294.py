from bokeh.plotting import figure,show
from bokeh.models import HoverTool

TOOLTIPS = HoverTool(tooltips=[
    ("index", "$index"),
    ("(Wage,Value)", "($Wage, $Value)"),
    ("Name", "@Name")]
)

p = figure(title="Soccer 2019", x_axis_label='Wage', y_axis_label='Value', plot_width=800, plot_height=350, tool[TOOLTIPS])
p.circle('Wage', 'Value', size=10, source=df1)
show(p)