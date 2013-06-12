SELECT A.row_num, AA.row_num,sum(A.value*AA.value)
FROM a as A
JOIN a as AA
on A.col_num=AA.col_num
WHERE A.row_num=3 AND AA.row_num=2
GROUP BY A.row_num, AA.row_num;
