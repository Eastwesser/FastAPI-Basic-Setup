--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: donuts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.donuts (
    id integer,
    donut character(50),
    description character(500)
);


ALTER TABLE public.donuts OWNER TO postgres;

--
-- Data for Name: donuts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.donuts (id, donut, description) FROM stdin;
1	Chocolate                                         	Classic donut covered in exquisite Belgian chocolate.                                                                                                                                                                                                                                                                                                                                                                                                                                                               
2	Vanilla                                           	Soft donut with a vanilla aroma, perfect for lovers of classics.                                                                                                                                                                                                                                                                                                                                                                                                                                                    
3	White Chocolate                                   	Exquisite donut covered in delicate white chocolate that melts in your mouth.                                                                                                                                                                                                                                                                                                                                                                                                                                       
4	Strawberry                                        	Juicy donut with a filling of fresh strawberries, perfectly complementing the soft dough.                                                                                                                                                                                                                                                                                                                                                                                                                           
5	Pistachio                                         	Refined donut with crushed pistachio nuts, giving it a unique taste and aroma.                                                                                                                                                                                                                                                                                                                                                                                                                                      
6	Blueberry                                         	Aromatic donut with a filling of ripe blueberries, creating a pleasant combination of sweetness and tartness.                                                                                                                                                                                                                                                                                                                                                                                                       
7	Currant                                           	Refreshing donut with a bright filling of currants, uplifting and quenching thirst perfectly.                                                                                                                                                                                                                                                                                                                                                                                                                       
8	Blueberry                                         	Saturated donut with a filling of blueberries, filling each piece with the natural taste of forest berries.                                                                                                                                                                                                                                                                                                                                                                                                         
9	Cherry                                            	Sweet donut with a fragrant filling of ripe cherries, adding bright notes of tartness.                                                                                                                                                                                                                                                                                                                                                                                                                              
10	Red & White                                       	Exquisite donut decorated with red sprinkles on a white glazed coating.                                                                                                                                                                                                                                                                                                                                                                                                                                             
11	Honey                                             	Donut with a delicate honey aroma and sweet yellow topping, immersing you in a festive atmosphere.                                                                                                                                                                                                                                                                                                                                                                                                                  
12	Carnival                                          	Festive donut covered in white chocolate and a blueberry-strawberry topping.                                                                                                                                                                                                                                                                                                                                                                                                                                        
\.


--
-- PostgreSQL database dump complete
--

