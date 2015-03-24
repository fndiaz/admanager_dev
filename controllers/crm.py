# -*- coding: utf-8 -*-

#########################################################################
## Integração CRM
#########################################################################
import os, commands

def envia_parametros():
	email='agente01@savol.com.br'
	senha='1123456'

	return response.render("listas/envia_parametros.html", 
									email=email, senha=senha)


def login_crm():
	login={}
	if request.env.request_method != "POST":
		log_actions("error_login", "method post failed")
		return response.json({"error": "method post failed"})
	res = valida_login(request.vars)
	if res[0] is False:
		log_actions("error_login", res[1])
		return response.json({'error': res[1]})
	else:
		print gera_apikey()
		login['email']='agente01@savol.com.br'
		login['name']='agent01'
		login['id']=1
		login['api_key']='wmt*paMQNNMEZzq4mvqMS$kgzJBXnkKX99bxF'#gera_apikey()

		log_actions("login_ok", login['name'])
		return response.json(login)

def disca_crm():
	disca={}
	d=request.vars
	if request.vars.api_key != 'wmt*paMQNNMEZzq4mvqMS$kgzJBXnkKX99bxF':
		log_actions("disca_error", "api_key invalido")
		return response.json({"error": "api_key invalido"})

	data=datetime.now().strftime("%Y%m%d")
	hora=datetime.now().strftime("%H%M%S")
	caminho='%s/CRM-%s-%s-%s' %(data, d.agent, d.phone, hora)
	if escreve_outgoing(request.vars, caminho) is True:
		disca['status']=0
		disca['callid']=caminho

		log_actions("disca_ok", "%s-%s %s" %(d.agent, d.phone, d.ts))
		return response.json(disca)
	else:
		log_actions("disca_error", "default")
		return response.json({'error': 'default'})


def escreve_outgoing(dado, caminho):
	#date = datetime.fromtimestamp(1426779840)
	#print date.strftime("%Y-%m-%d %H:%M:%S %z")
	print dado.ts
	if dado.ts == '0':
		f = open('/tmp/000.cal','w')
		f.write('Channel: Local/%s@crm\n' %(dado.agent))
		f.write('Context: crm\n')
		f.write('Extension: %s\n' %(dado.phone))
		f.write('Callerid: CRM\nMaxRetries: 1\nRetryTime: 30\nWaitTime: 60\n')
		f.write('Set:ts=%s\n' %(dado.ts))
		f.write('Set:callid=%s\n' %caminho)
		f.write('Set:id_empresa=1\n')
		f.write('Set:destino=%s\n' %(dado.phone))
		f.close()
		commands.getoutput("chmod 777 /tmp/000.cal")
		commands.getoutput("cp /tmp/000.cal /var/spool/asterisk/outgoing/")
		return True


def valida_login(dado):
	print dado
	if dado.email != 'agente01@savol.com.br':
		return False, 'email invalido'
	if dado.senha != '1123456':
		obs='senha incorreta'
		return False, 'senha incorreta'
	return True, 'login ok'

def log_actions(status, desc):
	logger.debug("crm-action: %s - %s" %(status, desc))