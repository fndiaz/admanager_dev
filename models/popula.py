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
if db(db.auth_group.role == 'gravacao_perm').isempty():
	db.auth_group.insert(role="gravacao_perm", description="ouvir gravacoes")

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
	db.f_menu.insert(nome="Bilhetes", controller="bilhetes", funcao="busca_chamadas", icone="icon-search", ordem="6", submenu=False)
	auth.add_group('Bilhetes', '')
	db.f_menu.insert(nome="Configs", controller="", funcao="", icone="icon-wrench", ordem="7", submenu=True)
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
	db.f_submenu.insert(nome="Troncos", controller="funcional", funcao="f_troncos", icone="icon-chevron-right", ordem="3", menu_ref=id_funcional)
	auth.add_group('Troncos', '')
	db.f_submenu.insert(nome="Troncos físicos", controller="funcional", funcao="f_troncos_fisicos", icone="icon-chevron-right", ordem="4", menu_ref=id_funcional)
	auth.add_group('Troncos físicos', '')
	db.f_submenu.insert(nome="Destinos", controller="funcional", funcao="f_destinos", icone="icon-chevron-right", ordem="5", menu_ref=id_funcional)
	auth.add_group('Destinos', '')
	db.f_submenu.insert(nome="Grupo Destinos", controller="ramais_v", funcao="f_grupo_destinos", icone="icon-chevron-right", ordem="6", menu_ref=id_funcional)
	auth.add_group('Grupo Destinos', '')
	db.f_submenu.insert(nome="Rotas saídas", controller="funcional", funcao="f_rotas", icone="icon-chevron-right", ordem="7", menu_ref=id_funcional)
	auth.add_group('Rotas saídas', '')
	db.f_submenu.insert(nome="Tarifação", controller="funcional", funcao="f_tarifacao", icone="icon-chevron-right", ordem="8", menu_ref=id_funcional)
	auth.add_group('Tarifação', '')
	db.f_submenu.insert(nome="Horário", controller="funcional", funcao="f_horario", icone="icon-chevron-right", ordem="9", menu_ref=id_funcional)
	auth.add_group('Horário', '')
	db.f_submenu.insert(nome="Ura", controller="funcional", funcao="f_ura", icone="icon-chevron-right", ordem="10", menu_ref=id_funcional)
	auth.add_group('Ura', '')
	##Menu Extensões
	db.f_submenu.insert(nome="SIP-IAX", controller="ramais", funcao="show_sip", icone="icon-list-alt", ordem="1", menu_ref=id_extensoes)
	auth.add_group('SIP-IAX', '')
	db.f_submenu.insert(nome="Tronco SIP-IAX", controller="ramais", funcao="show_tronco", icone="icon-list-alt", ordem="2", menu_ref=id_extensoes)
	auth.add_group('Tronco SIP-IAX', '')
	db.f_submenu.insert(nome="DAHDI-KHOMP", controller="ramais", funcao="show_dahdi", icone="icon-list-alt", ordem="3", menu_ref=id_extensoes)
	auth.add_group('DAHDI-KHOMP', '')
	db.f_submenu.insert(nome="Ramais", controller="ramais_v", funcao="f_ramal_virtual", icone="icon-list-alt", ordem="4", menu_ref=id_extensoes)
	auth.add_group('Ramais', '')
	db.f_submenu.insert(nome="Filas", controller="queues", funcao="queue", icone="icon-list-alt", ordem="5", menu_ref=id_extensoes)
	auth.add_group('Filas', '')
	db.f_submenu.insert(nome="Fax", controller="queues", funcao="f_fax", icone="icon-list-alt", ordem="6", menu_ref=id_extensoes)
	auth.add_group('Fax', '')
	db.f_submenu.insert(nome="Desvios", controller="ramais_v", funcao="f_desvios", icone="icon-list-alt", ordem="7", menu_ref=id_extensoes)
	auth.add_group('Desvios', '')
	db.f_submenu.insert(nome="Direcionamento", controller="ramais_v", funcao="f_direcionamento", icone="icon-list-alt", ordem="8", menu_ref=id_extensoes)
	auth.add_group('Direcionamento', '')
	db.f_submenu.insert(nome="DDR", controller="ramais_v", funcao="f_ddr", icone="icon-list-alt", ordem="9", menu_ref=id_extensoes)
	auth.add_group('DDR', '')
	##Pré Pago
	db.f_submenu.insert(nome="Usuários discagem", controller="prepago", funcao="f_usuarios", icone="icon-chevron-right", ordem="1", menu_ref=id_prepago)
	auth.add_group('Usuários discagem', '')
	db.f_submenu.insert(nome="Consultar saldo", controller="prepago", funcao="show_saldos", icone="icon-chevron-right", ordem="2", menu_ref=id_prepago)
	auth.add_group('Consultar saldo', '')
	db.f_submenu.insert(nome="Saldos Geral", controller="prepago", funcao="show_grid_saldos", icone="icon-chevron-right", ordem="3", menu_ref=id_prepago)
	auth.add_group('Saldos Geral', '')
	db.f_submenu.insert(nome="Cred Automático", controller="prepago", funcao="f_creditos_form", icone="icon-chevron-right", ordem="4", menu_ref=id_prepago)
	auth.add_group('Cred Automático', '')
	db.f_submenu.insert(nome="Cred Manual", controller="prepago", funcao="creditos_manual", icone="icon-chevron-right", ordem="5", menu_ref=id_prepago)
	auth.add_group('Cred Manual', '')
	##Configs
	db.f_submenu.insert(nome="Parâmetros", controller="funcional", funcao="f_parametros_form", icone="icon-chevron-right", ordem="1", menu_ref=id_configs)
	auth.add_group('Parâmetros', '')
	db.f_submenu.insert(nome="Portabilidade", controller="funcional", funcao="f_portabilidade_form", icone="icon-chevron-right", ordem="1", menu_ref=id_configs)
	auth.add_group('Portabilidade', '')


if db(db.f_portabilidade).isempty():
	db.f_portabilidade.insert(endereco='sippulse.com.br',usuario='adaldeia',senha='senha',ativo=False)


id_funcional= db(db.f_menu.nome == 'Funcional').select()[0].id
if db(db.f_submenu.nome == 'CallBack').isempty():
	db.f_submenu.insert(nome="CallBack", controller="listas", funcao="f_callback", icone="icon-chevron-right", ordem="11", menu_ref=id_funcional)
	auth.add_group('CallBack', '')
if db(db.f_submenu.nome == 'Listas').isempty():
	db.f_submenu.insert(nome="Listas", controller="listas", funcao="f_listas", icone="icon-chevron-right", ordem="12", menu_ref=id_funcional)
	auth.add_group('Listas', '')

