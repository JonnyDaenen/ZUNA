import os

from bigquery import clean_bigquery
from pubsub import clean_pubsub_subscriptions
from dataflow import clean_dataflow


# see: https://cloud.google.com/functions/docs/tutorials/pubsub#functions-prepare-environment-python
def app_zuna(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict):  The dictionary with data specific to this type of
         event. The `data` field contains the PubsubMessage message. The
         `attributes` field will contain custom attributes if there are any.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata. The `event_id` field contains the Pub/Sub message ID. The
         `timestamp` field contains the publish time.
    """
    import base64

    print("""This Function was triggered by messageId {} published at {}
    """.format(context.event_id, context.timestamp))

    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')
    else:
        name = 'N/A'
    print('Triggered ZUNA with {}!'.format(name))

    run()

def run():
    project_id = os.environ['GCP_PROJECT_ID']
    print("project:", project_id)

    print("Cleaning BigQuery...")
    clean_bigquery(delete=True)
    print("BigQuery cleaned!")

    print("Cleaning PubSub...")
    clean_pubsub_subscriptions(project_id=project_id, delete=True)
    print("PubSub cleaned!")

    print("Cleaning Dataflow...")
    clean_dataflow(project_id=project_id, delete=True)
    print("Dataflow cleaned!")

if __name__ == "__main__":
    run()
    