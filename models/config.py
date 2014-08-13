# -*- coding: utf-8 -*-

#########################################################################
## Configuração do Banco de dados
#########################################################################

from gluon.storage import Storage
from datetime import datetime
from pytz import timezone

config = Storage(
        db=Storage(),
        auth=Storage(),
        mail=Storage()
        )

#config.db.uri = "mysql://root:yma2578k@localhost/adm"
config.db.uri = "postgres:pg8000://postgres:123456@127.0.0.1/admanager_dev"
#config.db.uri = "sqlite://hosts.sqlite"
config.db.pool_size = 10
config.db.check_reserved = ['all']
#config.migrate_enable=True
#config.migrate=True

db = DAL(**config.db)

# logging
import logging
logger = logging.getLogger("web2py.admanager")
logger.setLevel(logging.DEBUG)

#auth Rbac
from gluon.tools import Auth

auth = Auth(db, controller="initial", function="user")

#settings
auth.settings.remember_me_form = False
auth.settings.formstyle = "divs"
auth.settings.login_next = URL(a='admanager', c='initial', f='dashboard')
auth.settings.request_reset_password_next = URL('initial', 'login')
auth.settings.logout_next = URL('login?_next=')
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
#auth.settings.formstyle = "divs"
auth.settings.actions_disabled = ['register']

auth.messages.logged_in = 'Bem Vindo' 
auth.messages.logged_out = ''
auth.messages.access_denied = 'Acesso negado! Contate o administrador'
auth.messages.invalid_email = 'email Inválido'
auth.messages.invalid_login = 'Login Inválido'
auth.messages.login_button = "Entrar"

#mail
mail = auth.settings.mailer
mail.settings.server = "zmail.ad2.com.br:587"
mail.settings.sender = "smtp_avisos@ad2.com.br"
mail.settings.login = "smtp_avisos@ad2.com.br:ad2root"


#signals
def notifica(form):
	logger.info("notifica")
	mail.send(
		to="fndiaz02@gmail.com",
		subject="Usuario %(first_name)s pendente" % form.vars,
		message="<html>Voce tem um novo usuario para aprovacao %(first_name)s %(last_name)s </html>" % form.vars
	)

#auth.settings.register_onaccept = notifica
#auth.settings.register_onaccept = funcao


#fields
auth.settings.extra_fields['auth_user'] = [
	Field("ramal", "string"),
	Field("photo", "upload", uploadfolder='/home/fernando/web2py/applications/admanager/static/images/avatar',)]
#	Field("gender", requires=IS_IN_SET(["masculino","feminino"]))
#]

#janrain
#from gluon.contrib.login_methods.rpx_account import use_janrain
#use_janrain(auth, filename="private/janrain.key")

auth.define_tables(username=False)

#genericas views
if request.is_local:
	response.generic_patterns = ['*']

#response
response.title= "Alternativo"
response.marca=""
response.meta.keywords= "chave, outra, e outra"



#if not 'ano' in session:
#    session.ano = '0'

#if not 'mes' in session:
#    session.mes = '0'

#if not 'form_ano' in session:
#    now = datetime.datetime.now()
#    ano = now.year
#    lista=[]
#    for i in range(12):
#        lista.append(ano)
#        ano = ano - 1
#    session.form_ano = lista
