from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse

from .models import Lead, Agent
from .forms import LeadForm

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
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads/')

    context = {'form': form}
    return render(request, 'leads/lead_create.html', context) 

def lead_delete(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    if lead:
        lead.delete()
    return redirect('/leads/')