-- script that creates an index idx_name_first_score on
-- the table name and the first letter of name and score
CREATE INDEX idx_name_first_score on names(name(1), score)
