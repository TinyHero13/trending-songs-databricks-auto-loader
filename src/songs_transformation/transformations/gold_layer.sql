CREATE OR REFRESH STREAMING TABLE gold_trending_songs
AS SELECT
  SongPosition
  , PositionChange
  , Artist
  , Title
  , DaysPosition
FROM STREAM(songs_trending.silver.silver_trending_songs)