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
		LogAcoes(evento='Login Erro', resposta='method post failed').geralog()
		return response.json({"error": "method post failed"})

	res = valida_login(request.vars)
	if res[0] is False:
		LogAcoes(evento='Login Erro', resposta=res[1], argumentos=request.vars).geralog()
		return response.json({'error': res[1]})
	else:
		query=(Voicemail.email == request.vars.email)
		con=db(query).select()[0]
		login['email']=con.email
		login['name']=con.pager
		login['id']=1
		login['api_key']=api_key=gera_apikey()
		db(query).update(api_key=api_key)

		LogAcoes(evento='Login OK', agent=login['name'], api_key=login['api_key'], argumentos=request.vars).geralog()
		return response.json(login)

def disca_crm():
	disca={}
	d=request.vars
	if db((Voicemail.api_key == d.api_key ) & (Voicemail.pager == d.agent)).isempty():
		LogAcoes(evento='Disca Erro', resposta='api_key invalido ou agente invalido', 
					agent=d.agent, api_key=d.api_key, argumentos=request.vars).geralog()
		return response.json({"error": "api_key invalido ou agente invalido"})

	caminho = gera_caminho(d)
	if escreve_outgoing(d, caminho) is True:
		disca['status']=0
		disca['callid']=caminho

		LogAcoes(evento='Disca Ok', resposta='ok', 
			agent=d.agent,	api_key=d.api_key, argumentos=request.vars).geralog()
		return response.json(disca)
	else:
		LogAcoes(evento='Disca Erro', resposta='default', 
			agent=d.agent, api_key=d.api_key, argumentos=request.vars).geralog()
		return response.json({'error': 'default'})


def escreve_outgoing(dado, caminho):
	print '-----------gera outgoing--------------'
	try:
		arquivo='%s.cal' %(caminho.split('/')[1])

		f = open('/tmp/%s' %(arquivo),'w')
		f.write('Channel: Local/%s@crm\n' %(dado.agent))
		f.write('Context: ramais\n')
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
		LogAcoes(evento='Arquivo gerado',
				resposta='gerado com sucesso',
				argumentos='ts:%s' %dado.ts, 
				agent=dado.agent).geralog()
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
	query=(Voicemail.email == dado.email)&\
		  (Voicemail.password == dado.senha)&\
		  (Voicemail.context == 'crm')

	print db(Voicemail.email == dado.email).select()
	if db((Voicemail.email == dado.email) & (Voicemail.context == 'crm')).isempty():
		return False, 'login inexistente'
	else:
		if db(query).isempty():
			return False, 'senha incorreta'
		else:
			return True, 'login ok'

def log_actions(status, desc):
	logger.debug("crm-action: %s - %s" %(status, desc))