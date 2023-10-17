-- script that creates a table second_table, if already exists should not fail
-- first we create the table
CREATE TABLE IF NOT IXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- then we insert the data into teh table
INSERT INTO second_table VALUES(
    (id = 1, name = “John”, score = 10),
    (id = 2, name = “Alex”, score = 3),
    (id = 3, name = “Bob”, score = 14),
    (id = 4, name = “George”, score = 8)
);