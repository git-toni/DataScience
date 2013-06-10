SELECT count(*) FROM (
	
	SELECT sum(count) AS NTERMS,docid FROM Frequency
	GROUP BY docid HAVING NTERMS>300
	);
