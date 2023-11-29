use resiliadata;
create table tecnologia(
id_tecnologia int(10) not null primary key auto_increment,
nome_tec varchar(15) not null,
tipo_tec varchar(10) not null,
data date
);


use resiliadata;
create table empresa(
id_empresa int(10) not null primary key auto_increment,
nome_emp varchar(15) not null,
endereco_emp varchar(10) not null,
telefone_emp varchar(10) not null,
data date
);

use resiliadata;
create table colaboradores(
id_colaboradores int(10) not null primary key auto_increment,
nome_cl varchar(15) not null,
cpf_cl varchar(12) not null,
endereco_cl varchar(10) not null,
data date
);

use resiliadata;
create table tec_emp(
id_tec_emp int(10) not null primary key,
id_tecnologia int(10) not null,
id_empresa int(10) not null,
data date 
);


use resiliadata;
create table emp_col(
id_emp_col int(10) not null primary key,
id_empresa int(10) not null,
id_colaboradores int(10) not null,
data date
);



ALTER TABLE tec_emp
ADD FOREIGN KEY (id_tecnologia) REFERENCES tecnologia(id_tecnologia),
ADD FOREIGN KEY (id_empresa) REFERENCES empresa(id_empresa);

ALTER TABLE emp_col
ADD FOREIGN KEY (id_empresa) REFERENCES empresa(id_empresa),
ADD FOREIGN KEY (id_colaboradores) REFERENCES colaboradores(id_colaboradores);

insert into tecnologia(nome_tec,tipo_tec,data)
values
('SQL','WEBDEV',2023-12-25)
('POWERBI','WEBDEV',2023-12-24)


insert into empresa(nome_emp,endereco_emp,telefone_emp,data)
values
('hstark',''toronto','95956210',2023-12-24) 
('BRA','RJ','25103652',2023-12-24)

insert into  colaboradores(nome_cl,cpf_cl,endereco_cl, data)
Values
('chris','25232621041','Quebec',2023-12-25)
('jube','15125481849','boston',2023-12-22)

insert into tec_emp(id_tecnologia,id_empresa, data)
values
(1,1,2023-12-25)
(2,2,2023-12-18)

insert into emp_col(id_empresa,id_colaboradores, data)
values
(1,1,2023-12-25)
(2,2,2023-12-24)