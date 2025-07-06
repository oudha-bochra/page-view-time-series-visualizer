from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Run each function and save the returned figure
line_fig = draw_line_plot()
bar_fig = draw_bar_plot()
box_fig = draw_box_plot()

line_fig.savefig('../output/line_plot.png')
bar_fig.savefig('../output/bar_plot.png')
box_fig.savefig('../output/box_plot.png')
