from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView

class BookListView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "books_list.html"
    permission_required = "books.development"
    login_url = '/accounts/login/'

# Create your views here.
