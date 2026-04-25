CREATE OR REFRESH STREAMING TABLE silver_trending_songs
  (CONSTRAINT valid_position EXPECT (SongPosition IS NOT NULL) ON VIOLATION DROP ROW,
   CONSTRAINT valid_artist_title EXPECT (Artist IS NOT NULL AND Title IS NOT NULL) ON VIOLATION DROP ROW)
AS SELECT
   SongPosition
  , PositionChange
  , Artist
  , Title
  , DaysPosition
FROM STREAM(songs_trending.bronze.bronze_trending_songs)
WHERE Artist IS NOT NULL AND Title IS NOT NULL