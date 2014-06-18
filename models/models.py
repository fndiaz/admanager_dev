# -*- coding: utf-8 -*-

#########################################################################
## Declaração do Banco de dados
#########################################################################

db.define_table('f_empresa',
	Field("id"),
	Field("empresa"),
	####Field("faixa_ramal"),
	format="%(empresa)s",
	migrate=False
	)

db.define_table('f_troncos',
	Field("id"),
	Field("tronco", "string", length="20"),
	Field("dispositivo", "string", length="30"),
	Field("chamadas_simultaneas", "integer"),
	Field("qtde_max_minutos", "integer"),
	Field("transbordo", "integer"),
	Field("csp", "integer"),
	Field("ddd", "integer"),
	Field("prefixo", "integer"),
	Field("chave", "integer"),
	Field("habilitado", "boolean"),
	Field("ciclo_conta", "integer"),
	Field("ramal_principal", "string", length="10"),
	Field("ura", "boolean"),
	Field("add_zero", "boolean"),
	Field("id_empresa", db.f_empresa),
	format="%(tronco)s",
	migrate=False
	)

db.define_table('f_troncos_fisicos',
	Field("id"),
	Field("id_tronco", db.f_troncos),
	Field("dispositivo", "string", length="30"),
	migrate=False
	)

db.define_table('f_destinos',
	Field("id"),
	Field("tipo_chamada", "string"),
	Field("expressao", "string"),
	Field("destino", "string"),
	Field("tamanho_max", "integer"),
	Field("tarifado", "boolean"),
	format="%(tipo_chamada)s",
	migrate=False
	)

db.define_table('f_tarifacao',
	Field("id"),
	Field("tarifacao", "string", length="30"),
	Field("passo", "string", length="30"),
	Field("valor", "double"),
	format="%(tarifacao)s",
	migrate=False
	)

db.define_table("f_horario",
    Field("id"),
    Field("dia_semana", "string", length="30"),
    Field("horario"),
    Field("acao_negativa", "string", length="100"),
    Field("descricao", "string", length="50"),
    format="%(horario)s",
    migrate=False)

db.define_table('f_rotas',
	Field("id"),
	Field("rota", "string", length="1"),
	Field("id_tronco", db.f_troncos),
	Field("prioridade", "integer"),
	Field("id_destino", "list:reference db.f_destinos"),
	Field("exclui_antes", "integer"),
	Field("adiciona_antes", "string"),
	Field("adiciona_depois", "string"),
	Field("id_empresa", "list:reference db.f_empresa"),
	Field("id_tarifacao", db.f_tarifacao),
	Field("id_horario", db.f_horario),
	Field("add_csp", "boolean"),
	format="%(rota)s",
	migrate=False
	)

db.define_table("f_parametros",
    Field("empresa", "string", length="100"),
    Field("tempo_chamada_externa", "integer"),
    Field("tempo_chamada_interna", "integer"),
    Field("gravacao_geral", "boolean"),
    Field("endereco_smtp", "string", length="100"),
    Field("usuario_smtp", "string", length="100"),
    Field("senha_smtp", "string", length="100"),
    Field("porta_smtp", "integer", default=0),
    Field("ssl_smtp", "boolean"),
    Field("email_admin", "string", length="100"),
    Field("faixa_ip_interna", "text"),
    Field("endereco_ip_externo", "string", length="20"),
    Field("endereco_host_externo", "string", length="100"),
    Field("toque_diferenciado", "boolean"),
    Field("toque_diff_sipheader", "string", length="100"),
    Field("spy_senha", "string", length="4"),
	Field("spy_ramal_proibe_monitora", "text"),
	Field("spy_ramal_espiao", "text"),
    Field("tamanho_pin", "integer", default=0),
    Field("fuso_horario", "string", length="3"),
	Field("credito_dia", "string", length="2"),
	Field("ura_antes_horario", "boolean"),
	Field("bloqueio_chamadacobrar", "boolean"),
	Field("tempo_chamada_transf", "integer"),
	Field("rechamada", "boolean"),
	Field("pin_temporario", "string", length="4"),
    format="%(empresa)s",
    migrate=False)

db.define_table("f_bilhetes_chamadas",
	Field("id_tronco", db.f_troncos),
	Field("origem"),
	Field("destino"),
	Field("linked_id"),
	Field("horario", "datetime"),
	Field("status"),
	Field("tarifacao", "double"),
	Field("tempo", "integer"),
	Field("id_empresa", db.f_empresa),
	Field("id_destino", db.f_destinos),
	Field("gravacao", "boolean"),
	Field("atendido", "string", length="10"),
	Field("nome_origem", "string", length="20"),
	Field("departamento", "string", length="50"),
	Field("transbordo", "string", length="5"),
    format="%(origem)s",
    migrate=False)

####--SIP/IAX
db.define_table("fisico_sip_iax",
	Field("usuario"),
	Field("secret"),
	Field("tecnologia", requires=IS_IN_SET(["SIP", "IAX"])),
	Field("type_f", "string", default="friend"),
	Field("host_f", "string", default="dynamic"),
	Field("context", "string", default="ramais"),
	Field("qualify", "boolean"),
	Field("disallow", "list:string"),
	Field("allow", "list:string"),
	Field("nat", "boolean"),
	Field("aut_externa", "boolean"),
	Field("tronco", "boolean", default=False),
	Field("extras", "text", default='requirecalltoken=no\ncanreinvite=no\n'),
	format="%(usuario)s",
	migrate=True)

db.define_table("fisico_dahdi_khomp",
	Field("tecnologia"),
	Field("porta"),
	Field("context"),
	format="%()s",
	migrate=True)

####--Menus Permissões
db.define_table('f_menu',
	Field("id"),
	Field("nome"),
	Field("icone"),
	Field("funcao"),
	Field("controller"),
	Field("ordem", "integer"),
	Field("submenu", "boolean", default=False),
	format="%(nome)s"
	#migrate=False
	)

db.define_table('f_submenu',
	Field("id"),
	Field("menu_ref", db.f_menu),
	Field("nome"),
	Field("icone"),
	Field("ordem", "integer"),
	Field("funcao"),
	Field("controller"),
	format="%(nome)s"#
	#migrate=False
	)

#db.define_table('f_permissao_menu',
#	Field("id_user"),
#	Field("menu", "boolean"),
#	Field("submenu", "boolean"),
#	#migrate=False
#	)

#db.define_table('f_permissao_menu2',
#	Field("id_user", db.auth_user),
#	Field("id_menu", db.f_menu),
#	Field("id_submenu", db.f_submenu),
#	Field("permissao", "boolean")
#	)