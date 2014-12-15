@auth.requires_login()
def prov_rede():
	response.title = 'Rede do Provisionamento'
	response.marca=['Provisionamento', 'Rede']
	editor = permissao()
	url = URL('admanager', 'provisionamento', 'prov_rede_form')

	con = db(Prov_rede).select(orderby=Prov_rede.id)
	
	return response.render("provisionamento/show_rede.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def prov_rede_form():
	response.title = 'Rede do Provisionamento'
	response.marca=['Provisionamento', 'Rede', 'Adiciona Rede']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(Prov_rede)
	else:
		form 	=	SQLFORM(Prov_rede, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	form.custom.widget.proxy['_placeholder'] = "ip do servidor asterisk"
	form.custom.widget.dns['_placeholder'] = "exemplo: 8.8.8.8"
	form.custom.widget.ntp['_placeholder'] = "exemplo: a.ntp.br"


	if form.process().accepted:
		redirect(URL('prov_rede'))

	return response.render("provisionamento/form_prov_rede.html", form=form)

@auth.requires_login()
def prov_equipamento():
	response.title = 'Equipamentos'
	response.marca=['Provisionamento', 'Equipamentos']
	editor = permissao()
	url = URL('admanager', 'provisionamento', 'prov_equipamento_form')

	con = db(Prov_equipamento).select(orderby=Prov_equipamento.id)
	
	return response.render("provisionamento/show_equipamento.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def prov_equipamento_form():
	response.title = 'Adicionar Equipamento'
	response.marca=['Provisionamento', 'Equipamento', 'Adicionar Equipamento']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(Prov_equipamento)
	else:
		form 	=	SQLFORM(Prov_equipamento, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	#form.custom.widget.proxy['_placeholder'] = "ip do servidor asterisk"

	if form.process().accepted:
		redirect(URL('prov_equipamento'))

	return response.render("provisionamento/form_prov_equipamento.html", form=form)

@auth.requires_login()
def prov_mac():
	response.title = 'Mac Address'
	response.marca=['Provisionamento', 'Mac Adress']
	editor = permissao()
	url = URL('admanager', 'provisionamento', 'prov_mac_form')

	con = db(Prov_mac).select(orderby=Prov_mac.id)
	
	return response.render("provisionamento/show_mac.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def prov_mac_form():
	response.title = 'Adicionar Mac'
	response.marca=['Provisionamento', 'Mac Address', 'Adicionar Mac']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(Prov_mac)
	else:
		form 	=	SQLFORM(Prov_mac, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	#form.custom.widget.proxy['_placeholder'] = "ip do servidor asterisk"

	if form.process().accepted:
		status, obs = escreve_prov()
		if status == False:
			print 'erro %s' %(obs)
			session.alerta_erro = 'Nem tudo funcionou como devia ramal %s não existe!' %(obs)
		else:
			session.alerta_sucesso = 'Provisionamento gerado!'
		redirect(URL('prov_mac'))

	return response.render("provisionamento/form_prov_mac.html", form=form)

@auth.requires_login()
def prov_ramal():
	response.title = 'Ramal'
	response.marca=['Provisionamento', 'Ramal']
	editor = permissao()
	url = URL('admanager', 'provisionamento', 'prov_ramal_form')

	query = (Prov_ramal.id_mac == Prov_mac.id) &\
			(Prov_mac.id_equipamento == Prov_equipamento.id)
	con = db(query).select(orderby=Prov_ramal.id)
	
	return response.render("provisionamento/show_ramal.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def prov_ramal_form():
	response.title = 'Adicionar Ramal'
	response.marca=['Provisionamento', 'Ramal', 'Adicionar Ramal']
	id_edit	= request.vars['id_edit']
	dict_edit={}

	if id_edit != None:
		ramal_req=IS_NOT_EMPTY()
	else:
		ramal_req=[IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'prov_ramal.ramal')]

	form = SQLFORM.factory(
		Field("mac", requires=IS_NOT_EMPTY()),
		Field("ramal", requires=ramal_req),
		Field("linha", requires=IS_IN_SET(['1','2','3','4','5','6','7','8','9'])),
		)
	for input in form.elements():
		input['_class'] = 'form-control'
		form.custom.widget.mac['_autocomplete'] = 'off'
		form.custom.widget.mac['_data-provide'] = 'typeahead'
		form.custom.widget.mac['_data-items'] = '4'
		form.custom.widget.mac['_data-source'] = ''

	if id_edit != None:
		query=(Prov_ramal.id == id_edit) & (Prov_mac.id == Prov_ramal.id_mac)
		con = db(query).select()
		for dado in con:
			dict_edit['mac'] = dado.prov_mac.mac
			dict_edit['ramal'] = dado.prov_ramal.ramal
			dict_edit['linha'] = dado.prov_ramal.linha		

	if form.process(onvalidation=valida_prov_ramal).accepted:
		id_mac=db(Prov_mac.mac == form.vars.mac).select(Prov_mac.id)[0].id
		if id_edit == None:
			db.prov_ramal.insert(id_mac=id_mac, ramal=form.vars.ramal, linha=form.vars.linha)
			status, obs = escreve_prov()
			if status == False:
				print 'erro %s' %(obs)
				session.alerta_erro = 'Nem tudo funcionou como devia ramal %s não existe!' %(obs)
			else:
				session.alerta_sucesso = 'Provisionamento gerado!'
			redirect(URL('prov_ramal'))
		else:
			db(db.prov_ramal.id == id_edit).update(id_mac=id_mac, ramal=form.vars.ramal, linha=form.vars.linha)
			status, obs = escreve_prov()
			if status == False:
				print 'erro %s' %(obs)
				session.alerta_erro = 'Nem tudo funcionou como devia ramal %s não existe!' %(obs)
			else:
				session.alerta_sucesso = 'Provisionamento gerado!'
			redirect(URL('prov_ramal'))

	return response.render("provisionamento/form_prov_ramal.html", 
										form=form, dict_edit=dict_edit)

def valida_prov_ramal(form):
	print form
	print 'valida'
	if db(Prov_mac.mac == form.vars.mac).isempty():
		form.errors.mac = 'mac não existe'

def json_mac():
	con = db(Prov_mac).select(Prov_mac.mac)
	lista 	=	[]
	for dado in con:
		lista.append(dado.mac)
	lista 	=	list(set(lista))

	return response.json(lista)


@auth.requires_login()
def delete():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']

	if funcao	== "prov_rede":
		tabela 	=	Prov_rede.id
		funcao	= 	"prov_rede"
	if funcao == "prov_equipamento":
		tabela = Prov_equipamento.id
		funcao = "prov_equipamento"
	if funcao == "prov_mac":
		tabela = Prov_mac.id
		funcao = "prov_mac"
		mac    = db(Prov_mac.id == id_tab).select()[0]['mac']
	if funcao == "prov_ramal":
		tabela = Prov_ramal.id
		funcao = "prov_ramal"

	db(tabela == id_tab).delete()
	
	if funcao == 'prov_ramal':
		status, obs = escreve_prov()
		if status == False:
			print 'erro %s' %(obs)
			session.alerta_erro = 'Nem tudo funcionou como devia ramal %s não existe!' %(obs)
		else:
			session.alerta_sucesso = 'Provisionamento gerado!'
		
	if funcao == 'prov_mac':
		status, obs = escreve_prov()
		if status == False:
			print 'erro %s' %(obs)
			session.alerta_erro = 'Nem tudo funcionou como devia ramal %s não existe!' %(obs)
		else:
			session.alerta_sucesso = 'Provisionamento gerado!'
	redirect(URL(funcao))