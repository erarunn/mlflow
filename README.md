conda create -n yolov5 python==3.8
!pip install -U segmentation-models-pytorch albumentations --user 
!pip install -U albumentations[imgaug]
!pip install -U \\Mayankppc\software\pytorch_11_3\torchvision-0.11.0+cu113-cp38-cp38-win_amd64.whl --user



deepchecks for model and data drift


from sklearn import datasets, metrics, model_selection, svm
>>> X, y = datasets.make_classification(random_state=0)

//kubeflow
deepchecks for model and data drift
install kubeflow
-- Docer Desttop   https://www.docker.com/products/docker-desktop/
-- Minikube
-- kubeflow pipeline 
//DVC

mlflow models server --model-uri models:/iris-classifier/Production --default-artifact-root ./artifacts --host 107.108.32.137 --port 1234
mlflow models serve --model-uri models:/iris-classifier/Production -p 1234 --no-conda

before mlflow serve need to set in env path
 mlflow models serve --model-uri models:/iris-classifier_4/Production --host 107.108.32.137 -p 5000 --no-conda
  mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root \\107.108.32.137\mlflow-main\unet\artifacts --host 107.108.32.137 --port 5000

mlflow.set_tracking_uri("http://107.108.32.137:5000")
#project name
mlflow.set_experiment('unet')
#experiment name
with mlflow.start_run(run_name='unet'):
    #mlflow.pytorch.save_model(model,"unet_model")
	#model register with loged the model
    mlflow.pytorch.log_model(model,"unet_model",registered_model_name="iris-classifier_4")
#making the model in production
client = mlflow.tracking.MlflowClient()
client.transition_model_version_stage(
    name="iris-classifier_5",
    version=1,
    stage="Production"
)






dvc stage add -n data_split -p data_source.local_path,base.random_state,split.split_ratio -d src/data_split.py -o data/split python src/data_split.py data/data.csv


dvc stage add -n data_processing -p split.dir,split.train_file,split.test_file,process.dir,process.train_file,process.test_file -d src/data_processing.py -d data/split -o data/processed python src/data_processing.py data/processed


dvc stage add -n train -p process.dir,process.train_file,process.test_file,base.random_state,base.target_col,train.n_est,model_dir -d src/train.py -d data/processed -o model/model.pkl python src/train.py data/features model/model.pkl


dvc stage add -n evaluate -d src/evaluate.py -d model/model.pkl -d data/processed -M eval/live/metrics.json -O eval/live/plots -O eval/prc -o eval/importance.png python src/evaluate.py model/model.pkl data/processed
  
  
dvc remove data_split
dvc remove data_processing
dvc remove train
dvc remove evaluate

dvc metrics show
dvc plots show

dvc metrics diff
dvc plots diff

https://github.com/erarunn/DVC.git
cd ..
 python -m venv dvc
 .\dvc\Scripts\activate
 
 conda create -n envname python=3.9 ipykernel
 conda activate envname
 python -m ipykernel install --user --name=envname
 pip install notebook
 
 
 
