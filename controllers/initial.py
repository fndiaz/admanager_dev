# coding=UTF-8
from datetime import datetime
import platform
import urllib2
#import urllib
#import requests
import cookielib
from xml.etree.ElementTree import ElementTree

def principal():
	redirect(URL(dashboard))

@auth.requires_login()
def dashboard():
	response.title = 'Principal'
	server = get_server()

	print db(db.auth_user.first_name == session.auth.user.first_name).select(db.auth_user.photo)

	#Ultimas chamadas
	query = (db.f_bilhetes_chamadas.status == 'ANSWER')|\
			(db.f_bilhetes_chamadas.status == 'CONTINUE')|\
			(db.f_bilhetes_chamadas.status == 'BUSY')|\
			(db.f_bilhetes_chamadas.status == 'NOANSWER')
	con = db(query).select(orderby=~db.f_bilhetes_chamadas.id,limitby=(0,8))

	##Chamadas de Hoje
	dict_ch_hoje = {}
	query_res = monta_query()

	ch_entrante = db(query_res['query_entrante']).select(db.f_bilhetes_chamadas.linked_id ,groupby=db.f_bilhetes_chamadas.linked_id)
	ch_sainte = db(query_res['query_sainte']).select(db.f_bilhetes_chamadas.linked_id ,groupby=db.f_bilhetes_chamadas.linked_id)
	ch_ramal = db(query_res['query_ramal']).select(db.f_bilhetes_chamadas.linked_id ,groupby=db.f_bilhetes_chamadas.linked_id)
	ch_local_fixo = db(query_res['query_localfixo']).select(db.f_bilhetes_chamadas.linked_id ,groupby=db.f_bilhetes_chamadas.linked_id)
	ch_local_celular = db(query_res['query_localcelular']).select(db.f_bilhetes_chamadas.linked_id ,groupby=db.f_bilhetes_chamadas.linked_id)
	ch_ddd_fixo = db(query_res['query_dddfixo']).select(db.f_bilhetes_chamadas.linked_id ,groupby=db.f_bilhetes_chamadas.linked_id)
	ch_ddd_celular = db(query_res['query_dddcelular']).select(db.f_bilhetes_chamadas.linked_id ,groupby=db.f_bilhetes_chamadas.linked_id)
	ch_0800 = db(query_res['query_0800']).select(db.f_bilhetes_chamadas.linked_id ,groupby=db.f_bilhetes_chamadas.linked_id)
	dict_ch_hoje['ch_entrante'] = len(ch_entrante.as_list())
	dict_ch_hoje['ch_sainte'] = len(ch_sainte.as_list())
	dict_ch_hoje['ch_ramal'] = len(ch_ramal.as_list())
	dict_ch_hoje['ch_localfixo'] = len(ch_local_fixo.as_list())
	dict_ch_hoje['ch_localcelular'] = len(ch_local_celular.as_list())
	dict_ch_hoje['ch_dddfixo'] = len(ch_ddd_fixo.as_list())
	dict_ch_hoje['ch_dddcelular'] = len(ch_ddd_celular.as_list())
	dict_ch_hoje['ch_0800'] = len(ch_0800.as_list())
	
	return response.render("initial/principal.html", server=server, con=con,
			dict_ch_hoje=dict_ch_hoje)

def monta_query():
	date = datetime.now()
	date = date.strftime("%Y-%m-%d")
	ano= date.split('-')[0]
	mes= date.split('-')[1]
	dia= date.split('-')[2]
	#mes = session.data_hoje.split('-')[1]
	dict_query = {}
	query_padrao = (db.f_bilhetes_chamadas.horario.year()==ano)&\
		   		   (db.f_bilhetes_chamadas.horario.month()==mes)&\
		            (db.f_bilhetes_chamadas.horario.day()==dia)

	dict_query['query_entrante']= query_padrao &\
								  (db.f_bilhetes_chamadas.id_destino == -1)
	dict_query['query_sainte']= query_padrao &\
								  (db.f_bilhetes_chamadas.id_destino > 0)
	dict_query['query_ramal']= query_padrao &\
								  (db.f_bilhetes_chamadas.id_destino == 0)
	id_destino = get_id_destino()
	dict_query['query_localfixo']= query_padrao &\
								  (db.f_bilhetes_chamadas.id_destino == id_destino['id_localfixo'])
	dict_query['query_localcelular']= query_padrao &\
								  (db.f_bilhetes_chamadas.id_destino == id_destino['id_localcelular'])
	dict_query['query_dddfixo']= query_padrao &\
								  (db.f_bilhetes_chamadas.id_destino == id_destino['id_dddfixo'])
	dict_query['query_dddcelular']= query_padrao &\
								  (db.f_bilhetes_chamadas.id_destino == id_destino['id_dddcelular1'])&\
								  (db.f_bilhetes_chamadas.id_destino == id_destino['id_dddcelular2'])
								  #(db.f_bilhetes_chamadas.id_destino == id_destino['id_dddcelular3'])
	dict_query['query_0800']= query_padrao &\
								  (db.f_bilhetes_chamadas.id_destino == id_destino['id_0800'])

	return dict_query


def get_id_destino():
	dict_id_dest = {}
	id_localfixo = db(db.f_destinos.tipo_chamada == 'LOCAL_FIXO').select(db.f_destinos.id)
	dict_id_dest['id_localfixo'] = id_localfixo[0].id
	
	id_localcelular = db(db.f_destinos.tipo_chamada == 'LOCAL_CELULAR').select(db.f_destinos.id)
	dict_id_dest['id_localcelular'] = id_localcelular[0].id

	id_dddfixo = db(db.f_destinos.tipo_chamada == 'DDD_FIXO').select(db.f_destinos.id)
	dict_id_dest['id_dddfixo'] = id_dddfixo[0].id

	id_0800 = db(db.f_destinos.tipo_chamada == '0800').select(db.f_destinos.id)
	dict_id_dest['id_0800'] = id_0800[0].id

	id_dddcelular = db(db.f_destinos.tipo_chamada == 'DDD_CELULAR').select(db.f_destinos.id)
	i=1
	n='id_dddcelular'
	for dest in id_dddcelular:
		nome=n+str(i)
		dict_id_dest[nome] = dest.id
		i=i+1
	print dict_id_dest 

	return dict_id_dest

def get_server():
	server = {}
	var = platform.platform()
	server['distribuicao'] = var.split('-')[6]
	server['versao'] = var.split('-')[7]
	server['arch'] = platform.processor()
	server['host'] =  platform.uname()[1]
	server['kernel'] =  platform.uname()[2]
	server['pythonv'] = platform.python_version()
	server['postgresql'] = commands.getoutput("psql --version")
	server['memory'] = int(commands.getoutput("cat /proc/meminfo | grep MemTotal").split(':')[1].split('k')[0])/1000
	disk = os.statvfs("/")
	totalBytes = float(disk.f_bsize*disk.f_blocks)
	server['disk'] = "%.2f GBytes" % (totalBytes/1024/1024/1024)

	#var = commands.getoutput("atop | grep cpu")
	print var
	return server

def gera_teste():
#	cj = cookielib.CookieJar()
#	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#	opener.open("http://192.168.100.253:8088/asterisk/mxml?action=login&username=python&secret=123456")
#
#	tree = ElementTree(file=opener.open('http://192.168.100.253:8088/asterisk/mxml?action=CoreShowChannels'))
	lista=[]
#	r = tree.getroot()
#	a=True
#	for child in r:
#		print child
#			if a == True:
#				print var.attrib['message']
#				a = False
#			else:
#				if var.attrib['event'] == 'CoreShowChannel':
#					print var.attrib['channel']
#				elif var.attrib['event'] == 'CoreShowChannelsComplete':
#					print 'fim'
#					total = var.attrib['listitems']
#					print total
	ch= '1'
	total='1'
	if not request.is_local:
		ch=commands.getoutput("sudo asterisk -rx 'core show channels' | grep 'active call' | awk '{print $1}'")
		total=commands.getoutput("sudo asterisk -rx 'core show channels' | grep 'active channel' | awk '{print $1}'")
	lista.append(total)
	lista.append(ch)

	return response.json(lista)

def get_chart():
	date = datetime.now()
	date = date.strftime("%Y-%m-%d")
	ano= date.split('-')[0]
	mes= date.split('-')[1]
	dia= date.split('-')[2]
	if request.is_local:
		ano=2014
		mes=05

	count = db.f_bilhetes_chamadas.origem.count()
	query = (db.f_bilhetes_chamadas.horario.year()==ano)&\
		   	(db.f_bilhetes_chamadas.horario.month()==mes)&\
		   	(db.f_bilhetes_chamadas.id_destino > 1)
	result = db(query).select(db.f_bilhetes_chamadas.origem, count, 
						groupby=db.f_bilhetes_chamadas.origem, orderby=~count, limitby=(0, 5))
	lista=[]
	for dado in result:
		if len(lista) == 0:
			lista.append(['Ramal', 'chamadas'])	
		lista.append([dado.f_bilhetes_chamadas['origem'], dado._extra['COUNT(f_bilhetes_chamadas.origem)']])
	print lista

	#formato
	#var =[
    #      ['Ramal', 'Chamadas'],
    #      ['8001',  1000],
    #      ['8050',  1170]]
	return response.json(lista)



##--Parte de Login e Usuários--##
def user():
	#	#if request.args(0) == 'register':
	#  	db.auth_user.bio.writable = db.auth_user.bio.readable = False
	print 'user'
	print request.args(0)
	if request.args(0) == 'not_authorized':
		redirect (URL('initial', 'not_authorized'))

	if request.args(0) == 'login':
		redirect(URL('initial', 'login'))
	return response.render("initial/user.html", user=auth())

def register():
	form = auth.register()
	form.element(_name='email')['_class'] = "form-control"
	form.element(_name='first_name')['_class'] = "form-control"
	form.element(_name='last_name')['_class'] = "form-control"
	form.element(_name='password')['_class'] = "form-control"
	form.element(_name='password_two')['_class'] = "form-control"

	return response.render("initial/register.html", form=form)

def profile():
	response.title = 'Profile'
	form = auth.profile()
	form.element(_name='email')['_class'] = "form-control"
	form.element(_name='first_name')['_class'] = "form-control"
	form.element(_name='last_name')['_class'] = "form-control"

	return response.render("initial/profile.html", form=form)

def not_authorized():
	return response.render("initial/not_authorized.html")

def change_password():
	response.title = 'Alterar Senha'
	form = auth.change_password()
	form.element(_name='old_password')['_class'] = "form-control"
	form.element(_name='new_password')['_class'] = "form-control"
	form.element(_name='new_password2')['_class'] = "form-control"

	return response.render("initial/change_password.html", form=form)

def request_reset_password():
	form = auth.request_reset_password()
	form.element(_name='email')['_class'] = "form-control"

	return response.render("initial/request_reset_password.html", form=form)

def login():
	print 'login'
	form = auth.login()
	form.element(_name='email')['_class'] = "form-control"
	form.element(_name='password')['_class'] = "form-control"

	return response.render("initial/login.html", form=form)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def users():
	response.title = 'Usuários'
	response.marca=['Acessos', 'Usuários']
	#grid 	= SQLFORM.grid(db.auth_user, user_signature=False, _class="dataTables_wrapper form-inline")
	editor = permissao()
	usuarios= db(db.auth_user.first_name != 'root').select()
	logger.debug("acesso a usuarios")
	
	return response.render("initial/show_usuarios.html", 
						editor=editor, usuarios=usuarios)

def form_users():
	response.title = 'Usuários'
	response.marca=['Acessos', 'Usuários', ' Adiciona Usuário']
	id_usuario = request.vars['id_usuario']
	
	if id_usuario is None:
		form 	=	SQLFORM(db.auth_user,  
				submit_button='Adicionar')
	else:
		form 	=	SQLFORM(db.auth_user, id_usuario, 
								submit_button='Editar')

	form.element(_name='first_name')['_class'] = "form-control"
	form.element(_name='last_name')['_class'] = "form-control"
	form.element(_name='email')['_class'] = "form-control"
	form.element(_name='ramal')['_class'] = "form-control"
	form.element(_name='password')['_class'] = "form-control"

	if form.process().accepted:
		nome = request.vars['first_name']
		id_user = db(db.auth_user.first_name == nome).select(db.auth_user.id)
		redirect(URL(a='admanager', c='initial', f='f_permissao_menu_form', 
										vars=dict(id_usuario=id_user[0].id)))

	return response.render("initial/form_usuarios.html", 
													form=form)

def groups():
    grid = SQLFORM.grid(db.auth_group)
    return response.render("initial/show_grid.html", grid=grid)

def membership():
    grid = SQLFORM.grid(db.auth_membership)
    return response.render("initial/show_grid.html", grid=grid)

def log():
	#form = auth.user
	response.title = 'Comunicação com o Opera'

	return response.render("initial/log.html")
	
def download():
	return response.download(request, db)


##--Parte de Menus e Submenus--##
@auth.requires_login()
def f_menu():
	print monta_query()
	response.title = 'Menu'
	editor 	= 	permissao()
	menu 	= 	db(db.f_menu).select()

	return response.render("initial/show_menu.html", 
							editor=editor, menu=menu)

@auth.requires_login()
def f_menu_form():
	response.title 	= 	'Menu'
	id_menu			= 	request.vars['id_menu']
	testa 			=	True
	
	if id_menu is None:
		form 	=	SQLFORM(db.f_menu,  
				submit_button='Adicionar')
	else:
		testa 	= 	False
		form 	=	SQLFORM(db.f_menu, id_menu, 
								submit_button='Editar')
		form.element(_name='nome')['_readonly'] = "readonly"

	form.element(_name='nome')['_class'] = "form-control"
	form.element(_name='icone')['_class'] = "form-control"
	form.element(_name='funcao')['_class'] = "form-control"
	form.element(_name='controller')['_class'] = "form-control"
	form.element(_name='ordem')['_class'] = "form-control"
	form.element(_name='submenu')['_class'] = "form-control"
	
	if form.process().accepted:
		if testa == True: 
			auth.add_group(request.vars['nome'], '')
		redirect(URL('f_menu'))

	return response.render("initial/form_menu.html", form=form)

@auth.requires_login()
def f_submenu():
	response.title = 'Submenu'
	editor 	= 	permissao()
	query 	= 	(db.f_menu.id == db.f_submenu.menu_ref)
	var	= 	db(query).select(orderby=db.f_submenu.menu_ref)

	return response.render("initial/show_submenu.html", 
								editor=editor, var=var)

@auth.requires_login()
def f_submenu_form():
	response.title 	= 	'Submenu'
	id_submenu		= 	request.vars['id_submenu']
	testa 			= 	True
	
	if id_submenu is None:
		form 	=	SQLFORM(db.f_submenu,  
				submit_button='Adicionar')
	else:
		testa 	=	False
		form 	=	SQLFORM(db.f_submenu, id_submenu, 
								submit_button='Editar')
		form.element(_name='nome')['_readonly'] = "readonly"

	form.element(_name='nome')['_class'] = "form-control"
	form.element(_name='menu_ref')['_class'] = "form-control"
	form.element(_name='icone')['_class'] = "form-control"
	form.element(_name='controller')['_class'] = "form-control"
	form.element(_name='funcao')['_class'] = "form-control"
	form.element(_name='ordem')['_class'] = "form-control"
	
	if form.process().accepted:
		if testa == True: 
			auth.add_group(request.vars['nome'], '')
		redirect(URL('f_submenu'))

	return response.render("initial/form_submenu.html", form=form)

@auth.requires_login()
def f_permissao_menu_form():
	response.title = 'Permissao menu'
	response.marca = ['Acessos', 'Usuários', ' Permissões']
	id_usuario = request.vars['id_usuario']
	check_ger = ""
	check_grav = ""

	if auth.has_membership('gerenciador', id_usuario):
		check_ger = "checked"

	if auth.has_membership('gravacao_perm', id_usuario):
		check_grav = "checked"

	return response.render("initial/form_permissao_menu.html",
		id_usuario=id_usuario, check_ger=check_ger, check_grav=check_grav)

@auth.requires_login()
def insert_permissao_menu():
	print request.vars
	id_usuario = request.vars['id_usuario']

	if request.vars.gerenciador == 'on':
		print 'adicionando gerenciador'
		auth.add_membership(auth.id_group('gerenciador'), id_usuario)
		auth.del_membership(auth.id_group('comum'), id_usuario)
	else:
		print 'del gerenciador'
		auth.del_membership(auth.id_group('gerenciador'), id_usuario)
		auth.add_membership(auth.id_group('comum'), id_usuario)

	if request.vars.gravacao_perm == 'on':
		print 'adicionando gravacao_perm'
		auth.add_membership(auth.id_group('gravacao_perm'), id_usuario)
	else:
		print 'del gravacao_perm'
		auth.del_membership(auth.id_group('gravacao_perm'), id_usuario)

	menu 	= 	db(db.f_menu).select()
	##Faz o loop retornando menus
	for dado in menu:
		query = (db.auth_group.role == dado.nome)
		id_grupo = db(query).select()
		id_grupo = id_grupo[0].id
		print id_grupo

		##verifica se menu está ticado e adiciona no membership
		var = request.vars['%s' %(dado.nome)]
		if var == 'on':
			auth.add_membership(id_grupo, id_usuario)
		else:
			auth.del_membership(id_grupo, id_usuario)

	##Faz o loop retornando submenus
	submenu = 	db(db.f_submenu).select()
	for dado in submenu:
		query = (db.auth_group.role == dado.nome)
		id_grupo = db(query).select()
		id_grupo = id_grupo[0].id
		#print id_grupo

		##verifica se submenu está ticado e adiciona no membership
		var = request.vars['%s' %(dado.nome)]
		if var == 'on':
			auth.add_membership(id_grupo, id_usuario)
		else:
			auth.del_membership(id_grupo, id_usuario)

	##Faz o loop retornando departamentos
	depta=db(db.f_departamentos).select(db.f_departamentos.departamento)
	for dept in depta:
		#logger.debug("dept:%s" %(dept))
		nome = 'dept_%s' %(dept.departamento) 
		query = (db.auth_group.role == nome)
		id_grupo = db(query).select()[0].id

		##verifica se departamento está ticado e adiciona no membership
		var = request.vars['%s' %(nome)]	
		if var == 'on':
			auth.add_membership(id_grupo, id_usuario)
		else:
			auth.del_membership(id_grupo, id_usuario)

	redirect(URL('users'))


##-- Extras --##
def permissao():
	editor = False
	for row in session.auth.user_groups:
		grupo = session.auth.user_groups[row]
		if (grupo == "gerenciador") or (grupo == "administrador"):
			editor = True
	return editor

@auth.requires_login()
def delete():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']
	if funcao 	== 	"auth_user":
		tabela 	= 	db.auth_user.id
		funcao 	=	"users"
	if funcao 	== 	"f_menu": 
		delete_role(request.vars['nome'], request.vars['tipo'])
		#role	= 	request.vars['nome']
		#id_role	= 	db(db.auth_group.role == role).select(db.auth_group.id) 
		#auth.del_group(id_role[0].id)
		tabela 	= 	db.f_menu.id
	if funcao 	== 	"f_submenu":
		delete_role(request.vars['nome'], request.vars['tipo'])
		#role	= 	request.vars['nome']
		#id_role	= 	db(db.auth_group.role == role).select(db.auth_group.id) 
		#auth.del_group(id_role[0].id)
		tabela 	= 	db.f_submenu.id

	db(tabela == id_tab).delete()	
	redirect(URL(funcao))

def delete_role(nome, tipo):
	print 'entrou'
	print nome
	print tipo
	id_role	= 	db(db.auth_group.role == nome).select(db.auth_group.id)
	auth.del_group(id_role[0].id)
	if tipo == "menu":
		menu = db(db.f_menu.nome == nome).select()
		if menu[0].submenu == True:
			var = db(db.f_submenu.menu_ref == menu[0].id).select()
			for dado in var:
				print dado
				id_role	= db(db.auth_group.role == dado.nome).select(db.auth_group.id)
				print id_role
				auth.del_group(id_role[0])


