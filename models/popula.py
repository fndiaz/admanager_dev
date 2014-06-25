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
	db.f_menu.insert(nome="Menu", controller="initial", funcao="f_menu", icone="icon-list-alt", ordem="1", submenu=False)
	auth.add_group('Menu', '')
	db.f_menu.insert(nome="Submenu", controller="initial", funcao="f_submenu", icone="icon-list-alt", ordem="2", submenu=False)
	auth.add_group('Submenu', '')
	db.f_menu.insert(nome="Acessos", controller="", funcao="", icone="icon-list-alt", ordem="3", submenu=True)
	auth.add_group('Acessos', '')
	db.f_menu.insert(nome="Troncos", controller="funcional", funcao="f_troncos", icone="icon-list-alt", ordem="4", submenu=False)
	auth.add_group('Troncos', '')
	db.f_menu.insert(nome="Troncos físicos", controller="funcional", funcao="f_troncos_fisicos", icone="icon-list-alt", ordem="5", submenu=False)
	auth.add_group('Troncos físicos', '')
	db.f_menu.insert(nome="Destinos", controller="funcional", funcao="f_destinos", icone="icon-list-alt", ordem="6", submenu=False)
	auth.add_group('Destinos', '')
	db.f_menu.insert(nome="Empresa", controller="funcional", funcao="f_empresa", icone="icon-list-alt", ordem="7", submenu=False)
	auth.add_group('Empresa', '')
	db.f_menu.insert(nome="Tarifação", controller="funcional", funcao="f_tarifacao", icone="icon-list-alt", ordem="8", submenu=False)
	auth.add_group('Tarifação', '')
	db.f_menu.insert(nome="Rotas", controller="funcional", funcao="f_rotas", icone="icon-list-alt", ordem="9", submenu=False)
	auth.add_group('Rotas', '')
	db.f_menu.insert(nome="Horário", controller="funcional", funcao="f_horario", icone="icon-list-alt", ordem="10", submenu=False)
	auth.add_group('Horário', '')
	db.f_menu.insert(nome="Parâmetros", controller="funcional", funcao="f_parametros_form", icone="icon-list-alt", ordem="14", submenu=False)
	auth.add_group('Parâmetros', '')
	db.f_menu.insert(nome="Ramais", controller="", funcao="", icone="icon-list-alt", ordem="15", submenu=True)
	auth.add_group('Ramais', '')
	db.commit()

if db(db.f_submenu).isempty():
	id_acessos = db(db.f_menu.nome == 'Acessos').select()[0].id
	id_ramais = db(db.f_menu.nome == 'Ramais').select()[0].id
	db.f_submenu.insert(nome="Usuários", controller="initial", funcao="users", icone="icon-chevron-right", ordem="1", menu_ref=id_acessos)
	auth.add_group('Usuários', '')
	db.f_submenu.insert(nome="Grupos", controller="initial", funcao="groups", icone="icon-chevron-right", ordem="2", menu_ref=id_acessos)
	auth.add_group('Grupos', '')
	db.f_submenu.insert(nome="Permissões", controller="initial", funcao="membership", icone="icon-chevron-right", ordem="3", menu_ref=id_acessos)
	auth.add_group('Permissões', '')
	db.f_submenu.insert(nome="SIP/IAX", controller="ramais", funcao="show_sip", icone="icon-chevron-right", ordem="1", menu_ref=id_ramais)
	auth.add_group('SIP/IAX', '')
	db.f_submenu.insert(nome="DAHDI/KHOMP", controller="ramais", funcao="show_dahdi", icone="icon-chevron-right", ordem="2", menu_ref=id_ramais)
	auth.add_group('DAHDI/KHOMP', '')
	db.f_submenu.insert(nome="Troncos SIP/IAX", controller="ramais", funcao="show_tronco", icone="icon-chevron-right", ordem="3", menu_ref=id_ramais)
	auth.add_group('Troncos SIP/IAX', '')
