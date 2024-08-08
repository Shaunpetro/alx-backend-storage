-- script that creates a function SafeDiv that divides
-- (& returns) the 1st by the 2nd num of returns
-- 0 if the 2nd num is = 0
DELIMITER $$ ;
CREATE FUNCTION SafeDiv(
        a INT,
        b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
        DECLARE result FLOAT;
        IF b = 0 THEN
                RETURN 0;
        END IF;
        SET result = (a * 1.0) / b;
        RETURN result;
END;$$
DELIMITER ;
