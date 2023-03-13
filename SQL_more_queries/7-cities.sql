-- Cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id int unique AUTO_INCREMENT not null PRIMARY KEY,
states_id int not null , name varchar(256) NOT NULL, foreign key(states_id) references states(id));
