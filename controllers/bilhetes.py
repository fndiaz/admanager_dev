# coding=UTF-8

@auth.requires_login()
def busca_chamadas():
	response.title = 'Bilhetes'
	response.marca=['Bilhetes']

	form = SQLFORM.factory(
		Field("origem"),
		Field("destino"),
		Field("data_inicio"),
		Field("data_fim"),
		Field("tipo", requires=IS_IN_SET(['Saintes', 'Entrantes', 'Ramais']))
	)
	for input in form.elements():
		input['_class'] = 'form-control'
	form.element(_name='data_inicio')['_class'] = "date form-control"
	form.element(_name='data_fim')['_class'] = "date form-control"
	form.element(_name='data_inicio')['_autocomplete'] = "off"
	form.element(_name='data_fim')['_autocomplete'] = "off"

	if form.process().accepted:
		response.flash=''
		query=query_monta(request.vars)
		con = db(query).select()
		#return con 
		return response.render("bilhetes/show_buscas.html", con=con)
	else:
		print request.vars

	return response.render("bilhetes/busca_saintes.html", form=form)


def query_monta(dado):
	print 'Monta query saintes'
	id_user = session.auth.user.id
	query_dept=''
		
	query = (db.f_bilhetes_chamadas.origem.like ('%'+dado.origem+'%'))&\
			(db.f_bilhetes_chamadas.destino.like ('%'+dado.destino+'%'))&\
	((db.f_bilhetes_chamadas.horario >= dado.data_inicio) 
		& (db.f_bilhetes_chamadas.horario <= dado.data_fim))

	if dado.tipo == 'Saintes':
		query=query & (db.f_bilhetes_chamadas.id_destino > 0)
	if dado.tipo == 'Entrantes':
		query=query & (db.f_bilhetes_chamadas.id_destino == -1)
	if dado.tipo == 'Ramais':
		query=query & (db.f_bilhetes_chamadas.id_destino == 0)

	##Adiciona query por departamento
 	depta=db(db.f_departamentos).select(db.f_departamentos.departamento)
	for dept in depta:
		dept_nome = 'dept_%s' %(dept.departamento)
	
		if (auth.has_membership(dept_nome) or auth.has_membership('administrador')) :
			if query_dept == '':
				query_dept=(db.f_bilhetes_chamadas.departamento == dept.departamento) |\
							(db.f_bilhetes_chamadas.departamento == '')
			else:
				query_dept=query_dept | (db.f_bilhetes_chamadas.departamento == dept.departamento)



	#print query
	#print query_dept
	query=query & query_dept
	print query
	return query


def link_player():
	print request.vars
	date = request.vars.date
	linked_id = request.vars.linked_id
	arq = request.vars.arq

	date = date.split(' ')[0]
	datef=''

	for i in range(0,3):
		dt = date.split('-')[i]
		datef = datef + dt
		i=i+1

	if request.vars.link == 'player':	
		if request.is_local:
			redirect(("http://127.0.0.1/wavplayer/index.php?audio=GRAVACOES/"+ datef +"/"+ arq +".WAV"))
		else:
			redirect(("http://"+ request.env.server_addr +"/wavplayer/index.php?audio=GRAVACOES/"+ datef +"/"+ arq +".WAV"))
		#***TROCAR por request.env.server_addr****
	elif request.vars.link == 'down':
		if request.is_local:
			redirect(("http://127.0.0.1/download_audio.php/?diretorio="+ datef +"&arquivo="+ arq +".WAV"))
		else:
			redirect(("http://"+ request.env.server_addr +"/download_audio.php/?diretorio="+ datef +"&arquivo="+ arq +".WAV"))
		#***TROCAR por request.env.server_addr****