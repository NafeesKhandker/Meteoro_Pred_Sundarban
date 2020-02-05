from Load_Dataset import load_dataset
import numpy as obj_numpy


def clean():
    weather_data = load_dataset("Datasets/Weather(Khulna).csv")
    # Handling missing value
    print(weather_data.loc[weather_data['mintemp'] == '****'].count())
    weather_data = weather_data.replace('****', obj_numpy.nan)
    print("Weather\n", weather_data.isnull().sum())


clean()