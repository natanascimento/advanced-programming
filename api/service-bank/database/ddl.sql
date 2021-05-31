CREATE DATABASE "service_bank";

CREATE SCHEMA "digital_account";

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE digital_account.address (
	address_id uuid DEFAULT uuid_generate_v4() NOT NULL,
	street VARCHAR(40) NOT NULL,
	house_number INT NOT NULL,
	cep INT NOT NULL,
	city VARCHAR(20) NOT NULL,
	"state" VARCHAR(20) NOT NULL,
	country VARCHAR(20) NOT NULL,
	PRIMARY KEY (address_id)
);

CREATE TABLE digital_account.customer (
    customer_id uuid DEFAULT uuid_generate_v4() NOT NULL,
    first_name VARCHAR(15) NOT NULL,
    last_name VARCHAR(15) NOT NULL,
    email VARCHAR(15) NOT NULL,
    date_of_birth TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    registration_date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    address_id uuid,
    PRIMARY KEY (customer_id),
    CONSTRAINT fk_address FOREIGN KEY(address_id) REFERENCES digital_account.address(address_id)
);

CREATE TABLE digital_account.account_type (
    account_type_id uuid DEFAULT uuid_generate_v4() NOT NULL,
    account_type_name VARCHAR(25) NOT NULL,
    PRIMARY KEY (account_type_id)
);

CREATE TABLE digital_account.account (
    account_id uuid DEFAULT uuid_generate_v4() NOT NULL,
    account_number INT NOT NULL,
    account_type_id uuid,
    customer_id uuid,
    date_opened TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    date_closed TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    balance NUMERIC NOT NULL,
    PRIMARY KEY (account_id),
    CONSTRAINT fk_account_type FOREIGN KEY(account_type_id) REFERENCES digital_account.account_type(account_type_id),
    CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES digital_account.customer(customer_id)
);

CREATE TABLE digital_account.transactions (
    transaction_id uuid DEFAULT uuid_generate_v4() NOT NULL,
    account_id uuid,
    transaction_date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    amount NUMERIC NOT NULL,
    balance_account NUMERIC NOT NULL,
    PRIMARY KEY (transaction_id),
    CONSTRAINT fk_account_type FOREIGN KEY(account_id) REFERENCES digital_account.account(account_id)
);

/*Drop all tables*/
DROP TABLE digital_account.customer CASCADE;
DROP TABLE digital_account.account CASCADE;
DROP TABLE digital_account.transations CASCADE;
DROP TABLE digital_account.account_type CASCADE;
DROP TABLE digital_account.address CASCADE;