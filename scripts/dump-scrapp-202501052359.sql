--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2 (Debian 17.2-1.pgdg120+1)
-- Dumped by pg_dump version 17.0

-- Started on 2025-01-05 23:59:46

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE scrapp;
--
-- TOC entry 3387 (class 1262 OID 17038)
-- Name: scrapp; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE scrapp WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


\connect scrapp

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- TOC entry 3388 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 17049)
-- Name: consultas; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.consultas (
    id_consulta integer NOT NULL,
    fecha_consulta date NOT NULL,
    resultados integer
);


--
-- TOC entry 219 (class 1259 OID 17048)
-- Name: consultas_id_consulta_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.consultas_id_consulta_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3389 (class 0 OID 0)
-- Dependencies: 219
-- Name: consultas_id_consulta_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.consultas_id_consulta_seq OWNED BY public.consultas.id_consulta;


--
-- TOC entry 222 (class 1259 OID 17056)
-- Name: historicos_productos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.historicos_productos (
    id_historico integer NOT NULL,
    id_producto integer NOT NULL,
    id_consulta integer NOT NULL
);


--
-- TOC entry 221 (class 1259 OID 17055)
-- Name: historicos_productos_id_historico_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.historicos_productos_id_historico_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3390 (class 0 OID 0)
-- Dependencies: 221
-- Name: historicos_productos_id_historico_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.historicos_productos_id_historico_seq OWNED BY public.historicos_productos.id_historico;


--
-- TOC entry 218 (class 1259 OID 17040)
-- Name: productos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.productos (
    id_producto integer NOT NULL,
    nombre character varying(255) NOT NULL,
    tipo text
);


--
-- TOC entry 217 (class 1259 OID 17039)
-- Name: productos_id_producto_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.productos_id_producto_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3391 (class 0 OID 0)
-- Dependencies: 217
-- Name: productos_id_producto_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.productos_id_producto_seq OWNED BY public.productos.id_producto;


--
-- TOC entry 3221 (class 2604 OID 17052)
-- Name: consultas id_consulta; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.consultas ALTER COLUMN id_consulta SET DEFAULT nextval('public.consultas_id_consulta_seq'::regclass);


--
-- TOC entry 3222 (class 2604 OID 17059)
-- Name: historicos_productos id_historico; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historicos_productos ALTER COLUMN id_historico SET DEFAULT nextval('public.historicos_productos_id_historico_seq'::regclass);


--
-- TOC entry 3220 (class 2604 OID 17043)
-- Name: productos id_producto; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.productos ALTER COLUMN id_producto SET DEFAULT nextval('public.productos_id_producto_seq'::regclass);


--
-- TOC entry 3379 (class 0 OID 17049)
-- Dependencies: 220
-- Data for Name: consultas; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.consultas VALUES (6, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (7, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (8, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (9, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (10, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (11, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (12, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (13, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (14, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (15, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (16, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (17, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (18, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (19, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (20, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (21, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (22, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (23, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (24, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (25, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (26, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (27, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (28, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (29, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (30, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (31, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (32, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (33, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (34, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (35, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (36, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (37, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (38, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (39, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (40, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (41, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (42, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (43, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (44, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (45, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (46, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (47, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (48, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (49, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (50, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (51, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (52, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (53, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (54, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (55, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (56, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (57, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (58, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (59, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (60, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (61, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (62, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (63, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (64, '2025-01-05', 20);
INSERT INTO public.consultas VALUES (65, '2025-01-05', 224);
INSERT INTO public.consultas VALUES (66, '2025-01-05', 6);
INSERT INTO public.consultas VALUES (67, '2025-01-05', 6);
INSERT INTO public.consultas VALUES (68, '2025-01-05', 6);
INSERT INTO public.consultas VALUES (69, '2025-01-05', 10);
INSERT INTO public.consultas VALUES (70, '2025-01-05', 10);
INSERT INTO public.consultas VALUES (71, '2025-01-05', 10);
INSERT INTO public.consultas VALUES (72, '2025-01-05', 10);
INSERT INTO public.consultas VALUES (73, '2025-01-05', 6);
INSERT INTO public.consultas VALUES (74, '2025-01-05', 6);
INSERT INTO public.consultas VALUES (75, '2025-01-05', 6);
INSERT INTO public.consultas VALUES (76, '2025-01-05', 6);
INSERT INTO public.consultas VALUES (77, '2025-01-05', 6);
INSERT INTO public.consultas VALUES (78, '2025-01-05', 6);
INSERT INTO public.consultas VALUES (79, '2025-01-05', 6);
INSERT INTO public.consultas VALUES (80, '2025-01-05', 6);
INSERT INTO public.consultas VALUES (81, '2025-01-05', 6);


--
-- TOC entry 3381 (class 0 OID 17056)
-- Dependencies: 222
-- Data for Name: historicos_productos; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.historicos_productos VALUES (5, 608, 79);
INSERT INTO public.historicos_productos VALUES (6, 609, 79);
INSERT INTO public.historicos_productos VALUES (7, 610, 79);
INSERT INTO public.historicos_productos VALUES (8, 611, 79);
INSERT INTO public.historicos_productos VALUES (9, 612, 79);
INSERT INTO public.historicos_productos VALUES (10, 613, 79);
INSERT INTO public.historicos_productos VALUES (11, 608, 80);
INSERT INTO public.historicos_productos VALUES (12, 609, 80);
INSERT INTO public.historicos_productos VALUES (13, 610, 80);
INSERT INTO public.historicos_productos VALUES (14, 611, 80);
INSERT INTO public.historicos_productos VALUES (15, 612, 80);
INSERT INTO public.historicos_productos VALUES (16, 613, 80);
INSERT INTO public.historicos_productos VALUES (17, 608, 81);
INSERT INTO public.historicos_productos VALUES (18, 609, 81);
INSERT INTO public.historicos_productos VALUES (19, 610, 81);
INSERT INTO public.historicos_productos VALUES (20, 611, 81);
INSERT INTO public.historicos_productos VALUES (21, 612, 81);
INSERT INTO public.historicos_productos VALUES (22, 613, 81);


--
-- TOC entry 3377 (class 0 OID 17040)
-- Dependencies: 218
-- Data for Name: productos; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.productos VALUES (599, 'Tenis de golf Curry 1 para hombre', 'rebaja');
INSERT INTO public.productos VALUES (600, 'Tenis de golf UA Phantom para hombre', 'rebaja');
INSERT INTO public.productos VALUES (601, 'Tenis de golf UA Charged Draw 2 Spikeless para hombre', 'rebaja');
INSERT INTO public.productos VALUES (602, 'Men''s UA Charged Medal Spikeless Golf Shoes', 'rebaja');
INSERT INTO public.productos VALUES (603, 'Tenis de golf UA Drive Pro para hombre', 'rebaja');
INSERT INTO public.productos VALUES (604, 'Tenis de golf UA Charged Phantom Spikeless para hombre', 'rebaja');
INSERT INTO public.productos VALUES (605, 'Tenis de golf UA Drive Pro LE para hombre', 'rebaja');
INSERT INTO public.productos VALUES (606, 'Tenis de golf UA Drive Pro Spikeless para hombre', 'rango');
INSERT INTO public.productos VALUES (607, 'Tenis de golf UA Phantom Goin'' Under para hombre', 'rebaja');
INSERT INTO public.productos VALUES (608, 'Tenis de béisbol UA Harper 8 Low ST para hombre', 'rebaja');
INSERT INTO public.productos VALUES (609, 'Tenis de béisbol UA Harper 8 Mid RM para hombre', 'rebaja');
INSERT INTO public.productos VALUES (610, 'Men''s UA Yard Low MT Baseball Cleats', 'rebaja');
INSERT INTO public.productos VALUES (611, 'Tenis de béisbol UA Leadoff Mid 3.0 para hombre', 'rango');
INSERT INTO public.productos VALUES (612, 'Tenis de béisbol UA Leadoff Low RM 3.0 para hombre', 'rebaja');
INSERT INTO public.productos VALUES (613, 'Tenis de béisbol UA Leadoff Mid RM para Hombre', 'rebaja');


--
-- TOC entry 3392 (class 0 OID 0)
-- Dependencies: 219
-- Name: consultas_id_consulta_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.consultas_id_consulta_seq', 81, true);


--
-- TOC entry 3393 (class 0 OID 0)
-- Dependencies: 221
-- Name: historicos_productos_id_historico_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.historicos_productos_id_historico_seq', 22, true);


--
-- TOC entry 3394 (class 0 OID 0)
-- Dependencies: 217
-- Name: productos_id_producto_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.productos_id_producto_seq', 613, true);


--
-- TOC entry 3226 (class 2606 OID 17054)
-- Name: consultas consultas_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.consultas
    ADD CONSTRAINT consultas_pkey PRIMARY KEY (id_consulta);


--
-- TOC entry 3228 (class 2606 OID 17061)
-- Name: historicos_productos historicos_productos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historicos_productos
    ADD CONSTRAINT historicos_productos_pkey PRIMARY KEY (id_historico);


--
-- TOC entry 3224 (class 2606 OID 17047)
-- Name: productos productos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT productos_pkey PRIMARY KEY (id_producto);


--
-- TOC entry 3229 (class 2606 OID 17067)
-- Name: historicos_productos fk_consulta; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historicos_productos
    ADD CONSTRAINT fk_consulta FOREIGN KEY (id_consulta) REFERENCES public.consultas(id_consulta) ON DELETE CASCADE;


--
-- TOC entry 3230 (class 2606 OID 17062)
-- Name: historicos_productos fk_producto; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historicos_productos
    ADD CONSTRAINT fk_producto FOREIGN KEY (id_producto) REFERENCES public.productos(id_producto) ON DELETE CASCADE;


-- Completed on 2025-01-05 23:59:46

--
-- PostgreSQL database dump complete
--

