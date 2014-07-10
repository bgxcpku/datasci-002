/* 1 */
select count(*) from frequency where docid = '10398_txt_earn'

/* 2 */
select count(*) from ( select term distict from frequency where docid = '10398_txt_earn' and count=1

/* 3 */
select count(*) from ( 
    select term distict from frequency where count = 1 and docid = '10398_txt_earn'
    union 
    select term distict from frequency where count = 1 and docid = '925_txt_trade'
)

/* 4 */
select count(*) from frequency where term like 'parliament'

/* 5 */
sqlite3 reuters.db "select count(*) from (select count(*) from frequency group by docid having sum(count) > 300);" > p5.txt

/* 6 */
sqlite3 reuters.db "select count(*) from frequency where docid in (select docid from frequency where term like 'transactions') and term like 'world'" > p6.txt

/* 7 */
sqlite3 matrix.db "select sum(A.value*B.value) from A join B on A.col_num = B.row_num where A.row_num=2 and B.col_num=3" > p7.txt

/* 8 */
select sum(f1.count*f2.count) from (
    (select * from frequency where docid = '10080_txt_crude') f1 
    join 
    (select * from frequency where docid = '17035_txt_earn') f2 
    on
    f1.term = f2.term
);

/* 9 */
select f.docid, sum(q.count*f.count) s from (
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count ) q
join frequency f
on q.term = f.term
group by f.docid
order by s desc