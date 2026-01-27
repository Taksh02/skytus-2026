create database StudentDB;
use StudentDB;

create table student(
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT);

INSERT INTO student VALUES
(1,'Taksh','IT','5','98'),
(2,'Parth','CSE','3','95'),
(3,'Dhruv','IT','4','90'),
(4,'Aryan','CSE','2','92'),
(5,'Krish','CSE','1','93'),
(6,'Ravi','BCA','4','70'),
(7,'Jay','IT','5','65')

--1> Display all student record
SELECT * FROM student;

--2> Display only name and department
SELECT name, department FROM student;

--3> Find studens with marks greater than 75
select * from student
where marks > 75;

--4> Display student from CSE Department
select * from student
where department = 'CSE';

--5> Sort student by marks(descending)
select * from student
order by marks desc;

--6> Display top 3 scorers
select top 3 * from student
order by marks desc ;



