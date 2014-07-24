# -*- coding: utf-8 -*-

#########################################################################
## Popula dados em primeiro acesso ao banco, caso tabela esteja vazia
#########################################################################

if db(db.auth_group.role == 'administrador').isempty():
	db.auth_group.insert(role="administrador", description="admin do sistema")
if db(db.auth_group.role == 'gerenciador').isempty():
	db.auth_group.insert(role="gerenciador", description="gerenciador cliente")
if db(db.auth_group.role == 'comum').isempty():
	db.auth_group.insert(role="comum", description="usuario leitura")

if db(db.auth_user.email == 'root@forip.com.br').isempty():
	##Inserindo user root
	root = db.auth_user.insert(first_name="root",last_name="root",\
	email="root@forip.com.br", ramal="0000",\
	password=db.auth_user.password.validate("root123")[0])
	##Inserindo permissão de administrador
	group_admin = db(db.auth_group.role == 'administrador').select()
	auth.add_membership(group_admin[0].id, root)

if db(db.f_menu).isempty():
	db.f_menu.insert(nome="Principal", controller="initial", funcao="dashboard", icone="icon-bar-chart", ordem="1", submenu=False)
	auth.add_group('Principal', '')
	db.f_menu.insert(nome="Acessos", controller="", funcao="", icone="icon-eye-open", ordem="2", submenu=True)
	auth.add_group('Acessos', '')
	db.f_menu.insert(nome="Funcional", controller="", funcao="", icone="icon-edit", ordem="3", submenu=True)
	auth.add_group('Funcional', '')
	db.f_menu.insert(nome="Extensões", controller="", funcao="", icone="icon-list-alt", ordem="4", submenu=True)
	auth.add_group('Extensões', '')
	db.f_menu.insert(nome="Pré Pago", controller="", funcao="", icone="icon-align-justify", ordem="5", submenu=True)
	auth.add_group('Pré Pago', '')
	db.f_menu.insert(nome="Configs", controller="", funcao="", icone="icon-wrench", ordem="6", submenu=True)
	auth.add_group('Configs', '')
	db.commit()

if db(db.f_submenu).isempty():
	id_acessos 	= db(db.f_menu.nome == 'Acessos').select()[0].id
	id_funcional= db(db.f_menu.nome == 'Funcional').select()[0].id
	id_extensoes= db(db.f_menu.nome == 'Extensões').select()[0].id
	id_prepago 	= db(db.f_menu.nome == 'Pré Pago').select()[0].id
	id_configs 	= db(db.f_menu.nome == 'Configs').select()[0].id
	##Menu Acessos
	db.f_submenu.insert(nome="Usuários", controller="initial", funcao="users", icone="icon-chevron-right", ordem="1", menu_ref=id_acessos)
	auth.add_group('Usuários', '')
	db.f_submenu.insert(nome="Grupos", controller="initial", funcao="groups", icone="icon-chevron-right", ordem="4", menu_ref=id_acessos)
	auth.add_group('Grupos', '')
	db.f_submenu.insert(nome="Permissões", controller="initial", funcao="membership", icone="icon-chevron-right", ordem="5", menu_ref=id_acessos)
	auth.add_group('Permissões', '')
	db.f_submenu.insert(nome="Menu", controller="initial", funcao="f_menu", icone="icon-chevron-right", ordem="2", menu_ref=id_acessos)
	auth.add_group('Menu', '')
	db.f_submenu.insert(nome="Submenu", controller="initial", funcao="f_submenu", icone="icon-chevron-right", ordem="3", menu_ref=id_acessos)
	auth.add_group('Submenu', '')
	##Menu Funcional
	db.f_submenu.insert(nome="Empresa", controller="funcional", funcao="f_empresa", icone="icon-chevron-right", ordem="1", menu_ref=id_funcional)
	auth.add_group('Empresa', '')
	db.f_submenu.insert(nome="Departamentos", controller="ramais_v", funcao="f_departamentos", icone="icon-chevron-right", ordem="2", menu_ref=id_funcional)
	auth.add_group('Departamentos', '')
	db.f_submenu.insert(nome="Departamentos", controller="ramais_v", funcao="f_departamentos", icone="icon-chevron-right", ordem="2", menu_ref=id_funcional)
	auth.add_group('Departamentos', '')

if db(db.f_portabilidade).isempty():
	db.f_portabilidade.insert(endereco='sippulse.com.br',usuario='adaldeia',senha='senha',ativo=False)
