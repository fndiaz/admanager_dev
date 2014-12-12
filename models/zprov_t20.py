# -*- coding: utf-8 -*-

#########################################################################
## Provisionamento T20
#########################################################################

def escreve_t20(dado):
	print "%s - %s" %(dado.prov_equipamento.modelo, dado.prov_mac.mac)
	con2=db((Prov_mac.id == Prov_ramal.id_mac) & (Prov_mac.mac == dado.prov_mac.mac)).count()
	print con2

	arq = open('/var/www/provisionamento/%s.cfg'%(dado.prov_mac.mac),'w')

	con3 =db(Prov_ramal.id_mac == dado.prov_mac.id).select()
	for x in con3:
		query=(x.ramal == Ramal_virtual.ramal_virtual) & (Ramal_virtual.ramal_fisico == Fisico.usuario)
		if db(query).isempty():
			arq.write('####RAMAL %s NAO EXISTE#####\n' %(x.ramal))
			return (False, x.ramal)
		aut=db(query).select(Fisico.usuario, Fisico.secret, Ramal_virtual.nome)
		print x
		print aut[0]

		arq.write('[account]\n')
		arq.write('path=/yealink/config/voip/sipAccount0.cfg\n')
		arq.write('Enable = 1\n')
		arq.write('DisplayName = %s\n' %(aut[0].f_ramal_virtual['nome']))
		arq.write('UserName = %s\n' %(aut[0].fisico_sip_iax['usuario']))
		arq.write('AuthName = %s\n' %(aut[0].fisico_sip_iax['usuario']))
		arq.write('password = %s\n' %(aut[0].fisico_sip_iax['secret']))
		arq.write('SIPServerHost = %s\n' %(dado.prov_rede.proxy))
		arq.write('SIPServerPort = 5060\n')
		arq.write('SIPListenPort = 5060\n')
		arq.write('Expire = 3600\n')
		arq.write('UseOutboundProxy = 0\n')
		arq.write('OutboundHost =\n')
		arq.write('OutboundPort = 5060\n')
		arq.write('EnableSTUN = 0\n\n')
	
	arq.write('Transport = 0\n')
	arq.write('BakOutboundHost = \n')
	arq.write('BakOutboundPort = 5060\n')
	arq.write('proxy-require = \n')
	arq.write('AnonymousCall = 0\n')
	arq.write('RejectAnonymousCall = 0\n')
	arq.write('Expire = 3600\n')
	arq.write('SIPListenPort = 5060\n')
	arq.write('Enable 100Rel = 0\n')
	arq.write('precondition = 0\n')
	arq.write('SubscribeRegister = 0\n')
	arq.write('SubscribeMWI = 0\n')
	arq.write('CIDSource = 0\n')
	arq.write('EnableSessionTimer = 0\n')
	arq.write('SessionExpires = \n')
	arq.write('SessionRefresher = 0\n')
	arq.write('EnableUserEqualPhone = 0\n')
	arq.write('srtp_encryption = 0\n')
	arq.write('ptime = 20\n')
	arq.write('ShareLine = \n')
	arq.write('dialoginfo_callpickup = \n')
	arq.write('MissedCallLog = 1\n')
	arq.write('AutoAnswer = 0\n')
	arq.write('AnonymousCall_OnCode = \n')
	arq.write('AnonymousCall_OffCode = \n')
	arq.write('AnonymousReject_OnCode = \n')
	arq.write('AnonymousReject_OffCode = \n')
	arq.write('BLANumber =\n')
	arq.write('conf-type = 0\n')
	arq.write('conf-uri = \n')
	arq.write('BlfListCode =\n')
	arq.write('SubscribeACDExpire= 3600\n')
	arq.write('SubscribeMWIToVM = \n')
	arq.write('SIPServerType =\n\n')
	arq.write('[ memory12 ]\n')
	arq.write('path = /config/vpPhone/vpPhone.ini\n')
	arq.write('#Set Memory key2\n')
	arq.write('Line = 1\n')
	arq.write('Value = \n')
	arq.write('type =\n')
	arq.write('PickupValue = \n')
	arq.write('DKtype = 15\n')
	arq.write('XMLPhoneBook =\n\n')
	arq.write('[ memory13 ]\n')
	arq.write('path = /config/vpPhone/vpPhone.ini\n')
	arq.write('#Set Memory key2\n')
	arq.write('Line = 1\n')
	arq.write('Value = \n')
	arq.write('type =\n')
	arq.write('PickupValue = \n')
	arq.write('DKtype = 15\n')
	arq.write('XMLPhoneBook =\n\n')
	arq.write('[ Time ]\n')
	arq.write('path = /config/Setting/Setting.cfg\n')
	arq.write('TimeZone = -3\n')
	arq.write('TimeZoneName = Brazil(DST)\n')
	arq.write('TimeServer1 = %s\n' %(dado.prov_rede.ntp))
	arq.write('TimeServer2 = \n')
	arq.write('Interval = 1000\n')
	arq.write('#Set daylight saving time.SummerTime 0 means disable,1 means enable, 2 means automatic\n')
	arq.write('SummerTime = 2\n')
	arq.write('StartTime = \n')
	arq.write('EndTime = \n')
	arq.write('TimeFormat = \n')
	arq.write('DateFormat = \n')
	arq.write('OffSetTime = \n')
	arq.write('DSTTimeType = \n\n')
	arq.write('[ WAN ]\n')
	arq.write('path = /config/Network/Network.cfg\n')
	arq.write('#WANType:0:DHCP,1:PPPoE,2:StaticIP\n')
	if dado.prov_mac.ip == "" or dado.prov_mac.ip == None:
		arq.write('WANType = 0\n')
	else:
		arq.write('WANType = 2\n')
	arq.write('WANStaticIP = %s\n' %(dado.prov_mac.ip))
	arq.write('WANSubnetMask = %s\n' %(dado.prov_mac.mascara))
	arq.write('WANDefaultGateway = %s\n' %(dado.prov_mac.gateway))
	arq.write('[ DNS ]\n')
	arq.write('path = /config/Network/Network.cfg\n')
	arq.write('PrimaryDNS = %s\n' %(dado.prov_rede.dns))
	arq.write('SecondaryDNS = \n\n')
	arq.write('[ Features ]\n')
	arq.write('path = /config/Features/Phone.cfg\n')
	arq.write('Call_Waiting = 1\n')
	arq.write('Hotlinenumber = \n')
	arq.write('BusyToneDelay = \n')
	arq.write('LCD_Logo =\n')
	arq.write('DND_Code = \n')
	arq.write('Refuse_Code = \n')
	arq.write('DND_On_Code = \n')
	arq.write('DND_Off_Code = \n')
	arq.write('ButtonSoundOn = 1\n')
	arq.write('CallCompletion = 0\n')
	arq.write('AllowIntercom  = 1\n')
	arq.write('IntercomMute  = 0\n')
	arq.write('IntercomTone  = 1\n')
	arq.write('IntercomBarge  = 1\n')
	arq.write('Call_WaitingTone = 1\n')
	arq.write('Hotlinedelay = 4\n')
	arq.write('SendKeySoundOn = 1\n')
	arq.write('BroadsoftFeatureKeySync = 0\n')
	arq.write('PswPrefix =\n')
	arq.write('PswLength =\n')
	arq.write('PswDialEnable = 0\n')
	arq.write('HistorySaveDisplay = 1\n')
	arq.write('SaveCallHistory = 1\n')
	arq.write('PswPrefix =\n')
	arq.write('PswLength =\n')
	arq.write('PswDialEnable = 0\n')
	arq.write('HistorySaveDisplay = 1\n')
	arq.write('SaveCallHistory = 1\n')
	arq.write('ButtonSoundOn = 1\n\n')
	arq.write('[ DTMF ]\n')
	arq.write('path = /config/voip/sipAccount0.cfg\n')
	arq.write('DTMFInbandTransfer = 1\n')
	arq.write('InfoType = 0\n')
	arq.write('DTMFPayload = 101\n\n')
	arq.write('[ autop_mode ]\n')
	arq.write('path = /config/Setting/autop.cfg\n')
	arq.write('mode = 1\n')
	arq.write('schedule_min = \n')
	arq.write('schedule_time = \n')
	arq.write('schedule_time_end = \n')
	arq.write('schedule_dayofweek = \n\n')
	arq.write('[ Lang ]\n')
	arq.write('path = /config/Setting/Setting.cfg\n')
	arq.write('ActiveWebLanguage = Portuguese\n\n')
	arq.write('[ telnet ]\n')
	arq.write('path = /config/Network/Network.cfg\n')
	arq.write('telnet_enable = 1\n\n')
	arq.write('[ VLAN ]\n')
	arq.write('path=/yealink/config/Network/Network.cfg\n')
	if dado.prov_mac.vlan == "" or dado.prov_mac.vlan == None:
		arq.write('ISVLAN = 0\n')
		arq.write('VID =1\n')
	else:
		arq.write('ISVLAN = 1\n')
		arq.write('VID =%s\n' %(dado.prov_mac.vlan))
	arq.write('USRPRIORITY =0\n')
	arq.write('PC_PORT_VLAN_ENABLE =\n')
	arq.write('PC_PORT_VID =\n')
	arq.write('PC_PORT_PRIORITY =\n')
	arq.close()
	return (True, 'ok')