# coding=UTF-8

######-Usuários
@auth.requires_login()
def f_usuarios():
	response.title = 'Usuários'
	response.marca=['PréPago', 'Usuários']
	editor 	= 	permissao()
	url 	=	URL('admanager', 'prepago', 'f_usuarios_form')
	query = (db.f_usuarios.id_departamento == db.f_departamentos.id)&\
			(db.f_usuarios.id_grupo_destinos == db.f_grupo_destinos.id)
	con = db(query).select()
	
	return response.render("prepago/show_usuarios.html", 
					editor=editor, url=url, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_usuarios_form():
	response.title = 'Usuários'
	id_edit = request.vars['id_edit']

	if id_edit is None:
		form 	=	SQLFORM(db.f_usuarios)
	else:
		form 	=	SQLFORM(db.f_usuarios, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		redirect(URL('f_usuarios'))

	return response.render("prepago/form_usuarios.html", form=form)


@auth.requires_login() 
def show_saldos():
	response.marca=['PréPago', 'Consultar Saldo']
	response.title = 'Consultar Saldo'
	usr=''
	form = SQLFORM.factory(
		Field('usuario', requires=
			IS_IN_DB(db(db.f_usuarios.credito == True),'f_usuarios.nome',"%(nome)s")
		)
	)
	for input in form.elements():
		input['_class'] = 'form-control'

	saldo, porcent, credito = calcula_saldo(request.vars.usr)
	print saldo
	print porcent
	print credito

	if request.vars.usr != None:
		query = (Usuariospp.nome == request.vars.usr)&\
		 (Usuariospp.id_departamento == Departamentos.id)&\
		 (Usuariospp.id_grupo_destinos == Grupo_destinos.id)

		usr=db(query).select()[0]
		print usr

	if form.process().accepted:
		print request.vars
		redirect(URL(vars={'usr':form.vars.usuario}))

	return response.render("prepago/show_saldos.html", form=form, 
			usr=usr, saldo=saldo, porcent=porcent, credito=credito)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_creditos_form():
	response.title = 'Créditos Automatizados'
	response.marca=['PréPago', 'Créditos Automatizados']
	editor 	= 	permissao()
	url 	=	URL('admanager', 'prepago', 'f_creditos_form')
	id_edit = request.vars['id_edit']

	if id_edit is None:
		form 	=	SQLFORM(db.f_creditos)
	else:
		form 	=	SQLFORM(db.f_creditos, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	form.element(_name='local_fixo')['_style'] = "width:100px; height:30px"
	form.custom.widget.local_celular['_style'] = "width:100px; height:30px"
	form.custom.widget.ddd_fixo['_style'] = "width:100px; height:30px"
	form.custom.widget.ddd_celular['_style'] = "width:100px; height:30px"
	form.custom.widget.ddi['_style'] = "width:100px; height:30px"
	form.custom.widget.f0300['_style'] = "width:100px; height:30px"
	form.custom.widget.id_departamento['_style'] = "width:200px; height:30px"

	if form.process(hideerror=True).accepted:
		redirect(URL('f_creditos_form'))

	con = db(Creditos.id_departamento == Departamentos.id).select(orderby=Creditos.id)

	return response.render("prepago/form_creditos.html", 
				editor=editor, url=url, con=con, form=form)

@auth.requires_login() 
def creditos_manual():
	dict_insert = {}
	form = SQLFORM.factory(
		Field('usuario', requires=
			IS_IN_DB(db(db.f_usuarios.credito == True),'f_usuarios.nome',"%(nome)s")),
		Field('local_fixo', requires=IS_INT_IN_RANGE(0,900000)),
		Field('local_celular', requires=IS_INT_IN_RANGE(0,900000)),
		Field('ddd_fixo', requires=IS_INT_IN_RANGE(0,900000)),
		Field('ddd_celular', requires=IS_INT_IN_RANGE(0,900000)),
		Field('ddi', requires=IS_INT_IN_RANGE(0,900000)),
		Field('f0300', requires=IS_INT_IN_RANGE(0,900000)),
		)
	for input in form.elements():
		input['_class'] = 'form-control'
	form.custom.widget.local_fixo['_style'] = "width:100px; height:30px"
	form.custom.widget.local_celular['_style'] = "width:100px; height:30px"
	form.custom.widget.ddd_fixo['_style'] = "width:100px; height:30px"
	form.custom.widget.ddd_celular['_style'] = "width:100px; height:30px"
	form.custom.widget.ddi['_style'] = "width:100px; height:30px"
	form.custom.widget.f0300['_style'] = "width:100px; height:30px"
	form.custom.widget.usuario['_style'] = "width:200px; height:30px"

	if form.process(hideerror=True).accepted:
		dict_insert = insere_manual(request.vars)
		return response.render("prepago/form_creditos_manual.html", 
									dict_insert=dict_insert, form=form)

	return response.render("prepago/form_creditos_manual.html", 
									dict_insert=dict_insert, form=form)


###-EXTRAS
def insere_manual(dados):
	date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	email=session.auth.user.email
	dict_insert = {}

	if dados.local_fixo is not '0':
		Saldos.insert(responsavel=dados.usuario, tipo_origem='U', datahora=date,
		tempo=int(dados.local_fixo), uniqueid=email, tipo='C', tipo_chamada='LOCAL_FIXO')
		dict_insert['local_fixo'] = dados.local_fixo
	if dados.local_celular is not '0':
		Saldos.insert(responsavel=dados.usuario, tipo_origem='U', datahora=date,
		tempo=int(dados.local_celular), uniqueid=email, tipo='C', tipo_chamada='LOCAL_CELULAR')
		dict_insert['local_celular'] = dados.local_celular
	if dados.ddd_fixo is not '0':
		Saldos.insert(responsavel=dados.usuario, tipo_origem='U', datahora=date,
		tempo=int(dados.ddd_fixo), uniqueid=email, tipo='C', tipo_chamada='DDD_FIXO')
		dict_insert['ddd_fixo'] = dados.ddd_fixo
	if dados.ddd_celular is not '0':
		Saldos.insert(responsavel=dados.usuario, tipo_origem='U', datahora=date,
		tempo=int(dados.ddd_celular), uniqueid=email, tipo='C', tipo_chamada='DDD_CELULAR')
		dict_insert['ddd_celular'] = dados.ddd_celular
	if dados.ddi is not '0':
		Saldos.insert(responsavel=dados.usuario, tipo_origem='U', datahora=date,
		tempo=int(dados.ddi), uniqueid=email, tipo='C', tipo_chamada='DDI')
		dict_insert['ddi'] = dados.ddi
	if dados.f0300 is not '0':
		Saldos.insert(responsavel=dados.usuario, tipo_origem='U', datahora=date,
		tempo=int(dados.f0300), uniqueid=email, tipo='C', tipo_chamada='0300')
		dict_insert['f0300'] = dados.f0300
	return dict_insert


def calcula_data():
	dict_date = {}
	date_now = datetime.now()
	dict_date['date_now'] = date_now
	dia = date_now.day

	if not db(Parametros.credito_dia != "").isempty():
		dia_c=db(Parametros).select(Parametros.credito_dia)[0].credito_dia

		if dia < int(dia_c):
			date_x = date_now.replace(day=int(dia_c), hour=00, minute=00, second=00)
			tm_date_x = time.mktime(date_x.timetuple())
			tm_date_ant = tm_date_x-(30*86400)
			date_ant = datetime.fromtimestamp(tm_date_ant)
			dict_date['date_ant'] = date_ant
			return dict_date
		else:
			date_ant = date_now.replace(day=int(dia_c), hour=00, minute=00, second=00)
			dict_date['date_ant'] = date_ant
			return dict_date

def calcula_saldo(usr):
	dict_credito = {}
	dict_saldo = {}
	dict_porcent = {}
	date=calcula_data()
	#TIRAR REPLACE--------------------------------------*****
	date_ant = date['date_ant'].replace(month=07).strftime("%Y-%m-%d %H:%M:%S")
	date_now = date['date_now'].replace(month=07).strftime("%Y-%m-%d %H:%M:%S")
	query = (Saldos.responsavel == usr)&\
			(Saldos.datahora > date_ant)&\
			(Saldos.datahora < date_now)
	query_c = query & (Saldos.tipo == 'C')
	query_d = query & (Saldos.tipo == 'D')
	
	soma = Saldos.tempo.sum()
	print db(query_c).select(Saldos.tipo_chamada, soma, groupby=Saldos.tipo_chamada)

	lista=['local_fixo', 'local_celular', 
		   'ddd_fixo',   'ddd_celular', 
		   'ddi',        '0300']
	for dado in lista:
		print '------%s-------' %(dado)

		if db(query_c & (Saldos.tipo_chamada == dado.upper() )).isempty():
			print '%s-vazio' %(dado)
			dict_saldo[dado] = 0
			dict_porcent[dado] = -1
			dict_credito[dado] = 0
		else:
			#Credito
			cred=db(query_c & (Saldos.tipo_chamada == dado.upper() ))\
				.select(Saldos.tipo_chamada, soma, groupby=Saldos.tipo_chamada)
			for c in cred:
				credito = c._extra['SUM(f_saldos.tempo)']
				print '%s-credito' %(credito)

			#Debito
			if db(query_d & (Saldos.tipo_chamada == dado.upper() )).isempty():
				print '0-debito' 
				debito = 0
			else:
				deb=db(query_d & (Saldos.tipo_chamada == dado.upper() ))\
					.select(Saldos.tipo_chamada, soma, groupby=Saldos.tipo_chamada)
				for d in deb:
					debito = d._extra['SUM(f_saldos.tempo)']
					print '%s-debito' %(debito)
			#Saldo
			saldo=int(credito) - int(debito)
			porcent= (100*int(debito))/int(credito)
			print '%s-saldo' %(saldo)
			print '%s-Porcentagem' %(porcent)
			dict_credito[dado] = int(credito)
			dict_saldo[dado] = saldo
			dict_porcent[dado] = porcent

	return dict_saldo, dict_porcent, dict_credito

@auth.requires_login()
def delete():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']
	if funcao 	== "f_creditos":
		tabela 	=	 db.f_creditos.id
		funcao  = 	 'f_creditos_form'

	db(tabela == id_tab).delete()
	redirect(URL(funcao))




