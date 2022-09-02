from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, get_object_or_404, redirect

from leads.models import Agent
from .forms import AgentModelForm
from .mixins import CustomLoginRequiredMixin

class AgentListView(CustomLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        print(self.request.user.user_type)
        return Agent.objects.filter(organisation=organisation)


class AgentCreateView(CustomLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:index")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
    
        return super(AgentCreateView,self).form_valid(form)


class AgentDetailView(CustomLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


# class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
#     template_name = "agents/agent_update.html"
#     queryset = Agent.objects.all()
#     form_class = AgentModelForm
#     context_object_name = "agent"

#     def get_success_url(self):
#         return reverse("agents:index")


@login_required
def agent_delete(request, pk):
    agent = get_object_or_404(Agent, id=pk)
    if agent:
        agent.delete()
    return redirect(reverse('agents:index'))