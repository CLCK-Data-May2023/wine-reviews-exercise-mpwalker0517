# add your code here
import pandas as pd

#read in data
reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

#number of reviews per country
country_count = reviews.country.value_counts()

#average points per country, rounded to one decimal place 
avg_points = reviews.groupby('country')['points'].mean().round(1)

#Create DataFrame 
df = pd.DataFrame.merge(country_count, avg_points, on = 'country')

#write data to csv
df.to_csv('data/reviews-per-country.csv')
