import plotly 
plotly.tools.set_credentials_file(username='mualchi', api_key='T1jnmoW4VMRH6O2kO1JV')

import plotly.plotly as py
import plotly.graph_objs as go

stream_id = 'dadmp7xv9p'
stream_1 = dict(token=stream_id, maxpoints=60)

trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1
)

data = go.Data([trace1])

layout = go.Layout(title='Time Series')
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='python-streaming')

s = py.Stream(stream_id)
s.open()

import datetime
import time
import random

time.sleep(5)

while True:

    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y = random.randrange(100)

    s.write(dict(x=x, y=y))

    time.sleep(1)  

s.close()
