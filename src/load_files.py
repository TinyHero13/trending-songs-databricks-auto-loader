from google.cloud import storage
import os

def send_to_gcs(bucket_name, source_folder):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    for filename in os.listdir(source_folder):
        if filename.endswith(".parquet"):
            source_file_name = os.path.join(source_folder, filename)
            blob = bucket.blob(filename)
            blob.upload_from_filename(source_file_name)

if __name__ == "__main__":
    send_to_gcs("songs-trending-data", "data")