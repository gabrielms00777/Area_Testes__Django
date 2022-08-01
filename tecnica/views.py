from django.shortcuts import render, redirect
from .models import Clientes

def painel(request):
    return render(request, 'painel.html')

def os(request):
    return render(request, 'os.html')
def clientes(request):
    # Status 1 = Empresa cadastrada com sucesso
    # Status 2 = CNPJ já cadastrado
    # Status 3 = Preencha todos os campos
    if request.method == 'GET':
        status = request.GET.get('status')
        clientes = Clientes.objects.all()
        return render(request, 'clientes.html', {'clientes':clientes, 'status':status})
    else:
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        status = request.POST.get('status')

        if (len(nome.strip()) == 0) or (len(cnpj.strip()) == 0):
            return redirect('/painel/clientes/?status=3') 

        cliente = Clientes.objects.filter(cnpj=cnpj)
        if cliente:
            return redirect('/painel/clientes/?status=2')   

        cliente = Clientes(nome=nome,
                            cnpj=cnpj,
                            status=status)
        cliente.save()

        return redirect('/painel/clientes/?status=1')

def pesquisa_cliente(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'pesquisa_cliente.html', {'status': status})
    else:
        cliente = request.POST.get('cliente')

        if cliente.isdigit():
            existe = Clientes.objects.filter(cnpj=cliente)
            if existe:
                cliente = Clientes.objects.get(cnpj=cliente)
                print(cliente)
                return render(request, 'pesquisa_cliente.html', {'cliente': cliente})
            else:
                return redirect('/painel/pesquisa_cliente/?status=1')
                
        else:
            existe = Clientes.objects.filter(nome=cliente)
            if existe:
                cliente = Clientes.objects.get(nome=cliente)
                return render(request, 'pesquisa_cliente.html', {'cliente': cliente})
            else:
                return redirect('/painel/pesquisa_cliente/?status=2')


            




