# -*- coding: utf-8 -*-

#########################################################################
## Funcional
#########################################################################

##Empresas
db.f_empresa.empresa.requires = IS_NOT_EMPTY()

##Troncos
db.f_troncos.tronco.requires = IS_NOT_EMPTY()
db.f_troncos.dispositivo.requires = IS_NOT_EMPTY()
db.f_troncos.chamadas_simultaneas.requires = IS_INT_IN_RANGE(0,101)
db.f_troncos.qtde_max_minutos.requires = IS_INT_IN_RANGE(0,999999999, 
								error_message="entre com 0 ou um número")
db.f_troncos.transbordo.requires = IS_EMPTY_OR(IS_IN_DB(db(db.f_troncos.mostrar == True),'f_troncos.id',"%(tronco)s"))
db.f_troncos.ddd.requires = IS_EMPTY_OR(IS_MATCH("[0-9][0-9]", error_message="entre com um número de dois dígitos"))
db.f_troncos.csp.requires = IS_EMPTY_OR(IS_MATCH("[0-9][0-9]", error_message="entre com um número de dois dígitos"))
db.f_troncos.chave.requires = IS_EMPTY_OR(IS_MATCH("^[0-9]", error_message="entre com um número chave"))
db.f_troncos.ciclo_conta.requires = IS_EMPTY_OR(IS_IN_SET(dia_mes()))
db.f_troncos.prefixo.requires = IS_EMPTY_OR(IS_MATCH("^[0-9]", error_message="digite um prefixo válido"))


#Troncos Físicos
db.f_troncos_fisicos.dispositivo.requires = IS_NOT_EMPTY()

#Destinos
dest = ["RAMAL", "0800", "0300", "EMERGENCIA", "LOCAL_FIXO", "LOCAL_CELULAR", "DDD_FIXO", "DDD_CELULAR", "DDI"]
db.f_destinos.tipo_chamada.requires = IS_IN_SET(dest)
db.f_destinos.destino.requires = IS_NOT_EMPTY()
db.f_destinos.tamanho_max.requires = IS_NOT_EMPTY()
db.f_destinos.expressao.requires = [
IS_NOT_EMPTY(),
IS_NOT_IN_DB(db, 'f_destinos.expressao') ]

##Tarifacao
db.f_tarifacao.tarifacao.requires = IS_NOT_EMPTY()
db.f_tarifacao.passo.requires = IS_NOT_EMPTY()
db.f_tarifacao.valor.requires = IS_NOT_EMPTY()

##Rotas
db.f_rotas.rota.requires = IS_IN_SET(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
db.f_rotas.prioridade.requires = IS_NOT_EMPTY()
db.f_rotas.exclui_antes.requires = IS_EMPTY_OR( IS_IN_SET(['1', '2', '3', '4', '5', '6', '7', '8', '9']) )
#db.f_rotas.id_tronco.requires = IS_IN_DB(db, 'f_troncos.id', '%(tronco)s',
#					error_message=T("valor inválido"))
db.f_rotas.id_tarifacao.requires = IS_IN_DB(db, 'f_tarifacao.id', '%(tarifacao)s', 
					error_message=T("valor inválido"))
db.f_rotas.id_horario.requires = IS_IN_DB(db, 'f_horario.id', '%(horario)s', 
					error_message=T("valor inválido"))
db.f_rotas.id_empresa.requires = IS_IN_DB(db(db.f_empresa.mostrar == True),'f_empresa.id',"%(empresa)s", multiple=True)
db.f_rotas.id_destino.requires = IS_IN_DB(db(db.f_destinos.mostrar == True),'f_destinos.id',"%(destino)s", multiple=True)

##Horários
#dias={"mon": "Segunda Feira", "tue": "Terça Feira", "wed" : "Quarta Feira", "thu" : "Quinta Feira", "fri" : "Sexta Feira", "sat" : "Sábado", "sun" : "Domingo"}
#db.f_horario.dia_semana.requires = IS_IN_SET(dias,
#					multiple=True, error_message=T("escolha uma opção"))
db.f_horario.horario.requires = IS_NOT_EMPTY()
db.f_horario.acao_negativa.requires = IS_NOT_EMPTY()
db.f_horario.descricao.requires = IS_NOT_EMPTY()

##Ura
db.f_ura.ramal_principal.requires = IS_NOT_EMPTY()
db.f_ura.ura.requires = IS_NOT_EMPTY()

##Parametros
tempo_chamda=[5,10,15,20,30,45,60,90,120]
gmt=['-12','-11','-10','-9','-8','-7','-6','-5','-4','-3','-2','-1',
	 '+1','+2','+3','+4','+5','+6','+7','+8','+9','+10','+11','+12']
db.f_parametros.faixa_ip_interna.requires = IS_NOT_EMPTY()
#db.f_parametros.endereco_smtp.requires = IS_NOT_EMPTY()
#db.f_parametros.usuario_smtp.requires = IS_EMAIL()
#db.f_parametros.senha_smtp.requires = IS_NOT_EMPTY()
#db.f_parametros.porta_smtp.requires = IS_NOT_EMPTY()
db.f_parametros.empresa.requires = IS_NOT_EMPTY()
db.f_parametros.tempo_chamada_externa.requires = IS_IN_SET(tempo_chamda)
db.f_parametros.tempo_chamada_interna.requires = IS_IN_SET(tempo_chamda)
db.f_parametros.tempo_chamada_transf.requires = IS_IN_SET(tempo_chamda)
db.f_parametros.fuso_horario.requires = IS_IN_SET(gmt)
db.f_parametros.credito_dia.requires = IS_EMPTY_OR(IS_IN_SET(dia_mes()))

##Feriados
db.f_feriados.dia.requires = IS_IN_SET(dia_mes())

mes_ano=[('Jan','Janeiro'),('Feb','Fevereiro'),('Mar','Março'),('Apr','Abril'),('May','Maio'),('Jun','Junho'),
('Jul','Julho'),('Aug','Agosto'),('Sep','Setembro'),('Oct','Outubro'),('Nov','Novembro'),('Dec','Dezembro')]
db.f_feriados.mes.requires = IS_IN_SET(mes_ano, error_message=T("escolha uma opção"))

##Portabilidade 
db.f_portabilidade.ddd_padrao.requires = IS_MATCH("^[0-9][0-9]$", error_message=T("DDD inválido"))
db.f_portabilidade.tempo_timeout.requires = IS_MATCH("[0-9]+", error_message=T("somente números"))


#########################################################################
## Ramais
#########################################################################

#db.fisico_sip_iax.tecnologia.requires = requires=IS_IN_SET(["SIP", "IAX"], zero="SIP")
codecs = ["all", "ulaw", "alaw", "g729", "gsm", "speex"]
db.fisico_sip_iax.disallow.requires = IS_IN_SET(codecs, multiple=True)
db.fisico_sip_iax.disallow.default = ["all"]
db.fisico_sip_iax.allow.requires = IS_IN_SET(codecs, multiple=True)
db.fisico_sip_iax.allow.default = ["ulaw", "alaw"]
db.fisico_sip_iax.qualify.default = True
db.fisico_sip_iax.usuario.requires = IS_NOT_IN_DB(db, 'fisico_sip_iax.usuario')
db.fisico_sip_iax.host_f.requires = IS_NOT_EMPTY()

#########################################################################
## Ramais_v
#########################################################################
#Grupo Destinos
destn = ["RAMAL", "0800", "0300", "EMERGENCIA", "LOCAL_FIXO", "LOCAL_CELULAR", "DDD_FIXO", "DDD_CELULAR", "DDI"]
db.f_grupo_destinos.id_destinos.requires = IS_IN_SET(destn, multiple=True)
#db.f_grupo_destinos.id_destinos.requires = IS_IN_DB(db(db.f_destinos.mostrar == True),'f_destinos.id',"%(destino)s", multiple=True)



#Departamentos
db.f_departamentos.departamento.requires = [
IS_NOT_EMPTY(),
IS_NOT_IN_DB(db, 'f_departamentos.departamento')
]

##Ramal Virtual
db.f_ramal_virtual.ramal_virtual.requires = [ 
IS_MATCH("[0-9]+", error_message='somente números'),
IS_NOT_IN_DB(db, 'f_ramal_virtual.ramal_virtual')
]
#db.f_ramal_virtual.nome.requires = IS_ALPHANUMERIC()
db.f_ramal_virtual.chamadas_simultaneas.requires = IS_INT_IN_RANGE(0,21)

##Desvios
#dias={"mon": "Segunda Feira", "tue": "Terça Feira", "wed" : "Quarta Feira", "thu" : "Quinta Feira", "fri" : "Sexta Feira", "sat" : "Sábado", "sun" : "Domingo"}
dias=[('mon','Segunda Feira'),('tue','Terça Feira'),('wed','Quarta Feira'),('thu','Quinta Feira'),('fri','Sexta Feira'),('sat','Sábado'),('sun','Domingo')]
db.f_desvios.dia_semana.requires = IS_IN_SET(dias,
					multiple=True, error_message=T("escolha uma opção"))
db.f_desvios.horario_inicio.requires = IS_NOT_EMPTY()
db.f_desvios.horario_fim.requires = IS_NOT_EMPTY()

##DA
db.f_discagem_abreviada.abreviado.requires = IS_MATCH("^.[2-6][0-9][0-9]", error_message='número inválido')
db.f_discagem_abreviada.destino.requires = IS_MATCH("[0-9]+", error_message='somente números')


#########################################################################
## Queues
#########################################################################
#Queue
db.queue.name.requires = [IS_NOT_IN_DB(db, 'queue.name'),
							IS_NOT_EMPTY(), IS_ALPHANUMERIC()]

#Queue Member
db.queue_members.queue_name.requires = IS_NOT_EMPTY()
db.queue_members.interface.requires = IS_NOT_EMPTY()
db.queue_members.membername.requires = IS_NOT_EMPTY()

#Fax
db.f_fax.nome.requires = IS_NOT_EMPTY()
db.f_fax.email.requires = IS_EMAIL()
db.f_fax.numero.requires = IS_NOT_EMPTY()

#Meetme
db.meetme.confno.requires = [IS_NOT_IN_DB(db, 'meetme.confno'), IS_ALPHANUMERIC()]
db.meetme.pin.requires = IS_EMPTY_OR(IS_MATCH("[0-9]+", error_message=T("somente números")))
db.meetme.adminpin.requires = IS_EMPTY_OR(IS_MATCH("[0-9]+", error_message=T("somente números")))
db.meetme.maxusers.requires = IS_NOT_EMPTY()

#########################################################################
## Prepago
#########################################################################
db.f_usuarios.nome.requires = IS_NOT_IN_DB(db, 'f_usuarios.nome')
db.f_usuarios.pin.requires = IS_NOT_IN_DB(db, 'f_usuarios.pin')

#Creditos
db.f_creditos.local_fixo.requires = IS_INT_IN_RANGE(0,900000)
db.f_creditos.local_celular.requires = IS_INT_IN_RANGE(0,900000)
db.f_creditos.ddd_fixo.requires = IS_INT_IN_RANGE(0,900000)
db.f_creditos.ddd_celular.requires = IS_INT_IN_RANGE(0,900000)
db.f_creditos.ddi.requires = IS_INT_IN_RANGE(0,900000)
db.f_creditos.f0300.requires = IS_INT_IN_RANGE(0,900000)


#########################################################################
## Listas
#########################################################################
#callback
db.f_callback.nome.requires = IS_NOT_EMPTY()
db.f_callback.numero.requires = IS_NOT_EMPTY()

#Listas
db.f_listas.numero.requires = IS_NOT_EMPTY()
db.f_listas.descricao.requires = IS_NOT_EMPTY()


#########################################################################
## Provisionamento
#########################################################################
#prov_rede
db.prov_rede.nome.requires = IS_NOT_EMPTY()
db.prov_rede.dns.requires = IS_NOT_EMPTY()
db.prov_rede.ntp.requires = IS_NOT_EMPTY()
db.prov_rede.proxy.requires = IS_NOT_EMPTY()

#prov_equipamento
db.prov_equipamento.modelo.requires = [IS_NOT_EMPTY(), IS_UPPER()]

#prov_mac
db.prov_mac.mac.requires = [IS_NOT_EMPTY(), IS_LOWER(), 
	IS_LENGTH(minsize=12, maxsize=12, error_message=T("12 caracteres")),]
db.prov_mac.vlan.requires = IS_EMPTY_OR( IS_IN_SET(['1','2','3','4','5','6','7','8','9']) )


#########################################################################
## Validadores
#########################################################################

##Agenda
#db.agenda.empresa.requires = IS_NOT_EMPTY(error_message=
#						T("valor não pode ser nulo"))

#db.agenda.telefone.requires = [IS_NOT_EMPTY(error_message=T("o telefone deve conter de 9 a 11 números")),
#IS_NOT_IN_DB(db, 'agenda.telefone', error_message=T("este número está em uso")),
#IS_LENGTH(minsize=9, maxsize=11, error_message=T("o telefone deve conter de 9 a 11 números")),
#IS_MATCH('[0-9]+', error_message=T("somente números"))]