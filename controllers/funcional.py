# coding=UTF-8

######-TRONCOS
@auth.requires_login()  
def f_troncos():
	response.title = 'Troncos'
	response.marca=['Funcional', 'Troncos']
	editor = permissao()
	url = URL('admanager', 'funcional', 'f_troncos_form')

	troncos = db(db.f_troncos.mostrar == True).select(orderby=db.f_troncos.id)
	
	return response.render("funcional/show_troncos.html",  
					url=url, editor=editor, troncos=troncos)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_troncos_form():
	response.title = 'Troncos'
	response.marca=['Funcional', 'Troncos', 'Adiciona Tronco']
	id_tronco	= request.vars['id_tronco']
	
	if id_tronco is None:
		form 	=	SQLFORM(db.f_troncos,  
				submit_button='Adicionar')
	else:
		form 	=	SQLFORM(db.f_troncos, id_tronco, 
								submit_button='Editar')

	for input in form.elements():
		input['_class'] = 'form-control'
	form.element(_name='habilitado')['_class'] = "checkbox"
	form.element(_name='chamadas_simultaneas')['_type'] = "number"
	form.element(_name='qtde_max_minutos')['_type'] = "number"

	#form.element(_name='ciclo_conta')['_value'] = "teste"
	if form.process().accepted:
		peers_fop2()
		redirect(URL('f_troncos'))
	elif form.errors:
		response.alerta_erro="Erros no formulário"

	return response.render("funcional/form_troncos.html", form=form)

######-TRONCOS-FISICOS
@auth.requires_login()
def f_troncos_fisicos():
	response.title = 'Troncos Físicos'
	response.marca=['Funcional', 'Troncos Físicos']
	query 	=	(db.f_troncos.id == db.f_troncos_fisicos.id_tronco)
	editor 	= 	permissao()
	url = URL('admanager', 'funcional', 'f_troncos_fisicos_form')

	troncos_fisicos = db(query).select(db.f_troncos.tronco,
		db.f_troncos_fisicos.id, db.f_troncos_fisicos.dispositivo)	

	return response.render("funcional/show_troncos_fisicos.html", 
			url=url, editor=editor, troncos_fisicos=troncos_fisicos)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_troncos_fisicos_form():
	response.title = 'Troncos Físicos'
	response.marca=['Funcional', 'Troncos Físicos', 'Adiciona Tronco Físico']
	id_tronco_fisico = request.vars['id_tronco_fisico']
	
	if id_tronco_fisico is None:
		form 	=	SQLFORM(db.f_troncos_fisicos,  
				submit_button='Adicionar')
	else:
		form 	=	SQLFORM(db.f_troncos_fisicos, id_tronco_fisico, 
								submit_button='Editar')

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		peers_fop2()
		redirect(URL('f_troncos_fisicos'))

	return response.render("funcional/form_troncos_fisicos.html", 
													form=form)

######-DESTINOS
@auth.requires_login()
def f_destinos():
	response.title = 'Destinos'
	response.marca=['Funcional', 'Destinos']
	url = URL('admanager', 'funcional', 'f_destinos_form')
	editor 	= 	permissao()
	destinos 	= 	db(db.f_destinos.mostrar == True).select(orderby=db.f_destinos.id)

	return response.render("funcional/show_destinos.html", 
				url=url, editor=editor, destinos=destinos)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_destinos_form():
	response.title = 'Destinos'
	response.marca=['Funcional', 'Destinos', 'Adiciona Destino']
	id_destino	= 	request.vars['id_destino']

	if id_destino is None:
		form 	=	SQLFORM(db.f_destinos,  
				submit_button='Adicionar')
	else:
		form 	=	SQLFORM(db.f_destinos, id_destino, 
								submit_button='Editar')

	for input in form.elements():
		input['_class'] = 'form-control'
		form.element(_name='tamanho_max')['_type'] = "number"

	if form.process().accepted:
		escreve_destino()
		redirect(URL('f_destinos'))

	return response.render("funcional/form_destinos.html", form=form)

######-EMPRESA
@auth.requires_login()
def f_empresa():
	response.title = 'Empresa'
	response.marca = ['Funcional', 'Empresa']
	editor 	= 	permissao()
	url 	=	URL('admanager', 'funcional', 'f_empresa_form')
	empresa	= 	db(db.f_empresa.mostrar == True).select(orderby=db.f_empresa.id)
	if (db(Empresa.mostrar == True).count() > 1)\
	and (auth.user.email != 'root@forip.com.br'):
		editor=False

	return response.render("funcional/show_empresa.html", 
				url=url, editor=editor, empresa=empresa)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_empresa_form():
	if (db(Empresa.mostrar == True).count() > 1)\
	and (auth.user.email != 'root@forip.com.br'):
		redirect(URL('f_empresa'))

	response.title = 'Empresa'
	response.marca = ['Funcional', 'Empresa', 'Adiciona Empresa']
	id_empresa	= 	request.vars['id_empresa']
	print id_empresa
	
	if id_empresa is None:
		form 	=	SQLFORM(db.f_empresa,  
				submit_button='Adicionar')
	else:
		form 	=	SQLFORM(db.f_empresa, id_empresa, 
								submit_button='Editar')

	form.element(_name='empresa')['_class'] = "form-control"
	#form.element(_name='faixa_ramal')['_class'] = "form-control"
	if form.process().accepted:
		print request.vars
		redirect(URL('f_empresa'))

	return response.render("funcional/form_empresa.html", form=form)

######-TARIFACAO
@auth.requires_login()
def f_tarifacao():
	response.title = 'Tarifação'
	response.marca=['Funcional', 'Tarifação']
	editor 	= 	permissao()
	url 	=	URL('admanager', 'funcional', 'f_tarifacao_form')
	tarifacao 	=	db(db.f_tarifacao).select(orderby=db.f_tarifacao.id)

	if auth.user.email != 'root@forip.com.br':
		editor=False

	return response.render("funcional/show_tarifacao.html", 
				editor=editor, url=url, tarifacao=tarifacao)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_tarifacao_form():
	if auth.user.email != 'root@forip.com.br':
		redirect(URL('f_empresa'))

	response.title = 'Tarifação'
	response.marca=['Funcional', 'Tarifação', 'Adiciona Tarifação']
	id_tarifacao=	request.vars['id_tarifacao']
	
	if id_tarifacao is None:
		form 	=	SQLFORM(db.f_tarifacao,  
				submit_button='Adicionar')
	else:
		form 	=	SQLFORM(db.f_tarifacao, id_tarifacao, 
								submit_button='Editar')

	for input in form.elements():
		input['_class'] = 'form-control'
	if form.process().accepted:
		redirect(URL('f_tarifacao'))

	return response.render("funcional/form_tarifacao.html", form=form)

######-ROTAS
@auth.requires_login()
def f_rotas():
	response.title = 'Rotas'
	response.marca=['Funcional', 'Rotas']
	editor 	= 	permissao()
	url 	=	URL('admanager', 'funcional', 'f_rotas_form')
	rota = db(db.f_rotas).select()	 
	
	return response.render("funcional/show_rotas.html", 
						editor=editor, url=url, rota=rota)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_rotas_form():
	response.title = 'Rotas'
	response.marca=['Funcional', 'Rotas', 'Adiciona Rota']
	id_rota 	= 	request.vars['id_rota']

	if id_rota is None:
		form 	=	SQLFORM(db.f_rotas,  
				submit_button='Adicionar')
	else:
		form 	=	SQLFORM(db.f_rotas, id_rota, 
								submit_button='Editar')

	for input in form.elements():
		input['_class'] = 'form-control'
		form.element(_name='prioridade')['_type'] = "number"
	if form.process().accepted:
		redirect(URL('f_rotas'))

	return response.render("funcional/form_rotas.html", form=form)

######-HORARIO
@auth.requires_login()
def f_horario():
	response.title = 'Horário'
	response.marca=['Funcional', 'Horário']
	editor 	= 	permissao()
	url 	=	URL('admanager', 'funcional', 'f_horario_form')
	horario = db(db.f_horario).select()
	
	return response.render("funcional/show_horario.html", 
					editor=editor, url=url, horario=horario)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_horario_form():
	response.title = 'Horário'
	response.marca=['Funcional', 'Horário', 'Adiciona Horário']
	id_horario 	= 	request.vars['id_horario']

	if id_horario is None:
		form 	=	SQLFORM(db.f_horario)
	else:
		form 	=	SQLFORM(db.f_horario, id_horario)

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		redirect(URL('f_horario'))

	return response.render("funcional/form_horario.html", form=form)

######-BILHETES-CHAMADAS
# coding=UTF-8

@auth.requires_login()
def f_bilhetes_chamadas():
	response.title = 'Bilhetes'
	editor 	= 	permissao()
	url 	=	URL('admanager', 'funcional', 'f_bilhetes_chamadas_form')
	query 	=  	(db.f_bilhetes_chamadas.id_tronco == db.f_troncos.id)&\
				(db.f_bilhetes_chamadas.id_empresa == db.f_empresa.id)&\
				(db.f_bilhetes_chamadas.id_destino == db.f_destinos.id)
	bilhetes = db(query).select()
	print bilhetes
	
	return response.render("funcional/show_bilhetes_chamadas.html", 
					editor=editor, url=url, bilhetes=bilhetes)

######-PARAMETROS
@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_parametros_form():
	response.title = 'Parâmetros'
	response.marca=['Configs', 'Parâmetros']
	id_parametro=	request.vars['id_parametro']
	
	form 	=	SQLFORM(db.f_parametros, 1)
	
	for input in form.elements():
		input['_class'] = 'form-control'
	form.element(_name='faixa_ip_interna')['_rows'] = "4"
	form.element(_name='spy_ramal_proibe_monitora')['_rows'] = "4"
	form.element(_name='spy_ramal_espiao')['_rows'] = "4"
	form.custom.widget.tempo_chamada_externa['_placeholder'] = "em segundos"
	form.custom.widget.tempo_chamada_interna['_placeholder'] = "em segundos"
	form.custom.widget.faixa_ip_interna['_placeholder'] = "Exemplo: 192.168.1.2/255.255.255.0"
	form.custom.widget.senha_smtp['_type'] = "password"

	if form.process(hideerror=True).accepted:
		escreve_sip_iax()
		escreve_smtp()
		escreve_localnet()
		session.alerta_sucesso = 'Parâmetros salvos com sucesso!'
		redirect(URL('f_parametros_form'))

	return response.render("funcional/form_parametros2.html", form=form)

######-URA
@auth.requires_login()
def f_ura():
	response.title = 'Ura'
	response.marca=['Funcional', 'Ura']
	editor 	= 	permissao()
	url 	=	URL('admanager', 'funcional', 'f_ura_form')
	con = db(db.f_ura).select()
	
	return response.render("funcional/show_ura.html", 
					editor=editor, url=url, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_ura_form():
	response.title = 'Ura'
	response.marca=['Funcional', 'Ura', 'Adiciona Ura']
	id_edit = request.vars['id_edit']

	if id_edit is None:
		form 	=	SQLFORM(db.f_ura)
	else:
		form 	=	SQLFORM(db.f_ura, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		escreve_ura()
		redirect(URL('f_ura'))

	return response.render("funcional/form_ura.html", form=form)

######-FERAIDOS
@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_feriados_form():
	response.title = 'Feriados'
	response.marca=['Funcional', 'Feriados', 'Adiciona Feriado']
	id_edit = request.vars['id_edit']
	editor 	= 	permissao()
	url 	=	URL('admanager', 'funcional', 'f_feriados_form')

	if id_edit is None:
		form 	=	SQLFORM(db.f_feriados, formstyle='divs')
	else:
		form 	=	SQLFORM(db.f_feriados, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	#form.element(_name='dia')['_type'] = "number"
	form.element(_name='dia')['_style'] = "width : 100px"
	form.element(_name='mes')['_style'] = "width : 100px"
	form.element(_name='acao')['_style'] = "width : 450px"
	form.element(_name='descricao')['_style'] = "width : 250px"

	con = db(Feriados).select()

	if form.process(hideerror=True).accepted:
		redirect(URL('f_feriados_form'))

	return response.render("funcional/form_feriados.html", form=form, con=con, 
															url=url, editor=editor)

######-PORTABILIDADE
@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_portabilidade_form():
	response.title = 'Portabilidade'
	response.marca=['Configs', 'Portabilidade']
	
	form 	=	SQLFORM(db.f_portabilidade, 1)

	for input in form.elements():
		input['_class'] = 'form-control'
	if auth.user.email != 'root@forip.com.br':
		form.element(_name='ativo')['_disabled'] = 'true'
	form.custom.widget.senha['_type'] = "password"
	

	if form.process().accepted:
		session.alerta_sucesso = 'Dados salvos com sucesso!'
		redirect(URL('f_portabilidade_form'))

	return response.render("funcional/form_portabilidade.html", form=form)


@auth.requires_login()
def delete():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']
	if funcao 	== "f_troncos":
		tabela 	=	 db.f_troncos.id
	if funcao 	==	"f_troncos_fisicos":
		tabela 	= 	db.f_troncos_fisicos.id
	if funcao 	== "f_tarifacao":
		tabela 	= 	db.f_tarifacao.id
		resp=trata_tarifacao(funcao, id_tab)
		if resp['status'] == False:
			session.alerta_erro = 'Erro, vínculo %s!' %(resp['tabela'])
			redirect(URL(funcao))
	if funcao 	== "f_rotas":
		tabela 	= 	db.f_rotas.id
	if funcao 	== 	"f_empresa":
		tabela 	= db.f_empresa.id
	if funcao 	== 	"f_destinos":
		tabela 	= 	db.f_destinos.id
	if funcao 	== 	"f_horario":
		tabela 	= 	db.f_horario.id
		resp=trata_horario(funcao, id_tab)
		if resp['status'] == False:
			session.alerta_erro = 'Erro, vínculo %s!' %(resp['tabela'])
			redirect(URL(funcao))
	if funcao 	== 	"f_ura":
		tabela 	=	db.f_ura.id
	if funcao 	== 	"f_feriados":
		tabela 	=	db.f_feriados.id
		funcao  = 	'f_feriados_form'

	db(tabela == id_tab).delete()
	if funcao == "f_destinos":
		escreve_destino()
	if funcao == "f_ura":
		escreve_ura()
	redirect(URL(funcao))

@auth.requires_login()
def delete_visao():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']
	if funcao 	== 	"f_empresa":
		resp=trata_empresa(funcao, id_tab)
		if  resp['status'] == False:
			session.alerta_erro = 'Erro, vínculo %s!' %(resp['tabela'])
			redirect(URL(funcao))
		tabela 	= db.f_empresa.id
	if funcao 	== "f_troncos":
		resp=trata_tronco(funcao, id_tab)
		if resp['status'] == False:
			session.alerta_erro = 'Erro, vínculo %s!' %(resp['tabela'])
			redirect(URL(funcao))
		tabela 	=	 db.f_troncos.id
	if funcao 	== 	"f_destinos":
		resp=trata_destino(funcao, id_tab)
		if resp['status'] == False:
			session.alerta_erro = 'Erro, vínculo %s!' %(resp['tabela'])
			redirect(URL(funcao))
		tabela 	= 	db.f_destinos.id

	db(tabela == id_tab).update(mostrar=False)
	if funcao == "f_destinos":
		escreve_destino()
	redirect(URL(funcao))



def escreve_destino():
	print 'escreve destinos'
	destinos = db(db.f_destinos.mostrar == True).select(orderby=db.f_destinos.id)
	arq = open('/aldeia/etc/asterisk/confs/entrada.ael','w')
	for destino in destinos:
		print destino.tipo_chamada
		arq.write('_%s => { \n' %(destino.expressao))
		arq.write('	Set(__id_destino=%s);\n' %(destino.id))
		arq.write('	AGI(rastreamento.php,${CHANNEL},${CDR(linkedid)},${STRFTIME(${EPOCH},,%F %T)},${CUT(CHANNEL,-,1)},${EXTEN},Context:${CONTEXT} | [id_destino=${id_destino}]); \n')
		arq.write('	goto ${proximo_contexto}|${EXTEN}|1;\n')
		arq.write('};\n\n')
	arq.close()
	commands.getoutput("sudo asterisk -rx 'ael reload'")

def escreve_ura():
	ura = db(db.f_ura).select()
	arq = open('/aldeia/etc/asterisk/confs/ura_manager.ael', 'w')
	for dado in ura:
		arq.write("%s => {\n" %(dado.ramal_principal))

		for linha in str(dado.ura).split('\n'):
			arq.write("%s \n" %(linha)) 

		arq.write("};\n\n")
	arq.close()
	commands.getoutput("sudo asterisk -rx 'ael reload'")

def escreve_smtp():
	dado=db(db.f_parametros).select()[0]
	arq1 = open('/etc/ssmtp/ssmtp.conf', 'w')
	arq2 = open('/usr/local/etc/email/email.conf', 'w')

	if dado.endereco_smtp.find('.') != -1:
		endereco=dado.endereco_smtp[dado.endereco_smtp.find('.') +1:]
	else:
		endereco=dado.endereco_smtp

	if dado.usuario_smtp != "":
		arq1.write("root=%s \n" %(dado.usuario_smtp))
		arq1.write("mailhub=%s:%s \n" %(dado.endereco_smtp, dado.porta_smtp))
		arq1.write("rewriteDomain=%s \n" %(endereco))
		arq1.write("hostname=%s \n" %(endereco))
		if dado.tls_smtp == True:
			arq1.write("UseTLS=Yes \n")
		else:
			arq1.write("UseTLS=No \n")
		if dado.start_tls_smtp == True:
			arq1.write("UseSTARTTLS=Yes \n")
		else:
			arq1.write("UseSTARTTLS=No \n")
		arq1.write("FromLineOverride=Yes\n")
		arq1.write("AuthUser=%s \n" %(dado.usuario_smtp))
		arq1.write("AuthPass=%s \n" %(dado.senha_smtp))
		arq1.close()

	arq2.write("SMTP_SERVER = '%s' \n" %(dado.endereco_smtp))
	arq2.write("SMTP_PORT = '%s' \n" %(dado.porta_smtp))
	arq2.write("MY_NAME  = 'PABX' \n")
	arq2.write("MY_EMAIL = '%s' \n" %(dado.usuario_smtp))
	arq2.write("SMTP_AUTH = 'LOGIN' \n")
	arq2.write("SMTP_AUTH_USER = '%s' \n" %(dado.usuario_smtp))
	arq2.write("SMTP_AUTH_PASS = '%s' \n" %(dado.senha_smtp))
	arq2.close()

def escreve_localnet():
	dado=db(db.f_parametros).select()[0]
	arq = open('/aldeia/etc/asterisk/confs/sip_localnet_admanager.conf', 'w')

	ips=db(db.f_parametros).select(db.f_parametros.faixa_ip_interna)[0].faixa_ip_interna

	for ip in str(ips).split('\n'):
		if ip != '':
			arq.write('localnet=%s\n' %(ip))
	if dado.endereco_ip_externo != '':
		arq.write('externip=%s\n' %(dado.endereco_ip_externo))
	arq.close()
	commands.getoutput("sudo asterisk -rx 'module reload chan_sip.so'")

def f_download():
	response.title = 'Área de Download'
	
	return response.render("funcional/download_area.html")

@auth.requires_login()
def insert_aplicacao():
	#insert aplicacao
	#con = db(db.f_ramal_virtual).select(db.f_ramal_virtual.id)
	#for dado in con:
	#	print dado.id
	#########################
	#update Grupo_destinos
	con = db(Grupo_destinos).select()
	try:
		for dado in con:
			lista=[]
			print dado
			for item in dado.id_destinos:
				print item
				print Destinos[item].tipo_chamada
				lista.append(Destinos[item].tipo_chamada)
			lista = list(set(lista))
			print 'update: %s - %s' %(dado.id, lista)
			db(Grupo_destinos.id == dado.id).update(id_destinos=lista)
	except:
		return ('Já Feito')
	
	#lista=[5,3,9,22,2]
	#db(Grupo_destinos.id == 14).update(id_destinos=lista)
	#Grupo_destinos.insert(id_destinos=lista, grupo_destino='Cel')

def testa_smtp():
	print request.vars
	us_smtp=request.vars.usr
	if '@' in request.vars.usr: us_smtp = request.vars.usr
	else: us_smtp= '%s@%s' %(request.vars.usr, request.vars.end[request.vars.end.find('.')+1::])
	print us_smtp
	print type(request.vars.end)

	mail = auth.settings.mailer
	mail.settings.server = '%s:%s' %(request.vars.end, request.vars.por)
	mail.settings.sender = us_smtp
	mail.settings.login = '%s:%s' %(request.vars.usr, request.vars.sen)
	try:
		if mail.send(
			to="fndiaz02@gmail.com",
			subject="teste conexao",
			message="ok" 
		) is True:
			print 'ok'
			return response.json([True, 'Ok'])
		else:
			print mail.error
			print 'Failed'
			return response.json([False, str(mail.error)])
	except:
		return response.json([False, 'Algo errado'])