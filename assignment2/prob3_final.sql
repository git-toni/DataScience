--NOW FOR THE DOCUMENT FOR REAL
--SELECT A.docid, AA.docid,sum(A.count*AA.count)
SELECT sum(A.count*AA.count)
FROM Frequency as A
JOIN Frequency as AA
on A.term=AA.term
WHERE A.docid='10080_txt_crude' AND AA.docid='17035_txt_earn'
GROUP BY A.docid, AA.docid;