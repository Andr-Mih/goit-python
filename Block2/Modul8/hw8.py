#создание таблицы оценок
CREATE TABLE public."values"
(
    id integer NOT NULL DEFAULT nextval('values_id_seq'::regclass),
    value integer NOT NULL,
    CONSTRAINT values_pkey PRIMARY KEY (id)
)

#создание таблицы учащихся с номером группы
CREATE TABLE public.users
(
    id integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    surname character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "group" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id)
)

#создание таблицы с перечнем предметов и преподавателем
CREATE TABLE public.subjects
(
    id integer NOT NULL DEFAULT nextval('subjects_id_seq'::regclass),
    subject character varying(20) COLLATE pg_catalog."default" NOT NULL,
    teacher character varying(20) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT subjects_pkey PRIMARY KEY (id)
)

#создание таблицы учашихся с посещаемыми предметами, преподавателями и оценками
CREATE TABLE public.advancements
(
    id integer NOT NULL DEFAULT nextval('advancements_id_seq'::regclass),
    student_id integer NOT NULL,
    subject_id integer NOT NULL,
    value_id integer NOT NULL,
    CONSTRAINT advancements_pkey PRIMARY KEY (id),
    CONSTRAINT subjects_fk FOREIGN KEY (subject_id)
        REFERENCES public.subjects (id) MATCH SIMPLE
        
    CONSTRAINT users_fk FOREIGN KEY (student_id)
        REFERENCES public.users (id) MATCH SIMPLE

    CONSTRAINT values_fk FOREIGN KEY (value_id)
        REFERENCES public."values" (id) MATCH SIMPLE
        
)


#5 студентов с наибольшим средним баллом по всем предметам
SELECT AVG(advancements.value_id) AS ser, users.name
FROM advancements
JOIN users ON student_id = users.id
JOIN values ON value_id = values.id
JOIN subjects ON subject_id = subjects.id
GROUP BY users.name
ORDER BY ser DESC
LIMIT 5

#1 студент с наивысшим средним баллом по одному предмету
SELECT AVG(advancements.value_id) AS ser, users.name
FROM advancements
JOIN users ON student_id = users.id
JOIN values ON value_id = values.id
JOIN subjects ON subject_id = subjects.id
WHERE subjects.subject LIKE 'English'
GROUP BY users.name
ORDER BY ser DESC
LIMIT 1

#средним балл в группе по одному предмету
SELECT AVG(advancements.value_id) AS ser, users.name
FROM advancements
JOIN users ON student_id = users.id
JOIN values ON value_id = values.id
JOIN subjects ON subject_id = subjects.id
WHERE users.group = '1' AND subjects.subject LIKE 'Englis%'
GROUP BY users.name
ORDER BY ser DESC
LIMIT 10

# средним балл в потоке
SELECT AVG(advancements.value_id) AS ser, users.name
FROM advancements
JOIN users ON student_id = users.id
JOIN values ON value_id = values.id
JOIN subjects ON subject_id = subjects.id
GROUP BY users.name
ORDER BY ser DESC

#список студентов в группе
SELECT users.name
FROM advancements
JOIN users ON student_id = users.id
JOIN values ON value_id = values.id
JOIN subjects ON subject_id = subjects.id
WHERE users.group = '1'
GROUP BY users.name

# оценки студентов в группе по предмету
SELECT users.name, values.value
FROM advancements
JOIN users ON student_id = users.id
JOIN values ON value_id = values.id
JOIN subjects ON subject_id = subjects.id
WHERE users.group = '1' AND subjects.subject LIKE 'Englis%'
ORDER BY users.name


#список курсов которые посещает студентов
SELECT DISTINCT users.name, subjects.subject
FROM advancements
JOIN users ON student_id = users.id
JOIN values ON value_id = values.id
JOIN subjects ON subject_id = subjects.id
WHERE users.name = 'Andrii'

#список курсов которые студенту читает преподаватель
SELECT DISTINCT users.name, subjects.subject, subjects.teacher
FROM advancements
JOIN users ON student_id = users.id
JOIN values ON value_id = values.id
JOIN subjects ON subject_id = subjects.id
WHERE users.name = 'Andrii' AND subjects.teacher LIKE '%nov'

#средний бал который ставит преподаватель студенту
SELECT AVG(values.value) as val, users.name, subjects.teacher
FROM advancements
JOIN users ON student_id = users.id
JOIN values ON value_id = values.id
JOIN subjects ON subject_id = subjects.id
WHERE users.name = 'Ella' AND subjects.teacher LIKE '%nov'
GROUP BY users.name, subjects.teacher

#средний бал который ставит преподаватель
SELECT AVG(values.value) as val, subjects.teacher
FROM advancements
JOIN users ON student_id = users.id
JOIN values ON value_id = values.id
JOIN subjects ON subject_id = subjects.id
WHERE subjects.teacher LIKE '%nov'
GROUP BY subjects.teacher


