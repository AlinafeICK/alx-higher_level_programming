-- 100-move_to_utf8.sql
-- Use the database hbtn_0c_0
USE hbtn_0c_0;

-- Convert the table first_table to UTF8
ALTER TABLE 'first_table'
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
