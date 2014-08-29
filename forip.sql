--
-- PostgreSQL database dump -- MANAGER FORIP
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;


--
-- Name: cdr; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE cdr (
    calldate timestamp with time zone DEFAULT now() NOT NULL,
    clid character varying(80) DEFAULT ''::character varying NOT NULL,
    src character varying(80) DEFAULT ''::character varying NOT NULL,
    dst character varying(80) DEFAULT ''::character varying NOT NULL,
    dcontext character varying(80) DEFAULT ''::character varying NOT NULL,
    channel character varying(80) DEFAULT ''::character varying NOT NULL,
    dstchannel character varying(80) DEFAULT ''::character varying NOT NULL,
    lastapp character varying(80) DEFAULT ''::character varying NOT NULL,
    lastdata character varying(80) DEFAULT ''::character varying NOT NULL,
    duration bigint DEFAULT (0)::bigint NOT NULL,
    billsec bigint DEFAULT (0)::bigint NOT NULL,
    disposition character varying(45) DEFAULT ''::character varying NOT NULL,
    amaflags bigint DEFAULT (0)::bigint NOT NULL,
    accountcode character varying(20) DEFAULT ''::character varying NOT NULL,
    uniqueid character varying(32) DEFAULT ''::character varying NOT NULL,
    userfield character varying(255) DEFAULT ''::character varying NOT NULL,
    linkedid character varying(32)
);


ALTER TABLE public.cdr OWNER TO forip;

--
-- Name: extensions; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE extensions (
    id integer NOT NULL,
    context character varying(20) NOT NULL,
    exten character varying(40) NOT NULL,
    priority integer NOT NULL,
    app character varying(20) NOT NULL,
    appdata character varying(128)
);


ALTER TABLE public.extensions OWNER TO forip;

--
-- Name: extensions_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE extensions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.extensions_id_seq OWNER TO forip;

--
-- Name: extensions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE extensions_id_seq OWNED BY extensions.id;


--
-- Name: f_agenda; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_agenda (
    id integer NOT NULL,
    empresa character varying(15) NOT NULL,
    telefone character varying(20) NOT NULL,
    contato character varying(50),
    departamento character varying(50),
    particular boolean NOT NULL,
    ramal character varying(10)
);


ALTER TABLE public.f_agenda OWNER TO forip;

--
-- Name: f_agenda_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_agenda_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_agenda_id_seq OWNER TO forip;

--
-- Name: f_agenda_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_agenda_id_seq OWNED BY f_agenda.id;


--
-- Name: f_aplicacao_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_aplicacao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_aplicacao_id_seq OWNER TO forip;

--
-- Name: f_aplicacao; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_aplicacao (
    id integer DEFAULT nextval('f_aplicacao_id_seq'::regclass) NOT NULL,
    id_ramalvirtual integer NOT NULL,
    cadeado_ativo boolean NOT NULL,
    cadeado_senha character varying(10),
    cs_ativo boolean NOT NULL,
    cs_chamadaexterna boolean NOT NULL,
    cs_chamadainterna boolean NOT NULL,
    cs_numero integer DEFAULT 0,
    cs_excecao character varying(255),
    voicemail_ativo boolean NOT NULL,
    voicemail_email character varying(100),
    voicemail_senha integer DEFAULT 0,
    agenda_cadastro boolean NOT NULL,
    agenda_senha integer DEFAULT 0
);


ALTER TABLE public.f_aplicacao OWNER TO forip;

--
-- Name: f_autenticacao; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_autenticacao (
    id integer NOT NULL,
    tecnologia character varying(10) NOT NULL,
    usuario character varying(20) NOT NULL,
    acao character varying(20) NOT NULL,
    horario timestamp without time zone NOT NULL,
    ip character varying(30)
);


ALTER TABLE public.f_autenticacao OWNER TO forip;

--
-- Name: f_autenticacao_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_autenticacao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_autenticacao_id_seq OWNER TO forip;

--
-- Name: f_autenticacao_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_autenticacao_id_seq OWNED BY f_autenticacao.id;


--
-- Name: f_bilhetes_chamadas_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_bilhetes_chamadas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_bilhetes_chamadas_id_seq OWNER TO forip;

--
-- Name: f_bilhetes_chamadas; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_bilhetes_chamadas (
    id integer DEFAULT nextval('f_bilhetes_chamadas_id_seq'::regclass) NOT NULL,
    id_tronco integer DEFAULT 0 NOT NULL,
    origem character varying NOT NULL,
    destino character varying NOT NULL,
    linked_id character varying NOT NULL,
    horario timestamp without time zone NOT NULL,
    status character varying NOT NULL,
    tarifacao double precision DEFAULT 0 NOT NULL,
    tempo integer NOT NULL,
    id_empresa integer NOT NULL,
    id_destino integer DEFAULT 0 NOT NULL,
    gravacao boolean NOT NULL,
    atendido character varying(10),
    nome_origem character varying(20),
    departamento character varying(50),
    transbordo character varying(5),
    arquivo_gravacao character varying(50)
);


ALTER TABLE public.f_bilhetes_chamadas OWNER TO forip;

--
-- Name: f_creditos_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_creditos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_creditos_id_seq OWNER TO forip;

--
-- Name: f_creditos; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_creditos (
    id integer DEFAULT nextval('f_creditos_id_seq'::regclass) NOT NULL,
    tipo character varying(1),
    id_responsavel integer,
    local_fixo integer,
    local_celular integer,
    ddd_fixo integer,
    ddd_celular integer,
    ddi integer,
    f0300 integer
);


ALTER TABLE public.f_creditos OWNER TO forip;

--
-- Name: f_ddr_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_ddr_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_ddr_id_seq OWNER TO forip;

--
-- Name: f_ddr; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_ddr (
    id integer DEFAULT nextval('f_ddr_id_seq'::regclass) NOT NULL,
    ddr character varying NOT NULL,
    id_ramalvirtual integer NOT NULL
);


ALTER TABLE public.f_ddr OWNER TO forip;

--
-- Name: f_departamentos_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_departamentos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_departamentos_id_seq OWNER TO forip;

SET default_with_oids = true;

--
-- Name: f_departamentos; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_departamentos (
    id integer DEFAULT nextval('f_departamentos_id_seq'::regclass) NOT NULL,
    departamento character varying(50) NOT NULL,
    id_empresa integer,
    mostrar boolean DEFAULT true NOT NULL
);


ALTER TABLE public.f_departamentos OWNER TO forip;

--
-- Name: f_destinos_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_destinos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_destinos_id_seq OWNER TO forip;

SET default_with_oids = false;

--
-- Name: f_destinos; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_destinos (
    id integer DEFAULT nextval('f_destinos_id_seq'::regclass) NOT NULL,
    tipo_chamada character varying NOT NULL,
    expressao character varying NOT NULL,
    destino character varying NOT NULL,
    tamanho_max integer NOT NULL,
    tarifado boolean NOT NULL,
    portabilidade boolean NOT NULL,
    mostrar boolean DEFAULT true NOT NULL
);


ALTER TABLE public.f_destinos OWNER TO forip;

--
-- Name: f_desvios_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_desvios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_desvios_id_seq OWNER TO forip;

--
-- Name: f_desvios; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_desvios (
    id integer DEFAULT nextval('f_desvios_id_seq'::regclass) NOT NULL,
    id_ramalvirtual integer NOT NULL,
    tipo_desvio character varying(30) NOT NULL,
    dia_semana character varying(30) NOT NULL,
    horario_inicio character varying(20) NOT NULL,
    numero character varying(20) NOT NULL,
    horario_fim character varying(5)
);


ALTER TABLE public.f_desvios OWNER TO forip;

--
-- Name: f_direcionamento_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_direcionamento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_direcionamento_id_seq OWNER TO forip;

--
-- Name: f_direcionamento; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_direcionamento (
    id integer DEFAULT nextval('f_direcionamento_id_seq'::regclass) NOT NULL,
    origem character varying(20) NOT NULL,
    ddr character varying(10) NOT NULL,
    ramal_virtual character varying(10) NOT NULL
);


ALTER TABLE public.f_direcionamento OWNER TO forip;

--
-- Name: f_empresa_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_empresa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_empresa_id_seq OWNER TO forip;

--
-- Name: f_empresa; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_empresa (
    id integer DEFAULT nextval('f_empresa_id_seq'::regclass) NOT NULL,
    empresa character varying(50) NOT NULL,
    mostrar boolean DEFAULT true NOT NULL
);


ALTER TABLE public.f_empresa OWNER TO forip;



--
-- Name: f_fax; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_fax (
    id integer NOT NULL,
    nome character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    numero character varying(10) NOT NULL
);


ALTER TABLE public.f_fax OWNER TO forip;

--
-- Name: f_fax_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_fax_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_fax_id_seq OWNER TO forip;

--
-- Name: f_fax_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_fax_id_seq OWNED BY f_fax.id;


--
-- Name: f_grupo_destinos_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_grupo_destinos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_grupo_destinos_id_seq OWNER TO forip;

--
-- Name: f_grupo_destinos; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_grupo_destinos (
    id integer DEFAULT nextval('f_grupo_destinos_id_seq'::regclass) NOT NULL,
    id_destinos character varying(255) NOT NULL,
    grupo_destino character varying(30) NOT NULL
);


ALTER TABLE public.f_grupo_destinos OWNER TO forip;

--
-- Name: f_horario_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_horario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_horario_id_seq OWNER TO forip;

--
-- Name: f_horario; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_horario (
    id integer DEFAULT nextval('f_horario_id_seq'::regclass) NOT NULL,
    dia_semana character varying(30) NOT NULL,
    horario character varying(20) NOT NULL,
    acao_negativa character varying(100) NOT NULL,
    descricao character varying(50) NOT NULL
);


ALTER TABLE public.f_horario OWNER TO forip;

--
-- Name: f_listas_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_listas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_listas_id_seq OWNER TO forip;

SET default_with_oids = true;

--
-- Name: f_listas; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_listas (
    id integer DEFAULT nextval('f_listas_id_seq'::regclass) NOT NULL,
    numero character varying(20) NOT NULL,
    descricao character varying(50) NOT NULL,
    categoria character varying(50) NOT NULL,
    objeto character varying(20) NOT NULL,
    tipo character varying(20) NOT NULL
);


ALTER TABLE public.f_listas OWNER TO forip;

SET default_with_oids = false;






--
-- Name: f_parametros_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_parametros_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_parametros_id_seq OWNER TO forip;

--
-- Name: f_parametros; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_parametros (
    id integer DEFAULT nextval('f_parametros_id_seq'::regclass) NOT NULL,
    empresa character varying(100) NOT NULL,
    tempo_chamada_externa integer NOT NULL,
    tempo_chamada_interna integer NOT NULL,
    gravacao_geral boolean NOT NULL,
    endereco_smtp character varying(100),
    usuario_smtp character varying(100),
    senha_smtp character varying(100),
    porta_smtp integer DEFAULT 0,
    ssl_smtp boolean,
    email_admin character varying(100),
    faixa_ip_interna text,
    endereco_ip_externo character varying(20),
    endereco_host_externo character varying(100),
    toque_diferenciado boolean,
    toque_diff_sipheader character varying(100),
    spy_senha character varying(4),
    spy_ramal_proibe_monitora text,
    spy_ramal_espiao text,
    tamanho_pin integer DEFAULT 0,
    fuso_horario character varying(3) NOT NULL,
    credito_dia character varying(2) NOT NULL,
    ura_antes_horario boolean NOT NULL,
    bloqueio_chamadacobrar boolean NOT NULL,
    tempo_chamada_transf integer NOT NULL,
    rechamada boolean NOT NULL,
    pin_temporario character varying(4) DEFAULT 0
);


ALTER TABLE public.f_parametros OWNER TO forip;

--
-- Name: f_pin_temporario; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_pin_temporario (
    id integer NOT NULL,
    pin character varying(20) NOT NULL,
    nome character varying(20) NOT NULL,
    ramal_fisico character varying(20) NOT NULL,
    "timestamp" character varying(32) NOT NULL,
    uniqueid character varying(32) NOT NULL
);


ALTER TABLE public.f_pin_temporario OWNER TO forip;

--
-- Name: f_pin_temporario_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_pin_temporario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_pin_temporario_id_seq OWNER TO forip;

--
-- Name: f_pin_temporario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_pin_temporario_id_seq OWNED BY f_pin_temporario.id;


--
-- Name: f_portabilidade_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_portabilidade_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_portabilidade_id_seq OWNER TO forip;

--
-- Name: f_portabilidade; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_portabilidade (
    id integer DEFAULT nextval('f_portabilidade_id_seq'::regclass) NOT NULL,
    endereco character varying(100) NOT NULL,
    usuario character varying(50) NOT NULL,
    senha character varying(50) NOT NULL,
    ativo boolean NOT NULL,
    tempo_timeout integer NOT NULL
);


ALTER TABLE public.f_portabilidade OWNER TO forip;

--
-- Name: f_portabilidade_blacklist; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_portabilidade_blacklist (
    id integer NOT NULL,
    numero character varying(20) NOT NULL,
    operadora character varying(10) NOT NULL
);


ALTER TABLE public.f_portabilidade_blacklist OWNER TO forip;

--
-- Name: f_portabilidade_blacklist_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_portabilidade_blacklist_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_portabilidade_blacklist_id_seq OWNER TO forip;

--
-- Name: f_portabilidade_blacklist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_portabilidade_blacklist_id_seq OWNED BY f_portabilidade_blacklist.id;


--
-- Name: f_portabilidade_consulta; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_portabilidade_consulta (
    id integer NOT NULL,
    horario timestamp with time zone NOT NULL,
    numero character varying(20) NOT NULL,
    operadora character varying(10) NOT NULL,
    uniqueid character varying(32) NOT NULL,
    externa boolean NOT NULL
);


ALTER TABLE public.f_portabilidade_consulta OWNER TO forip;

--
-- Name: f_portabilidade_consulta_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_portabilidade_consulta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_portabilidade_consulta_id_seq OWNER TO forip;

--
-- Name: f_portabilidade_consulta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_portabilidade_consulta_id_seq OWNED BY f_portabilidade_consulta.id;


--
-- Name: f_prov_empresa; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_prov_empresa (
    id integer NOT NULL,
    proxy character varying(30) NOT NULL,
    dns character varying(30) NOT NULL,
    ntp character varying(30) NOT NULL,
    empresa character varying(30) NOT NULL
);


ALTER TABLE public.f_prov_empresa OWNER TO forip;

--
-- Name: f_prov_empresa_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_prov_empresa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_prov_empresa_id_seq OWNER TO forip;

--
-- Name: f_prov_empresa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_prov_empresa_id_seq OWNED BY f_prov_empresa.id;


--
-- Name: f_prov_equipamento; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_prov_equipamento (
    id integer NOT NULL,
    fabricante character varying(30) NOT NULL,
    modelo character varying(30) NOT NULL,
    linha integer NOT NULL
);


ALTER TABLE public.f_prov_equipamento OWNER TO forip;

--
-- Name: f_prov_equipamento_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_prov_equipamento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_prov_equipamento_id_seq OWNER TO forip;

--
-- Name: f_prov_equipamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_prov_equipamento_id_seq OWNED BY f_prov_equipamento.id;


--
-- Name: f_prov_mac; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_prov_mac (
    id integer NOT NULL,
    id_equipamento integer NOT NULL,
    id_empresa integer NOT NULL,
    mac character varying(30) NOT NULL,
    ip character varying(30),
    mascara character varying(30),
    gateway character varying(30),
    vlan integer
);


ALTER TABLE public.f_prov_mac OWNER TO forip;

--
-- Name: f_prov_mac_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_prov_mac_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_prov_mac_id_seq OWNER TO forip;

--
-- Name: f_prov_mac_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_prov_mac_id_seq OWNED BY f_prov_mac.id;


--
-- Name: f_prov_ramal; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_prov_ramal (
    id integer NOT NULL,
    id_mac integer NOT NULL,
    ramal character varying(10) NOT NULL,
    linha integer NOT NULL
);


ALTER TABLE public.f_prov_ramal OWNER TO forip;

--
-- Name: f_prov_ramal_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_prov_ramal_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_prov_ramal_id_seq OWNER TO forip;

--
-- Name: f_prov_ramal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_prov_ramal_id_seq OWNED BY f_prov_ramal.id;


--
-- Name: f_ramal_virtual_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_ramal_virtual_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_ramal_virtual_id_seq OWNER TO forip;

--
-- Name: f_ramal_virtual; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_ramal_virtual (
    id integer DEFAULT nextval('f_ramal_virtual_id_seq'::regclass) NOT NULL,
    tecnologia character varying(10) NOT NULL,
    ramal_fisico character varying(20) NOT NULL,
    id_departamento integer NOT NULL,
    ramal_virtual character varying(10) NOT NULL,
    gravacao boolean,
    blacklist boolean,
    mesa_fop2 boolean,
    chamadas_simultaneas integer NOT NULL,
    id_grupo_destinos integer,
    nome character varying(20) NOT NULL,
    bina_interno character varying(10) NOT NULL,
    bina_externo character varying(10) NOT NULL,
    credito boolean NOT NULL
);


ALTER TABLE public.f_ramal_virtual OWNER TO forip;

--
-- Name: f_rastreamento; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_rastreamento (
    id integer NOT NULL,
    channel character varying(50) NOT NULL,
    linked_id character varying(50) NOT NULL,
    id_acao integer NOT NULL,
    horario character varying(20) NOT NULL,
    origem character varying(20) NOT NULL,
    destino character varying(20) NOT NULL,
    valor character varying(255)
);


ALTER TABLE public.f_rastreamento OWNER TO forip;

--
-- Name: f_rastreamento_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_rastreamento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_rastreamento_id_seq OWNER TO forip;

--
-- Name: f_rastreamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_rastreamento_id_seq OWNED BY f_rastreamento.id;


--
-- Name: f_rotas; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_rotas (
    id integer NOT NULL,
    rota character varying(1) NOT NULL,
    id_tronco integer NOT NULL,
    prioridade integer NOT NULL,
    id_destino character varying(255) NOT NULL,
    exclui_antes integer,
    adiciona_antes character varying,
    adiciona_depois character varying,
    id_empresa character varying(30) NOT NULL,
    id_tarifacao integer NOT NULL,
    id_horario integer NOT NULL,
    add_csp boolean NOT NULL
);


ALTER TABLE public.f_rotas OWNER TO forip;

--
-- Name: f_rotas_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_rotas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_rotas_id_seq OWNER TO forip;

--
-- Name: f_rotas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_rotas_id_seq OWNED BY f_rotas.id;


--
-- Name: f_saldos_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_saldos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_saldos_id_seq OWNER TO forip;

--
-- Name: f_saldos; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_saldos (
    id integer DEFAULT nextval('f_saldos_id_seq'::regclass) NOT NULL,
    responsavel character varying(10) NOT NULL,
    tipo_origem character varying(1) NOT NULL,
    datahora character varying(20) NOT NULL,
    tempo integer NOT NULL,
    uniqueid character varying(32) NOT NULL,
    tipo character varying(1) NOT NULL,
    tipo_chamada character varying NOT NULL
);


ALTER TABLE public.f_saldos OWNER TO forip;



--
-- Name: f_tarifacao_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_tarifacao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_tarifacao_id_seq OWNER TO forip;

--
-- Name: f_tarifacao; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_tarifacao (
    id integer DEFAULT nextval('f_tarifacao_id_seq'::regclass) NOT NULL,
    tarifacao character varying(30) NOT NULL,
    passo character varying(10) NOT NULL,
    valor double precision DEFAULT 0.00 NOT NULL
);


ALTER TABLE public.f_tarifacao OWNER TO forip;

--
-- Name: f_tipo_desvios_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_tipo_desvios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_tipo_desvios_id_seq OWNER TO forip;

--
-- Name: f_troncos_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_troncos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_troncos_id_seq OWNER TO forip;

--
-- Name: f_troncos; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_troncos (
    id integer DEFAULT nextval('f_troncos_id_seq'::regclass) NOT NULL,
    tronco character varying(20) NOT NULL,
    dispositivo character varying(30) NOT NULL,
    chamadas_simultaneas integer NOT NULL,
    qtde_max_minutos integer DEFAULT 0,
    transbordo integer DEFAULT 0,
    csp integer,
    ddd integer,
    prefixo integer,
    chave integer,
    habilitado boolean NOT NULL,
    ciclo_conta integer,
    ramal_principal character varying(10) NOT NULL,
    ura boolean NOT NULL,
    add_zero boolean NOT NULL,
    id_empresa integer NOT NULL,
    mostrar boolean DEFAULT true NOT NULL
);


ALTER TABLE public.f_troncos OWNER TO forip;

--
-- Name: f_troncos_fisicos_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_troncos_fisicos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_troncos_fisicos_id_seq OWNER TO forip;

--
-- Name: f_troncos_fisicos; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_troncos_fisicos (
    id integer DEFAULT nextval('f_troncos_fisicos_id_seq'::regclass) NOT NULL,
    id_tronco integer NOT NULL,
    dispositivo character varying(30) NOT NULL
);


ALTER TABLE public.f_troncos_fisicos OWNER TO forip;

--
-- Name: f_ura; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_ura (
    id integer NOT NULL,
    ramal_principal character varying(10) NOT NULL,
    ura text NOT NULL
);


ALTER TABLE public.f_ura OWNER TO forip;

--
-- Name: f_ura_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_ura_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_ura_id_seq OWNER TO forip;

--
-- Name: f_ura_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_ura_id_seq OWNED BY f_ura.id;


--
-- Name: f_usuarios; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE f_usuarios (
    id integer NOT NULL,
    pin character varying(20) NOT NULL,
    id_departamento integer DEFAULT 0 NOT NULL,
    nome character varying(20) NOT NULL,
    gravacao boolean NOT NULL,
    blacklist boolean NOT NULL,
    id_grupo_destinos integer DEFAULT 0 NOT NULL,
    credito boolean NOT NULL
);


ALTER TABLE public.f_usuarios OWNER TO forip;

--
-- Name: f_usuarios_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE f_usuarios_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.f_usuarios_id_seq OWNER TO forip;

--
-- Name: f_usuarios_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE f_usuarios_id_seq OWNED BY f_usuarios.id;


--
-- Name: fisico_dahdi_khomp; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE fisico_dahdi_khomp (
    id integer NOT NULL,
    tecnologia character varying(512),
    porta character varying(512),
    context character varying(512)
);


ALTER TABLE public.fisico_dahdi_khomp OWNER TO forip;

--
-- Name: fisico_dahdi_khomp_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE fisico_dahdi_khomp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fisico_dahdi_khomp_id_seq OWNER TO forip;

--
-- Name: fisico_dahdi_khomp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE fisico_dahdi_khomp_id_seq OWNED BY fisico_dahdi_khomp.id;


--
-- Name: fisico_sip_iax; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE fisico_sip_iax (
    id integer NOT NULL,
    usuario character varying(512),
    secret character varying(512),
    tecnologia character varying(512),
    type_f character varying(512),
    host_f character varying(512),
    context character varying(512),
    qualify character(1),
    disallow text,
    allow text,
    nat character(1),
    aut_externa character(1),
    tronco character(1),
    extras text,
    register character(1)
);


ALTER TABLE public.fisico_sip_iax OWNER TO forip;

--
-- Name: fisico_sip_iax_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE fisico_sip_iax_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fisico_sip_iax_id_seq OWNER TO forip;

--
-- Name: fisico_sip_iax_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE fisico_sip_iax_id_seq OWNED BY fisico_sip_iax.id;


--
-- Name: iax; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE iax (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    username character varying(30),
    type character varying(6) NOT NULL,
    secret character varying(50),
    md5secret character varying(32),
    dbsecret character varying(100),
    notransfer character varying(10) DEFAULT 'yes'::character varying,
    inkeys character varying(100),
    outkeys character varying(100),
    auth character varying(100) DEFAULT 'plaintext'::character varying NOT NULL,
    accountcode character varying(100),
    amaflags character varying(100),
    callerid character varying(100),
    context character varying(100) NOT NULL,
    defaultip character varying(15),
    host character varying(31) DEFAULT 'dynamic'::character varying NOT NULL,
    language character(5),
    mailbox character varying(50),
    deny character varying(95),
    permit character varying(95),
    qualify character varying(4) DEFAULT 'yes'::character varying,
    disallow character varying(100) DEFAULT 'all'::character varying NOT NULL,
    allow character varying(100) DEFAULT 'gsm'::character varying NOT NULL,
    ipaddr character varying(15) DEFAULT ''::character varying,
    port integer DEFAULT 0,
    regseconds integer DEFAULT 0,
    requirecalltoken character varying DEFAULT 'no'::character varying NOT NULL
);


ALTER TABLE public.iax OWNER TO forip;

--
-- Name: iax_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE iax_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.iax_id_seq OWNER TO forip;

--
-- Name: iax_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE iax_id_seq OWNED BY iax.id;


--
-- Name: meetme; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE meetme (
    id integer NOT NULL,
    confno character varying(80) NOT NULL,
    starttime timestamp with time zone,
    endtime timestamp with time zone,
    pin character varying(20),
    opts character varying(100),
    adminpin character varying(20),
    adminopts character varying(100),
    members integer NOT NULL,
    maxusers integer NOT NULL,
    atributo character varying(30)
);


ALTER TABLE public.meetme OWNER TO forip;

--
-- Name: meetme_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE meetme_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.meetme_id_seq OWNER TO forip;

--
-- Name: meetme_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE meetme_id_seq OWNED BY meetme.id;


--
-- Name: meetme_maxusers_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE meetme_maxusers_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.meetme_maxusers_seq OWNER TO forip;

--
-- Name: meetme_maxusers_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE meetme_maxusers_seq OWNED BY meetme.maxusers;


--
-- Name: meetme_members_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE meetme_members_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.meetme_members_seq OWNER TO forip;

--
-- Name: meetme_members_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE meetme_members_seq OWNED BY meetme.members;


--
-- Name: queue_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE queue_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.queue_id_seq OWNER TO postgres;

--
-- Name: queue; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE queue (
    name character varying(128) NOT NULL,
    musiconhold character varying(128),
    announce character varying(128),
    context character varying(128),
    timeout bigint,
    monitor_join boolean,
    monitor_format character varying(128),
    queue_youarenext character varying(128),
    queue_thereare character varying(128),
    queue_callswaiting character varying(128),
    queue_holdtime character varying(128),
    queue_minutes character varying(128),
    queue_seconds character varying(128),
    queue_lessthan character varying(128),
    queue_thankyou character varying(128),
    queue_reporthold character varying(128),
    announce_frequency bigint,
    announce_round_seconds bigint,
    announce_holdtime character varying(128),
    retry bigint,
    wrapuptime bigint,
    maxlen bigint,
    servicelevel bigint,
    strategy character varying(128),
    joinempty character varying(128),
    leavewhenempty character varying(128),
    eventmemberstatus boolean,
    eventwhencalled boolean,
    reportholdtime boolean,
    memberdelay bigint,
    weight bigint,
    timeoutrestart boolean,
    setinterfacevar boolean,
    atributo character varying(30),
    ringinuse character varying(5),
    id integer DEFAULT nextval('queue_id_seq'::regclass)
);


ALTER TABLE public.queue OWNER TO forip;

--
-- Name: queue_log; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE queue_log (
    id integer NOT NULL,
    "time" timestamp without time zone DEFAULT now() NOT NULL,
    callid character varying(50) NOT NULL,
    queuename character varying(50) NOT NULL,
    agent character varying(50) NOT NULL,
    event character varying(20) NOT NULL,
    data1 character varying(50) NOT NULL,
    data2 character varying(50) NOT NULL,
    data3 character varying(50) NOT NULL,
    data4 character varying(50) NOT NULL,
    data5 character varying(50) NOT NULL
);


ALTER TABLE public.queue_log OWNER TO forip;

--
-- Name: queue_log_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE queue_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.queue_log_id_seq OWNER TO forip;

--
-- Name: queue_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE queue_log_id_seq OWNED BY queue_log.id;


--
-- Name: queue_members_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE queue_members_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.queue_members_id_seq OWNER TO forip;

--
-- Name: queue_members; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE queue_members (
    queue_name character varying(128) NOT NULL,
    interface character varying(128) NOT NULL,
    penalty bigint,
    membername character varying(40),
    paused integer,
    uniqueid bigint NOT NULL,
    id integer DEFAULT nextval('queue_members_id_seq'::regclass)
);


ALTER TABLE public.queue_members OWNER TO forip;

--
-- Name: queue_members_uniqueid_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE queue_members_uniqueid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.queue_members_uniqueid_seq OWNER TO forip;

--
-- Name: queue_members_uniqueid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE queue_members_uniqueid_seq OWNED BY queue_members.uniqueid;


--
-- Name: sip; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE sip (
    id integer NOT NULL,
    name character varying(80) DEFAULT ''::character varying NOT NULL,
    accountcode character varying(20),
    amaflags character varying(7),
    callgroup character varying(10),
    callerid character varying(80),
    canreinvite character varying(3) DEFAULT 'yes'::character varying,
    context character varying(80) DEFAULT 'ramais'::character varying,
    defaultip character varying(45),
    dtmfmode character varying(7) DEFAULT 'RFC2833'::character varying,
    fromuser character varying(80),
    fromdomain character varying(80),
    host character varying(31) DEFAULT 'dynamic'::character varying NOT NULL,
    insecure character varying(20),
    language character varying(2),
    mailbox character varying(50),
    md5secret character varying(80),
    nat character varying(29) DEFAULT 'no'::character varying NOT NULL,
    permit character varying(95),
    deny character varying(95),
    mask character varying(95),
    pickupgroup character varying(10),
    port character varying(5) DEFAULT ''::character varying NOT NULL,
    qualify character varying(3) DEFAULT 'yes'::character varying,
    restrictcid character varying(1),
    rtptimeout character varying(3),
    rtpholdtimeout character varying(3),
    secret character varying(80),
    type character varying DEFAULT 'friend'::character varying NOT NULL,
    disallow character varying(100) DEFAULT 'all'::character varying,
    allow character varying(100) DEFAULT 'ulaw;alaw'::character varying,
    musiconhold character varying(100),
    regseconds bigint DEFAULT (0)::bigint NOT NULL,
    ipaddr character varying(45) DEFAULT ''::character varying NOT NULL,
    regexten character varying(80) DEFAULT ''::character varying NOT NULL,
    cancallforward character varying(3) DEFAULT 'yes'::character varying,
    lastms integer DEFAULT 0 NOT NULL,
    defaultuser character varying(80),
    fullcontact character varying(80),
    regserver character varying(30),
    useragent character varying(255),
    tronco boolean NOT NULL
);


ALTER TABLE public.sip OWNER TO forip;

--
-- Name: sip_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE sip_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sip_id_seq OWNER TO forip;

--
-- Name: sip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE sip_id_seq OWNED BY sip.id;


--
-- Name: sipregs; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE sipregs (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    ipaddr character varying(45),
    port character varying(5),
    regseconds bigint,
    defaultuser character varying(80),
    fullcontact character varying(80),
    regserver character varying(30),
    useragent character varying(255),
    lastms integer,
    username character varying(80)
);


ALTER TABLE public.sipregs OWNER TO forip;

--
-- Name: sipregs_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE sipregs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sipregs_id_seq OWNER TO forip;

--
-- Name: sipregs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE sipregs_id_seq OWNED BY sipregs.id;


--
-- Name: teste_query; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE teste_query (
    query character varying(60)
);


ALTER TABLE public.teste_query OWNER TO forip;

--
-- Name: view_queue_log; Type: VIEW; Schema: public; Owner: forip
--

CREATE VIEW view_queue_log AS
 SELECT queue_log.id,
    queue_log."time",
    queue_log.callid,
    queue_log.queuename,
    queue_log.agent,
    queue_log.event,
    queue_log.data1,
    queue_log.data2,
    queue_log.data3,
    queue_log.data4,
    queue_log.data5,
        CASE
            WHEN ((queue_log.event)::text ~~ 'COMPLETE%'::text) THEN 'ATENDIDA'::character varying
            WHEN ((queue_log.event)::text = 'ABANDON'::text) THEN 'ABANDONADA'::character varying
            WHEN ((queue_log.event)::text = 'TRANSFER'::text) THEN 'TRANSFERIDA'::character varying
            WHEN ((queue_log.event)::text = 'ENTERQUEUE'::text) THEN 'ENTRANTE'::character varying
            ELSE queue_log.event
        END AS evento
   FROM queue_log;


ALTER TABLE public.view_queue_log OWNER TO forip;

--
-- Name: voicemail; Type: TABLE; Schema: public; Owner: forip; Tablespace: 
--

CREATE TABLE voicemail (
    uniqueid integer NOT NULL,
    customer_id bigint DEFAULT (0)::bigint NOT NULL,
    context character varying(50) DEFAULT ''::character varying NOT NULL,
    mailbox bigint DEFAULT (0)::bigint NOT NULL,
    password character varying(4) DEFAULT '0'::character varying NOT NULL,
    fullname character varying(50) DEFAULT ''::character varying NOT NULL,
    email character varying(50) DEFAULT ''::character varying NOT NULL,
    pager character varying(50) DEFAULT ''::character varying NOT NULL,
    stamp timestamp(6) without time zone
);


ALTER TABLE public.voicemail OWNER TO forip;

--
-- Name: voicemail_id_seq; Type: SEQUENCE; Schema: public; Owner: forip
--

CREATE SEQUENCE voicemail_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voicemail_id_seq OWNER TO forip;

--
-- Name: voicemail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: forip
--

ALTER SEQUENCE voicemail_id_seq OWNED BY voicemail.uniqueid;




--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY extensions ALTER COLUMN id SET DEFAULT nextval('extensions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_agenda ALTER COLUMN id SET DEFAULT nextval('f_agenda_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_autenticacao ALTER COLUMN id SET DEFAULT nextval('f_autenticacao_id_seq'::regclass);




--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_fax ALTER COLUMN id SET DEFAULT nextval('f_fax_id_seq'::regclass);



--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_pin_temporario ALTER COLUMN id SET DEFAULT nextval('f_pin_temporario_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_portabilidade_blacklist ALTER COLUMN id SET DEFAULT nextval('f_portabilidade_blacklist_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_portabilidade_consulta ALTER COLUMN id SET DEFAULT nextval('f_portabilidade_consulta_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_prov_empresa ALTER COLUMN id SET DEFAULT nextval('f_prov_empresa_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_prov_equipamento ALTER COLUMN id SET DEFAULT nextval('f_prov_equipamento_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_prov_mac ALTER COLUMN id SET DEFAULT nextval('f_prov_mac_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_prov_ramal ALTER COLUMN id SET DEFAULT nextval('f_prov_ramal_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_rastreamento ALTER COLUMN id SET DEFAULT nextval('f_rastreamento_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_rotas ALTER COLUMN id SET DEFAULT nextval('f_rotas_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_ura ALTER COLUMN id SET DEFAULT nextval('f_ura_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY f_usuarios ALTER COLUMN id SET DEFAULT nextval('f_usuarios_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY fisico_dahdi_khomp ALTER COLUMN id SET DEFAULT nextval('fisico_dahdi_khomp_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY fisico_sip_iax ALTER COLUMN id SET DEFAULT nextval('fisico_sip_iax_id_seq'::regclass);


--
--

ALTER TABLE ONLY iax ALTER COLUMN id SET DEFAULT nextval('iax_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY meetme ALTER COLUMN id SET DEFAULT nextval('meetme_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY queue_log ALTER COLUMN id SET DEFAULT nextval('queue_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY sip ALTER COLUMN id SET DEFAULT nextval('sip_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY sipregs ALTER COLUMN id SET DEFAULT nextval('sipregs_id_seq'::regclass);


--
-- Name: uniqueid; Type: DEFAULT; Schema: public; Owner: forip
--

ALTER TABLE ONLY voicemail ALTER COLUMN uniqueid SET DEFAULT nextval('voicemail_id_seq'::regclass);







-- Data for Name: f_horario; Type: TABLE DATA; Schema: public; Owner: forip
--

COPY f_horario (id, dia_semana, horario, acao_negativa, descricao) FROM stdin;
1	mon,tue,wed,thu,fri,sat,sun	00:00-23:59		Horario Geral
\.


--
-- Name: f_horario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: forip
--

SELECT pg_catalog.setval('f_horario_id_seq', 1, true);




--
-- Data for Name: f_parametros; Type: TABLE DATA; Schema: public; Owner: forip
--

COPY f_parametros (id, empresa, tempo_chamada_externa, tempo_chamada_interna, gravacao_geral, endereco_smtp, usuario_smtp, senha_smtp, porta_smtp, ssl_smtp, email_admin, faixa_ip_interna, endereco_ip_externo, endereco_host_externo, toque_diferenciado, toque_diff_sipheader, spy_senha, spy_ramal_proibe_monitora, spy_ramal_espiao, tamanho_pin, fuso_horario, credito_dia, ura_antes_horario, bloqueio_chamadacobrar, tempo_chamada_transf, rechamada, pin_temporario) FROM stdin;
1	Forip Tecnologia	60	10	f				\N	f		192.168.100.0/255.255.255.0\r\n192.168.1.0/255.255.255.0		forip.noip.me	f		1234		8011|8031|8061|8041	4	-3	01	f	f	15	t	20
\.


--
-- Name: f_parametros_id_seq; Type: SEQUENCE SET; Schema: public; Owner: forip
--

SELECT pg_catalog.setval('f_parametros_id_seq', 1, false);



--
-- Data for Name: f_portabilidade; Type: TABLE DATA; Schema: public; Owner: forip
--

insert into f_portabilidade (endereco, usuario, senha, ativo, tempo_timeout) values ('http://lnpcluster.sippulse.com:9090', 'adaldeia', '#4Ld31A%', true, 30);


--
-- Data for Name: f_destinos; Type: TABLE DATA; Schema: public; Owner: forip
--

INSERT INTO f_destinos VALUES (1, 'LOCAL_FIXO', '[2-5]XXXXXXX', 'Local Fixo', 9, true, true, true);
INSERT INTO f_destinos VALUES (2, 'LOCAL_CELULAR', '9[456789]XXXXXXX', 'Local Celular', 10, true, true, true);
INSERT INTO f_destinos VALUES (4, 'DDD_FIXO', '[1-9][1-9][2345]XXXXXXX', 'DDD Fixo', 11, true, false, true);
INSERT INTO f_destinos VALUES (5, 'DDD_CELULAR', '[1-9][1-9][456789]XXXXXXX', 'DDD Celular', 15, true, false, true);
INSERT INTO f_destinos VALUES (6, 'DDI', '0XXXXXXXXXXX.', 'DDI', 20, true, false, true);
INSERT INTO f_destinos VALUES (8, '0300', '0300XXXXXX.', '0300', 15, true, false, true);
INSERT INTO f_destinos VALUES (9, 'DDD_CELULAR', '3499724376', 'DDD Celular', 11, true, false, true);
INSERT INTO f_destinos VALUES (10, 'RAMAL', '[0-2]XXXXXX', 'Entroncamento', 8, false, false, true);
INSERT INTO f_destinos VALUES (13, 'EMERGENCIA', '10XXX', 'Emergencia', 6, false, false, true);
INSERT INTO f_destinos VALUES (11, 'RAMAL', 'XXXXXX', 'TellFree', 7, false, false, true);
INSERT INTO f_destinos VALUES (7, '0800', '0800XXXXXX.', '0800', 15, false, false, true);
INSERT INTO f_destinos VALUES (3, 'DDD_CELULAR', '[1-9][1-9]9[456789]XXXXXXX', 'DDD Celular', 15, true, false, true);
INSERT INTO f_destinos VALUES (21, 'teste', '456', 'teste', 5, true, false, false);


--
-- Alterando sequence
--

alter sequence f_destinos_id_seq restart 22;






--
-- Data for Name: f_tarifacao; Type: TABLE DATA; Schema: public; Owner: forip
--

COPY f_tarifacao (id, tarifacao, passo, valor) FROM stdin;
1	Padrao	30/6	0.0
\.



--
-- Name: F_destinos_expressao_key; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_destinos
    ADD CONSTRAINT "F_destinos_expressao_key" UNIQUE (expressao);


--
-- Name: F_destinos_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_destinos
    ADD CONSTRAINT "F_destinos_pkey" PRIMARY KEY (id);


--
-- Name: F_rotas_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_rotas
    ADD CONSTRAINT "F_rotas_pkey" PRIMARY KEY (id);


--
-- Name: F_troncos_descricao_key; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_troncos
    ADD CONSTRAINT "F_troncos_descricao_key" UNIQUE (tronco);


--
-- Name: F_troncos_fisicos_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_troncos_fisicos
    ADD CONSTRAINT "F_troncos_fisicos_pkey" PRIMARY KEY (id);


--
-- Name: F_troncos_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_troncos
    ADD CONSTRAINT "F_troncos_pkey" PRIMARY KEY (id);












--
-- Name: extensions_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY extensions
    ADD CONSTRAINT extensions_pkey PRIMARY KEY (id);


--
-- Name: f_agenda_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_agenda
    ADD CONSTRAINT f_agenda_pkey PRIMARY KEY (id);


--
-- Name: f_bilhete_chamada_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_bilhetes_chamadas
    ADD CONSTRAINT f_bilhete_chamada_pkey PRIMARY KEY (id);


--
-- Name: f_ddr_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_ddr
    ADD CONSTRAINT f_ddr_pkey PRIMARY KEY (id);


--
-- Name: f_departamentos_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_departamentos
    ADD CONSTRAINT f_departamentos_pkey PRIMARY KEY (id);


--
-- Name: f_desvios_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_desvios
    ADD CONSTRAINT f_desvios_pkey PRIMARY KEY (id);


--
-- Name: f_direcionamento_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_direcionamento
    ADD CONSTRAINT f_direcionamento_pkey PRIMARY KEY (id);





--
-- Name: f_empresa_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_empresa
    ADD CONSTRAINT f_empresa_pkey PRIMARY KEY (id);


--
-- Name: f_fax_numero_key; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_fax
    ADD CONSTRAINT f_fax_numero_key UNIQUE (numero);


--
-- Name: f_fax_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_fax
    ADD CONSTRAINT f_fax_pkey PRIMARY KEY (id);


--
-- Name: f_grupo_destinos_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_grupo_destinos
    ADD CONSTRAINT f_grupo_destinos_pkey PRIMARY KEY (id);


--
-- Name: f_horario_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_horario
    ADD CONSTRAINT f_horario_pkey PRIMARY KEY (id);


--
-- Name: f_listas_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_listas
    ADD CONSTRAINT f_listas_pkey PRIMARY KEY (id);





--
-- Name: f_parametros_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_parametros
    ADD CONSTRAINT f_parametros_pkey PRIMARY KEY (id);


--
-- Name: f_permissao_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_aplicacao
    ADD CONSTRAINT f_permissao_pkey PRIMARY KEY (id);


--
-- Name: f_pin_temporario_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_pin_temporario
    ADD CONSTRAINT f_pin_temporario_pkey PRIMARY KEY (id);


--
-- Name: f_portabilidade_blacklist_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_portabilidade_blacklist
    ADD CONSTRAINT f_portabilidade_blacklist_pkey PRIMARY KEY (id);


--
-- Name: f_portabilidade_consulta_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_portabilidade_consulta
    ADD CONSTRAINT f_portabilidade_consulta_pkey PRIMARY KEY (id);


--
-- Name: f_portabilidade_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_portabilidade
    ADD CONSTRAINT f_portabilidade_pkey PRIMARY KEY (id);


--
-- Name: f_prov_empresa_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_prov_empresa
    ADD CONSTRAINT f_prov_empresa_pkey PRIMARY KEY (id);


--
-- Name: f_prov_equipamento_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_prov_equipamento
    ADD CONSTRAINT f_prov_equipamento_pkey PRIMARY KEY (id);


--
-- Name: f_prov_mac_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_prov_mac
    ADD CONSTRAINT f_prov_mac_pkey PRIMARY KEY (id);


--
-- Name: f_prov_ramal_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_prov_ramal
    ADD CONSTRAINT f_prov_ramal_pkey PRIMARY KEY (id);


--
-- Name: f_ramal_virtual_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_ramal_virtual
    ADD CONSTRAINT f_ramal_virtual_pkey PRIMARY KEY (id);


--
-- Name: f_rastreamento_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_rastreamento
    ADD CONSTRAINT f_rastreamento_pkey PRIMARY KEY (id);





--
-- Name: f_tarifacao_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_tarifacao
    ADD CONSTRAINT f_tarifacao_pkey PRIMARY KEY (id);


--
-- Name: f_ura_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_ura
    ADD CONSTRAINT f_ura_pkey PRIMARY KEY (id);


--
-- Name: f_ura_ramal_principal_key; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_ura
    ADD CONSTRAINT f_ura_ramal_principal_key UNIQUE (ramal_principal);


--
-- Name: f_usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_usuarios
    ADD CONSTRAINT f_usuarios_pkey PRIMARY KEY (id);


--
-- Name: firstkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY f_autenticacao
    ADD CONSTRAINT firstkey PRIMARY KEY (id);


--
-- Name: fisico_dahdi_khomp_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY fisico_dahdi_khomp
    ADD CONSTRAINT fisico_dahdi_khomp_pkey PRIMARY KEY (id);


--
-- Name: fisico_sip_iax_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY fisico_sip_iax
    ADD CONSTRAINT fisico_sip_iax_pkey PRIMARY KEY (id);


--
-- Name: iax_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY iax
    ADD CONSTRAINT iax_pkey PRIMARY KEY (name);


--
-- Name: iax_username_key; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY iax
    ADD CONSTRAINT iax_username_key UNIQUE (username);


--
-- Name: meetme_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY meetme
    ADD CONSTRAINT meetme_pkey PRIMARY KEY (id);


--
-- Name: queue_id_key; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY queue
    ADD CONSTRAINT queue_id_key UNIQUE (id);


--
-- Name: queue_log_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY queue_log
    ADD CONSTRAINT queue_log_pkey PRIMARY KEY (id);


--
-- Name: queue_member_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY queue_members
    ADD CONSTRAINT queue_member_pkey PRIMARY KEY (queue_name, interface);


--
-- Name: queue_members_id_key; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY queue_members
    ADD CONSTRAINT queue_members_id_key UNIQUE (id);


--
-- Name: queue_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY queue
    ADD CONSTRAINT queue_pkey PRIMARY KEY (name);


--
-- Name: sip_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY sip
    ADD CONSTRAINT sip_pkey PRIMARY KEY (id);


--
-- Name: sipregs_pkey; Type: CONSTRAINT; Schema: public; Owner: forip; Tablespace: 
--

ALTER TABLE ONLY sipregs
    ADD CONSTRAINT sipregs_pkey PRIMARY KEY (id);







--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

