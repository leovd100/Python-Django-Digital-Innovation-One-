from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Transacao

# Create your views here.
def home(requests):
	data = {
		'trasacoes':['t1','t2','t3']
	}
	#data_today = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'

	data['agora'] = datetime.now().strftime('%d/%m/%Y')

	#html = '<html><body>Data e Hora atual %s</body></html>'% agora
	return render(requests, 'contas/home.html',data)



def listagem(requests):
	data = {}
	data['transacao'] = Transacao.objects.all()
	return render(requests, 'contas/lista.html',data)