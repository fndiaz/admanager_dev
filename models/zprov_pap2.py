# -*- coding: utf-8 -*-

#########################################################################
## Provisionamento PAP2
#########################################################################

def escreve_pap2(dado):
	print "%s - %s" %(dado.prov_equipamento.modelo, dado.prov_mac.mac)
	con2=db((Prov_mac.id == Prov_ramal.id_mac) & (Prov_mac.mac == dado.prov_mac.mac)).count()
	print con2

	arq = open('/var/www/provisionamento/%s.cfg'%(dado.prov_mac.mac),'w')

	arq.write("<?xml version='1.0' encoding='ISO-8859-1'?>\n")
	arq.write("<!-- Provisining PAP2 -->\n")
	arq.write("<flat-profile>\n")
	arq.write("<Resync_Periodic>3600</Resync_Periodic>\n")
	arq.write("<Profile_Rule>http://%s/provisionamento/%s.cfg</Profile_Rule>\n" %(dado.prov_rede.proxy, dado.prov_mac.mac))
	arq.write("<!-- tag case appears to be important -->\n")
	arq.write("<!-- system, system configuration -->\n")
	arq.write("<Admin_Passwd></Admin_Passwd>\n")
	arq.write("<User_Passwd></User_Passwd>\n")
	arq.write("<!-- system, optional network configuration -->\n")
	arq.write("<HostName>Provisionamento</HostName>\n")
	arq.write("<Domain></Domain>\n")
	arq.write("<Primary_DNS>%s</Primary_DNS>\n" %(dado.prov_rede.dns))
	arq.write("<Secondary_DNS></Secondary_DNS>\n")
	arq.write("<DNS_Server_Order>Manual</DNS_Server_Order>\n")
	arq.write("<Primary_NTP_Server>%s</Primary_NTP_Server>\n\n" %(dado.prov_rede.ntp))

	con3 =db(Prov_ramal.id_mac == dado.prov_mac.id).select()
	for x in con3:
		query=(x.ramal == Ramal_virtual.ramal_virtual) & (Ramal_virtual.ramal_fisico == Fisico.usuario)
		if db(query).isempty():
			arq.write('####RAMAL %s NAO EXISTE#####\n' %(x.ramal))
			return (False, x.ramal)
		aut=db(query).select(Fisico.usuario, Fisico.secret, Ramal_virtual.nome)
		print x
		print aut[0]

		arq.write("<Proxy_%s_>%s</Proxy_%s_>\n" %(x.linha, dado.prov_rede.proxy, x.linha))
		arq.write("<Display_Name_%s_>%s</Display_Name_%s_>\n" %(x.linha, aut[0].f_ramal_virtual['nome'], x.linha))
		arq.write("<User_ID_%s_>%s</User_ID_%s_>\n" %(x.linha, aut[0].fisico_sip_iax['usuario'], x.linha))
		arq.write("<Password_%s_>%s</Password_%s_>\n" %(x.linha, aut[0].fisico_sip_iax['secret'], x.linha))
		arq.write("<Dial_Plan_%s_>(*xx.|#xx.|[3469]11|0|00|[2-9]xxxxxx|1xxx[2-9]xxxxxxS0|xxxxxxxxxxxx.)</Dial_Plan_%s_>\n\n" %(x.linha, x.linha))

	arq.write("<Call_Return_Code></Call_Return_Code>\n")
	arq.write("<Blind_Transfer_Code></Blind_Transfer_Code>\n")
	arq.write("<Call_Back_Act_Code></Call_Back_Act_Code>\n")
	arq.write("<Call_Back_Deact_Code></Call_Back_Deact_Code>\n")
	arq.write("<Cfwd_All_Act_Code></Cfwd_All_Act_Code>\n")
	arq.write("<Cfwd_All_Deact_Code></Cfwd_All_Deact_Code>\n")
	arq.write("<Cfwd_Busy_Act_Code></Cfwd_Busy_Act_Code>\n")
	arq.write("<Cfwd_Busy_Deact_Code></Cfwd_Busy_Deact_Code>\n")
	arq.write("<Cfwd_No_Ans_Act_Code></Cfwd_No_Ans_Act_Code>\n")
	arq.write("<Cfwd_No_Ans_Deact_Code></Cfwd_No_Ans_Deact_Code>\n")
	arq.write("<Cfwd_Last_Act_Code></Cfwd_Last_Act_Code>\n")
	arq.write("<Cfwd_Last_Deact_Code></Cfwd_Last_Deact_Code>\n")
	arq.write("<Block_Last_Act_Code></Block_Last_Act_Code>\n")
	arq.write("<Block_Last_Deact_Code></Block_Last_Deact_Code>\n")
	arq.write("<Accept_Last_Act_Code></Accept_Last_Act_Code>\n")
	arq.write("<Accept_Last_Deact_Code></Accept_Last_Deact_Code>\n")
	arq.write("<CW_Act_Code></CW_Act_Code>\n")
	arq.write("<CW_Deact_Code></CW_Deact_Code>\n")
	arq.write("<CW_Per_Call_Act_Code></CW_Per_Call_Act_Code>\n")
	arq.write("<CW_Per_Call_Deact_Code></CW_Per_Call_Deact_Code>\n")
	arq.write("<Block_CID_Act_Code></Block_CID_Act_Code>\n")
	arq.write("<Block_CID_Deact_Code></Block_CID_Deact_Code>\n")
	arq.write("<Block_CID_Per_Call_Act_Code></Block_CID_Per_Call_Act_Code>\n")
	arq.write("<Block_CID_Per_Call_Deact_Code></Block_CID_Per_Call_Deact_Code>\n")
	arq.write("<Block_ANC_Act_Code></Block_ANC_Act_Code>\n")
	arq.write("<Block_ANC_Deact_Code></Block_ANC_Deact_Code>\n")
	arq.write("<DND_Act_Code></DND_Act_Code>\n")
	arq.write("<DND_Deact_Code></DND_Deact_Code>\n")
	arq.write("<CID_Act_Code></CID_Act_Code>\n")
	arq.write("<CID_Deact_Code></CID_Deact_Code>\n")
	arq.write("<CWCID_Act_Code></CWCID_Act_Code>\n")
	arq.write("<CWCID_Deact_Code></CWCID_Deact_Code>\n")
	arq.write("<Dist_Ring_Act_Code></Dist_Ring_Act_Code>\n")
	arq.write("<Dist_Ring_Deact_Code></Dist_Ring_Deact_Code>\n")
	arq.write("<Vertical_Service_Announcement_Codes></Vertical_Service_Announcement_Codes>\n")
	arq.write("<Time_Zone>GMT-03:00</Time_Zone>\n")
	arq.write("<Networking_Service>Bridge</Networking_Service>\n")
	arq.write("<Interdigit_Long_Timer>3</Interdigit_Long_Timer>\n")
	arq.write("<Enable_WAN_Web_Server>Yes</Enable_WAN_Web_Server>\n")
	arq.write("<Web_Management><Web_Utility_Access_HTTP>1</Web_Utility_Access_HTTP></Web_Management>\n\n")

	if dado.prov_mac.ip == "" or dado.prov_mac.ip == None:
		arq.write("<Connection_Type>DHCP</Connection_Type>\n")
		arq.write("<DHCP>Yes</DHCP>\n\n")
	else:
		arq.write("<Connection_Type>Static IP</Connection_Type>\n")
		arq.write("<DHCP>No</DHCP>\n\n")

	arq.write("<Static_IP>%s</Static_IP>\n" %(dado.prov_mac.ip))
	arq.write("<NetMask>%s</NetMask>\n" %(dado.prov_mac.mascara))
	arq.write("<Gateway>%s</Gateway>\n" %(dado.prov_mac.gateway))
	arq.write("</flat-profile>\n")
	arq.close()
	return (True, 'ok')

