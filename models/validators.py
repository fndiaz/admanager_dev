# -*- coding: utf-8 -*-

#########################################################################
## Funcional
#########################################################################

##Empresas
db.f_empresa.empresa.requires = IS_NOT_EMPTY()

##Troncos
db.f_troncos.tronco.requires = IS_NOT_EMPTY()
db.f_troncos.dispositivo.requires = IS_NOT_EMPTY()
db.f_troncos.chamadas_simultaneas.requires = IS_NOT_EMPTY()
db.f_troncos.ramal_principal.requires = IS_NOT_EMPTY()

#Troncos Físicos
db.f_troncos_fisicos.dispositivo.requires = IS_NOT_EMPTY()

#Destinos
db.f_destinos.tipo_chamada.requires = IS_NOT_EMPTY()
db.f_destinos.expressao.requires = IS_NOT_EMPTY()
db.f_destinos.destino.requires = IS_NOT_EMPTY()
db.f_destinos.tamanho_max.requires = IS_NOT_EMPTY()

##Tarifacao
db.f_tarifacao.tarifacao.requires = IS_NOT_EMPTY()
db.f_tarifacao.passo.requires = IS_NOT_EMPTY()
db.f_tarifacao.valor.requires = IS_NOT_EMPTY()

##Rotas
db.f_rotas.rota.requires = IS_NOT_EMPTY()
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
db.f_parametros.faixa_ip_interna.requires = IS_NOT_EMPTY()


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
db.f_grupo_destinos.id_destinos.requires =\
IS_IN_DB(db,'f_destinos.id',"%(tipo_chamada)s",multiple=True)
db.f_grupo_destinos.grupo_destino.requires = IS_NOT_EMPTY()

#Departamentos
db.f_departamentos.departamento.requires = IS_NOT_EMPTY()

##Ramal Virtual
db.f_ramal_virtual.ramal_virtual.requires = [
IS_INT_IN_RANGE(0, 99999999999, error_message='somente números'),
IS_NOT_IN_DB(db, 'f_ramal_virtual.ramal_virtual')
]
db.f_ramal_virtual.chamadas_simultaneas.requires = IS_INT_IN_RANGE(1,21)

##Desvios
dias={"mon": "Segunda Feira", "tue": "Terça Feira", "wed" : "Quarta Feira", "thu" : "Quinta Feira", "fri" : "Sexta Feira", "sat" : "Sábado", "sun" : "Domingo"}
db.f_desvios.dia_semana.requires = IS_IN_SET(dias,
					multiple=True, error_message=T("escolha uma opção"))
db.f_desvios.horario_inicio.requires = IS_NOT_EMPTY()
db.f_desvios.horario_fim.requires = IS_NOT_EMPTY()


#########################################################################
## Queues
#########################################################################
#Queue
db.queue.name.requires = [IS_NOT_EMPTY(), IS_ALPHANUMERIC()]

#Queue Member
db.queue_members.queue_name.requires = IS_NOT_EMPTY()
db.queue_members.interface.requires = IS_NOT_EMPTY()
db.queue_members.membername.requires = IS_NOT_EMPTY()

#Fax
db.f_fax.nome.requires = IS_NOT_EMPTY()
db.f_fax.email.requires = IS_EMAIL()
db.f_fax.numero.requires = IS_NOT_EMPTY()





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