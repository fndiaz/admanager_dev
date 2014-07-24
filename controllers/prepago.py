# coding=UTF-8

######-Usuários
@auth.requires_login()
def f_usuarios():
	response.title = 'Usuários'
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