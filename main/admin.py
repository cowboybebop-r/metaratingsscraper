from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect

from .models import Feedback
from .tasks import crawl


@staff_member_required
def export(self, request):
    crawl.apply_async()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    change_list_template = 'change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(f'parse_feedback/', self.parse_feedback),
        ]
        return my_urls + urls

    def parse_feedback(self, request):
        crawl.apply_async()
        self.message_user(request, f"Данные спаршены")
        return HttpResponseRedirect("../")
