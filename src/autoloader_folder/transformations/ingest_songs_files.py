import dlt as dp

@dp.table(
    table_properties={"delta.columnMapping.mode": "name"}
)
def raw_trending_songs():
    return (
        spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "parquet") \
        .load("gs://songs-trending-data")
    )