-- create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- drop user if exists
DROP USER IF EXISTS 'hbnb_test'@'localhost';

-- create user with password
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- grant select privilege on performance_schema to hbnb_dev
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;