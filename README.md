# Trending Songs

## Overview

This project extracts worldwide trending songs from Kworb, saves the result as Parquet, and uploads the files to Google Cloud Storage.

## Prerequisites

1. Python 3.13 or newer.
2. `uv` installed.
3. Google Cloud SDK (`gcloud`) installed.
4. Access to a Google Cloud project and a target GCS bucket.

## Setup

1. Install dependencies.

```bash
uv sync
```

## Google Cloud Access (ADC)

The uploader uses Application Default Credentials.

### User login

1. Authenticate your Google user.

```bash
gcloud auth login
```

2. Set the active project.

```bash
gcloud config set project <YOUR_PROJECT_ID>
```

3. Create local ADC credentials.

```bash
gcloud auth application-default login
```

## Usage

1. Extract data and create a Parquet file in `data/`.

```bash
uv run python src/extract_songs.py
```

2. Upload Parquet files to GCS.

```bash
uv run python src/load_files.py
```
## Reference

https://docs.cloud.google.com/docs/authentication/provide-credentials-adc