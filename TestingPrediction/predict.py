from google.cloud import automl
from google.oauth2 import service_account

# TODO(developer): Uncomment and set the following variables
project_id = "arched-branch-270112"
model_id = "ICN980197023976259584"
file_path = "CHANGE_TO_IMAGE_PATH"

# to get key go to: 
# https://console.cloud.google.com/iam-admin/serviceaccounts/details/107662540146781122485?project=arched-branch-270112
# and create a key and download json key
credentials = service_account.Credentials.from_service_account_file("privatekey.json")

prediction_client = automl.PredictionServiceClient(credentials=credentials)

# Get the full path of the model.
model_full_id = prediction_client.model_path(
    project_id, "us-central1", model_id
)

# Read the file.
with open(file_path, "rb") as content_file:
    content = content_file.read()

image = automl.types.Image(image_bytes=content)
payload = automl.types.ExamplePayload(image=image)

# params is additional domain-specific parameters.
# score_threshold is used to filter the result
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictrequest
params = {"score_threshold": "0.8"}

response = prediction_client.predict(model_full_id, payload, params)
print("Prediction results:")
for result in response.payload:
    print("Predicted class name: {}".format(result.display_name))
    print("Predicted class score: {}".format(result.classification.score))