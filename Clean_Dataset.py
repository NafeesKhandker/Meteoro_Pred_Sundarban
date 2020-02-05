from Load_Dataset import load_dataset
import numpy as np

def clean():
    weather = load_dataset("Datasets/Weather(Khulna).csv")
    # Handling missing value
    print(weather.loc[weather['mintemp'] == '****'].count())
    weather = weather.replace('****', np.nan)
    print("Weather\n", weather.isnull().sum())

clean()