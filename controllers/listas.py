######-CallBack
@auth.requires_login()
def f_callback():
	response.title = 'CallBack'
	response.marca=['Extensões', 'CallBack']
	editor = permissao()
	url = URL('admanager', 'listas', 'f_callback_form')

	con = db(Callback).select(orderby=Callback.id)
	
	return response.render("listas/show_callback.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_callback_form():
	response.title = 'CallBack'
	response.marca=['Extensões', 'CallBack', 'Adiciona CallBack']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(Callback)
	else:
		form 	=	SQLFORM(Callback, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	form.custom.widget.numero['_placeholder'] = "exemplo: 01699999999"

	if form.process().accepted:
		redirect(URL('f_callback'))

	return response.render("listas/form_callback.html", form=form)

@auth.requires_login()
def delete():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']

	if funcao	== "f_callback":
		tabela 	=	Callback.id
		funcao	= 	"f_callback"

	db(tabela == id_tab).delete()
	redirect(URL(funcao))