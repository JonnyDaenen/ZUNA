import os
from google.cloud import bigquery

def clean_bigquery(delete=False):

    # Construct a BigQuery client object.
    client = bigquery.Client()

    datasets = list(client.list_datasets())  # Make an API request.
    project = client.project

    # TODO check:
    # - [x] datasets to delete -> delete
    # - [ ] tables to delete -> delete
    # - [ ] non EU regions tables -> warning

    # Cleanup
    if datasets:
        to_delete = []

        # Print datasets that will be deleted
        print("Datasets in project {}:".format(project))
        for dataset in datasets:
            # print(dataset.labels)
            try:
                if (dataset.labels['autodelete'] == 'true'):
                    print("\t{}".format(dataset.dataset_id))
                    to_delete.append(dataset.dataset_id)
            except:
                pass
        # Delete
        if delete:
            for dataset_id in to_delete:
                print("deleting %s"%dataset_id)
                client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)
            print("deletion completed")
        else:
            print("skipping deletion")
    else:
        print("{} project does not contain any datasets.".format(project))