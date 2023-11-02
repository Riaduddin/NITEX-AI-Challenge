import tensorflow as tf
from tensorflow import keras
import argparse
import os
import pandas as pd
import numpy as np
from processing import data_processing
from sklearn.metrics import accuracy_score, precision_score, f1_score

def read_file(folder_path):
    # List all CSV files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    # Load your pre-trained deep learning model (replace with your model loading code)
    model = keras.models.load_model('my_model.h5')
    
    # Iterate through the CSV files in the folder
    for csv_file in csv_files:
        # Read the CSV file
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        test_labels=df.iloc[:,0]
        df.drop('label',axis=1,inplace=True)
        df=data_processing(df)
        
        # Perform any necessary data preprocessing here
        
        # Make predictions using the loaded model
        predictions = model.predict(df)
        
        # Process and save the predictions as needed
        # For example, you can save them to another CSV file
        predicted_labels=np.argmax(predictions,axis=1)
        
        #Human in the loop
        expert_labels=np.array(test_labels)

        #Weighted to combine modeling
        weight_model=0.5
        weight_expert=0.5

        final_predictions=(weight_model * predicted_labels) + (weight_expert*expert_labels)
        final_predictions=np.round(final_predictions)
        #without human expertise
        #test_labels = test_labels.astype(int)
        combined_predictions = final_predictions.astype(int)    
        accuracy = accuracy_score(test_labels, predicted_labels)
        precision = precision_score(test_labels, predicted_labels, average='weighted')
        f1 = f1_score(test_labels, predicted_labels, average='weighted')

        #with human epxertise
        accuracy_human = accuracy_score(test_labels, combined_predictions)
        precision_human = precision_score(test_labels, combined_predictions, average='weighted')
        f1_human = f1_score(test_labels, combined_predictions, average='weighted')

        # # Store the metrics in a text file

        with open('output.txt', 'w') as f:
            f.write(f"file_name:{csv_file}")
            # Write the metrics to the file
            f.write("without human expertise:\n")
            f.write(f"Accuracy: {accuracy}\n")
            f.write(f"Precision: {precision}\n")
            f.write(f"F1-Score: {f1}\n\n")

            f.write("with human expertise:\n")
            f.write(f"Accuracy: {accuracy_human}\n")
            f.write(f"Precision: {precision_human}\n")
            f.write(f"F1-Score: {f1_human}\n\n")

            # Write the model summary to the file
            f.write("Model Summary:\n")
            model.summary(print_fn=lambda x: f.write(x + '\n'))
        
        #print(f"Predictions for {csv_file} saved.")

def main():
  parser=argparse.ArgumentParser(description="Process of the pdf directory")
  parser.add_argument("directory",help='Path of the directory')
  args = parser.parse_args()
  directory_path = args.directory
  if os.path.exists(directory_path) and os.listdir(directory_path):
       read_file(directory_path)
  else:
        print("The folder does not exist or is empty. Please provide valid CSV files.")
if __name__ == "__main__":
    main()
