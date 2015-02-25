# -*- coding: utf-8 -*-

#########################################################################
## Provisionamento 310HD
#########################################################################

def escreve_310hd(dado):
	print "%s - %s" %(dado.prov_equipamento.modelo, dado.prov_mac.mac)
	con2=db((Prov_mac.id == Prov_ramal.id_mac) & (Prov_mac.mac == dado.prov_mac.mac)).count()
	print con2

	arq = open('/var/www/provisionamento/%s.cfg'%(dado.prov_mac.mac),'w')

	arq.write('system/type=310HD\n')
	arq.write('system/user_name=admin\n')
	arq.write('system/password=$1$FZ6rOGS1$54ZXSmjh7nod.kXFRyLx70\n')
	arq.write('system/syslog/component/cgi=NONE\n')
	arq.write('system/syslog/component/control_center=NONE\n')
	arq.write('system/syslog/component/kernel=NONE\n')
	arq.write('system/syslog/component/lcd_display=NONE\n')
	arq.write('system/syslog/component/sip_call_control=NONE\n')
	arq.write('system/syslog/component/sip_stack=NONE\n')
	arq.write('system/syslog/component/voip_application=NONE\n')
	arq.write('ystem/syslog/component/watchdog=NONE\n')
	arq.write('system/syslog/component/web_server=NONE\n')
	arq.write('system/syslog/component/ieee802_1x=NONE\n')
	arq.write('system/watchdog/enabled=1\n')
	arq.write('system/syslog/sip_log_filter=0\n')
	arq.write('system/syslog/server_address=0.0.0.0\n')
	arq.write('system/syslog/server_port=514\n')
	arq.write('system/syslog/mode=DISABLE\n\n')

	arq.write('system/ntp/enabled=1\n')
	arq.write('system/ntp/primary_server_address=%s\n' %(dado.prov_rede.ntp))
	arq.write('system/ntp/secondary_server_address=ntp.usp.br\n')
	arq.write('system/ntp/gmt_offset=-0%s:00\n' %(Parametros[1].fuso_horario[1]))
	arq.write('system/ntp/sync_time/days=0\n')
	arq.write('system/ntp/sync_time/hours=12\n\n')

	arq.write('system/daylight_saving/activate=DISABLE\n')
	arq.write('system/daylight_saving/mode=FIXED\n')
	arq.write('system/daylight_saving/start_date/month=1\n')
	arq.write('system/daylight_saving/start_date/day=1\n')
	arq.write('system/daylight_saving/start_date/week=1\n')
	arq.write('system/daylight_saving/start_date/day_of_week=SUNDAY\n')
	arq.write('system/daylight_saving/start_date/hour=0\n')
	arq.write('system/daylight_saving/start_date/minute=0\n')
	arq.write('system/daylight_saving/end_date/month=1\n')
	arq.write('system/daylight_saving/end_date/day=1\n')
	arq.write('system/daylight_saving/end_date/week=1\n')
	arq.write('system/daylight_saving/end_date/day_of_week=SUNDAY\n')
	arq.write('system/daylight_saving/end_date/hour=0\n')
	arq.write('system/daylight_saving/end_date/minute=0\n')
	arq.write('system/daylight_saving/offset=60\n')
	arq.write('system/ntp/time_display_format=24HOUR\n')
	arq.write('system/ldap/enabled=0\n')
	arq.write('system/ldap/server_address=\n')
	arq.write('system/ldap/port=389\n')
	arq.write('system/ldap/user_name=\n')
	arq.write('system/ldap/password=\n')
	arq.write('system/ldap/base=\n')
	arq.write('system/ldap/name_filter=(|(sn=%)(givenname=%)(displayname=%))\n')
	arq.write('system/ldap/name_attrs=sn givenname displayname\n')
	arq.write('system/ldap/number_filter=(|(telephoneNumber=%)(Mobile=%)(homePhone=%)(facsimileTelephoneNumber=%)(ipPhone=%)(pager=%))\n')
	arq.write('system/ldap/display_name=%displayname\n')
	arq.write('system/ldap/number_attrs=telephoneNumber Mobile homePhone  facsimileTelephoneNumber ipPhone pager\n')
	arq.write('system/ldap/max_hits=50\n')
	arq.write('system/ldap/sorting_result=1\n')
	arq.write('system/ldap/predict_text=0\n')
	arq.write('system/ldap/search_timeout=5\n')
	arq.write('system/ldap/ui/use_right_arrow_active_search=0\n')
	arq.write('system/ldap/lookup_incoming_call=0\n')
	arq.write('system/ldap/call_lookup=1\n')
	arq.write('system/ldap/country_code=\n')
	arq.write('system/ldap/area_code=\n')
	arq.write('system/ldap/minimal_name_search_length=0\n')
	arq.write('system/activation_keys/tr069=\n')
	arq.write('system/activation_keys/portuguese_language=dhey5823kmf8j48g\n')
	arq.write('system/activation_keys/amr_coder=\n\n')

	arq.write('provisioning/method=DYNAMIC\n')
	arq.write('system/hot_desking/enabled=0\n')
	arq.write('system/hot_desking/auto_login=\n')
	arq.write('system/hot_desking/action_url_server=\n')
	arq.write('provisioning/firmware/url=http://%s/provisionamento/310HD.img\n' %(dado.prov_rede.proxy))
	arq.write('provisioning/configuration/url=http://%s/provisionamento/%s.cfg\n' %(dado.prov_rede.proxy, dado.prov_mac.mac))
	arq.write('provisioning/period/type=DAILY\n')
	arq.write('provisioning/period/hourly/hours_interval=24\n')
	arq.write('provisioning/period/daily/time=00:00\n')
	arq.write('provisioning/period/weekly/day=SUNDAY\n')
	arq.write('provisioning/period/weekly/time=00:00\n')
	arq.write('provisioning/url_option_value=160\n')
	arq.write('provisioning/random_provisioning_time=120\n')
	arq.write('provisioning/ring_tone_uri=\n')
	arq.write('provisioning/corporate_directory_uri=\n')
	arq.write('provisioning/speed_dial_uri=\n')
	arq.write('provisioning/certificate/private_key_uri=\n')
	arq.write('provisioning/certificate/ca_uri=\n')
	arq.write('provisioning/certificate/private_key_content=\n')
	arq.write('provisioning/certificate/ca_certificate_content=\n')
	arq.write('management/tr069/enabled=0\n')
	arq.write('management/tr069/acs_url=\n')
	arq.write('management/tr069/user_name=\n')
	arq.write('management/tr069/password=\n')
	arq.write('management/tr069/inform/enabled=1\n')
	arq.write('management/tr069/inform/interval=3600\n')
	arq.write('management/tr069/connection_request/user_name=\n')
	arq.write('management/tr069/connection_request/password=\n')
	arq.write('management/telnet/enabled=0\n\n')

	if dado.prov_mac.ip == "" or dado.prov_mac.ip == None:
		arq.write("network/lan_type=DHCP\n")
	else:
		arq.write("network/lan_type=STATIC\n")

	arq.write('network/lan/dhcp/domain_name/enabled=1\n')
	arq.write('network/lan/dhcp/ip_address/enabled=1\n')
	arq.write('network/lan/dhcp/netmask/enabled=1\n')
	arq.write('network/lan/dhcp/gateway/enabled=1\n')
	arq.write('network/lan/dhcp/primary_dns/enabled=1\n')
	arq.write('network/lan/dhcp/secondary_dns/enabled=1\n')
	arq.write('network/lan/fixed_ip/ip_address=%s\n' %(dado.prov_mac.ip))
	arq.write('network/lan/fixed_ip/netmask=%s\n' %(dado.prov_mac.mascara))
	arq.write('network/lan/fixed_ip/gateway=%s\n' %(dado.prov_mac.gateway))
	arq.write('network/lan/fixed_ip/primary_dns=%s\n' %(dado.prov_rede.dns))
	arq.write('network/lan/fixed_ip/secondary_dns=8.8.8.8\n')
	arq.write('network/lan/fixed_ip/domain_name=\n\n')


	if dado.prov_mac.vlan == "" or dado.prov_mac.vlan == None:
		arq.write('network/lan/vlan/mode=DISABLE\n')
		arq.write('network/lan/vlan/period=30\n')
		arq.write('network/lan/vlan/id=0\n')
		arq.write('network/lan/vlan/priority=0\n\n')
	else:
		arq.write('network/lan/vlan/mode=MANUAL\n')
		arq.write('network/lan/vlan/period=30\n')
		arq.write('network/lan/vlan/id=%s\n' %(dado.prov_mac.vlan))
		arq.write('network/lan/vlan/priority=0\n\n')

	arq.write('network/lan/dhcp/ntp/server_list/enabled=1\n')
	arq.write('network/lan/dhcp/ntp/gmt_offset/enabled=0\n')
	arq.write('network/lan/_802_1x/eap_type=DISABLE\n')
	arq.write('network/lan/_802_1x/md5_identity=\n')
	arq.write('network/lan/_802_1x/md5_password=\n')
	arq.write('network/lan/_802_1x/tls_identity=\n')
	arq.write('network/lan/_802_1x/root_ca_url=\n')
	arq.write('network/lan/_802_1x/trust_ca_url=\n')
	arq.write('network/lan/_802_1x/local_ca_url=\n')
	arq.write('network/lan/_802_1x/private_key_url=\n')
	arq.write('network/lan/_802_1x/private_key_password=\n')
	arq.write('network/lan/port_mode=AUTOMATIC\n')
	arq.write('network/pc/port_mode=AUTOMATIC\n')
	arq.write('network/pc_port_mirroring/enabled=0\n\n')



	con3 =db(Prov_ramal.id_mac == dado.prov_mac.id).select()
	for x in con3:
		query=(x.ramal == Ramal_virtual.ramal_virtual) & (Ramal_virtual.ramal_fisico == Fisico.usuario)
		if db(query).isempty():
			arq.write('####RAMAL %s NAO EXISTE#####\n' %(x.ramal))
			return (False, x.ramal)
		aut=db(query).select(Fisico.usuario, Fisico.secret, Ramal_virtual.nome)
		print x
		print aut[0]

		arq.write('voip/line/0/enabled=1\n')
		arq.write('voip/line/0/id=%s\n' %(aut[0].fisico_sip_iax['usuario']))
		arq.write('voip/line/0/description=310HD\n')
		arq.write('voip/line/0/auth_name=%s\n' %(aut[0].fisico_sip_iax['usuario']))
		arq.write('voip/line/0/auth_password=%s\n' %(aut[0].fisico_sip_iax['secret']))
		arq.write('voip/line/0/call_forward/enabled=1\n')
		arq.write('voip/line/0/call_forward/timeout=6\n')
		arq.write('voip/line/0/call_forward/type=NO_REPLY\n')
		arq.write('voip/line/0/call_forward/destination=\n')
		arq.write('voip/line/0/call_forward/active=0\n')
		arq.write('voip/line/0/extension_display=%s\n\n' %(aut[0].f_ramal_virtual['nome']))

	arq.write('voip/audio/gain/additional_speaker_gain=3\n')
	arq.write('voip/audio/gain/tone_signal_level=10\n')
	arq.write('voip/audio/gain/ringer_signal_level=0\n')
	arq.write('voip/audio/gain/handsfree_digital_output_gain=15\n')
	arq.write('voip/audio/gain/handsfree_digital_input_gain=0\n')
	arq.write('voip/audio/gain/handsfree_analog_output_gain=0DB\n')
	arq.write('voip/audio/gain/handsfree_analog_input_gain=PLUS33DB\n')
	arq.write('voip/audio/gain/handset_digital_output_gain=6\n')
	arq.write('voip/audio/gain/handset_digital_input_gain=0\n')
	arq.write('voip/audio/gain/handset_analog_output_gain=MINUS9DB\n')
	arq.write('voip/audio/gain/handset_analog_input_gain=PLUS19_5DB\n')
	arq.write('voip/audio/gain/handset_analog_sidetone_gain=MINUS12DB\n')
	arq.write('voip/audio/gain/headset_digital_output_gain=6\n')
	arq.write('voip/audio/gain/headset_digital_input_gain=0\n')
	arq.write('voip/audio/gain/headset_analog_output_gain=MINUS12DB\n')
	arq.write('voip/audio/gain/headset_analog_input_gain=PLUS10_5DB\n')
	arq.write('voip/audio/gain/headset_analog_sidetone_gain=MINUS12DB\n')
	arq.write('voip/codec/g722_bitrate=G722_64K\n')
	arq.write('voip/codec/g723_bitrate=HIGH\n')
	arq.write('voip/codec/codec_info/0/enabled=1\n')
	arq.write('voip/codec/codec_info/0/name=PCMU\n')
	arq.write('voip/codec/codec_info/0/ptime=20\n')
	arq.write('voip/codec/codec_info/1/enabled=1\n')
	arq.write('voip/codec/codec_info/1/name=G722\n')
	arq.write('voip/codec/codec_info/1/ptime=20\n')
	arq.write('voip/codec/codec_info/2/enabled=0\n')
	arq.write('voip/codec/codec_info/2/name=PCMA\n')
	arq.write('voip/codec/codec_info/2/ptime=20\n')
	arq.write('voip/codec/codec_info/3/enabled=0\n')
	arq.write('voip/codec/codec_info/3/name=G729\n')
	arq.write('voip/codec/codec_info/3/ptime=20\n')
	arq.write('voip/codec/codec_info/4/enabled=0\n')
	arq.write('voip/codec/codec_info/4/name=PCMU\n')
	arq.write('voip/codec/codec_info/4/ptime=30\n')
	arq.write('voip/dialing/timeout=3\n')
	arq.write('voip/dialing/auto_dialing/enabled=0\n')
	arq.write('voip/dialing/auto_dialing/timeout=15\n')
	arq.write('voip/dialing/auto_dialing/destination=0\n')
	arq.write('voip/dialing/phone_number_max_size=19\n')
	arq.write('voip/dialing/dialtone_timeout=30\n')
	arq.write('voip/dialing/warning_tone_timeout=40\n')
	arq.write('voip/dialing/offhook_tone_timeout=120\n')
	arq.write('voip/dialing/unanswered_call_timeout=60\n')
	arq.write('voip/dialing/on_hook_dialing=OPEN_DEFAULT_AUDIO_DEVICE\n\n')

	arq.write('voip/signalling/sip/sdp_include_ptime=0\n')
	arq.write('voip/signalling/sip/transport_protocol=UDP\n')
	arq.write('voip/signalling/sip/port=5060\n')
	arq.write('voip/signalling/sip/proxy_address=%s\n' %(dado.prov_rede.proxy))
	arq.write('voip/signalling/sip/proxy_port=5060\n')
	arq.write('voip/signalling/sip/auth_retries=4\n')
	arq.write('voip/signalling/sip/tls_port=5061\n')
	arq.write('voip/signalling/sip/enable_sips=0\n')
	arq.write('voip/signalling/sip/proxy_timeout=3600\n')
	arq.write('voip/signalling/sip/registration_failed_timeout=60\n')
	arq.write('voip/signalling/sip/sip_registrar/enabled=0\n')
	arq.write('voip/signalling/sip/sip_registrar/port=5060\n')
	arq.write('voip/signalling/sip/sip_registrar/addr=0.0.0.0\n')
	arq.write('voip/signalling/sip/sip_outbound_proxy/enabled=0\n')
	arq.write('voip/signalling/sip/sip_outbound_proxy/port=5060\n')
	arq.write('voip/signalling/sip/sip_outbound_proxy/addr=0.0.0.0\n\n')

	arq.write('voip/signalling/sip/redundant_outbound_proxy/enabled=0\n')
	arq.write('voip/signalling/sip/redundant_outbound_proxy/port=5060\n')
	arq.write('voip/signalling/sip/redundant_outbound_proxy/address=0.0.0.0\n')
	arq.write('voip/signalling/sip/redundant_outbound_proxy/keepalive_period=60\n')
	arq.write('voip/signalling/sip/redundant_outbound_proxy/symmetric_mode=0\n')
	arq.write('voip/signalling/sip/sip_t1=500\n')
	arq.write('voip/signalling/sip/sip_t2=4000\n')
	arq.write('voip/signalling/sip/sip_t4=5000\n')
	arq.write('voip/signalling/sip/subs_no_notify_timer=32000\n')
	arq.write('voip/signalling/sip/sip_invite_timer=32000\n')
	arq.write('voip/signalling/sip/session_timer=1800\n')
	arq.write('voip/signalling/sip/min_session_interval=90\n')
	arq.write('voip/signalling/sip/block_callerid_on_outgoing_calls=0\n')
	arq.write('voip/signalling/sip/anonymous_calls_blocking=0\n')
	arq.write('voip/signalling/sip/proxy_gateway=\n')
	arq.write('voip/signalling/sip/digit_map=\n')
	arq.write('voip/signalling/sip/number_rules=\n')
	arq.write('voip/signalling/sip/use_proxy_ip_port_for_registrar=1\n')
	arq.write('voip/signalling/sip/prack/enabled=1\n')
	arq.write('voip/signalling/sip/rport/enabled=1\n')
	arq.write('voip/signalling/sip/connect_media_on_180=0\n')
	arq.write('voip/signalling/sip/keepalive_options/enabled=0\n')
	arq.write('voip/signalling/sip/keepalive_options/timeout=300\n')
	arq.write('voip/signalling/sip/use_proxy=1\n')
	arq.write('voip/signalling/sip/tos=96\n')
	arq.write('voip/signalling/sip/redundant_proxy/enabled=0\n')
	arq.write('voip/signalling/sip/redundant_proxy/port=5060\n')
	arq.write('voip/signalling/sip/redundant_proxy/address=0.0.0.0\n')
	arq.write('voip/signalling/sip/redundant_proxy/keepalive_period=60\n')
	arq.write('voip/signalling/sip/redundant_proxy/symmetric_mode=0\n')
	arq.write('voip/signalling/sip/display_name_in_registration_msg/enabled=0\n')
	arq.write('voip/signalling/sip/semi_transfer_with_no_cancel/enabled=0\n')
	arq.write('voip/signalling/sip/registrar_ka/enabled=0\n')
	arq.write('voip/signalling/sip/registrar_ka/timeout=60\n')
	arq.write('voip/dialing/allow_calling_self_extension/enabled=0\n')
	arq.write('voip/dialing/dial_complete_key/enabled=1\n')
	arq.write('voip/dialing/dial_complete_key/key=#\n')
	arq.write('voip/media/out_of_band_dtmf=RFC2833\n')
	arq.write('voip/media/srtp/enabled=0\n')
	arq.write('voip/media/srtp/method=AES_CM_128_HMAC_SHA1_32\n')
	arq.write('voip/media/srtp/aria_support_enabled=0\n')
	arq.write('voip/dialing/automatic_disconnect=1\n')
	arq.write('voip/media/dtmf_payload=101\n')
	arq.write('voip/media/rtp_mute_on_hold=1\n')
	arq.write('voip/media/allow_multiple_rtp=0\n')
	arq.write('voip/media/ignore_rfc_2833_packets=1\n')
	arq.write('voip/media/broken_connection_detection=0\n')
	arq.write('voip/media/broken_connection_timeout=10\n')
	arq.write('voip/services/call_waiting/enabled=1\n')
	arq.write('voip/services/call_waiting/sip_reply=QUEUED\n')
	arq.write('voip/services/msg_waiting_ind/enabled=1\n')
	arq.write('voip/services/msg_waiting_ind/subscribe=1\n')
	arq.write('voip/services/msg_waiting_ind/subscribe_port=5060\n')
	arq.write('voip/services/msg_waiting_ind/subscribe_address=192.168.1.1\n')
	arq.write('voip/services/msg_waiting_ind/expiraition_timeout=3600\n')
	arq.write('voip/services/msg_waiting_ind/voice_mail_number=0909\n')
	arq.write('voip/services/msg_waiting_ind/always_send_port=1\n')
	arq.write('voip/services/msg_waiting/stutter_tone_duration=2500\n')
	arq.write('voip/services/busy_lamp_field/enabled=0\n')
	arq.write('voip/services/busy_lamp_field/subscription_period=3600\n')
	arq.write('voip/services/busy_lamp_field/application_server/use_registrar=1\n')
	arq.write('voip/services/busy_lamp_field/application_server/addr=0.0.0.0\n')
	arq.write('voip/services/busy_lamp_field/uri=\n')
	arq.write('voip/services/busy_lamp_field/color_settings=OPTION_2\n')
	arq.write('voip/services/call_pickup/enabled=0\n')
	arq.write('voip/services/call_pickup/access_code=**\n')
	arq.write('voip/services/out_of_service_bahavior=REORDER_TONE\n')
	arq.write('voip/services/electronic_hook_switch/enabled=0\n')
	arq.write('voip/services/conference/mode=LOCAL\n')
	arq.write('voip/services/conference/conf_ms_addr=0.0.0.0\n')
	arq.write('voip/services/reject_code=CODE_603\n')
	arq.write('voip/dialing/secondary_dial_tone/enabled=1\n')
	arq.write('voip/dialing/secondary_dial_tone/key_sequence=9\n')
	arq.write('voip/services/do_not_disturb/enabled=1\n')
	arq.write('voip/media/media_port=4000\n')
	arq.write('voip/media/media_tos=184\n')
	arq.write('voip/audio/jitter_buffer/min_delay=35\n')
	arq.write('voip/audio/jitter_buffer/optimization_factor=7\n')
	arq.write('voip/audio/echo_cancellation/enabled=1\n')
	arq.write('voip/audio/gain/automatic_gain_control/enabled=0\n')
	arq.write('voip/audio/gain/automatic_gain_control/direction=CTL_REMOTE\n')
	arq.write('voip/audio/gain/automatic_gain_control/target_energy=-19\n')
	arq.write('voip/audio/silence_compression/enabled=0\n')
	arq.write('voip/auto_answer/enabled=0\n')
	arq.write('voip/talk_event/enabled=0\n')
	arq.write('voip/headset_only/enabled=0\n')
	arq.write('voip/answer_device=SPEAKER\n')
	arq.write('voip/regional_settings/selected_country=Brazil\n')
	arq.write('voip/regional_settings/use_config_file_values=0\n')
	arq.write('voip/regional_settings/call_progress_tones/0/enabled=1\n')
	arq.write('voip/regional_settings/call_progress_tones/0/name=call_progress_howler_tone_call_waiting_tone_2\n')
	arq.write('voip/regional_settings/call_progress_tones/0/cadence=0\n')
	arq.write('voip/regional_settings/call_progress_tones/0/frequency_a=350\n')
	arq.write('voip/regional_settings/call_progress_tones/0/frequency_b=440\n')
	arq.write('voip/regional_settings/call_progress_tones/0/frequency_a_level=19\n')
	arq.write('voip/regional_settings/call_progress_tones/0/frequency_b_level=19\n')
	arq.write('voip/regional_settings/call_progress_tones/0/tone_on_0=500\n')
	arq.write('voip/regional_settings/call_progress_tones/0/tone_off_0=0\n')
	arq.write('voip/regional_settings/call_progress_tones/0/tone_on_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/0/tone_off_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/0/tone_on_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/0/tone_off_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/0/tone_on_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/0/tone_off_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/1/enabled=1\n')
	arq.write('voip/regional_settings/call_progress_tones/1/name=ringback_tone\n')
	arq.write('voip/regional_settings/call_progress_tones/1/cadence=1\n')
	arq.write('voip/regional_settings/call_progress_tones/1/frequency_a=440\n')
	arq.write('voip/regional_settings/call_progress_tones/1/frequency_b=480\n')
	arq.write('voip/regional_settings/call_progress_tones/1/frequency_a_level=19\n')
	arq.write('voip/regional_settings/call_progress_tones/1/frequency_b_level=19\n')
	arq.write('voip/regional_settings/call_progress_tones/1/tone_on_0=200\n')
	arq.write('voip/regional_settings/call_progress_tones/1/tone_off_0=400\n')
	arq.write('voip/regional_settings/call_progress_tones/1/tone_on_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/1/tone_off_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/1/tone_on_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/1/tone_off_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/1/tone_on_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/1/tone_off_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/2/enabled=1\n')
	arq.write('voip/regional_settings/call_progress_tones/2/name=busy_tone\n')
	arq.write('voip/regional_settings/call_progress_tones/2/cadence=1\n')
	arq.write('voip/regional_settings/call_progress_tones/2/frequency_a=480\n')
	arq.write('voip/regional_settings/call_progress_tones/2/frequency_b=620\n')
	arq.write('voip/regional_settings/call_progress_tones/2/frequency_a_level=24\n')
	arq.write('voip/regional_settings/call_progress_tones/2/frequency_b_level=24\n')
	arq.write('voip/regional_settings/call_progress_tones/2/tone_on_0=50\n')
	arq.write('voip/regional_settings/call_progress_tones/2/tone_off_0=50\n')
	arq.write('voip/regional_settings/call_progress_tones/2/tone_on_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/2/tone_off_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/2/tone_on_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/2/tone_off_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/2/tone_on_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/2/tone_off_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/3/enabled=1\n')
	arq.write('voip/regional_settings/call_progress_tones/3/name=reorder_tone\n')
	arq.write('voip/regional_settings/call_progress_tones/3/cadence=1\n')
	arq.write('voip/regional_settings/call_progress_tones/3/frequency_a=480\n')
	arq.write('voip/regional_settings/call_progress_tones/3/frequency_b=620\n')
	arq.write('voip/regional_settings/call_progress_tones/3/frequency_a_level=24\n')
	arq.write('voip/regional_settings/call_progress_tones/3/frequency_b_level=24\n')
	arq.write('voip/regional_settings/call_progress_tones/3/tone_on_0=25\n')
	arq.write('voip/regional_settings/call_progress_tones/3/tone_off_0=25\n')
	arq.write('voip/regional_settings/call_progress_tones/3/tone_on_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/3/tone_off_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/3/tone_on_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/3/tone_off_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/3/tone_on_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/3/tone_off_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/4/enabled=1\n')
	arq.write('voip/regional_settings/call_progress_tones/4/name=off_hook_warning_tone\n')
	arq.write('voip/regional_settings/call_progress_tones/4/cadence=1\n')
	arq.write('voip/regional_settings/call_progress_tones/4/frequency_a=480\n')
	arq.write('voip/regional_settings/call_progress_tones/4/frequency_b=620\n')
	arq.write('voip/regional_settings/call_progress_tones/4/frequency_a_level=24\n')
	arq.write('voip/regional_settings/call_progress_tones/4/frequency_b_level=24\n')
	arq.write('voip/regional_settings/call_progress_tones/4/tone_on_0=25\n')
	arq.write('voip/regional_settings/call_progress_tones/4/tone_off_0=25\n')
	arq.write('voip/regional_settings/call_progress_tones/4/tone_on_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/4/tone_off_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/4/tone_on_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/4/tone_off_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/4/tone_on_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/4/tone_off_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/5/enabled=1\n')
	arq.write('voip/regional_settings/call_progress_tones/5/name=call_waiting_tone\n')
	arq.write('voip/regional_settings/call_progress_tones/5/cadence=1\n')
	arq.write('voip/regional_settings/call_progress_tones/5/frequency_a=350\n')
	arq.write('voip/regional_settings/call_progress_tones/5/frequency_b=440\n')
	arq.write('voip/regional_settings/call_progress_tones/5/frequency_a_level=13\n')
	arq.write('voip/regional_settings/call_progress_tones/5/frequency_b_level=13\n')
	arq.write('voip/regional_settings/call_progress_tones/5/tone_on_0=30\n')
	arq.write('voip/regional_settings/call_progress_tones/5/tone_off_0=1000\n')
	arq.write('voip/regional_settings/call_progress_tones/5/tone_on_1=30\n')
	arq.write('voip/regional_settings/call_progress_tones/5/tone_off_1=1000\n')
	arq.write('voip/regional_settings/call_progress_tones/5/tone_on_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/5/tone_off_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/5/tone_on_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/5/tone_off_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/6/enabled=1\n')
	arq.write('voip/regional_settings/call_progress_tones/6/name=call_waiting_ringback_tone\n')
	arq.write('voip/regional_settings/call_progress_tones/6/cadence=1\n')
	arq.write('voip/regional_settings/call_progress_tones/6/frequency_a=440\n')
	arq.write('voip/regional_settings/call_progress_tones/6/frequency_b=480\n')
	arq.write('voip/regional_settings/call_progress_tones/6/frequency_a_level=19\n')
	arq.write('voip/regional_settings/call_progress_tones/6/frequency_b_level=19\n')
	arq.write('voip/regional_settings/call_progress_tones/6/tone_on_0=200\n')
	arq.write('voip/regional_settings/call_progress_tones/6/tone_off_0=400\n')
	arq.write('voip/regional_settings/call_progress_tones/6/tone_on_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/6/tone_off_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/6/tone_on_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/6/tone_off_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/6/tone_on_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/6/tone_off_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/7/enabled=1\n')
	arq.write('voip/regional_settings/call_progress_tones/7/name=call_progress_stutter_tone\n')
	arq.write('voip/regional_settings/call_progress_tones/7/cadence=1\n')
	arq.write('voip/regional_settings/call_progress_tones/7/frequency_a=350\n')
	arq.write('voip/regional_settings/call_progress_tones/7/frequency_b=440\n')
	arq.write('voip/regional_settings/call_progress_tones/7/frequency_a_level=19\n')
	arq.write('voip/regional_settings/call_progress_tones/7/frequency_b_level=19\n')
	arq.write('voip/regional_settings/call_progress_tones/7/tone_on_0=25\n')
	arq.write('voip/regional_settings/call_progress_tones/7/tone_off_0=15\n')
	arq.write('voip/regional_settings/call_progress_tones/7/tone_on_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/7/tone_off_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/7/tone_on_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/7/tone_off_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/7/tone_on_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/7/tone_off_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/8/enabled=1\n')
	arq.write('voip/regional_settings/call_progress_tones/8/name=call_progress_howler_tone\n')
	arq.write('voip/regional_settings/call_progress_tones/8/cadence=1\n')
	arq.write('voip/regional_settings/call_progress_tones/8/frequency_a=1400\n')
	arq.write('voip/regional_settings/call_progress_tones/8/frequency_b=2600\n')
	arq.write('voip/regional_settings/call_progress_tones/8/frequency_a_level=0\n')
	arq.write('voip/regional_settings/call_progress_tones/8/frequency_b_level=0\n')
	arq.write('voip/regional_settings/call_progress_tones/8/tone_on_0=10\n')
	arq.write('voip/regional_settings/call_progress_tones/8/tone_off_0=10\n')
	arq.write('voip/regional_settings/call_progress_tones/8/tone_on_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/8/tone_off_1=0\n')
	arq.write('voip/regional_settings/call_progress_tones/8/tone_on_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/8/tone_off_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/8/tone_on_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/8/tone_off_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/9/enabled=1\n')
	arq.write('voip/regional_settings/call_progress_tones/9/name=NULL\n')
	arq.write('voip/regional_settings/call_progress_tones/9/cadence=1\n')
	arq.write('voip/regional_settings/call_progress_tones/9/frequency_a=350\n')
	arq.write('voip/regional_settings/call_progress_tones/9/frequency_b=440\n')
	arq.write('voip/regional_settings/call_progress_tones/9/frequency_a_level=13\n')
	arq.write('voip/regional_settings/call_progress_tones/9/frequency_b_level=13\n')
	arq.write('voip/regional_settings/call_progress_tones/9/tone_on_0=30\n')
	arq.write('voip/regional_settings/call_progress_tones/9/tone_off_0=1000\n')
	arq.write('voip/regional_settings/call_progress_tones/9/tone_on_1=30\n')
	arq.write('voip/regional_settings/call_progress_tones/9/tone_off_1=1000\n')
	arq.write('voip/regional_settings/call_progress_tones/9/tone_on_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/9/tone_off_2=0\n')
	arq.write('voip/regional_settings/call_progress_tones/9/tone_on_3=0\n')
	arq.write('voip/regional_settings/call_progress_tones/9/tone_off_3=0\n')
	arq.write('voip/packet_recording/enabled=0\n')
	arq.write('voip/packet_recording/remote_ip=0.0.0.0\n')
	arq.write('voip/packet_recording/remote_port=50000\n')
	arq.write('voip/packet_recording/rtp_recording/enabled=0\n')
	arq.write('voip/packet_recording/ec_debug_recording/enabled=0\n')
	arq.write('voip/packet_recording/network_recording/enabled=0\n')
	arq.write('voip/packet_recording/tdm_recording/enabled=0\n')
	arq.write('voip/call_list_support_uri=0\n')
	arq.write('personal_settings/language=PORTUGUESE\n')
	arq.write('personal_settings/max_directory_size=700\n')
	arq.write('voip/dialing/speed_dial/double_press/enabled=1\n')
	arq.write('system/aoc/enabled=0\n')
	arq.write('system/aoc/currency=usd\n')
	arq.write('system/aoc/ratio=1\n')
	arq.write('voip/media/srtp/use_MKI=0\n')
	arq.write('voip/media/srtp/MKI_length=1\n')
	arq.write('voip/services/application_server_type=ASTERISK\n')
	arq.write('system/server_lock_error_code=400\n')
	arq.write('system/lock/0/enabled=0\n')
	arq.write('system/lock/0/allow_incoming_calls=0\n')
	arq.write('system/current_user_presence_status/enabled=0\n')
	arq.write('system/action_url/hosts=\n')
	arq.write('system/action_url/send_timeout=10\n')
	arq.write('system/action_url/lock=\n')
	arq.write('system/action_url/unlock=\n')
	arq.write('system/action_url/lock_status=\n')
	arq.write('system/http_server_port=80\n')
	arq.write('system/https_server_port=443\n')
	arq.close()
	return (True, 'ok')


