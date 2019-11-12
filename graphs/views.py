from django.http import HttpResponse
from django.views.generic import TemplateView
from . import plots
from django.shortcuts import render

class SimpleCandlestickWithPandas(TemplateView):
    template_name = 'plot.html'
    def get_context_data(self, **kwargs):
        context = super(SimpleCandlestickWithPandas, self).get_context_data(**kwargs)
        #context['simplecandlestick'] = plots.get_simple_candlestick()
        #context['3dplot'] = plots.get_topographical_3D_surface_plot()
        #context['piechart'] = plots.pie_chart()
        context['logresiduals'] = plots.get_log_residual_plot()
        context['groundtruth'] = plots.get_ground_truth()
        context['performance'] = plots.get_radar_chart()
        context['rmse'] = plots.get_rmse()
        #context['SummaryResiduals'] = plots.SummaryResiduals()
        return context


def dash_example_1_view(request, template_name="plot.html", **kwargs):
#def dash_example_1_view(request, template_name="plot.html", **kwargs):
    'Example view that inserts content into the dash context passed to the dash application'

    context = {}

    # create some context to send over to Dash:
    dash_context = request.session.get("django_plotly_dash", dict())
    dash_context['django_to_dash_context'] = "I am Dash receiving context from Django"
    request.session['django_plotly_dash'] = dash_context

    return render(request, template_name=template_name, context=context)
    #return render(request, 'demo_six.html', {'chart' : 'dash_example_1',})
    #return render(request, 'plot.html', {'chart' : 'SummaryResiduals',})


def session_state_view(request, template_name, **kwargs):
    'Example view that exhibits the use of sessions to store state'

    session = request.session

    demo_count = session.get('django_plotly_dash', {})

    ind_use = demo_count.get('ind_use', 0)
    ind_use += 1
    demo_count['ind_use'] = ind_use

    context = {'ind_use' : ind_use}

    session['django_plotly_dash'] = demo_count

    return render(request, template_name=template_name, context=context)