import numpy as np
import pandas as pd 
from scipy.spatial import ConvexHull
import plotly.graph_objects as go

# Sample sales data
np.random.seed(42)
region = ['East', 'West', 'North', 'South'] * 5  
sales = np.random.gamma(15, 5, 20)  
profit = np.random.normal(5, 2, 20) 

df = pd.DataFrame({'region': region, 
                   'sales': sales,  
                   'profit': profit})
                   
# Create plot                   
fig = go.Figure(data=[
    go.Scatter3d(
        x=df['region'], y=df['sales'], z=df['profit'],
        mode='markers',
        marker=dict(size=10, color=df['sales'],  
                    colorscale='bluered', opacity=0.8) 
    )
    
])

fig.update_layout(
    scene = dict(
        xaxis = dict(title='Region'), 
        yaxis = dict(title='Sales'),
        zaxis = dict(title='Profit'),),
    width=800,
    title='Regional Sales vs Profit Volcano Plot'
)

fig.show()