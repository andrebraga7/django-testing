from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin


class Home(View):

    def get(self, request):
        return render(request, 'app/home.html')


class ManagerDashboard(PermissionRequiredMixin, View):
    permission_required = 'job.is_manager'

    def handle_no_permission(self):
        return redirect('home')

    def get(self, request):
        return render(request, 'app/manager_dashboard.html')
