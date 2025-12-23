-- Write your PostgreSQL query statement below
SELECT
  s.student_id,
  s.student_name,
  sub.subject_name,
  COALESCE(e.cnt, 0) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN (
  SELECT student_id, subject_name, COUNT(*) AS cnt
  FROM Examinations
  GROUP BY student_id, subject_name
) e
  ON e.student_id = s.student_id
 AND e.subject_name = sub.subject_name
ORDER BY s.student_id, sub.subject_name;
