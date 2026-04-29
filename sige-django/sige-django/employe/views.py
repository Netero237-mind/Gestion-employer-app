from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Sum, Count
from .models import Employe
from .forms import EmployeForm


def liste_employes(request):
    employes = Employe.objects.all()
    stats = {
        'total': employes.count(),
        'masse_salariale': employes.aggregate(total=Sum('salaire'))['total'] or 0,
        'postes': employes.values('poste').annotate(count=Count('id')).order_by('-count'),
    }
    return render(request, 'employe/liste.html', {'employes': employes, 'stats': stats})


def ajouter_employe(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Employé ajouté avec succès !')
            return redirect('liste_employes')
    else:
        form = EmployeForm()
    return render(request, 'employe/ajouter.html', {'form': form})


def modifier_employe(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            messages.success(request, '✏️ Employé modifié avec succès !')
            return redirect('liste_employes')
    else:
        form = EmployeForm(instance=employe)
    return render(request, 'employe/modifier.html', {'form': form, 'employe': employe})


def supprimer_employe(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        employe.delete()
        messages.success(request, '🗑️ Employé supprimé avec succès !')
        return redirect('liste_employes')
    return render(request, 'employe/supprimer.html', {'employe': employe})
