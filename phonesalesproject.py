import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go 
data = pd.read_csv("apple_products.csv")
#print(data.head())
#print(data.isnull().sum())
#print(data.describe())
#highest rated phones analysis 
sorting= data.sort_values(by=["Star Rating"],ascending=False) #sorting the coloumn values by column name 
highest_rated = sorting.head(15)  #no of items need to sort like here 15 hai and stored in variable highest_rated
#print(highest_rated['Product Name']) #show the top 15 values under product name 
iphone= highest_rated['Product Name'].value_counts() #counting the value of rating
label= iphone.index
counts= highest_rated["Number of Ratings"]
fig= px.histogram(highest_rated,x=label, y=counts,title="Number of ratings of highest selling iphones" )
fig.show()

#Reviews analysis --#only coloumn name need to change

iphone= highest_rated['Product Name'].value_counts() #counting the value of rating
label= iphone.index
counts= highest_rated["Number of Reviews"]
fig= px.bar(highest_rated,x=label, y=counts,title="Number of reviews of highest selling iphones" )
fig.show()

#scatter plot--sale price and rating relate including discount --linear relationship
figure= px.scatter(data_frame=data,x="Number of Ratings",y="Sale Price",size="Discount Percentage",trendline="ols", title=" Relationship between sale price and rating of iphones")
figure.show()


#analysis of discount and sale of iphones

figure1= px.scatter(data_frame=data,x="Number of Ratings",y="Discount Percentage",size="Sale Price",trendline="ols", title=" Relationship between Discount percentage and rating of iphones")
figure1.show()
