from django.views.generic import ListView


# Create your views here.
class VisitorListView(ListView):
    model = 'visitor'
    template_name = 'VisitorList.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Visitantes'
        return contex