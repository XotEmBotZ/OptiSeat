-- Create the 'teachers' table
CREATE TABLE teachers (
    id SMALLSERIAL PRIMARY KEY,
    name VARCHAR NOT NULL
);

-- Create the 'rooms' table
CREATE TABLE rooms (
    id SMALLSERIAL PRIMARY KEY,
    name CHAR(3) NOT NULL,
    num_benches INT NOT NULL,
    bench_stud INT DEFAULT 2 NOT NULL
);

-- Create the 'students' table
CREATE TABLE students (
    id SMALLSERIAL PRIMARY KEY,
    std INT NOT NULL,
    sec CHAR(1) NOT NULL,
    sub CHAR(3) NOT NULL,
    is_seq BOOLEAN NOT NULL,
    roll_start INT NOT NULL,
    roll_end INT NOT NULL,
    roll_arr INT[] NOT NULL
);

-- Create the 'timetable' table
CREATE TABLE timetable (
    id SMALLSERIAL PRIMARY KEY,
    date DATE NOT NULL,
    std INT NOT NULL,
    sub CHAR(3) NOT NULL
);