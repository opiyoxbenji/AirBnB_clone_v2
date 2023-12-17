-- create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- drop user if exists
DROP USER IF EXISTS 'hbnb_dev'@'localhost';

-- create user with password
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- grant select privilege on performance_schema to hbnb_dev
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;