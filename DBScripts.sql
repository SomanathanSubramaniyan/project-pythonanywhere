DROP DATABASE IF EXISTS `Accidents`;
CREATE DATABASE `Accidents`;
USE `Accidents`;

DROP TABLE IF EXISTS Accidents;
CREATE TABLE Accidents (
  id INT NOT NULL AUTO_INCREMENT, 
  province varchar(20) NOT NULL,
  VehicleType varchar(20) NOT NULL,
  DriverAge varchar(20) NOT NULL,
  DriverSex varchar(20) NOT NULL,
  MonthYear varchar(20) NOT NULL,
  primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

show tables;
select * from accidents;

insert into accidents values ('Bus', 'Feb-2019', 'Male', '40 to 50', 'Munster')


