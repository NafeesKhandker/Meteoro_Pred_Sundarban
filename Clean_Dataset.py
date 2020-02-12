from Load_Dataset import load_dataset

import numpy as obj_numpy

def clean(data="Datasets/Weather(Khulna).csv", type="mean"):
    weather_data = load_dataset(data)
    # Handling missing value(in this data, '****' is represented as null values)
    print(weather_data.loc[weather_data['mintemp'] == '****'].count())
    weather_data = weather_data.replace('****', obj_numpy.nan)
    print("Weather\n", weather_data.isnull().sum())

    # Create three column for day, month, year
    date_list = weather_data.drop(['rainfall', 'cloudamount', 'sunshine', 'humidity', 'maxtemp', 'mintemp'], axis=1)
    date_list = date_list.astype({"Day": int})

    # Convert all the value in float
    weather_data = weather_data.astype(
        {"rainfall": float,
         "cloudamount": float,
         "sunshine": float,
         "humidity": float,
         "maxtemp": float,
         "mintemp": float})

    if type == "mean":
        # Replace all the null values with their mean values
        weather_data["sunshine"] = weather_data.sunshine.fillna(round(weather_data['sunshine'].mean(), 1))
        weather_data["maxtemp"] = weather_data.maxtemp.fillna(round(weather_data['maxtemp'].mean(), 1))
        weather_data["mintemp"] = weather_data.mintemp.fillna(round(weather_data['mintemp'].mean(), 1))
    elif type == "delete":
        weather_data.drop(weather_data[weather_data['sunshine'] == obj_numpy.nan].index, inplace = True)
        weather_data.drop(weather_data[weather_data['maxtemp'] == obj_numpy.nan].index, inplace = True)
        weather_data.drop(weather_data[weather_data['mintemp'] == obj_numpy.nan].index, inplace = True)
    elif type == "median":
        # Replace all the null values with their mean values
        weather_data["sunshine"] = weather_data.sunshine.fillna(round(weather_data['sunshine'].median(), 1))
        weather_data["maxtemp"] = weather_data.maxtemp.fillna(round(weather_data['maxtemp'].median(), 1))
        weather_data["mintemp"] = weather_data.mintemp.fillna(round(weather_data['mintemp'].median(), 1))

    print(weather_data)

clean()