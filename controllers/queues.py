# coding=UTF-8
### Queue-Fax
from datetime import datetime

@auth.requires_login()
def queue():
	response.title = 'Filas'
	response.marca=['Extensões', 'Filas']
	editor = permissao()
	url = URL('admanager', 'queues', 'queue_form')
	print editor

	con = db(db.queue).select()
	
	return response.render("queue/show_queue.html",  
					url=url, editor=editor, con=con)

@auth.requires_login()
def queue_form():
	response.title = 'Filas'
	response.marca=['Extensões', 'Filas', 'Adiciona Fila']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(db.queue)
	else:
		form 	=	SQLFORM(db.queue, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'

	#form.element(_name='ciclo_conta')['_value'] = "teste"
	if form.process().accepted:
		redirect(URL('queue'))

	return response.render("queue/form_queue.html", form=form)

@auth.requires_login()
def queue_extra_form():
	response.title = 'Filas'
	response.marca=['Extensões', 'Filas', 'Extras da Fila']
	id_edit	= request.vars['id_edit']
	
	form 	=	SQLFORM(db.queue, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'

	#form.element(_name='ciclo_conta')['_value'] = "teste"
	if form.process().accepted:
		redirect(URL('queue'))
	else:
		print request.vars

	return response.render("queue/form_queue_extra.html", form=form)

@auth.requires_login()
def queue_members():
	response.title='Queue members'
	response.marca=['Extensões', 'Filas', 'Membros da Fila']
	editor = permissao()
	id_queue = request.vars.id_queue
	url = URL('admanager', 'queues', 'queue_members_form', vars={'id_queue':id_queue})
	name = db(db.queue.id == id_queue).select(db.queue.name)[0].name

	query = (db.queue_members.queue_name == name)
	con = db(query).select()

	return response.render("queue/show_queue_members.html", 
						url=url, editor=editor, con=con)

@auth.requires_login()
def queue_members_form():
	print request.vars.id_queue
	response.title='Queue members'
	response.marca=['Extensões', 'Filas', 'Membros da Fila', 'Adiciona Membro']
	id_edit = request.vars.id_edit
	id_queue = request.vars.id_queue
	name = db(db.queue.id == id_queue).select(db.queue.name)[0].name
	db.queue_members.queue_name.default = name

	print id_queue
	print name
	print id_edit

	if id_edit is None:
		form = SQLFORM(db.queue_members)
	else:
		form = SQLFORM(db.queue_members, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	form.element(_name='queue_name')['_readonly'] = "readonly"
	#form.element(_name='interface')['_readonly'] = "readonly"
	#form.element(_name='membername')['_readonly'] = "readonly"

	if form.process().accepted:
		print 'ok'
		redirect(URL(a='admanager', c='queues', f='queue_members', 
							vars={'id_queue':request.vars.id_queue}))
	elif form.errors:
		print request.vars
		print 'no'

	return response.render("queue/form_queue_members.html", form=form)

#Popula físico na fila
def busca_fisico():
	print 'entrou'
	query1 = (db.f_ramal_virtual.ramal_virtual == request.vars['ramal'])&\
			 (db.f_ramal_virtual.tecnologia != 'QUEUE')&\
			 (db.f_ramal_virtual.tecnologia != 'FAX')
	con = db(query1).select(db.f_ramal_virtual.tecnologia, db.f_ramal_virtual.ramal_fisico, db.f_ramal_virtual.ramal_virtual)

	return con.as_json()

def f_fax():
	response.title='Fax'
	response.marca=['Extensões', 'Fax']
	editor = permissao()
	id_edit = request.vars.id_edit
	url = URL('admanager', 'queues', 'f_fax_form')
	
	con = db(db.f_fax).select()

	return response.render("queue/show_fax.html", 
						url=url, editor=editor, con=con)

def f_fax_form():
	response.title = 'Fax'
	response.marca=['Extensões', 'Fax', 'Adiciona Fax']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(db.f_fax)
	else:
		form 	=	SQLFORM(db.f_fax, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		redirect(URL('f_fax'))

	return response.render("queue/form_fax.html", form=form)

def f_local():
	response.title='Local'
	response.marca=['Extensões', 'Local']
	editor = permissao()
	url = URL('admanager', 'queues', 'f_local_form')
	
	con = db(db.f_local).select()

	return response.render("queue/show_local.html", 
						url=url, editor=editor, con=con)

def f_local_form():
	response.title = 'Local'
	response.marca=['Extensões', 'Local', 'Adiciona Local']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(db.f_local)
	else:
		form 	=	SQLFORM(db.f_local, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		redirect(URL('f_local'))

	return response.render("queue/form_local.html", form=form)

@auth.requires_login()
def delete():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']
	if funcao 	== "queue":
		tabela 	=	 db.queue.id
		funcao  = 	 'queue'
	if funcao 	== "queue_members":
		tabela 	=	 db.queue_members.uniqueid
		funcao  = 	 'queue_members'
	if funcao 	== "f_fax":
		tabela 	=	 db.f_fax.id
	if funcao 	== "f_local":
		tabela 	=	 db.f_local.id
	
	db(tabela == id_tab).delete()
	if funcao == 'queue_members':
		redirect(URL(a='admanager', c='queues', f='queue_members', 
							vars={'id_queue':request.vars.id_queue}))
	else:
		redirect(URL(funcao))



