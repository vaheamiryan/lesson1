from gpcharts import figure

# simple line graph, as described in the readme.
fig1 = figure()
fig1.plot([8, 7, 6, 5, 4])

# another line graph, but with two data types. Also adding title
fig2 = figure(title='Two lines', xlabel='Days', ylabel='Count', height=600, width=600)
xVals = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
yVals = [[5, 4], [8, 7], [4, 8], [10, 10], [3, 12]]
fig2.plot(xVals, yVals)
