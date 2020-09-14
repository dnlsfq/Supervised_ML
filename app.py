import streamlit as st 
import pandas as pd 
import requests 
import datetime
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 


@st.cache 
def get_covid_df(url):
    response_json = requests.get(url).json()
    df = pd.DataFrame(response_json['data'])
    return df 

url = 'https://raw.githubusercontent.com/tokyo-metropolitan-gov/covid19/development/data/daily_positive_detail.json'
df_covid = get_covid_df(url)

#############################################

diagnosed_date_list = df_covid['diagnosed_date'].values
str_maxdate  = diagnosed_date_list[len(diagnosed_date_list) - 1]
mindate  = datetime.datetime.strptime(diagnosed_date_list[0],'%Y-%m-%d')
maxdate = datetime.datetime.strptime(str_maxdate,'%Y-%m-%d')

selected_date = st.sidebar.date_input(
    'Pick Date',
    [mindate,maxdate],
    min_value=mindate,
    max_value=maxdate
)

str_startdate = selected_date[0].strftime('%Y-%m-%d')
str_enddate = selected_date[1].strftime('%Y-%m-%d') if len(selected_date) == 2 else str_maxdate

df_selected = df_covid.query(
    f'"{str_startdate}" <= diagnosed_date <= "{str_enddate}"'
)

st.write(df_selected)

#############################################

# st.write(df_covid)



x = [
    datetime.datetime.strptime(diagnosed_date,'%Y-%m-%d')
    for diagnosed_date in df_selected['diagnosed_date'].values
]

y_count = df_selected['count'].values

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y_count)

wac_shown = st.sidebar.checkbox('Show Graph')
if wac_shown:
    y_weekly_average_count = df_selected['weekly_average_count'].values
    ax.plot(x,y_weekly_average_count)


xfmt = mdates.DateFormatter('%m/%d')
xloc = mdates.DayLocator(interval=30)

ax.xaxis.set_major_locator(xloc)
ax.xaxis.set_major_formatter(xfmt)


st.write(fig)

