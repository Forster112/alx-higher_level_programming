-- Creates the table id_not_null
-- adds default value for the id row
CREATE TABLE id_not_null IF NOT EXISTS (id INT DEFAULT 1, name VARCHAR(256));
