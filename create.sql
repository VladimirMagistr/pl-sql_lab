create table Vid_irisa(
species_id number,
spicies_name varchar(20));

Create Table Petal (
flower_id number,
lengh_cm number,
width_cm  number,
species_id number
);


Create Table Sepal (
flower_id number,
lengh_cm number,
width_cm  number,
species_id number
);


ALTER TABLE Vid_irisa
ADD CONSTRAINT vid_irisa_klych PRIMARY KEY (species_id);

ALTER TABLE Sepal
ADD CONSTRAINT sepal_named_klych1 PRIMARY KEY (flower_id );

ALTER TABLE Petal
ADD CONSTRAINT petal_named_klych2 PRIMARY KEY (flower_id);


Alter Table Sepal
ADD CONSTRAINT vidriski_key1 FOREIGN KEY (species_id) REFERENCES Vid_irisa (species_id);


Alter Table Petal
ADD CONSTRAINT vidriski_key2 FOREIGN KEY (species_id) REFERENCES Vid_irisa (species_id);




--Alter Table Sepal2
--ADD CONSTRAINT sepal_forkey_id FOREIGN KEY (flower_id) REFERENCES Petal2 (flower_id);




--Alter Table Petal2
--ADD CONSTRAINT petal_forkey_id2 FOREIGN KEY (flower_id) REFERENCES Sepal2 (flower_id);
--Alter Table Petal2
--Drop CONSTRAINT petal_forkey_id2 ;
