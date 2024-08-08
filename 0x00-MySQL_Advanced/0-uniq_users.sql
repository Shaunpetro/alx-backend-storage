-- script that create a table users with this feilds:
-- id, email & name
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255)
)
