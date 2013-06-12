CREATE VIEW queried AS
SELECT * FROM Frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count;


--SELECT count(*) FROM (
SELECT MAX(suma) FROM (
SELECT sum(A.count*AA.count) as suma
FROM queried as A
JOIN queried as AA
on A.term=AA.term
--WHERE A.docid='10080_txt_crude' AND AA.docid='q'
WHERE AA.docid='q'
GROUP BY A.docid, AA.docid
)
;

DROP VIEW queried;
