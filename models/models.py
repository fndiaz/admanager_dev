# -*- coding: utf-8 -*-

#########################################################################
## Declaração do Banco de dados
#########################################################################

db.define_table('f_empresa',
	Field("id"),
	Field("empresa"),
	Field("mostrar", "boolean", default=True),
	format="%(empresa)s",
	migrate=False
	)

db.f_empresa._enable_record_versioning()

Troncos = db.define_table('f_troncos',
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
	Field("id_empresa", db.f_empresa, requires=IS_IN_DB(db(db.f_empresa.mostrar == True),'f_empresa.id',"%(empresa)s")),
	Field("mostrar", "boolean", default=True),
	format="%(tronco)s",
	migrate=False
	)

Troncos_fisicos = db.define_table('f_troncos_fisicos',
	Field("id"),
	Field("id_tronco", db.f_troncos, requires=IS_IN_DB(db(db.f_troncos.mostrar == True),'f_troncos.id',"%(tronco)s")),
	Field("dispositivo", "string", length="30"),
	migrate=False
	)

Destinos = db.define_table('f_destinos',
	Field("id"),
	Field("tipo_chamada", "string"),
	Field("expressao", "string"),
	Field("destino", "string"),
	Field("tamanho_max", "integer"),
	Field("tarifado", "boolean"),
	Field("portabilidade", "boolean"),
	Field("mostrar", "boolean", default=True),
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

Rotas = db.define_table('f_rotas',
	Field("id"),
	Field("rota", "string", length="1"),
	Field("id_tronco", db.f_troncos, requires=IS_IN_DB(db(db.f_troncos.mostrar == True),'f_troncos.id',"%(tronco)s")),
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

db.define_table("f_ura",
	Field("ramal_principal"),
	Field("ura", "text"),
	format="%(empresa)s",
    migrate=False)

db.define_table("f_portabilidade",
	Field("endereco"),
	Field("usuario"),
	Field("senha"),
	Field("ativo", "boolean"),
	format="%(usuario)s",
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
	Field("arquivo_gravacao", "string"),
    format="%(origem)s",
    migrate=False)

Grupo_destinos = db.define_table("f_grupo_destinos",
	Field("id_destinos", "list:reference db.f_destinos"),
	Field("grupo_destino", "string"),
	format="%(grupo_destino)s",
    migrate=False)

Departamentos = db.define_table("f_departamentos",
	Field("departamento", "string", length="50"),
	Field("id_empresa", db.f_empresa, requires=IS_IN_DB(db(db.f_empresa.mostrar == True),'f_empresa.id',"%(empresa)s")),
	Field("mostrar", "boolean", default=True),
	format="%(departamento)s",
    migrate=False)

Ramal_virtual = db.define_table("f_ramal_virtual",
	Field("tecnologia", requires=IS_IN_SET(["SIP", "IAX", "DAHDI", "KHOMP", "QUEUE", "FAX"])),
	Field("ramal_fisico"),
	Field("id_departamento", db.f_departamentos, requires=IS_IN_DB(db(db.f_departamentos.mostrar == True),'f_departamentos.id',"%(departamento)s")),
	Field("ramal_virtual"),
	Field("gravacao", "boolean"),
	Field("blacklist", "boolean"),
	Field("mesa_fop2", "boolean"),
	Field("chamadas_simultaneas", "integer"),
	Field("id_grupo_destinos", db.f_grupo_destinos),
	Field("nome", "string", length="20"),
	Field("bina_interno"),
	Field("bina_externo"),
	Field("credito", "boolean"),
	format="%(ramal_virtual)s",
    migrate=False)

Aplicacao = db.define_table("f_aplicacao",
	Field("id_ramalvirtual", db.f_ramal_virtual),
	Field("cadeado_ativo", "boolean", default=False),
	Field("cadeado_senha"),
	Field("cs_ativo", "boolean", default=False),
	Field("cs_chamadaexterna", "boolean", default=False),
	Field("cs_chamadainterna", "boolean", default=False),
	Field("cs_numero", "integer"),
	Field("cs_excecao"),
	Field("voicemail_ativo", "boolean", default=False),
	Field("voicemail_email"),
	Field("voicemail_senha", "integer"),
	Field("agenda_cadastro", "boolean", default=False),
	Field("agenda_senha", "integer"),
    migrate=False)

desvio={"INDISPONIVEL": "Indisponivel", "OCUPADO": "Ocupado", "NAOATENDIMENTO" : "Não Atendimento", "IMEDIATO" : "Imediato"}
Desvios = db.define_table("f_desvios",
	Field("id_ramalvirtual", db.f_ramal_virtual),
	Field("tipo_desvio", requires=IS_IN_SET(desvio)),
	Field("dia_semana", "list:string"),
	Field("horario_inicio"),
	Field("horario_fim"),
	Field("numero"),
	format="%(numero)s",
    migrate=False)

db.define_table("f_direcionamento",
	Field("origem"),
	Field("ddr"),
	Field("ramal_virtual"),
	format="%(origem)s",
    migrate=False)

####--SIP/IAX
db.define_table("fisico_sip_iax",
	Field("usuario"),
	Field("secret"),
	Field("tecnologia", requires=IS_IN_SET(["SIP", "IAX"])),
	Field("type_f", requires=IS_IN_SET(["friend", "peer", "user"])),
	Field("host_f", "string", default="dynamic"),
	Field("context", "string", default="ramais"),
	Field("qualify", "boolean"),
	Field("disallow", "list:string"),
	Field("allow", "list:string"),
	Field("nat", "boolean"),
	Field("aut_externa", "boolean"),
	Field("tronco", "boolean", default=False),
	Field("extras", "text", default='requirecalltoken=no\ncanreinvite=no\n'),
	Field("register", "boolean"),
	format="%(usuario)s",
	migrate=False)

db.define_table("fisico_dahdi_khomp",
	Field("tecnologia"),
	Field("porta"),
	Field("context"),
	format="%(porta)s",
	migrate=False)

##Queues
estrategia = ["ringall", "roundrobin", "leastrecent", "fewestcalls", "random", "rrmemory"]
db.define_table("queue",
	Field("name"),
	Field("strategy", requires=IS_IN_SET(estrategia), default='ringall'),
	Field("musiconhold", default='default'),
	Field("ringinuse", requires=IS_IN_SET(["yes", "no"]), default='no'),
	Field("retry", "integer", default=1),
	Field("timeout", "integer", default=15),
	Field("timeoutrestart", "boolean"),
	Field("joinempty", requires=IS_IN_SET(["yes", "no"]), default='yes'),
	Field("leavewhenempty", requires=IS_IN_SET(["yes", "no"]), default='yes'),
	Field("eventwhencalled", "boolean", default=True),
	Field("wrapuptime", "integer", default=0),
	Field("maxlen", "integer", default=100), 

	Field("announce"),
	Field("context", default="ramais"),
	Field("monitor_join", "boolean", default=False),
	Field("monitor_format"),
	Field("queue_youarenext"),
	Field("queue_thereare"),
	Field("queue_callswaiting"),
	Field("queue_holdtime"),
	Field("queue_minutes"),
	Field("queue_seconds"),
	Field("queue_lessthan"),
	Field("queue_thankyou"),
	Field("queue_reporthold"),
	Field("announce_frequency", "integer"),
	Field("announce_round_seconds", "integer"),
	Field("announce_holdtime"),
	Field("servicelevel", "integer"),
	Field("eventmemberstatus", "boolean", default=False),
	Field("reportholdtime", "boolean", default=False),
	Field("memberdelay", "integer", default=0),
	Field("weight", "integer", default=0),
	Field("setinterfacevar", "boolean", default=True),
	Field("atributo"),
	format="%(name)s",
	migrate=False)

db.define_table("queue_members",
	Field("uniqueid"),
	Field("queue_name"),
	Field("interface"),
	Field("penalty", "integer"),
	Field("membername"),
	Field("paused", "integer"),
	format="%(queue_name)s",
	migrate=False)

db.define_table("f_fax",
	Field("nome"),
	Field("email"),
	Field("numero"),
	format="%(nome)s",
	migrate=False)

Ddr = db.define_table("f_ddr",
	Field("ddr"),
	Field("id_ramalvirtual", db.f_ramal_virtual),
	format="%(ddr)s",
	migrate=False)

####--Usuarios/PrePago
db.define_table("f_usuarios",
	Field("pin", "string", length=20),
	Field("id_departamento", db.f_departamentos, requires=IS_IN_DB(db(db.f_departamentos.mostrar == True),'f_departamentos.id',"%(departamento)s")),
	Field("nome", "string", length=20),
	Field("gravacao", "boolean"),
	Field("blacklist", "boolean"),
	Field("id_grupo_destinos", db.f_grupo_destinos),
	Field("credito", "boolean"),
	format="%(nome)s",
	migrate=False)

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