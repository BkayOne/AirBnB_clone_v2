-- This script prepares a MySQL server for the project

-- Create the project development database named hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create or update the user hbnb_dev with all privileges on the hbnb_dev_db database
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to the hbnb_dev user on the hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to reload the privileges table
FLUSH PRIVILEGES;

-- Grant the SELECT privilege to the hbnb_dev user on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges again to reload the privileges table
FLUSH PRIVILEGES;
