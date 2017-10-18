import plotly 
plotly.tools.set_credentials_file(username='mualchi', api_key='mwUGNdNXuR8B7j4IMHs7')

import plotly.plotly as py
import plotly.graph_objs as go

stream_id = 'dadmp7xv9p'
stream_1 = dict(token=stream_id, maxpoints=181)

trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines',
    stream=stream_1
)

data = go.Data([trace1])

layout = go.Layout(title='Heart')
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='python-streaming')

s = py.Stream(stream_id)
s.open()

import datetime
import time
import random
import math as m

time.sleep(5)

for i in range(0, 181):
    t = m.radians(i*2)
    x = 16*m.sin(t)**3
    y = 13*m.cos(t) - 5*m.cos(2*t) - 2*m.cos(3*t) - m.cos(4*t)
    s.write(dict(x=x, y=y))
    time.sleep(0.1)  

s.close()
