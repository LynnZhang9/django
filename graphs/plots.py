from plotly.offline import plot
#import plotly.graph_objs as go 
import plotly.graph_objects as go
import pandas as pd 
from datetime import datetime
import requests
import numpy as np
import os

import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash

def get_ground_truth():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_file = os.path.join(current_dir,'data', 'summary_final_result.csv')
    g8_result_final = pd.read_csv(data_file)

    fig = go.Figure(data=go.Scatter(x=g8_result_final["name"],
                                    y=g8_result_final["ground_truth"],
                                    mode='markers',
                                    marker_color=g8_result_final["ground_truth"],
                                    text=g8_result_final["name"])) # hover text goes here(movie_title)

    fig.update_layout(title='Groundtruth value of testset')
    #fig.show()
    plot_div = plot(fig, output_type='div',filename='Groundtruth value of testset')
    
    return plot_div    

#def get_dash_table():


def get_radar_chart():
    categories=['Spearman coefficient for meta prediction','Spearman coefficient for video prediction', 'RMSE performance for meta prediction', 'Performance of Percentage of error for meta prediction']

    max_Median_meta = 5
    max_rmse_meta = 40000000

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[0.6582904769874289*10, 0.16653001679379817*10, (1-28888342.58686307/max_rmse_meta)*10, (1-4.2876993170270365/max_Median_meta)*10],
        theta=categories,
        fill='toself',
        name='Group 1'
    ))
    fig.add_trace(go.Scatterpolar(
        #r=[4, 3, 2.5, 1],
        r=[0.8723381396803299*10, 0.2922855963494693*10, (1-13121368.585826622/max_rmse_meta)*10, (1-3.36926003654089/max_Median_meta)*10],
        theta=categories,
        fill='toself',
        name='Group 2'
    ))
    fig.add_trace(go.Scatterpolar(
        #r=[4, 3, 2.5, 1],
        r=[0.7329164181320348*10, 0.07285007218008188*10, (1-26752050.14513523/max_rmse_meta)*10, (1-4.0359255440653135/max_Median_meta)*10],
        theta=categories,
        fill='toself',
        name='Group 3'
    ))
    fig.add_trace(go.Scatterpolar(
        #r=[4, 3, 2.5, 1],
        r=[0.8556864252958706*10, 0.03774428547308085*10, (1-33061458.81144035/max_rmse_meta)*10, (1-4.235314260605321/max_Median_meta)*10],
        theta=categories,
        fill='toself',
        name='Group 4'
    ))
    fig.add_trace(go.Scatterpolar(
        #r=[4, 3, 2.5, 1],
        r=[0.8500682780122241*10, 0.4424006649665537*10, (1-37707867.70159658/max_rmse_meta)*10, (1-4.338897582826931/max_Median_meta)*10],
        theta=categories,
        fill='toself',
        name='Group 5'
    ))
    fig.add_trace(go.Scatterpolar(
        #r=[4, 3, 2.5, 1],
        r=[0.8560044192862486*10, 0.23361959951841244*10, (1-30443149.229962822/max_rmse_meta)*10, (1-3.8593549834327208/max_Median_meta)*10],
        theta=categories,
        fill='toself',
        name='Group 6'
    ))
    fig.add_trace(go.Scatterpolar(
        #r=[4, 3, 2.5, 1],
        r=[0.3412739489635925*10, 0.4051980915221735*10, (1-37997717.08891821/max_rmse_meta)*10, (1-4.61512051684126/max_Median_meta)*10],
        theta=categories,
        fill='toself',
        name='Group 7'
    ))
    fig.add_trace(go.Scatterpolar(
        #r=[4, 3, 2.5, 1],
        r=[0.19247275955465332*10, 0.10569914787024105*10, (1-38546594.435367346/max_rmse_meta)*10, (1-4.605151691424046/max_Median_meta)*10],
        theta=categories,
        fill='toself',
        name='Group 8'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 10]
        )),
    showlegend=True
    )

    #fig.show()

    plot_div = plot(fig, output_type='div',filename='Performance of all Groups')
    
    return plot_div


def get_log_residual_plot():
    #meta_pre = ['meta_pre_g1', 'meta_pre_g2', 'meta_pre_g3', 'meta_pre_g4', 'meta_pre_g5', 'meta_pre_g6', 'meta_pre_g7', 'meta_pre_g8']
    #video_pre = ['video_pre_g1', 'video_pre_g2', 'video_pre_g3', 'video_pre_g4', 'video_pre_g5', 'video_pre_g6', 'video_pre_g7', 'video_pre_g8']
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_file = os.path.join(current_dir,'data', 'summary_final_result.csv')
    #csv = np.genfromtxt(data_file, delimiter=None,  comments='#')
    g8_result_final = pd.read_csv(data_file)

    meta_res_log = ['meta_res_log_g1', 'meta_res_log_g2', 'meta_res_log_g3', 'meta_res_log_g4', 'meta_res_log_g5', 'meta_res_log_g6', 'meta_res_log_g7', 'meta_res_log_g8']
    video_res_log = ['video_res_log_g1', 'video_res_log_g2', 'video_log_res_g3', 'video_res_log_g4', 'video_res_log_g5', 'video_res_log_g6', 'video_res_log_g7', 'video_res_log_g8']
    #g8_result_final = pd.read_csv('summary_final_result.csv')
    
    N = 8
    c = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]
    d = ['hsl('+str(h)+',30%'+',30%)' for h in np.linspace(0, 360, N)]    
    group = ['Group1', 'Group2', 'Group3', 'Group4',
         'Group5', 'Group6', 'Group7', 'Group8']
    
    fig = go.Figure()
    for i in range(int(N)):
        fig.add_trace(go.Box(
            x=g8_result_final[meta_res_log[i]],
            y=[group[i]]*len(g8_result_final[meta_res_log[i]]),
            name='Logarithm of meta residuals of Group ''{}'.format(i+1),
            marker_color=c[i]
        ))
        fig.add_trace(go.Box(
            x=g8_result_final[video_res_log[i]],
            y=[group[i]]*len(g8_result_final[video_res_log[i]]),
            name='Logarithm of video residuals of Group ''{}'.format(i+1),
            marker_color=d[i]
        ))   
    
    
    fig.update_layout(
        xaxis=dict(title='The absolute logarithm of residuals', zeroline=False),
        boxmode='group'
    )
    
    fig.update_traces(orientation='h') # horizontal box plots
    #fig.show() 
    plot_div = plot(fig, output_type='div',filename='Logarithm of residuals for 8 groups')
    
    return plot_div

def get_rmse():
    group=['group1', 'group2', 'group3', 'group4', 'group5', 'group6', 'group7', 'group8']


    fig = go.Figure(data=[
        go.Bar(name='meta RMSE', x=group, y=[28888342.58686307, 13121368.585826622, 26752050.14513523, 33061458.81144035, 37707867.70159658, 30443149.229962822, 37997717.08891821, 38546594.435367346]),
        go.Bar(name='video RMSE', x=group, y=[37023059.12633596, 41262144.0770966, 44429960.0950124, 46094575.98337922, 46493371.11989302, 106964726.69744653, 39497815.44164435, 44573607.99274869])
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    #fig.show()

    plot_div = plot(fig, output_type='div',filename='RMSEs for 8 Groups')
    
    return plot_div    


def get_topographical_3D_surface_plot():
    raw_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

    data = [go.Surface(z=raw_data.as_matrix())]

    layout = go.Layout(
       
        autosize=False,
        width=800,
        height=700,
        margin=dict(
            l=65,
            r=50,
            b=65,
            t=90
            )
        )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div',filename='elevations-3d-surface')

    return plot_div


def pie_chart():
    fig = {
  "data": [
    {
      "values": [16, 15, 12, 6, 5, 4, 42],
      "labels": [
        "US",
        "China",
        "European Union",
        "Russian Federation",
        "Brazil",
        "India",
        "Rest of World"
      ],
      "domain": {"column": 0},
      "name": "GHG Emissions",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },
    {
      "values": [27, 11, 25, 8, 1, 3, 25],
      "labels": [
        "US",
        "China",
        "European Union",
        "Russian Federation",
        "Brazil",
        "India",
        "Rest of World"
      ],
      "text":["CO2"],
      "textposition":"inside",
      "domain": {"column": 1},
      "name": "CO2 Emissions",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    }],
  "layout": {
        "title":"Global Emissions 1990-2011",
        "grid": {"rows": 1, "columns": 2},
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "GHG",
                "x": 0.20,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "CO2",
                "x": 0.8,
                "y": 0.5
            }
        ]
    }
}
    
    plot_div = plot(fig, output_type='div',filename='donut')
    return plot_div

current_dir_residuals = os.path.dirname(os.path.realpath(__file__))
data_file_residuals = os.path.join(current_dir_residuals,'data', 'final_result_residuals.csv')
df_residuals = pd.read_csv(data_file_residuals)
df_residuals_filter = df_residuals.drop(["meta_res_log_g1", "video_res_log_g1", "meta_res_log_g2", "video_res_log_g2", "meta_res_log_g3", "video_res_log_g3", "meta_res_log_g4", "video_res_log_g4", "meta_res_log_g5", "video_res_log_g5", "meta_res_log_g6", "video_res_log_g6", "meta_res_log_g7", "video_res_log_g7", "meta_res_log_g8", "video_res_log_g8"], axis=1)
df_residuals_filter = df_residuals_filter.loc[:, ~df_residuals_filter.columns.str.contains('^Unnamed')]


#app = dash.Dash(__name__)
app = DjangoDash('SummaryResiduals')

app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        #columns=[
        #    {"name": i, "id": i, "deletable": True, "selectable": True} for i in df_residuals.columns
        #],
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df_residuals_filter.columns
        ],
        data=df_residuals.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        #row_deletable=True,
        row_deletable=False,
        selected_columns=['name'],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
        #virtualization=True,
    ),
    
    html.Div(id='datatable-interactivity-container')
])

@app.callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    [Input('datatable-interactivity', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]

@app.callback(
    Output('datatable-interactivity-container', "children"),
    [Input('datatable-interactivity', "derived_virtual_data"),
     Input('datatable-interactivity', "derived_virtual_selected_rows")])
def update_graphs(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncracy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []
    #!!!!!df --->dff
    dff = df_residuals if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]
    
    
    return [
        dcc.Graph(
            id=column,
            figure={
                "data": [
                    {
                        "x": dff["name"],
                        "y": dff[column],
                        "type": "bar",
                        "marker": {"color": colors},
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True,
                        "title": {"text": column}
                    },
                    "height": 250,
                    "margin": {"t": 10, "l": 10, "r": 10},
                },
            },
        )
        # check if column exists - user may have deleted it
        # If `column.deletable=False`, then you don't
        # need to do this check.
        for column in ["meta_res_log_g1", "video_res_log_g1", "meta_res_log_g2", "video_res_log_g2", "meta_res_log_g3", "video_res_log_g3", "meta_res_log_g4", "video_res_log_g4", "meta_res_log_g5", "video_res_log_g5", "meta_res_log_g6", "video_res_log_g6", "meta_res_log_g7", "video_res_log_g7", "meta_res_log_g8", "video_res_log_g8"] if column in dff
    ]