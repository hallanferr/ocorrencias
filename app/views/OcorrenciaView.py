from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.forms.OcorrenciaForm import OcorrenciaForm
from app.forms.EnderecoForm import EnderecoForm
#from app.forms.ProtecForm import ProtecForm


@login_required
def new_view(request):
    return render(request, template_name='registros/new.html', status=200)

@login_required(login_url='login')
def create_ocorrencia(request):
    form = OcorrenciaForm()
    form2 = EnderecoForm()
    if request.method=='POST':
        form = OcorrenciaForm(request.POST)
        form2 = EnderecoForm(request.POST)
        if form.is_valid() and form2.is_valid():
            
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            f2 = form2.save(commit=False)
            f2.ocorrencia = f
            f2.save()
            context = {
                'f': form,
                'f2': form2
            }
            return redirect('home_view')
    else:
        context= {'form':form, 'form2': form2}    
        return render(request, template_name = 'registros/new.html', context = context)
