# Deploy

[Cloud Deploy](https://cloud.google.com/deploy) makes continuous delivery of models easy by allowing users to define releases and progress them through environments such as test, stage, and production. It provides easy promotion, approval and rollback of releases. 


## Deploy Model (draft)

Deploy your model to the production endpoint using Cloud Deploy. 

The Vertex AI model deployer image is required for deploying your model to a production endpoint through Cloud Deploy. Before proceeding, ensure you have a Vertex AI model deployer image. If you already have one, you can proceed. If not, consult this [guide] to build and publish the image. 

[guide]: https://github.com/GoogleCloudPlatform/cloud-deploy-samples/blob/11731ca9481020ca7c1f6efa2d546e8dee9c6823/custom-targets/vertex-ai/README.md#building-the-sample-image


```shell
endpoint = aiplatform.Endpoint.create(
    display_name=metadata.ENDPOINT_DISPLAY_NAME
)

ENDPOINT_ID = endpoint.name
```

Create Cloud Deploy delivery pipeline, target, and skaffold.

```shell
TMPDIR="deploy/tmp"

! mkdir -p $TMPDIR

! deploy/replace_variables.sh -p $PROJECT_ID -r $REGION -e $ENDPOINT_ID -t $TMPDIR
```

Apply the Cloud Deploy configuration defined in `clouddeploy.yaml`.

```shell
! gcloud deploy apply --file=$TMPDIR/clouddeploy.yaml --project=$PROJECT_ID --region=$REGION
```

Get the model ID.

```shell
stdout = ! gcloud ai models list --project=$PROJECT_ID --region=$REGION --filter="DISPLAY_NAME: $metadata.MODEL_DISPLAY_NAME" --sort-by=~creationTimestamp --limit=1 --format="flattened(deployedModels[0].deployedModelId)" 2>/dev/null
MODEL_ID = stdout[1].split()[1]
print("Model ID:", MODEL_ID)
```

Create a release and rollout.

```shell
DELIVERY_PIPELINE_NAME = "vertex-ai-cloud-deploy-pipeline" # from clouddeploy.yaml
TARGET_NAME = "prod-endpoint" # from clouddeploy.yaml
RELEASE_NAME = f"release-{UUID}"
DEPLOY_PARAMS = f'customTarget/vertexAIModel=projects/{PROJECT_ID}/locations/{REGION}/models/{MODEL_ID}'

! gcloud deploy releases create $RELEASE_NAME \
    --delivery-pipeline=$DELIVERY_PIPELINE_NAME \
    --project=$PROJECT_ID \
    --region=$REGION \
    --source=$TMPDIR/configuration \
    --deploy-parameters=$DEPLOY_PARAMS
```

Monitor the release progress.

```shell
! gcloud deploy releases describe $RELEASE_NAME \
    --delivery-pipeline=$DELIVERY_PIPELINE_NAME \
    --project=$PROJECT_ID \
    --region=$REGION
```

Monitor the rollout status.

```shell
! gcloud deploy rollouts describe $(gcloud deploy targets describe $TARGET_NAME --delivery-pipeline=$DELIVERY_PIPELINE_NAME --region=$REGION --format="value('Latest rollout')") \
    --release=$RELEASE_NAME \
    --delivery-pipeline=$DELIVERY_PIPELINE_NAME \
    --project=$PROJECT_ID \
    --region=$REGION
```
