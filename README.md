# Z-UWN-STF

Collection of scripts to decommission GCP test resources, which are labelled by `autodelete:true`.

## Features

## Core

- [x] List active dataflow jobs
- [x] Drain dataflow jobs
- [x] List BigQuery datasets
- [x] Delete BigQuery datasets 
- [x] Pub/Sub subscription list
- [x] Pub/Sub subscription deletion
- [ ] Pub/Sub topic list
- [ ] Pub/Sub topic deletion
- [ ] GCS bucket list
- [ ] GCS bucket deletion

## Basic

- [ ] BigQuery table deletion
- [ ] BigQuery non-EU datasets
- [ ] Dataflow drain/cancel wait
- [ ] Dataflow cancel option
- [ ] Main script with ordered execution (DF, BQ, PS sub, PS top, GCS)

### Usage

- [ ] Pass in project id
- [ ] Dockerize
- [ ] Publish to docker hub
- [ ] Service account support
- [ ] Flag to override input (Y/n)