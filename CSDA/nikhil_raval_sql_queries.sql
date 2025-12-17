-- LIST ALL STUDENTS
use datascience;
SELECT * from students;

-- LIST ALL 9TH GRADERS
use datascience;
SELECT * from students WHERE grade_level = 9;

-- LIST ALL COURSES AND CREDITS FOR EACH
use datascience;
SELECT course_id, course_name, course_code, period, credits from courses;

-- SHOW ALL TEACHERS AND THEIR DEPARTMENTS
use datascience; 
SELECT last_name, first_name, department from teachers;

-- FIND ALL COURSES THAT HAPPEN DURING PERIOD 1
use datascience;
SELECT course_id, course_name, course_code, period from courses WHERE period = 1;

-- PULL EACH STUDENT'S SCHEDULE
use datascience; 
SELECT distinct students.student_id, students.last_name, students.first_name, enrollments.course_id, courses.course_name, 
courses.course_code from students, courses JOIN enrollments WHERE enrollments.student_id = students.student_id 
and enrollments.course_id = courses.course_id;

-- SHOW WHAT COURSES EACH TEACHER TEACHES
use datascience;
SELECT distinct teachers.teacher_id, teachers.last_name, teachers.first_name, courses.course_id, courses.course_name, 
courses.course_code, courses.period from teachers JOIN courses where courses.teacher_id = teachers.teacher_id
ORDER BY teachers.teacher_id ASC;

-- SELECT ALL STUDENTS AND SHOW THEIR GRADES
use datascience;
SELECT distinct students.student_id, students.last_name, students.first_name, enrollments.course_id,
courses.course_name, courses.course_code, enrollments.grade from students, courses JOIN enrollments 
WHERE students.student_id = enrollments.student_id and enrollments.course_id = courses.course_id
ORDER BY students.student_id ASC;

-- SHOW ALL STUDENTS IN A SPECIFIC SEMESTER
use datascience;
SELECT distinct students.student_id, students.last_name, students.first_name, enrollments.semester 
from students, courses JOIN enrollments WHERE students.student_id = enrollments.student_id 
and enrollments.course_id = courses.course_id and enrollments.semester = 1
ORDER BY students.student_id ASC;

-- SHOW NUMBER OF STUDENTS IN EACH COURSE
use datascience;
SELECT distinct courses.course_id, courses.course_name, courses.course_code, COUNT(enrollments.course_id) as Number_of_Students_Enrolled from courses
JOIN enrollments WHERE courses.course_id = enrollments.course_id
GROUP BY courses.course_id;

-- HOW MANY CLASSES IS EACH STUDENT TAKING?
use datascience;
SELECT distinct students.student_id, students.last_name, students.first_name, COUNT(enrollments.student_id) as Number_of_Courses
from students JOIN enrollments WHERE students.student_id = enrollments.student_id
GROUP BY students.student_id;

-- WHAT TEACHER TEACHES THE MOST STUDENTS?
use datascience;
SELECT teachers.teacher_id, teachers.last_name, teachers.first_name, COUNT(distinct courses.course_id) as Number_of_Students
from teachers, courses JOIN enrollments WHERE enrollments.course_id = courses.course_id
GROUP BY teachers.teacher_id, teachers.last_name, teachers.first_name
ORDER BY Number_of_Students DESC LIMIT 1;

-- GET THE SCHEDULE OF STUDENT ID 8
use datascience;
SELECT * from enrollments WHERE student_id = 8;

-- GET THE LIST OF STUDENT IDs THAT HAVE A CLASS TAUGHT BY TEACHER 232
use datascience;
SELECT distinct enrollments.student_id, courses.teacher_id from enrollments JOIN courses on enrollments.course_id = courses.course_id 
WHERE courses.teacher_id = 232;