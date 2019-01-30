from django.shortcuts import render, redirect
from .models import Candidate, Position, Vote
from .forms import CandidateModelForm, PositionModelForm

# Create your views here.
def index(request):
    context = {}
    candidates = Candidate.objects.all().order_by('position')
    context['candidates'] = candidates
    return render(request, 'index.html', context)

def candidate_detail(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)
    context['candidate'] = candidate
    return render(request, 'detail.html', context)

def candidate_create(request):
    context = {}
    if request.method == 'POST':
        form = CandidateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')
        else:
            context['form'] = form
    else:
        form = CandidateModelForm()
        context['form'] = form
    return render(request, 'create.html', context)

def candidate_update(request, candidate_id):
    context = {}
    candidate = Candidate.objects.get(id=candidate_id)
    if request.method == 'POST':
        form = CandidateModelForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('votes:detail', form.instance.id)
        else:
            context['form'] = form
    else:
        form = CandidateModelForm(instance=candidate)
        context['form'] = form
    return render(request, 'update.html', context)

def position_create(request):
    context = {}
    if request.method == 'POST':
        form = PositionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')
        else:
            context['form'] = form
    else:
        form = PositionModelForm()
        context['form'] = form
    return render(request, 'pos_create.html', context)

def vote(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    vote = Vote(candidate=candidate)
    vote.save()
    return redirect('votes:index')
