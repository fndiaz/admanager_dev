# coding=UTF-8
import random

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def fisico_sip_iax_form():
	response.title = 'Autenticação SIP/IAX'
	response.marca=['Extensões', 'Autenticação SIP/IAX', 'Adiciona SIP/IAX']
	
	if request.vars.id_edit is None:
		form 	=	SQLFORM(db.fisico_sip_iax)
		form.element(_name='usuario')['_value'] = gera_sip_iax()
		form.element(_name='secret')['_value'] = gera_senha()
	else:
		form 	=	SQLFORM(db.fisico_sip_iax, request.vars.id_edit)
	

	for input in form.elements():
		input['_class'] = 'form-control'
	form.element(_name='extras')['_rows'] = "4"
	form.element(_name='extras')['_style'] = "width:303px"

	if form.process(onvalidation=valida_fisico_sip_iax_form).accepted:
		escreve_sip_iax()
		redirect(URL('show_sip'))

	return response.render("ramais/form_sip_iax.html", form=form)

def valida_fisico_sip_iax_form(form):
	print '-----VALIDA-----'
	print form.vars
	if form.vars.nat == 'on' or form.vars.aut_externa == 'on':
		if form.vars.usuario.isdigit():
			print 'somento numeros'
			form.errors.usuario = 'Usuário fraco'
		if form.vars.usuario.isalpha():
			print 'somente letras'
			form.errors.usuario = 'Usuário fraco'

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def fisico_tronco_form():
	response.title = 'Tronco SIP/IAX'
	response.marca=['Extensões', 'Tronco SIP/IAX', 'Adiciona Tronco SIP/IAX']
	db.fisico_sip_iax.tronco.default = True

	if request.vars.id_edit is None:
		db.fisico_sip_iax.aut_externa.default = True
		db.fisico_sip_iax.tronco.default = True
		form 	=	SQLFORM(db.fisico_sip_iax)
		form.element(_name='host_f')['_value'] = ""
	else:
		form 	=	SQLFORM(db.fisico_sip_iax, request.vars.id_edit)
	

	for input in form.elements():
		input['_class'] = 'form-control'
	form.element(_name='extras')['_rows'] = "4"
	form.element(_name='extras')['_style'] = "width:303px"
	form.element(_name='aut_externa')['_type'] = "hidden"
	form.element(_name='tronco')['_type'] = "hidden"

	if form.process().accepted:
		escreve_sip_iax()
		escreve_tronco()
		redirect(URL('show_tronco'))
	else:
		print request.vars

	return response.render("ramais/form_tronco.html", 
											form=form)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def lote_fisico_form():
	response.title = 'Lote SIP/IAX'
	response.marca=['Extensões', 'Autenticação SIP/IAX', 'Adiciona SIP/IAX', 'Lote SIP/IAX']
	form = SQLFORM.factory(
		Field('tecnologia', requires=
			IS_IN_SET(["SIP", "IAX"], error_message=T("não nulo"))),
		Field('simbolo', requires=
			IS_IN_SET(["S", "G", "-"], error_message=T("não nulo"))),
		Field('inicio', requires=[
			IS_NOT_EMPTY(error_message=T("não nulo")),
			IS_INT_IN_RANGE(1000, 9999, error_message=T("fora da range"))]),
		Field('fim', requires=[
			IS_NOT_EMPTY(error_message=T("não nulo")),
			IS_INT_IN_RANGE(1000, 9999, error_message=T("fora da range"))]),
		Field('senha'),
		Field('gerar_senha', type='boolean')
	)
	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		if insert_lote_fisico(form.vars) == False:
			response.alerta_erro = 'Erro, verifique a range'
		else:
			escreve_sip_iax()
			response.alerta_sucesso = 'Lote criado com sucesso'
		#print form.vars.inicio + 1
	elif form.errors:
		print form.vars
		#response.flash = 'erros'
		response.alerta_erro = 'Algo não está correto'
	return response.render("ramais/form_lote_fisico.html", form=form)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def fisico_dahdi_khomp_form():
	response.title = 'Canais DAHDI/KHOMP'
	response.marca=['Extensões', 'Canais DAHDI/KHOMP', 'Adiciona DAHDI/KHOMP']
	##DAHDI
	form_dahdi = SQLFORM.factory(
		Field('porta', requires=IS_NOT_IN_DB(db, 'fisico_dahdi_khomp.porta')),
		Field('context', requires=IS_NOT_EMPTY())
	)
	for input in form_dahdi.elements():
		input['_class'] = 'form-control'
	form_dahdi.element(_name='context')['_value'] = 'ramais'
	form_dahdi.element(_name='porta')['_value'] = gera_dahdi()

	##KHOMP
	form_khomp = SQLFORM.factory(
		Field('dispositivo', 
			requires=
			IS_IN_SET(["B0", "B1", 
					   "B2", "B3", 
					   "B4", "B5", 
					   "B6", "B7",
					   "B8", "B9"]),
			default=gera_khomp())
	)

	for input in form_khomp.elements():
		input['_class'] = 'form-control'

	##DAHDI
	if form_dahdi.process(formname='form_dahdi').accepted:
		insert_dahdi(request.vars)
		session.alerta_sucesso = 'criado com sucesso'
		escreve_dahdi()
		redirect(URL('fisico_dahdi_khomp_form'))
	elif form_dahdi.errors:
		response.alerta_erro = 'Erros'
		print 'dahdi error'

	##KHOMP
	if form_khomp.process(formname='form_khomp').accepted:
		if verifica_khomp(request.vars) == True:
			print 'passou'
			insert_khomp(request.vars)
			session.alerta_sucesso = 'criado com sucesso'
			redirect(URL('fisico_dahdi_khomp_form'))
		else:
			print 'nao'
			response.alerta_erro = 'Erro, verifique a range'
		#redirect(URL('fisico_dahdi_khomp_form'))
	elif form_khomp.errors:
		response.alerta_erro = 'Erros'

	return response.render("ramais/form_dahdi_khomp.html", 
		form_dahdi=form_dahdi, form_khomp=form_khomp)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def lote_dahdi_form():
	response.title = 'Lote SIP/IAX'
	form = SQLFORM.factory(
		Field('inicio', requires=[
			IS_NOT_EMPTY(error_message=T("não nulo")),
			IS_INT_IN_RANGE(1, 500, error_message=T("fora da range"))]),
		Field('fim', requires=[
			IS_NOT_EMPTY(error_message=T("não nulo")),
			IS_INT_IN_RANGE(1, 500, error_message=T("fora da range"))]),
		Field('context', requires=IS_NOT_EMPTY(), default='ramais')
	)
	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		if insert_lote_dahdi(form.vars) == False:
			response.alerta_erro = 'Erro, verifique a range'
		else:
			escreve_dahdi()
			response.alerta_sucesso = 'Lote criado com sucesso'
		print form.vars
	elif form.errors:
		print form.vars
		#response.flash = 'erros'
		response.alerta_erro = 'Algo não está correto'
	return response.render("ramais/form_lote_dahdi.html", form=form)


##Extras
def gera_senha():
	caracteres = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	tamanho = 8
	senha = ''

	for i in range(tamanho):
		next_index = random.randrange(len(caracteres))
		senha = senha + caracteres[next_index]

	return senha

#gera sip iax
def gera_sip_iax():
	n=1000
	s='S'
	var='%s%i' %(s,n)

	lista=[]
	con = db(db.fisico_sip_iax).select(db.fisico_sip_iax.usuario)
	for data in con:
		lista.append(data.usuario)

	for i in range(8999):
		if var in lista:
			n=n+1
			var='%s%i' %(s,n)
		else:
			fisico = var
			break

	return fisico

# gera lote fisico iax
@auth.requires_login() 
def insert_lote_fisico(var):
	print var
	num=var.inicio
	simb=var.simbolo
	if var.inicio > var.fim:
		return False #erro na range

	total = (var.fim - var.inicio)+1
	for i in range(total):
		fisico='%s%i' %(simb, num)
		print fisico
		if not db(db.fisico_sip_iax.usuario == str(fisico)).isempty():
			return False #ramal contem na range
		num = num + 1

	num=var.inicio
	for i in range(total):
		#if var.senha == '':
		fisico='%s%i' %(simb, num)
		db.fisico_sip_iax.insert(
			usuario=fisico,
			secret=var.senha, 
			tecnologia=var.tecnologia, 
			type_f="friend", 
			host_f="dynamic", 
			context="ramais",
			qualify=True,
			disallow=["all"],
			allow=["ulaw", "alaw", "g729"],
			nat=False,
			aut_externa=False,
			tronco=False)
		if var.gerar_senha == True:
			db(db.fisico_sip_iax.usuario==fisico).update(secret=gera_senha())
		num = num + 1



@auth.requires_login() 
def gera_dahdi():
	con = db(db.fisico_dahdi_khomp).select(db.fisico_dahdi_khomp.porta)
	lista=[]
	for data in con:
		lista.append(data.porta)

	for i in range(500):
		porta=i+1
		if str(porta) in lista:
			dahdi= 'porta:%s' %(porta)
		else:
			dahdi = porta
			break

	return str(dahdi)

@auth.requires_login() 
def insert_dahdi(var):
	db.fisico_dahdi_khomp.insert(
		tecnologia='dahdi',
		porta=var.porta,
		context=var.context)

@auth.requires_login() 
def gera_khomp():
	con = db(db.fisico_dahdi_khomp.porta.like('B%')).select(db.fisico_dahdi_khomp.porta)
	#print con
	lista=[]
	for data in con:
		lista.append(data.porta)
	#print lista
	for i in range(10):
		porta='B%sC1' %(i)
		#print porta
		if porta in lista:
			print 'porta existe:%s' %(porta)
		else:
			#print 'porta não existe:%s' %(porta)
			khomp=porta[0] + porta[1]
			break

	return str(khomp)

@auth.requires_login() 
def insert_khomp(var):
	for i in range(24):
		porta=i+1
		#print '%sc%s' %(var.dispositivo,porta)
		db.fisico_dahdi_khomp.insert(
			tecnologia='khomp',
			porta='%sC%s' %(var.dispositivo,porta),
			context=var.context)

@auth.requires_login()
def verifica_khomp(var):
	con = db(db.fisico_dahdi_khomp.porta.like('B%')).select(db.fisico_dahdi_khomp.porta)
	lista=[]
	for data in con:
		lista.append(data.porta)

	if '%sC1' %(var.dispositivo) in lista:
		return False
	else:
		return True

@auth.requires_login()
def insert_lote_dahdi(var):
	inicio=var.inicio
	fim=var.fim
	if inicio > fim:
		return False #erro na range

	total = (fim - inicio)+1
	for i in range(total):
		if not db(db.fisico_dahdi_khomp.porta == str(inicio)).isempty():
			return False #ramal contem na range
		inicio = inicio + 1

	inicio=var.inicio
	for i in range(total):
		db.fisico_dahdi_khomp.insert(
			tecnologia='dahdi',
			porta=inicio,
			context=var.context)
		inicio = inicio + 1

@auth.requires_login()
def escreve_dahdi():
	ramais = db(db.fisico_dahdi_khomp.tecnologia == 'dahdi').select(orderby=db.fisico_dahdi_khomp.porta)
	dahdi = open('/aldeia/etc/asterisk/confs/chan_dahdi_admanager.conf','w')
	for ramal in ramais:
		print ramal.porta
		dahdi.write('signalling=fxo_ks\n')
		dahdi.write('context=%s\n' %(ramal.context))
		dahdi.write('faxdetect=both\n')
		dahdi.write('faxbuffers=>6,full\n')
		dahdi.write('channel=>%s\n\n' %(ramal.porta))

	dahdi.close()
	commands.getoutput("sudo asterisk -rx 'module reload chan_dahdi.so'")

@auth.requires_login()
def escreve_tronco():
	troncos = db(db.fisico_sip_iax.tronco == True).select(orderby=db.fisico_sip_iax.usuario)
	arq_sip = open('/aldeia/etc/asterisk/confs/sip_trunk_admanager.conf','w')
	arq_iax = open('/aldeia/etc/asterisk/confs/iax_trunk_admanager.conf','w')
	for tronco in troncos:
		if tronco.register == True:
			if tronco.tecnologia == 'SIP':
				arq_sip.write('register=> %s:%s@%s/%s\n' 
				%(tronco.usuario, tronco.secret, tronco.host_f, tronco.usuario))
			if (tronco.tecnologia == 'IAX') or (tronco.tecnologia == 'IAX2'):
				arq_iax.write('register=> %s:%s@%s\n' 
				%(tronco.usuario, tronco.secret, tronco.host_f))
	arq_sip.close()
	arq_iax.close()
	commands.getoutput("sudo asterisk -rx 'module reload chan_sip.so'")
	commands.getoutput("sudo asterisk -rx 'module reload chan_iax2.so'")


#SHOW
@auth.requires_login()
def show_sip():
	response.title = 'Usuários SIP/IAX'
	response.marca=['Extensões', 'Autenticação SIP/IAX']
	editor 	= 	permissao()
	url 	=	URL('admanager', 'ramais', 'fisico_sip_iax_form')
	query 	= 	(db.fisico_sip_iax.tronco != True)
	con = db(query).select()

	return response.render("ramais/show_sip.html", 
					con=con, url=url, editor=editor)

@auth.requires_login()
def show_tronco():
	response.title = 'Troncos SIP/IAX'
	response.marca=['Extensões', 'Troncos SIP/IAX']
	editor 	= 	permissao()
	url 	=	URL('admanager', 'ramais', 'fisico_tronco_form')
	query = (db.fisico_sip_iax.tronco == True)
	con = db(query).select()

	return response.render("ramais/show_tronco.html", 
						con=con, url=url, editor=editor)

@auth.requires_login()
def show_dahdi():
	response.title = 'Portas DAHDI'
	response.marca=['Extensões', 'Canais DAHDI/KHOMP']
	editor 	=	permissao()
	url 	= 	URL('admanager', 'ramais', 'fisico_dahdi_khomp_form')
	con = db(db.fisico_dahdi_khomp.tecnologia == 'dahdi').select()
	con2 = db(db.fisico_dahdi_khomp.tecnologia == 'khomp').select(orderby=db.fisico_dahdi_khomp.porta)

	return response.render("ramais/show_dahdi.html",
				con2=con2, con=con, url=url, editor=editor)

@auth.requires_login()
def delete():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']
	if funcao 	== "fisico_sip_iax":
		tabela 	=	 db.fisico_sip_iax.id
		funcao  = 	 'show_sip'
	if funcao 	== "fisico_tronco":
		tabela 	=	 db.fisico_sip_iax.id
		funcao  = 	 'show_tronco'
	if funcao 	== "fisico_dahdi_khomp":
		tabela 	= 	db.fisico_dahdi_khomp.id
		funcao 	= 	'show_dahdi'

	db(tabela == id_tab).delete()
	if (funcao == 'show_sip') or (funcao == 'show_tronco'):
		escreve_sip_iax()
		escreve_tronco()
	elif funcao == 'show_dahdi':
		escreve_dahdi()
	redirect(URL(funcao))

@auth.requires_login()
def delete_khomp():
	dispositivo = request.vars.porta.split('C')[0]
	for i in range(24):
		porta=i+1
		print 'delete %sC%s' %(dispositivo,porta)
		var = '%sC%s' %(dispositivo,porta)
		db(db.fisico_dahdi_khomp.porta == var).delete()	
	
	redirect(URL('show_dahdi'))



