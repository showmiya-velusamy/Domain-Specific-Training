

insert into tblPerson(id,name,Email,GenderId)
VALUES(1,'Tom','tom@gmail.com',1),
(2,'Jessy', 'jessy@gmail.com', 2),
(3, 'Kristy' , 'kristy@gmail.com',2),
(4, 'John', 'john@gmail.com' , 1),
(5, 'Rob' , 'rob@gmil.com' , 1);

insert into tblGender(Genderid,Gender)
VALUES(1,'Male'),
(2,'Female'),
(3,'others');

update tblPerson
set Email= 'tomupdated@gmail.com'
where id=1;

update tblPerson
set GenderId=1
where name='Jessy';

delete from tblPerson
where id=3;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO students (student_id,first_name, last_name, age, email) VALUES
(1,'John', 'Doe', 20, 'john.doe@example.com'),
(2,'Jessy', 'Smith', 22, 'jane.smith@example.com'),
(3,'Emily', 'Jones', 21, 'emily.jones@example.com'),
(4,'Michael', 'Brown', 23, 'michael.brown@example.com');

CREATE TABLE courses (
    course_id INT  PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_description TEXT
);

INSERT INTO courses (course_id, course_name,course_description) VALUES
(1001,'Introduction to Programming', 'An introductory course to programming using Python.'),
(1003,'Data Structures and Algorithms', 'A course on fundamental data structures and algorithms.'),
(1006,'Database Management Systems', 'An overview of database management concepts and SQL.'),
(1009,'Web Development Fundamentals', 'A beginner course on web development including HTML, CSS, and JavaScript.');

update courses
set course_id=1004
where course_name='Introduction to Programming';

select * from courses;

delete students
where student_id=2;

select * from students;
