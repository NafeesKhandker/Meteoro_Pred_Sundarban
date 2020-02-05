import pandas as pd

def load_dataset(dataset):
    data = pd.read_csv(dataset)
    return data

weather_data = load_dataset("Datasets/Weather(Khulna).csv")
# print(weather_data)

