-- Cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id int unique AUTO_INCREMENT not null PRIMARY KEY,
states_id int not null foreign key references states(id), name varchar(256));
