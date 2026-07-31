SELECT author_id AS id
FROM Views
GROUP BY author_id, viewer_id
HAVING author_id = viewer_id