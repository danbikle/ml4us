SELECT * FROM prices WHERE cdate = (SELECT MAX(cdate) FROM prices);
SELECT cdate,closep FROM prices WHERE cdate = (SELECT MAX(cdate)-1 FROM prices);
SELECT cdate,closep FROM prices WHERE cdate > (SELECT MAX(cdate)-10 FROM prices);
