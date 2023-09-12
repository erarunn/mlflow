import mlflow
import mlflow.pytorch
import os 
#mlflow.start_run()
uri_path= mlflow.get_artifact_uri()
print(uri_path)
#model=mlflow.pytorch.load_model(os.path.join(uri_path, "unet_model"))
#model=mlflow.pytorch.load_model("D:\\mlflow-main\\unet\\artifacts\\1\\577def8abed3445da9f463bbfdae0871\\artifacts\\unet_model")
import mlflow.pyfunc

model_name = "iris-classifier_4"
stage = 'Production'


model=mlflow.pytorch.load_model( model_uri=f"models:/{model_name}/{stage}")
#print(model)
# client = mlflow.tracking.MlflowClient()
# client.transition_model_version_stage(
    # name="unet",
    # version=1,
    # stage="Production"
# )
