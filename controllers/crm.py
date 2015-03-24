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
		login['name']='agente01'
		login['id']=1
		login['api_key']='wmt*paMQNNMEZzq4mvqMS$kgzJBXnkKX99bxF'#gera_apikey()

		log_actions("login_ok", login['name'])
		return response.json(login)

def disca_crm():
	disca={}
	d=request.vars
	if (d.api_key != 'wmt*paMQNNMEZzq4mvqMS$kgzJBXnkKX99bxF') or (d.agent != 'agente01'):
		log_actions("disca_error", "api_key invalido ou agente invalido")
		return response.json({"error": "api_key invalido ou agente invalido"})

	caminho = gera_caminho(d)
	if escreve_outgoing(d, caminho) is True:
		disca['status']=0
		disca['callid']=caminho

		log_actions("disca_ok", "%s-%s %s" %(d.agent, d.phone, d.ts))
		return response.json(disca)
	else:
		log_actions("disca_error", "default")
		return response.json({'error': 'default'})


def escreve_outgoing(dado, caminho):
	print '-----------gera outgoing--------------'
	try:
		arquivo='%s.cal' %(caminho.split('/')[1])

		f = open('/tmp/%s' %(arquivo),'w')
		f.write('Channel: Local/%s@crm\n' %(dado.agent))
		f.write('Context: crm\n')
		f.write('Extension: %s\n' %(dado.phone))
		f.write('Callerid: CRM\nMaxRetries: 1\nRetryTime: 30\nWaitTime: 60\n')
		f.write('Set:ts=%s\n' %(dado.ts))
		f.write('Set:callid=%s\n' %caminho)
		f.write('Set:id_empresa=1\n')
		f.write('Set:destino=%s\n' %(dado.phone))
		f.close()
		commands.getoutput("chmod 777 /tmp/%s" %(arquivo))
		if dado.ts != '0':
			perm=datetime.fromtimestamp(int(dado.ts)).strftime("%Y%m%d%H%M.%S")
			commands.getoutput("touch -t %s /tmp/%s" %(perm, arquivo))
		commands.getoutput("mv /tmp/%s /var/spool/asterisk/outgoing/" %(arquivo))
		log_actions("arquivo gerado", arquivo)
		return True
	except():
		return False

def gera_caminho(d):
	print '-----------gera caminho--------------'
	if d.ts == '0':
		data=datetime.now().strftime("%Y%m%d")
		hora=datetime.now().strftime("%H%M%S")
	else:
		var=datetime.fromtimestamp(int(d.ts))
		data=var.strftime("%Y%m%d")
		hora=var.strftime("%H%M%S")

	caminho ='%s/CRM-%s-%s-%s' %(data, d.agent, d.phone, hora)
	print 'caminho:%s' %(caminho)
	return caminho


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