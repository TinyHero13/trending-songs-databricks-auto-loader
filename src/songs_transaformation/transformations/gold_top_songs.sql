CREATE OR REFRESH STREAMING TABLE gold_top_songs
AS SELECT
  Artist
  , Title
  , MAX(DaysPosition) AS DaysOnChart
  , MIN(SongPosition) AS BestPosition
FROM STREAM(silver_trending_songs)
GROUP BY Artist, Title