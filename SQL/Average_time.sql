SELECT
  machine_id,
  ROUND(AVG(end_time - start_time)::numeric, 3) AS processing_time
FROM (
  SELECT
    machine_id,
    process_id,
    MAX(timestamp) FILTER (WHERE activity_type = 'start') AS start_time,
    MAX(timestamp) FILTER (WHERE activity_type = 'end')   AS end_time
  FROM Activity
  GROUP BY machine_id, process_id
) t
GROUP BY machine_id;
