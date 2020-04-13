
gcloud config set project $GCP_PROJECT_ID

# Activation topic
gcloud pubsub topics create app-zuna-cloudscheduler

# gcloud pubsub subscriptions create app-zuna-cloudscheduler-subscription --topic app-zuna-cloudscheduler


# Service account
gcloud iam service-accounts create sa-app-zuna \
    --description "Service account for ZUNA app." \
    --display-name "ZUNA Service Account"

# Roles for the service account
# !!! Review these carefully and adjust to your needs !!!

gcloud projects add-iam-policy-binding $GCP_PROJECT_ID \
  --member serviceAccount:sa-app-zuna@$GCP_PROJECT_ID.iam.gserviceaccount.com \
  --role roles/bigquery.dataOwner \
  --no-user-output-enabled

gcloud projects add-iam-policy-binding $GCP_PROJECT_ID \
  --member serviceAccount:sa-app-zuna@$GCP_PROJECT_ID.iam.gserviceaccount.com \
  --role roles/pubsub.editor \
  --no-user-output-enabled

gcloud projects add-iam-policy-binding $GCP_PROJECT_ID \
  --member serviceAccount:sa-app-zuna@$GCP_PROJECT_ID.iam.gserviceaccount.com \
  --role roles/dataflow.developer \
  --no-user-output-enabled

# Deploy the function
gcloud functions deploy \
    app-zuna \
    --entry-point=app_zuna \
    --region=europe-west1 \
    --runtime python37 \
    --service-account=sa-app-zuna@$GCP_PROJECT_ID.iam.gserviceaccount.com \
    --trigger-topic app-zuna-cloudscheduler \
    --set-env-vars GCP_PROJECT_ID=$GCP_PROJECT_ID \
    --timeout=540s \
    --quiet

# Trigger every Friday at 21:00 
gcloud scheduler jobs \
    create pubsub \
    app-zuna-trigger \
    --time-zone="Etc/UTC" \
    --schedule="0 21 * * 5" \
    --topic=app-zuna-cloudscheduler \
    --message-body="cloud scheduler trigger"