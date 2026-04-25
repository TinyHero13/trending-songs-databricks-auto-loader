CREATE OR REFRESH STREAMING TABLE bronze_trending_songs
AS SELECT
  CAST(`Pos` AS INT) AS SongPosition
  , `P+` AS PositionChange
  , TRIM(SPLIT(`Artist and Title`, '-')[0]) AS Artist
  , TRIM(SPLIT(`Artist and Title`, '-')[1]) AS Title
  , CAST(`Days` AS INT) AS DaysPosition
  , current_timestamp() AS IngestedAt
FROM STREAM(songs_trending.raw.raw_trending_songs)