"""
Title: data_processing.py
Author: Ann Hagan
Purpose: Ingest the initial dataset from Kaggle, create synthenic geospatial data, and create a final dataset for analysis.
Data: 12/10/2024
"""

from zenml.steps import step
import os
import pandas as pd
import random


@step
def generate_coordinates_and_combine(dataframes: list)-> pd.DataFrame:
    def generate_coordinates():
        """
        Generates syntheic coordinates in the US for each of the four locations.
        """
        latitude = random.uniform(25.0, 48.0)
        longitude = random.uniform(-125.0, -66.9)
        return latitude, longitude

    def ingest_and_combine_data(folder_path):
        """
        Ingests the initial dataset from Kaggle and combines it with the synthetic geospatial data.
        """
        combined_data = []

        #Loop through each CSV file in the folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".csv"):
                file_path=os.path.join(folder_path, file_name)
                print(f"Processing file: {file_path}")

                #Read the CSV file
                df = pd.read_csv(file_path)

                #generate coordinates for each row
                df["latitude"], df["longitude"] = zip(*[generate_coordinates() for _ in range(len(df))])

                #add to the combined data
                combined_data.append(df)
        #combin all dataframes into one
        final_df = pd.concat(combined_data, ignore_index=True)
        return final_df 

    if __name__=="__main__":
        folder_path = "./initial_data"
        
        #process and combine the data
        combined_data = ingest_and_combine_data

        #save the combined data to a new CSV file
        combined_data.to_csv("combined_location_data.csv", index=False)
        print("Combined data saved to combined_location_data.csv")