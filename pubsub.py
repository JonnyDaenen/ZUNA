import os
from google.cloud import pubsub_v1

def clean_pubsub_subscriptions(project_id, delete=False):

    # Subscriptions
    # see: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/efe5e78451c59415a7dcaaf72db77b13085cfa51/pubsub/cloud-client/subscriber.py#L43
    subscriber = pubsub_v1.SubscriberClient()
    project_path = subscriber.project_path(project_id)

    to_delete = []

    for subscription in subscriber.list_subscriptions(project_path):
        if subscription.labels['autodelete'] == 'true':
            print(subscription.name)
            print(subscription)
            to_delete.append(subscription.name)

    if delete:
        for subscription_name in to_delete:
            subscriber.delete_subscription(subscription_name)
    subscriber.close()