-- Create the 'teachers' table
CREATE TABLE teacher (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL
);

-- Create the 'rooms' table
CREATE TABLE room (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(3) NOT NULL,
    num_benches INTEGER NOT NULL,
    bench_stud INTEGER DEFAULT 2 NOT NULL
);

-- Create the 'students' table
CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    std INTEGER NOT NULL,
    sec CHAR(1) NOT NULL,
    sub CHAR(3) NOT NULL,
    is_seq BOOLEAN NOT NULL,
    roll_start INTEGER,
    roll_end INTEGER,
    roll_arr INTEGER[]
);

-- Create the 'timetabl' table
CREATE TABLE timetable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    std INTEGER NOT NULL,
    sub CHAR(3) NOT NULL
);