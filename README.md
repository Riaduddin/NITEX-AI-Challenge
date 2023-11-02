# NITEX-AI-Challenge
### Human-in-the-loop
 - Final prediction is based on 50% of human expert and 50% of model which increase the all metrics.
### Details of the files
 -  Data_analysis_and_model_development.ipynb is preprocessing the data, data mining and model training details.
 -  model_trainer.py where the model is defined.
 -  preprocessing.py where the provided data will be preprocessed.
 -  evaluate_model.py to evaluate the model 
### Instruction for evaluating the model
 - Pull the github reprository
 - install the required files using the below command:
   ```
   pip install requirements.txt
   ```
 - run the evaluate_model.py
   ```
   python evaluate_model.py path/to/dir
   ```
 - It will return as text file named output.txt like the above output.txt and will give the metris such as accuracy, precision and f-1 with and without human expertise. It will also give summary of the model that are used.

Note: All files should be in the same directory.

## Technologies Used
![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src='https://avatars0.githubusercontent.com/u/15658638?v=3&s=100' width=150>](https://www.tensorflow.org/)
[<img target="_blank" src="https://keras.io/img/logo.png" width=200>](https://keras.io/)

[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png">]()