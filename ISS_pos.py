import pandas as pd 
import plotly.express as px

url = "http://api.open-notify.org/iss-now.json"

#df = dataframe, line converts json file that is given from this url
#into something that we can read and use
df = pd.read_json(url)

#make two new columns for latitude and longitude from their value in the grid
df["latitude"] = df.loc["latitude", "iss_position"]
df["longitude"] = df.loc["longitude", "iss_position"]
df.reset_index(inplace=True)

#delete the index and message columns
df = df.drop(["index", "message"], axis=1)

#create a geographical scatter plot of the dataframe
fig = px.scatter_geo(df, lat="latitude", lon="longitude")

#show the scatter plot
fig.show()