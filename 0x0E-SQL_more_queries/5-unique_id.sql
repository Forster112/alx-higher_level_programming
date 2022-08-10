-- Creates the table unique_id
-- with row id that has default value 1 and distinct
CREATE TABLE unique_id IF NOT EXISTS (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
