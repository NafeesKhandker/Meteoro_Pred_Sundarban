import pandas as obj_pandas


def load_dataset(dataset):
    data = obj_pandas.read_csv(dataset)
    return data


weather_data = load_dataset("Datasets/Weather(Khulna).csv")
# print(weather_data)

