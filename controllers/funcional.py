# coding=UTF-8

######-TRONCOS
@auth.requires_login()  
def f_troncos():
	response.title = 'Troncos'
	response.marca=['Funcional', 'Troncos']
	editor = permissao()
	url = URL('admanager', 'funcional', 'f_troncos_form')
	print editor

	troncos = db(db.f_troncos).select(orderby=db.f_troncos.id)
	
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

	#form.element(_name='ciclo_conta')['_value'] = "teste"
	if form.process().accepted:
		redirect(URL('f_troncos'))

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
	destinos 	= 	db(db.f_destinos).select(orderby=db.f_destinos.id)

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
	empresa	= 	db(db.f_empresa).select(orderby=db.f_empresa.id)

	return response.render("funcional/show_empresa.html", 
				url=url, editor=editor, empresa=empresa)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_empresa_form():
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

	return response.render("funcional/show_tarifacao.html", 
				editor=editor, url=url, tarifacao=tarifacao)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_tarifacao_form():
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
		form 	=	SQLFORM(db.f_rotas, id_horario)

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

	if form.process().accepted:
		escreve_sip_iax()
		session.alerta_sucesso = 'Parâmetros salvos com sucesso!'
		redirect(URL('f_parametros_form'))

	return response.render("funcional/form_parametros.html", form=form)

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

######-PORTABILIDADE
@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_portabilidade_form():
	response.title = 'Portabilidade'
	response.marca=['Configs', 'Portabilidade']
	
	form 	=	SQLFORM(db.f_portabilidade, 1)

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		redirect(URL('f_portabilidade'))

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
	if funcao 	== "f_rotas":
		tabela 	= 	db.f_rotas.id
	if funcao 	== 	"f_tarifacao":
		tabela 	=	db.f_tarifacao.id
	if funcao 	== 	"f_empresa":
		tabela 	= db.f_empresa.id
	if funcao 	== 	"f_destinos":
		tabela 	= 	db.f_destinos.id
	if funcao 	== 	"f_horario":
		tabela 	= 	db.f_horario.id
	if funcao 	== 	"f_ura":
		tabela 	=	db.f_ura.id

	db(tabela == id_tab).delete()
	if funcao == "f_destinos":
		escreve_destino()
	if funcao == "f_ura":
		escreve_ura()
	redirect(URL(funcao))

def escreve_destino():
	destinos = db(db.f_destinos).select(orderby=db.f_destinos.id)
	arq = open('/tmp/entrada.ael','w')
	for destino in destinos:
		print destino.tipo_chamada
		arq.write('_X%s => { \n' %(destino.expressao))
		arq.write('	Set(__id_destino=%s);\n' %(destino.id))
		arq.write('	AGI(rastreamento.php,${CHANNEL},${CDR(linkedid)},${STRFTIME(${EPOCH},,%F %T)},${CUT(CHANNEL,-,1)},${EXTEN},Context:${CONTEXT} | [id_destino=${id_destino}]); \n')
		arq.write('	goto ${proximo_contexto}|${EXTEN}|1;\n')
		arq.write('};\n\n')
	arq.close()

def escreve_ura():
	ura = db(db.f_ura).select()
	arq = open('/tmp/ura_manager.ael', 'w')
	for dado in ura:
		arq.write("%s => {\n" %(dado.ramal_principal))

		for linha in str(dado.ura).split('\n'):
			arq.write("%s \n" %(linha)) 

		arq.write("};\n\n")

