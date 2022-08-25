from django.core.mail import send_mail
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404, redirect,reverse
from django.http import HttpResponse, JsonResponse


from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView

from .models import Lead, User
from .forms import LeadForm,CustomUserForm


def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads/login/')
    else:
        form = CustomUserForm()
    return render(request, 'registration/register.html', {'form': form})


# class CustomLoginView(LoginView):
#     form_class = UserForm
#     authentication_form = None
#     template_name = "registration/login.html"
#     # redirect_authenticated_user = False



# CRUD+L -> Class Based Views

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all() # context['object_list']
    context_object_name = "leads"

class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all() # context['object_list']
    context_object_name = "lead"

class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:index")

    def form_valid(self, form):
        # TODO send email
        html_message = """
            <div style="display:flex; flex-direction:column; background: #f4f4f4;padding: 10px;">
                <h1>Testing the HTML template</h1>
                <p>I am simply testing how it will turn out</p>
            </div>
        """
        send_mail(
            subject="A lead has been created",
            message="Go to the site to check",
            from_email="test@test.com",
            recipient_list=['sammyjayden27@gmail.com'],
            html_message=html_message
        )
        return super(LeadCreateView,self).form_valid(form)

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:index")

# class LeadDeleteView(DeleteView):
#     template_name = "leads/lead_delete.html"
#     queryset = Lead.objects.all()

#     def get_success_url(self):
#         return reverse("leads:index")

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }

    return render(request, 'leads/lead_list.html', context)


def lead_detail(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    # lead = Lead.objects.get(id=pk)
    context = {"lead": lead}

    return render(request, 'leads/lead_detail.html', context)


def lead_create(request):
    form = LeadForm()

    if request.method == 'POST':
        print(request.POST)
        form = LeadForm(request.POST,request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('/leads/')

    context = {'form': form}
    return render(request, 'leads/lead_create.html', context) 


def lead_update(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    context = {}
    if lead:
        context['lead'] = lead

    form = LeadForm(instance=lead)
    context['form'] = form

    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead, files=request.FILES)
        if form.is_valid():
            lead.save()
            return redirect('/leads/')
    
    return render(request, 'leads/lead_update.html', context) 


@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    if lead:
        lead.delete()
    return redirect('/leads/')
