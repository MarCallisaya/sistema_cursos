from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
#decorador (a esta vista solo puedes entrar SI iniciaste sesion)
@login_required 
def dasboard(request):
    if request.user.rol == 'administrador':
        return render(request,'dashboard_admin.html')
    elif request.user.rol == 'profesor':
        return render(request,'dashboard_docente.html')
    elif request.user.rol == 'estudiante':
        return render(request,'dashboard_estudiante.html')
    else:
        return redirect('login')
    
