# Setup

## Initialize

1. In the Google Cloud console, on the project selector page, select or [create] a Google Cloud project. 
   
   1. Set the `PROJECT_ID` environment variable.

   ```shell
   export PROJECT_ID="<your-project-id>"
   ```

   2. Set the `REGION` environment variable; it defaults to `"us-central1"`. For now, the only other supported region is `europe-west4`. Learn more about Vertex AI [regions].

   ```shell
   export REGION="us-central1"
   ```
   
2. Make sure that billing is [enabled][billing] for your Google Cloud project.

3. [Install][gcloud] the Google Cloud CLI.

4. [Initialize][init] the gcloud CLI.
   
   ```shell
   gcloud init
   ```

5. Enable the [Vertex AI][vertex], [Artifact Registry][ar], [Cloud Build][cb], [Cloud Deploy][cd]
   and [Cloud Storage][cs] APIs.
   
    ```shell
    gcloud services enable \
      aiplatform.googleapis.com \
      artifactregistry.googleapis.com \
      compute.googleapis.com \
      cloudbuild.googleapis.com \
      clouddeploy.googleapis.com  \
      notebooks.googleapis.com \
      --project $PROJECT_ID
    ```

## Permissions

Make sure the default Compute Engine [service account][sa] has sufficient permissions.
   
 1. Add the `iam.serviceAccountUser` role, which includes the `actAs` permission to deploy to the runtime.
 
     ```shell
     gcloud iam service-accounts add-iam-policy-binding $(gcloud projects describe $PROJECT_ID \
     --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
     --member=serviceAccount:$(gcloud projects describe $PROJECT_ID \
     --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
     --role="roles/iam.serviceAccountUser" \
     --project=$PROJECT_ID
     ```

 2. Add the `clouddeploy.jobRunner` role.

     ```shell
     gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member=serviceAccount:$(gcloud projects describe $PROJECT_ID \
     --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
     --role="roles/clouddeploy.jobRunner"
     ```

 3. Add the `roles/clouddeploy.viewer` role.

     ```shell
     gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member=serviceAccount:$(gcloud projects describe $PROJECT_ID \
     --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
     --role="roles/clouddeploy.viewer"
     ```

 4. Add the `roles/aiplatform.user` role.

     ```shell
     gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member=serviceAccount:$(gcloud projects describe $PROJECT_ID \
     --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
     --role="roles/aiplatform.user"
     ```

 5. Add the `roles/storage.objectCreator` role.

     ```shell
     gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member=serviceAccount:$(gcloud projects describe $PROJECT_ID \
     --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
     --role="roles/storage.objectCreator"
     ```

 6. Add the `roles/storage.objectViewer` role.

     ```shell
     gcloud projects add-iam-policy-binding $PROJECT_ID \
     --member=serviceAccount:$(gcloud projects describe $PROJECT_ID \
     --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
     --role="roles/storage.objectViewer"
    ```

## Storage

1. Create a Cloud Storage bucket.
   
   1. Set the `BUCKET_URI` variable. If you change the value, make sure to also
    update it in the [configuration](/pkg/tuner/metadata.py).
   
   ```shell
   export BUCKET_URI="gs://rlhf-artifacts"
   ``` 
   
   2. Create the Cloud Storage bucket used to store the tuning artifacts.
   
    ```shell
    gsutil mb -l $REGION -p $PROJECT_ID $BUCKET_URI
    ```

2. Create Vertex AI Pipeline Registry repository.
   
   1. Set the `PIPELINE_REGISTRY` variable. If you change the value, make sure to also
    update it in the [configuration](/pkg/tuner/metadata.py).
   
   ```shell
   export PIPELINE_REGISTRY="rlhf-pipelines"
   ``` 
   
   2. Create the Artifact Registry backing the Vertex AI Pipeline Registry.
   
    ```shell
    gcloud artifacts repositories create $PIPELINE_REGISTRY \
    --location=$REGION \
    --repository-format=KFP
    ```

## Configuration

The table below shows the supported models, hardware and regions.

| large_model_reference | supported accelerator_type    | supported region          |
| --------------------- | ----------------------------- | ------------------------- |
| `text-bison@001`      | `TPU_V3`, `NVIDIA_TESLA_A100` | europe-west4, us-central1 |
| `chat-bison@001`      | `TPU_V3`, `NVIDIA_TESLA_A100` | europe-west4, us-central1 |
| `t5-small`            | `TPU_V3`, `NVIDIA_TESLA_A100` | europe-west4, us-central1 |
| `t5-large`            | `TPU_V3`                      | europe-west4              |
| `t5-xl`               | `TPU_V3`                      | europe-west4              |
| `t5-xxl`              | `TPU_V3`                      | europe-west4              |

Note that tuning jobs that run in:

* `us-central1` will use 8 Nvidia A100 80GB. 
* `europe-west4` will use 64 v3 TPUs.

[create]: https://cloud.google.com/resource-manager/docs/creating-managing-projects
[billing]: https://cloud.google.com/billing/docs/how-to/verify-billing-enabled#console
[gcloud]: https://cloud.google.com/sdk/docs/install
[init]: https://cloud.google.com/sdk/docs/initializing
[sa]: https://cloud.google.com/iam/docs/service-account-types#default
[vertex]: https://cloud.google.com/vertex-ai
[ar]: https://cloud.google.com/artifact-registry
[cb]: https://cloud.google.com/build
[cd]: https://cloud.google.com/deploy
[cs]: https://cloud.google.com/storage
[regions]: https://cloud.google.com/vertex-ai/docs/general/locations
