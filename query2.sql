SELECT COUNT(*) as japanese_universities_top200
FROM university_rankings
WHERE country = 'Japan' 
  AND year = 2013 
  AND world_rank <= 200;