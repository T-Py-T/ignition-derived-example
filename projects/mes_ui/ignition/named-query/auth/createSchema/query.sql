DO $$

BEGIN

	DROP TABLE IF EXISTS s2credential;
	DROP TABLE IF EXISTS s2person;
	DROP TABLE IF EXISTS s2cardformat;
	DROP TABLE IF EXISTS s2partition;
	
	DROP TABLE IF EXISTS userrole;
	DROP TABLE IF EXISTS role;

	DROP TABLE IF EXISTS credential;
	DROP TABLE IF EXISTS person;
	DROP TABLE IF EXISTS cardformat;
	DROP TABLE IF EXISTS partition;
	
	DROP TABLE IF EXISTS accesslevel;
	DROP TABLE IF EXISTS deviceip;
	DROP TABLE IF EXISTS personcontact;
	DROP TABLE IF EXISTS personothercontact;
	DROP TABLE IF EXISTS personrole;
	DROP TABLE IF EXISTS persontoaccesslevel;
	DROP TABLE IF EXISTS portal;
	DROP TABLE IF EXISTS reader;
	DROP TABLE IF EXISTS s2logactivity;
	DROP TABLE IF EXISTS systeminfo;
	DROP TABLE IF EXISTS threatlevel;
	DROP TABLE IF EXISTS threatlevelgroup;
	DROP TABLE IF EXISTS vehicle;

	CREATE TABLE s2partition (
		partitionkey integer PRIMARY KEY,
		name varchar,
		description text
	);
	
	CREATE TABLE s2person (
		personkey integer PRIMARY KEY,
		actdate timestamp,
		deleted boolean,
		expdate timestamp,
		firstname varchar(32),
		lastname varchar(32),
		middlename varchar(32),
		moddate date,
		notes varchar(255),
		partitionkey integer REFERENCES s2partition(partitionkey),
		personid varchar(255),
		pictureurl varchar(255)
	);
	
	CREATE TABLE s2cardformat (
		cardformatkey integer PRIMARY KEY,
		bitlen integer,
		cardidbitlen integer,
		cardidstartbit integer,
		facilitycode integer,
		description varchar(255),
		name varchar(64)
	);
	
	CREATE TABLE s2credential (
		credentialkey integer PRIMARY KEY,
		cardformatkey integer REFERENCES  s2cardformat(cardformatkey),
		credentialprofile varchar,
		disabled boolean,
		encodednum varchar,
		hotstamp varchar(255),
		partitionkey integer REFERENCES s2partition(partitionkey),
		personkey integer REFERENCES s2person(personkey),
		status varchar
	);
	
			
	CREATE TABLE partition (
		partitionkey integer PRIMARY KEY,
		name varchar,
		description text
	);
	
	CREATE TABLE person (
		personkey integer PRIMARY KEY,
		actdate timestamp,
		deleted boolean,
		expdate timestamp,
		firstname varchar(32),
		lastname varchar(32),
		middlename varchar(32),
		moddate date,
		notes varchar(255),
		partitionkey integer REFERENCES partition(partitionkey),
		personid varchar(255),
		pictureurl varchar(255)
	);
	
	CREATE TABLE cardformat (
		cardformatkey integer PRIMARY KEY,
		bitlen integer,
		cardidbitlen integer,
		cardidstartbit integer,
		facilitycode integer,
		description varchar(255),
		name varchar(64)
	);
	
	CREATE TABLE credential (
		credentialkey integer PRIMARY KEY,
		cardformatkey integer REFERENCES  cardformat(cardformatkey),
		credentialprofile varchar,
		disabled boolean,
		encodednum varchar,
		hotstamp varchar(255),
		partitionkey integer REFERENCES partition(partitionkey),
		personkey integer REFERENCES person(personkey),
		status varchar
	);
	
	CREATE TABLE accesslevel (
		accesslevelkey integer PRIMARY KEY,
		description varchar(255),
		name varchar(64),
		partitionkey integer
	);

	CREATE TABLE roles (
		roleid serial PRIMARY KEY,
		rolename varchar(255),
		enabled boolean DEFAULT TRUE
	);
	
	INSERT INTO roles 
		(rolename)
	VALUES
		('Administrator'),
		('Supervisor'),
		('Operator'),
		('Mechanic'),
		('User'),
		('Guest');
		
	CREATE TABLE userroles (
		userid integer REFERENCES person(personkey),
		roleid integer REFERENCES roles(roleid),
		enabled boolean DEFAULT TRUE
	);
		

	

END $$;