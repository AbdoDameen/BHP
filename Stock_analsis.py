#!/usr/bin/env python
# coding: utf-8

# In[6]:


from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file


start=datetime.datetime(2020,9,1)
end=datetime.datetime(2020,12,31)

df=data.DataReader(name="BHP",data_source="yahoo",start=start,end=end)

#df

def inc_dec(c, o):
    if c > o:
        Value="Increase"
    elif c < o:
        Value="Decrease"
    else:
        Value="Equal"
    return Value

df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close,df.Open)]  #

df["Middle"]=(df.Open+df.Close)/2

df["Height"]=abs(df.Close-df.Open)


#df.index[df.Close > df.Open]  #to check when close was ha

date_increase=df.index[df.Close > df.Open]
date_decrease=df.index[df.Close < df.Open]

#df

p=figure(x_axis_type='datetime', width=1200, height=400,title="Candelstick Chart")
#p.title="Candelstick Chart"
p.grid.grid_line_alpha=0.3

hours_12=12*60*60*1000

p.segment(df.index, df.High, df.index, df.Low, color="black")

p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],
      hours_12,df.Height[df.Status=="Increase"],fill_color="#4dff4d",line_color="black")

p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],
      hours_12,df.Height[df.Status=="Decrease"],fill_color="#ff4d4d",line_color="black")



output_file=("CS.html")
show(p)

