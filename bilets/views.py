from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from bilets.models import Bilets
from django.core.mail import send_mail
from bilets.forms import ProverkaForm
from django.views import View
import uuid


class IndexView(TemplateView):
    template_name = 'bilets/bilets_index.html'
    title = 'Buy bilets'


class BuyBilets(ListView):
    model = Bilets
    template_name = 'bilets/confirmation.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        new_bilet = Bilets.objects.create(user=self.request.user, invoiceId=uuid.uuid4())
        self.send_email_notification(new_bilet)
        latest_bilet = Bilets.objects.filter(user=self.request.user).last()
        return [latest_bilet]


    def send_email_notification(self, bilet):
        subject = 'Успешная покупка билета'
        message = f'Вы успешно купили билет с номером {bilet.invoiceId}. Билет был отправлен на вашу почту.'
        from_email = 'olezkayou.2@gmail.com'
        recipient_list = [bilet.user.email]
        send_mail(subject, message, from_email, recipient_list)


class ProverkaBilets(View):
    template_name = 'bilets/check_ticket.html'
    form_class = ProverkaForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'is_valid_ticket': None})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                invoice_id_vvod = form.cleaned_data['invoiceId_Vvod']
                bilet = Bilets.objects.get(invoiceId=invoice_id_vvod)
                return render(request, self.template_name, {'form': form, 'is_valid_ticket': True, 'bilet': bilet})

            except Bilets.DoesNotExist:
                return render(request, self.template_name, {'form': form, 'is_valid_ticket': False, 'bilet': None})

        return render(request, self.template_name, {'form': form, 'is_valid_ticket': None, 'bilet': None})


