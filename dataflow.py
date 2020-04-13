import os
from googleapiclient.discovery import build
# from oauth2client.client import GoogleCredentials
import json

def clean_dataflow(project_id, delete=False):

    # credentials = GoogleCredentials.get_application_default()
    dataflow_service = build('dataflow', 'v1b3', cache_discovery=False)

    # https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs/list
    result = (
                dataflow_service
                .projects()
                .locations()
                .jobs()
                .list(
                    projectId=project_id,
                    location='europe-west1',
                    filter='ACTIVE', # https://cloud.google.com/dataflow/docs/reference/rest/v1b3/Filter
                    view='JOB_VIEW_ALL', # https://cloud.google.com/dataflow/docs/reference/rest/v1b3/JobView
                )
                .execute()
            )

    print(json.dumps(result, indent=4))

    to_delete = []
    for job in result['jobs']:
        print(job['id'])
        job_details = (
                dataflow_service
                .projects()
                .locations()
                .jobs()
                .get(
                    # Path Params
                    projectId=project_id,
                    location='europe-west1',
                    jobId=job['id'],
                    # query params
                    view='JOB_VIEW_ALL', # https://cloud.google.com/dataflow/docs/reference/rest/v1b3/JobView
                )
                .execute()
            )
        try:
            # print(json.dumps(job_details['environment'], indent=4))
            print(json.dumps(job_details['labels'], indent=4))
            if job_details['labels']['autodelete'] == "true":
                print('found job to delete: '+ job['id'])
                to_delete.append(job['id'])
        except:
            pass
            # print(json.dumps(job_details['sdkPipelineOptions']['labels'], indent=4))

    print(to_delete)

    if delete:
        for job_id in to_delete:
            result = (
                    dataflow_service
                    .projects()
                    .locations()
                    .jobs()
                    .update(
                        # Parameters
                        projectId=project_id,
                        location='europe-west1',
                        jobId=job_id,
                        # Body
                        body={
                            "id": job_id,
                            "requestedState": "JOB_STATE_DRAINED",
                        }
                    )
                    .execute()
                    # TODO: wait for completion?
                )