from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ad, Category, AdResponse
from .forms import AdvertisementForm, ResponseForm
from .filters import AdFilter


class AdList(ListView):
    model = Ad
    ordering = '-date_creation'
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 10


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'
    queryset = Ad.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['responses'] = self.object.responses.all()
        return context


class AdCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('fan_site.add_ad',)
    form_class = AdvertisementForm
    model = Ad
    template_name = 'ad_create.html'

    def form_valid(self, form):
        ad = form.save(commit=False)
        if self.request.method == 'POST':
            ad.user = self.request.user
        ad.save()
        return super().form_valid(form)


class AdUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('fan_site.change_ad',)
    form_class = AdvertisementForm
    model = Ad
    template_name = 'ad_update.html'

    def has_permission(self):
        ad = self.get_object()
        return self.request.user == ad.user


class AdDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('fan_site.delete_ad',)
    model = Ad
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ad_list')

    def has_permission(self):
        ad = self.get_object()
        return self.request.user == ad.user


class AdAdResponse(CreateView):
    form_class = ResponseForm
    model = AdResponse
    template_name = 'ad_response.html'

    def form_valid(self, form):
        ad = get_object_or_404(Ad, pk=self.kwargs['pk'])
        form.instance.ad = ad
        form.instance.user = self.request.user

        ad_user_email = ad.user.email
        if ad_user_email:
            subject = 'Новый отклик'
            message = 'На ваше объявление поступил новый отклик.'
            from_email = None
            send_mail(subject, message, from_email, [ad_user_email])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ad_detail', kwargs={'pk': self.kwargs['pk']})


class AdResponsesPersonalList(ListView):
    model = AdResponse
    template_name = 'responses_list.html'
    context_object_name = 'responses'

    def post(self, request, *args, **kwargs):
        response_id = request.POST.get('response_id')
        response = get_object_or_404(AdResponse, id=response_id)
        if 'delete_response' in request.POST:
            if response.ad.user == request.user:
                response.delete()
        elif 'accept_response' in request.POST:
            if response.ad.user == request.user:
                response.accepted = True
                response.save()

                response_user_email = response.user.email
                if response_user_email:
                    subject = 'Ваш отклик был принят'
                    message = 'Ваш отклик был успешно принят автором объявления.'
                    from_email = None
                    send_mail(subject, message, from_email, [response_user_email])
        return redirect('responses_list')

    def get_queryset(self):
        queryset = AdResponse.objects.filter(ad__user_id=self.request.user.id)
        self.filterset = AdFilter(self.request.GET, queryset, request=self.request.user.id)
        if self.request.GET:
            return self.filterset.qs
        return AdResponse.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



