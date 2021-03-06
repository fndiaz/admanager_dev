# coding=UTF-8

######-Grupos
@auth.requires_login()  
def f_grupo_destinos():
	response.title = 'Grupos de destino'
	response.marca=['Extensões', 'Grupos de Destino']
	editor = permissao()
	url = URL('admanager', 'ramais_v', 'f_grupo_destinos_form')

	con = db(db.f_grupo_destinos).select(orderby=db.f_grupo_destinos.id)
	
	return response.render("ramais_v/show_grupo_destinos.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_grupo_destinos_form():
	response.title = 'Grupo de destino'
	response.marca=['Extensões', 'Grupos de Destino', 'Adiciona Grupo de Destino']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(db.f_grupo_destinos)
	else:
		form 	=	SQLFORM(db.f_grupo_destinos, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		redirect(URL('f_grupo_destinos'))
	elif form.errors:
		print 'erro'
		print form.vars

	return response.render("ramais_v/form_grupo_destinos.html", form=form)

######-DEPARTAMENTOS
@auth.requires_login()  
def f_departamentos():
	response.title = 'Departamentos'
	response.marca=['Extensões', 'Departamentos']
	editor = permissao()
	url = URL('admanager', 'ramais_v', 'f_departamentos_form')

	query = (db.f_departamentos.mostrar == True)&\
			(db.f_departamentos.id_empresa == db.f_empresa.id)
	con = db(query).select(orderby=db.f_departamentos.id)
	
	return response.render("ramais_v/show_departamentos.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_departamentos_form():
	response.title = 'Departamentos'
	response.marca=['Extensões', 'Departamentos', 'Adiciona Departamentos']
	id_edit	= request.vars['id_edit']
	testa = True
	
	if id_edit is None:
		form 	=	SQLFORM(db.f_departamentos)
	else:
		testa 	=	False
		form 	=	SQLFORM(db.f_departamentos, id_edit)
		form.element(_name='departamento')['_readonly'] = "readonly"

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		if testa == True:
			var= 'dept_%s' %(request.vars['departamento'])
			auth.add_group(var, '')
		redirect(URL('f_departamentos'))

	return response.render("ramais_v/form_departamentos.html", form=form)

######-RAMAL VIRTUAL
@auth.requires_login()  
def f_ramal_virtual():
	response.title = 'Ramal Virtual'
	response.marca=['Extensões', 'Ramal Virtual']
	editor = permissao()
	url = URL('admanager', 'ramais_v', 'f_ramal_virtual_form')

	query = (db.f_ramal_virtual.id_departamento == db.f_departamentos.id)&\
			(db.f_ramal_virtual.id_grupo_destinos == db.f_grupo_destinos.id)
	con = db(query).select(orderby=db.f_ramal_virtual.ramal_virtual)
	#print con
	
	return response.render("ramais_v/show_ramal_virtual.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_ramal_virtual_form():
	response.title = 'Ramal'
	response.marca=['Extensões', 'Ramal Virtual', 'Adiciona Ramal Virtual']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(db.f_ramal_virtual)
	else:
		form 	=	SQLFORM(db.f_ramal_virtual, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	form.element(_name='chamadas_simultaneas')['_type'] = "number"

	if form.process().accepted:
		if id_edit is None:
			insert_aplicacao(request.vars.ramal_virtual.strip(' ') )
		else:
			update_voicemail(request.vars)
		peers_fop2()
		redirect(URL('f_ramal_virtual'))

	return response.render("ramais_v/form_ramal_virtual.html", form=form)

##Quando edita f_ramal_virtual_form
def update_voicemail(dados):
	print dados
	query1=(Voicemail.id_ramalvirtual == dados.id)
	if not db(query1).isempty():
		db(query1).update(mailbox=int(dados.ramal_virtual),
						  fullname=dados.nome)


def insert_aplicacao(ramalv):
	query=(db.f_ramal_virtual.ramal_virtual == ramalv)
	id_ramalv=db(query).select(db.f_ramal_virtual.id)[0].id
	db.f_aplicacao.insert(id_ramalvirtual=id_ramalv,
							cadeado_ativo=False,
							cadeado_senha="",
							cs_ativo=False,
							cs_chamadaexterna=False,
							cs_chamadainterna=False,
							cs_numero="",
							cs_excecao="",
							voicemail_ativo=False,
							voicemail_email="",
							voicemail_senha="",
							agenda_cadastro=False,
							agenda_senha="")

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_aplicacao_form():
	response.title = 'Aplicação'
	response.marca=['Extensões', 'Ramal Virtual', 'Aplicações do Ramal']
	ramalv	= request.vars['id_edit']
	query=(db.f_aplicacao.id_ramalvirtual == ramalv)
	id_apl=db(query).select(db.f_aplicacao.id)[0].id
	
	form 	=	SQLFORM(db.f_aplicacao, id_apl)

	for input in form.elements():
		input['_class'] = 'form-control'
	form.element(_name='cs_excecao')['_rows'] = "4"

	#form.element(_name='ciclo_conta')['_value'] = "teste"
	if form.process().accepted:
		insert_voicemail(request.vars)
		redirect(URL('f_ramal_virtual'))
	else:
		print request.vars

	return response.render("ramais_v/form_aplicacao.html", form=form)

##Quando insere f_aplicacao_form
def insert_voicemail(dados):
	print dados
	ramal= db(Ramal_virtual.id == dados.id_ramalvirtual).select()[0]
	query1=(Voicemail.id_ramalvirtual == ramal.id)

	if dados.voicemail_ativo == 'on':
		if db(query1).isempty():
			print 'vazio'
			Voicemail.insert(customer_id=0,
							context="default",
							mailbox=int(ramal.ramal_virtual),
							password=dados.voicemail_senha,
							fullname=ramal.nome,
							email=dados.voicemail_email,
							pager="0",
							id_ramalvirtual=dados.id_ramalvirtual)
		else:
			db(query1).update(customer_id=0,
							context="default",
							mailbox=int(ramal.ramal_virtual),
							password=dados.voicemail_senha,
							fullname=ramal.nome,
							email=dados.voicemail_email,
							pager="0",
							id_ramalvirtual=dados.id_ramalvirtual)
	else:
		db(query1).delete()
			

######-DIRECIONAMENTO
@auth.requires_login()
def f_direcionamento():
	response.title = 'Direcionamento'
	response.marca=['Extensões', 'Direcionamento']
	editor = permissao()
	url = URL('admanager', 'ramais_v', 'f_direcionamento_form')

	con = db(db.f_direcionamento).select()
	
	return response.render("ramais_v/show_direcionamento.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_direcionamento_form():
	response.title = 'Direcionamento'
	response.marca=['Extensões', 'Direcionamento', 'Adiciona Direcionamento']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(db.f_direcionamento)
	else:
		form 	=	SQLFORM(db.f_direcionamento, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		redirect(URL('f_direcionamento'))

	return response.render("ramais_v/form_direcionamento.html", form=form)

######-DESVIOS
@auth.requires_login()
def f_desvios():
	response.title = 'Desvios'
	response.marca=['Extensões', 'Desvios']
	editor = permissao()
	url = URL('admanager', 'ramais_v', 'f_desvios_form')

	query = (db.f_desvios.id_ramalvirtual == db.f_ramal_virtual.id)
	con = db(query).select(orderby=db.f_desvios.numero)
	
	return response.render("ramais_v/show_desvios.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_desvios_form():
	response.title = 'Desvios'
	response.marca=['Extensões', 'Desvios', 'Adiciona Desvios']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(db.f_desvios)
	else:
		form 	=	SQLFORM(db.f_desvios, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process(onvalidation=valida_f_desvios_form).accepted:
		redirect(URL('f_desvios'))

	return response.render("ramais_v/form_desvios.html", form=form)

def valida_f_desvios_form(form):
	print '-----VALIDA-----'
	#print form.vars
	h1 = form.vars.horario_inicio.split(':')[0]
	h2 = form.vars.horario_fim.split(':')[0]
	m1 = form.vars.horario_inicio.split(':')[1]
	m2 = form.vars.horario_fim.split(':')[1]
	if h1 > '23' or m1 > '59':
		form.errors.horario_inicio = 'horário inválido'
	if h2 > '23' or m2 > '59':
		form.errors.horario_fim = 'horário inválido'
	if h2 < h1:
		form.errors.horario_fim = 'não pode ser menor, igual que horário início'
	if h2 == h1:
		if m2 <= m1:
			form.errors.horario_fim = 'não pode ser menor, igual que horário início'

######-DDR
@auth.requires_login()
def f_ddr():
	response.title = 'DDR'
	response.marca=['Extensões', 'DDR']
	editor = permissao()
	url = URL('admanager', 'ramais_v', 'f_ddr_form')

	query = (db.f_ddr.id_ramalvirtual == db.f_ramal_virtual.id)
	con = db(query).select(orderby=db.f_ddr.ddr)
	
	return response.render("ramais_v/show_ddr.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_ddr_form():
	response.title = 'DDR'
	response.marca=['Extensões', 'DDR', 'Adiciona DDR']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(db.f_ddr)
	else:
		form 	=	SQLFORM(db.f_ddr, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		redirect(URL('f_ddr'))

	return response.render("ramais_v/form_ddr.html", form=form)

######-DA
@auth.requires_login()
def f_discagem_abreviada():
	response.title = 'Discagem Abreviada'
	response.marca=['Extensões', 'Discagem Abreviada']
	editor = permissao()
	url = URL('admanager', 'ramais_v', 'f_discagem_abreviada_form')

	con = db(db.f_discagem_abreviada).select(orderby=db.f_discagem_abreviada.id)
	
	return response.render("ramais_v/show_discagema.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_discagem_abreviada_form():
	response.title = 'Discagem Abreviada'
	response.marca=['Extensões', 'Discagem Abreviada', 'Adiciona']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(db.f_discagem_abreviada)
	else:
		form 	=	SQLFORM(db.f_discagem_abreviada, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	form.custom.widget.abreviado['_placeholder'] = "exemplo *200"

	if form.process().accepted:
		redirect(URL('f_discagem_abreviada'))

	return response.render("ramais_v/form_discagema.html", form=form)

######-CRM
@auth.requires_login()
def crm_agent():
	response.title = 'CRM Agente'
	response.marca=['CRM', 'Agente']
	editor = permissao()
	url = URL('admanager', 'ramais_v', 'crm_agent_form')

	query=(Voicemail.context == 'crm')
	con = db(query).select(orderby=Voicemail.mailbox)
	
	return response.render("ramais_v/show_crmagent.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def crm_agent_form():
	id_edit	= request.vars['id_edit']

	#define requires
	if id_edit is None:
		req_mailbox=[IS_MATCH("^[0-9][0-9][0-9][0-9]$", error_message='quarto números'),
								   IS_NOT_IN_DB(db, 'voicemail.mailbox')]
		req_email=[IS_EMAIL(), IS_NOT_IN_DB(db, 'voicemail.email')]
		req_pager=[IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'voicemail.pager')]
	else:
		req_mailbox=IS_MATCH("^[0-9][0-9][0-9][0-9]$", error_message='quarto números')
		req_email=IS_EMAIL()
		req_pager=IS_NOT_EMPTY()

	form = SQLFORM.factory(
		Field("fullname", requires=IS_NOT_EMPTY()),
		Field("email", requires=req_email),
		Field("pager", requires=req_pager),
		Field("password", requires=IS_MATCH("^[0-9][0-9][0-9][0-9]$", error_message='quarto números')),
		Field("mailbox", requires=req_mailbox),
		Field("id_editar"),
	)

	if id_edit is not None:
		form.element(_name='fullname')['_value'] = Voicemail[id_edit].fullname
		form.element(_name='email')['_value'] = Voicemail[id_edit].email
		form.element(_name='pager')['_value'] = Voicemail[id_edit].pager
		form.element(_name='password')['_value'] = Voicemail[id_edit].password
		form.element(_name='mailbox')['_value'] = Voicemail[id_edit].mailbox
		form.element(_name='id_editar')['_value'] = id_edit

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process(onvalidation=valida_agent).accepted:
		print 'id_edit:%s' %(id_edit)
		if id_edit is None:
			if insert_crmagent(request.vars) is True:
				redirect(URL('crm_agent'))
			session.alerta_erro = 'Erro de inclusão!'
		else:
			if update_crmagent(request.vars) is True:
				redirect(URL('crm_agent'))
			session.alerta_erro = 'Erro de inclusão!'

	return response.render("ramais_v/form_crmagent.html", form=form)

def valida_agent(form):
	print 'valida'
	if form.vars.id_editar != None:
		query=((Voicemail.uniqueid != form.vars.id_editar) & (Voicemail.context == 'crm'))
		con_email=db(query).select(Voicemail.email)
		for dado in con_email:
			if dado.email == form.vars.email:
				form.errors.email = 'email existente'

		con_mailbox=db(query).select(Voicemail.mailbox)
		for dado in con_mailbox:
			if dado.mailbox == int(form.vars.mailbox):
				form.errors.mailbox = 'número existente'

		con_pager=db(query).select(Voicemail.pager)
		for dado in con_pager:
			if dado.pager == form.vars.pager:
				form.errors.pager = 'agente existente'


def insert_crmagent(d):
	print 'insert'
	Voicemail.insert(customer_id=0,
					context="crm",
					password=d.password,
					fullname=d.fullname,
					email=d.email,
					pager=d.pager,
					mailbox=int(d.mailbox),
	)
	return True

def update_crmagent(d):
	print 'update'
	query1=(Voicemail.uniqueid == d.id_edit)
	if not db(query1).isempty():
		db(query1).update(customer_id=0,
					context="crm",
					password=d.password,
					fullname=d.fullname,
					email=d.email,
					pager=d.pager,
					mailbox=int(d.mailbox),
	)
	return True


@auth.requires_login()
def crm_queue():
	response.title = 'CRM Filas'
	response.marca=['CRM', 'Filas']
	editor = permissao()
	url = URL('admanager', 'queues', 'queue_form')
	print editor

	con = db(db.queue.crm == True).select()
	
	return response.render("ramais_v/show_crmqueue.html",  
					url=url, editor=editor, con=con)

@auth.requires_login()
def crm_queue_members_form():
	#print request.vars.id_queue
	response.title='Queue members'
	response.marca=['Extensões', 'Filas', 'Membros da Fila', 'Adiciona Membro']
	editor = permissao()
	id_edit = request.vars.id_edit
	id_queue= request.vars.id_queue
	db.f_agente_filas.id_fila.default = id_queue
	query=(db.voicemail.context == 'crm')
	db.f_agente_filas.id_agente.requires = IS_IN_DB(db(query),'voicemail.id',"%(pager)s")


	con=db(Agente_filas.id_fila == id_queue).select()

	if id_edit is None:
		form = SQLFORM(Agente_filas)
	else:
		form = SQLFORM(Agente_filas, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	form.element(_name='id_fila')['_readonly'] = "readonly"

	if form.process(onvalidation=valida_agente_fila).accepted:
		print 'ok'
		redirect(URL(a='admanager', c='ramais_v', f='crm_queue_members_form', 
							vars={'id_queue':request.vars.id_queue}))
	elif form.errors:
		print request.vars
		print 'no'

	return response.render("ramais_v/form_crm_queuemembers.html", 
										editor=editor, con=con, form=form)

def valida_agente_fila(form):
	print 'valida'
	print form.vars
	for dado in db(Agente_filas).select():
		if (dado.id_agente == int(form.vars.id_agente)) & (dado.id_fila == int(form.vars.id_fila)):
		   form.errors.id_agente = 'Agente já existe'
	



######-EXTRAS
def link_fisico():
	print 'link_fisico'
	print request.vars
	if (request.vars['tec'] == 'SIP') or (request.vars['tec'] == 'IAX') or (request.vars['tec'] == 'IAX2'):
		id_fis=db(db.fisico_sip_iax.usuario == request.vars.fisico).select(db.fisico_sip_iax.id)[0].id
		redirect(URL(a='admanager',c='ramais',f='fisico_sip_iax_form',vars=dict(id_edit=id_fis)))
	if (request.vars['tec'] == 'DAHDI') or (request.vars['tec'] == 'KHOMP'):
		redirect(URL(a='admanager',c='ramais',f='show_dahdi'))
	if (request.vars['tec'] == 'QUEUE'):
		id_fis=db(db.queue.name == request.vars.fisico).select(db.queue.id)[0].id
		redirect(URL(a='admanager',c='queues',f='queue_form',vars=dict(id_edit=id_fis)))
	if (request.vars['tec'] == 'FAX'):
		id_fis=db(db.f_fax.numero == request.vars.fisico).select(db.f_fax.id)[0].id
		redirect(URL(a='admanager',c='queues',f='f_fax_form',vars=dict(id_edit=id_fis)))
	if (request.vars['tec'] == 'LOCAL'):
		id_fis=db(db.f_local.numero == request.vars.fisico).select(db.f_local.id)[0].id
		redirect(URL(a='admanager',c='queues',f='f_local_form',vars=dict(id_edit=id_fis)))
	if (request.vars['tec'] == 'MEETME'):
		id_fis=db(db.meetme.confno == request.vars.fisico).select(db.meetme.id)[0].id
		redirect(URL(a='admanager',c='queues',f='meetme_form',vars=dict(id_edit=id_fis)))


def ajax_fisico():
	print 'entrou'
	print request.vars
	if (request.vars['tec'] == 'SIP') or (request.vars['tec'] == 'IAX2'):
		if request.vars['tec'] == 'SIP':
			ramal_virtual = db(db.f_ramal_virtual.tecnologia == 'SIP')._select(db.f_ramal_virtual.ramal_fisico)
		if request.vars['tec'] == 'IAX2':
			ramal_virtual = db(db.f_ramal_virtual.tecnologia == 'IAX2')._select(db.f_ramal_virtual.ramal_fisico)
		query = (db.fisico_sip_iax.tecnologia == request.vars['tec'])&\
				(db.fisico_sip_iax.tronco == False)&\
				(~db.fisico_sip_iax.usuario.belongs(ramal_virtual))
		con = db(query).select(db.fisico_sip_iax.usuario,orderby=db.fisico_sip_iax.usuario)
		print con

	if (request.vars['tec'].lower() == 'dahdi') or (request.vars['tec'].lower() == 'khomp'):
		if request.vars['tec'].lower() == 'dahdi':
			porta = db(db.f_ramal_virtual.tecnologia == 'DAHDI')._select(db.f_ramal_virtual.ramal_fisico)
		if request.vars['tec'].lower() == 'khomp':
			porta = db(db.f_ramal_virtual.tecnologia == 'KHOMP')._select(db.f_ramal_virtual.ramal_fisico)
		query = (db.fisico_dahdi_khomp.tecnologia == request.vars['tec'].lower())&\
				(~db.fisico_dahdi_khomp.porta.belongs(porta))
		con = db(query).select(db.fisico_dahdi_khomp.porta,orderby=db.fisico_dahdi_khomp.porta)
		print con

	if request.vars['tec'] == 'QUEUE':
		fila = db(db.f_ramal_virtual.tecnologia == 'QUEUE')._select(db.f_ramal_virtual.ramal_fisico) 
		query = (~db.queue.name.belongs(fila))
		con = db(query).select(db.queue.name,orderby=db.queue.name)

	if request.vars['tec'] == 'FAX':
		fila = db(db.f_ramal_virtual.tecnologia == 'FAX')._select(db.f_ramal_virtual.ramal_fisico) 
		query = (~db.f_fax.numero.belongs(fila))
		con = db(query).select(db.f_fax.numero,orderby=db.f_fax.numero)

	if request.vars['tec'] == 'LOCAL':
		loc = db(db.f_ramal_virtual.tecnologia == 'LOCAL')._select(db.f_ramal_virtual.ramal_fisico) 
		query = (~db.f_local.numero.belongs(loc))
		con = db(query).select(db.f_local.numero,orderby=db.f_local.numero)

	if request.vars['tec'] == 'MEETME':
		met = db(db.f_ramal_virtual.tecnologia == 'MEETME')._select(db.f_ramal_virtual.ramal_fisico)
		query = (~db.meetme.confno.belongs(met))
		con = db(query).select(db.meetme.confno,orderby=db.meetme.confno)
		print con
	
	return con.as_json()


@auth.requires_login()
def delete():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']

	if funcao 	== "f_ramal_virtual":
		tabela 	=	 db.f_ramal_virtual.id
		resp=trata_ramal_virtual(funcao, id_tab)
		if resp['status'] == False:
			session.alerta_erro = 'Erro, vínculo %s!' %(resp['tabela'])
			redirect(URL(funcao))
		funcao  = 	 'f_ramal_virtual'

	if funcao	== "f_departamentos":
		delete_role(request.vars['nome'])
		tabela 	=	db.f_departamentos.id
		funcao	= 	"f_departamentos"

	if funcao	==	"f_desvios":
		tabela	= 	db.f_desvios.id
		funcao	= 	"f_desvios"

	if funcao	==	"f_ddr":
		tabela	= 	db.f_ddr.id
		funcao	= 	"f_ddr"

	if funcao	==	"voicemail":
		tabela	= 	db.voicemail.uniqueid
		funcao	= 	"crm_agent"

	if funcao	==	"f_discagem_abreviada":
		tabela	= 	db.f_discagem_abreviada.id
		funcao	= 	"f_discagem_abreviada"

	if funcao	==	"f_agente_filas":
		tabela	= 	db.f_agente_filas.id
		funcao 	= 	"f_agente_filas"

	if funcao	== "f_grupo_destinos":
		tabela	= 	db.f_grupo_destinos.id
		resp=trata_grupo_destino(funcao, id_tab)
		if resp['status'] == False:
			session.alerta_erro = 'Erro, vínculo %s!' %(resp['tabela'])
			redirect(URL(funcao))
		funcao	= 	"f_grupo_destinos"
	
	db(tabela == id_tab).delete()
	if funcao == "f_ramal_virtual":
		db(Aplicacao.id_ramalvirtual == id_tab).delete()
		db(Voicemail.id_ramalvirtual == id_tab).delete()
	if funcao == 'f_agente_filas':
		print request.vars.id_queue
		redirect(URL(a='admanager', c='ramais_v', f='crm_queue_members_form', 
							vars={'id_queue':request.vars.id_queue}))
	redirect(URL(funcao))

@auth.requires_login()
def delete_visao():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']
	if funcao 	== 	"f_departamentos":
		resp=trata_departamento(funcao, id_tab)
		if resp['status'] == False:
			session.alerta_erro = 'Erro, vínculo %s!' %(resp['tabela'])
			redirect(URL(funcao))
		tabela 	= db.f_departamentos.id

	db(tabela == id_tab).update(mostrar=False)
	redirect(URL(funcao))

def delete_role(nome):
	print 'entrou'
	print nome
	nome = 'dept_%s' %(nome)
	id_role	= 	db(db.auth_group.role == nome).select(db.auth_group.id)
	auth.del_group(id_role[0].id)