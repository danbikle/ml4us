
-- Copy rows from table to table:
INSERT INTO prices3
SELECT cdate,openp,closep, closep - openp AS diff FROM prices
WHERE cdate = '2016-08-01';

-- Copy rows from table to table2 where rows not in table2 already:
INSERT INTO prices3
SELECT cdate,openp,closep, closep - openp AS diff FROM prices
WHERE  cdate BETWEEN '2016-08-01' AND '2016-08-31'
AND    cdate NOT IN (SELECT cdate FROM prices3);

-- Update all rows of a column:
UPDATE prices3 SET diff = 0;

-- rpt:
SELECT * FROM prices3;
