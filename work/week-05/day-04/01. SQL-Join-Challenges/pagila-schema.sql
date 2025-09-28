-- Drop database if exists and create new
DROP DATABASE IF EXISTS sakila_pg;
CREATE DATABASE sakila_pg;

-- Switch connection to new database
\connect sakila_pg;

--
-- Name: mpaa_rating; Type: TYPE
--
CREATE TYPE mpaa_rating AS ENUM (
    'G',
    'PG',
    'PG-13',
    'R',
    'NC-17'
);
ALTER TYPE mpaa_rating OWNER TO postgres;

--
-- Name: year; Type: DOMAIN
--
CREATE DOMAIN year AS integer
	CONSTRAINT year_check CHECK (((VALUE >= 1901) AND (VALUE <= 2155)));
ALTER DOMAIN year OWNER TO postgres;

--
-- Name: customer_customer_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE customer_customer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE customer_customer_id_seq OWNER TO postgres;

SET default_tablespace = '';
SET default_with_oids = false;

--
-- Name: customer; Type: TABLE
--
CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    store_id smallint NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email text,
    address_id smallint NOT NULL,
    activebool boolean DEFAULT true NOT NULL,
    create_date date DEFAULT ('now'::text)::date NOT NULL,
    last_update timestamp with time zone DEFAULT now(),
    active integer
);
ALTER TABLE customer OWNER TO postgres;

--
-- Name: actor_actor_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE actor_actor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE actor_actor_id_seq OWNER TO postgres;

--
-- Name: actor; Type: TABLE
--
CREATE TABLE actor (
    actor_id integer DEFAULT nextval('actor_actor_id_seq'::regclass) NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    last_update timestamp with time zone DEFAULT now() NOT NULL
);
ALTER TABLE actor OWNER TO postgres;

--
-- Name: category_category_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE category_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE category_category_id_seq OWNER TO postgres;

--
-- Name: category; Type: TABLE
--
CREATE TABLE category (
    category_id integer DEFAULT nextval('category_category_id_seq'::regclass) NOT NULL,
    name text NOT NULL,
    last_update timestamp with time zone DEFAULT now() NOT NULL
);
ALTER TABLE category OWNER TO postgres;

--
-- Name: film_film_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE film_film_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE film_film_id_seq OWNER TO postgres;

--
-- Name: film; Type: TABLE
--
CREATE TABLE film (
    film_id integer DEFAULT nextval('film_film_id_seq'::regclass) NOT NULL,
    title text NOT NULL,
    description text,
    release_year year,
    language_id smallint NOT NULL,
    original_language_id smallint,
    rental_duration smallint DEFAULT 3 NOT NULL,
    rental_rate numeric(4,2) DEFAULT 4.99 NOT NULL,
    length smallint,
    replacement_cost numeric(5,2) DEFAULT 19.99 NOT NULL,
    rating mpaa_rating DEFAULT 'G'::mpaa_rating,
    last_update timestamp with time zone DEFAULT now() NOT NULL,
    special_features text[],
    fulltext tsvector NOT NULL
);
ALTER TABLE film OWNER TO postgres;

--
-- Name: film_actor; Type: TABLE
--
CREATE TABLE film_actor (
    actor_id smallint NOT NULL,
    film_id smallint NOT NULL,
    last_update timestamp with time zone DEFAULT now() NOT NULL
);
ALTER TABLE film_actor OWNER TO postgres;

--
-- Name: film_category; Type: TABLE
--
CREATE TABLE film_category (
    film_id smallint NOT NULL,
    category_id smallint NOT NULL,
    last_update timestamp with time zone DEFAULT now() NOT NULL
);
ALTER TABLE film_category OWNER TO postgres;

--
-- Name: address_address_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE address_address_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE address_address_id_seq OWNER TO postgres;

--
-- Name: address; Type: TABLE
--
CREATE TABLE address (
    address_id integer DEFAULT nextval('address_address_id_seq'::regclass) NOT NULL,
    address text NOT NULL,
    address2 text,
    district text NOT NULL,
    city_id smallint NOT NULL,
    postal_code text,
    phone text NOT NULL,
    last_update timestamp with time zone DEFAULT now() NOT NULL
);
ALTER TABLE address OWNER TO postgres;

--
-- Name: city_city_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE city_city_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE city_city_id_seq OWNER TO postgres;

--
-- Name: city; Type: TABLE
--
CREATE TABLE city (
    city_id integer DEFAULT nextval('city_city_id_seq'::regclass) NOT NULL,
    city text NOT NULL,
    country_id smallint NOT NULL,
    last_update timestamp with time zone DEFAULT now() NOT NULL
);
ALTER TABLE city OWNER TO postgres;

--
-- Name: country_country_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE country_country_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE country_country_id_seq OWNER TO postgres;

--
-- Name: country; Type: TABLE
--
CREATE TABLE country (
    country_id integer DEFAULT nextval('country_country_id_seq'::regclass) NOT NULL,
    country text NOT NULL,
    last_update timestamp with time zone DEFAULT now() NOT NULL
);
ALTER TABLE country OWNER TO postgres;

--
-- Name: inventory_inventory_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE inventory_inventory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE inventory_inventory_id_seq OWNER TO postgres;

--
-- Name: inventory; Type: TABLE
--
CREATE TABLE inventory (
    inventory_id integer DEFAULT nextval('inventory_inventory_id_seq'::regclass) NOT NULL,
    film_id smallint NOT NULL,
    store_id smallint NOT NULL,
    last_update timestamp with time zone DEFAULT now() NOT NULL
);
ALTER TABLE inventory OWNER TO postgres;

--
-- Name: language_language_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE language_language_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE language_language_id_seq OWNER TO postgres;

--
-- Name: language; Type: TABLE
--
CREATE TABLE language (
    language_id integer DEFAULT nextval('language_language_id_seq'::regclass) NOT NULL,
    name character(20) NOT NULL,
    last_update timestamp with time zone DEFAULT now() NOT NULL
);
ALTER TABLE language OWNER TO postgres;


--
-- Name: rental_rental_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE rental_rental_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE rental_rental_id_seq OWNER TO postgres;

--
-- Name: rental; Type: TABLE
--
CREATE TABLE rental (
    rental_id integer DEFAULT nextval('rental_rental_id_seq'::regclass) NOT NULL,
    rental_date timestamp with time zone NOT NULL,
    inventory_id integer NOT NULL,
    customer_id smallint NOT NULL,
    return_date timestamp with time zone,
    staff_id smallint NOT NULL,
    last_update timestamp with time zone DEFAULT now() NOT NULL
);
ALTER TABLE rental OWNER TO postgres;

--
-- Name: staff_staff_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE staff_staff_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE staff_staff_id_seq OWNER TO postgres;

--
-- Name: staff; Type: TABLE
--
CREATE TABLE staff (
    staff_id integer DEFAULT nextval('staff_staff_id_seq'::regclass) NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    address_id smallint NOT NULL,
    email text,
    store_id smallint NOT NULL,
    active boolean DEFAULT true NOT NULL,
    username text NOT NULL,
    password text,
    last_update timestamp with time zone DEFAULT now() NOT NULL,
    picture bytea
);
ALTER TABLE staff OWNER TO postgres;

--
-- Name: store_store_id_seq; Type: SEQUENCE
--
CREATE SEQUENCE store_store_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
ALTER TABLE store_store_id_seq OWNER TO postgres;

--
-- Name: store; Type: TABLE
--
CREATE TABLE store (
    store_id integer DEFAULT nextval('store_store_id_seq'::regclass) NOT NULL,
    manager_staff_id smallint NOT NULL,
    address_id smallint NOT NULL,
    last_update timestamp with time zone DEFAULT now() NOT NULL
);
ALTER TABLE store OWNER TO postgres;

--
-- Name: actor actor_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY actor
    ADD CONSTRAINT actor_pkey PRIMARY KEY (actor_id);

--
-- Name: address address_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY address
    ADD CONSTRAINT address_pkey PRIMARY KEY (address_id);

--
-- Name: category category_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY category
    ADD CONSTRAINT category_pkey PRIMARY KEY (category_id);

--
-- Name: city city_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY city
    ADD CONSTRAINT city_pkey PRIMARY KEY (city_id);

--
-- Name: country country_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY country
    ADD CONSTRAINT country_pkey PRIMARY KEY (country_id);

--
-- Name: film_actor film_actor_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY film_actor
    ADD CONSTRAINT film_actor_pkey PRIMARY KEY (actor_id, film_id);

--
-- Name: film_category film_category_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY film_category
    ADD CONSTRAINT film_category_pkey PRIMARY KEY (film_id, category_id);

--
-- Name: film film_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY film
    ADD CONSTRAINT film_pkey PRIMARY KEY (film_id);

--
-- Name: inventory inventory_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY inventory
    ADD CONSTRAINT inventory_pkey PRIMARY KEY (inventory_id);

--
-- Name: language language_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY language
    ADD CONSTRAINT language_pkey PRIMARY KEY (language_id);

--
-- Name: rental rental_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY rental
    ADD CONSTRAINT rental_pkey PRIMARY KEY (rental_id);

--
-- Name: staff staff_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY staff
    ADD CONSTRAINT staff_pkey PRIMARY KEY (staff_id);

--
-- Name: store store_pkey; Type: CONSTRAINT (PK)
--
ALTER TABLE ONLY store
    ADD CONSTRAINT store_pkey PRIMARY KEY (store_id);

--
-- Name: customer customer_address_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY customer
    ADD CONSTRAINT customer_address_id_fkey FOREIGN KEY (address_id) REFERENCES address(address_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: customer customer_store_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY customer
    ADD CONSTRAINT customer_store_id_fkey FOREIGN KEY (store_id) REFERENCES store(store_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: inventory inventory_film_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY inventory
    ADD CONSTRAINT inventory_film_id_fkey FOREIGN KEY (film_id) REFERENCES film(film_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: inventory inventory_store_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY inventory
    ADD CONSTRAINT inventory_store_id_fkey FOREIGN KEY (store_id) REFERENCES store(store_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: film film_language_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY film
    ADD CONSTRAINT film_language_id_fkey FOREIGN KEY (language_id) REFERENCES language(language_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: film film_original_language_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY film
    ADD CONSTRAINT film_original_language_id_fkey FOREIGN KEY (original_language_id) REFERENCES language(language_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: rental rental_customer_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY rental
    ADD CONSTRAINT rental_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: rental rental_inventory_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY rental
    ADD CONSTRAINT rental_inventory_id_fkey FOREIGN KEY (inventory_id) REFERENCES inventory(inventory_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: rental rental_staff_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY rental
    ADD CONSTRAINT rental_staff_id_fkey FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: film_actor film_actor_actor_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY film_actor
    ADD CONSTRAINT film_actor_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES actor(actor_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: film_actor film_actor_film_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY film_actor
    ADD CONSTRAINT film_actor_film_id_fkey FOREIGN KEY (film_id) REFERENCES film(film_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: film_category film_category_category_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY film_category
    ADD CONSTRAINT film_category_category_id_fkey FOREIGN KEY (category_id) REFERENCES category(category_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: film_category film_category_film_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY film_category
    ADD CONSTRAINT film_category_film_id_fkey FOREIGN KEY (film_id) REFERENCES film(film_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: staff staff_address_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY staff
    ADD CONSTRAINT staff_address_id_fkey FOREIGN KEY (address_id) REFERENCES address(address_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: staff staff_store_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY staff
    ADD CONSTRAINT staff_store_id_fkey FOREIGN KEY (store_id) REFERENCES store(store_id);

--
-- Name: store store_address_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY store
    ADD CONSTRAINT store_address_id_fkey FOREIGN KEY (address_id) REFERENCES address(address_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: store store_manager_staff_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY store
    ADD CONSTRAINT store_manager_staff_id_fkey FOREIGN KEY (manager_staff_id) REFERENCES staff(staff_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: address address_city_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY address
    ADD CONSTRAINT address_city_id_fkey FOREIGN KEY (city_id) REFERENCES city(city_id) ON UPDATE CASCADE ON DELETE RESTRICT;

--
-- Name: city city_country_id_fkey; Type: CONSTRAINT (FK)
--
ALTER TABLE ONLY city
    ADD CONSTRAINT city_country_id_fkey FOREIGN KEY (country_id) REFERENCES country(country_id) ON UPDATE CASCADE ON DELETE RESTRICT;