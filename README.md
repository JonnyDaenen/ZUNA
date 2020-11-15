# ZUNA

Collection of scripts to decommission GCP test resources, which are labelled by `autodelete:true`.

## Features

### Core

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

### Basic

- [x] Main script with ordered execution
- [x] Local invocation possible
- [ ] BigQuery table deletion
- [ ] BigQuery non-EU datasets
- [ ] Dataflow drain/cancel wait
- [ ] Dataflow cancel option (env var)

### Usage

- [x] Pass in project id (env var)
- [x] Cloud function support
- [x] Cloud scheduler support
- [x] Installer: resource creation script
- [x] Dedicated service account
- [x] Standard roles on service account (project-level)
- [ ] Dockerize
- [ ] Publish to docker hub
- [ ] Flag to override input (Y/n)


## Installation
```bash
export GCP_PROJECT_ID=<your projecy id>
bash ./scripts/001_deploy.sh
```
