CREATE OR REFRESH STREAMING TABLE gold_top_artists
AS SELECT
   Artist
  , COUNT(*) AS TotalSongs
  , AVG(SongPosition) AS AvgPosition
  , MIN(SongPosition) AS BestPosition
FROM STREAM(songs_trending.silver.silver_trending_songs)
GROUP BY Artist