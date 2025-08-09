# Chest-Disease-Classification-from-Chest-CT-Scan-Image

- [Data Link](https://drive.google.com/file/d/1z0mreUtRmR-P-magILsDR3T7M6IkGXtY/view?usp=drive_link)
## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

## Create  virtual env
```bash
conda create -n chest python=3.8 -y
```
## Activate virtual env
```bash
conda activate chest
```
##  Install libraries frim requirement file
```bash
pip install -r requirements.txt
```
##  Run python file
```bash
python app.py
```


## Workflows

1. Update config.yaml 
2. Update params.yaml
3. Update the entity           # return type of a function
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml

Create an account in dagshub to store the mlflow model, track experiment
https://dagshub.com/ 

Log in with Github


## Mlflow dagshub connection uri

```bash
MLFLOW_TRACKING_URI=https://dagshub.com/harik76/MLflow-Experiment-demo.mlflow \
MLFLOW_TRACKING_USERNAME=harik76 \
MLFLOW_TRACKING_PASSWORD=6a5aadabe5c9c54d7ee9f8d09b1d529194e2d9a7 \
python script.py

MLFLOW_TRACKING_URI=https://dagshub.com/harik76/MLflow-Experiment-demo.mlflow\
MLFLOW_TRACKING_USERNAME=harik76 \
MLFLOW_TRACKING_PASSWORD=6a5aadabe5c9c54d7ee9f8d09b1d529194e2d9a7 \
python script.py

```





## MLflow dagshub connectrion uri
```bash
MLFLOW_TRACKING_URI=https://dagshub.com/harik76/MLflow-Experiment-demo.mlflow \
MLFLOW_TRACKING_USERNAME=harik76 \
MLFLOW_TRACKING_PASSWORD=6a5aadabe5c9c54d7ee9f8d09b1d529194e2d9a7 \
python script.py
```

## RUN from bash terminal
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/harik76/MLflow-Experiment-demo.mlflow
export MLFLOW_TRACKING_USERNAME=harik76 
export MLFLOW_TRACKING_PASSWORD=6a5aadabe5c9c54d7ee9f8d09b1d529194e2d9a7
```

# Demo for MLflow
run this command for MLflow test for wine quality  with different parameter
```bash
python mlflow_demo.py 0.7 0.8
```
### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

### DVC cmd
``` python
def create_padding_mask(batch, padding_token_id):
    batch_size, seq_len = batch.shape
    device = batch.device
    padded = torch.zeros_like(batch, device=device).float().masked_fill(batch == padding_token_id, float('-inf'))
    mask = torch.zeros(batch_size, seq_len, seq_len, device=device) + padded[:,:,None] + padded[:,None,:]
    return mask[:, None, :, :]
```
