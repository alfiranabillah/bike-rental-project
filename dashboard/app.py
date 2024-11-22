import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st


df = pd.read_csv("https://raw.githubusercontent.com/alfiranabillah/bike-rental-project/main/dashboard/day_cleaned.csv")
df['dteday'] = pd.to_datetime(df['dteday'])

st.set_page_config(page_title="Bike Rental Dashboard",
                   layout="wide")

# FUNCTIONS

def create_monthly_users_df(df):
    monthly_users_df = df.resample(rule='M', on='dteday').agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    monthly_users_df.index = monthly_users_df.index.strftime('%b-%y')
    monthly_users_df = monthly_users_df.reset_index()
    monthly_users_df.rename(columns={
        "dteday": "yearmonth",
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)

    return monthly_users_df

def create_seasonly_users_df(df):
    seasonly_users_df = df.groupby("season").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    seasonly_users_df = seasonly_users_df.reset_index()
    seasonly_users_df.rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)

    seasonly_users_df = pd.melt(seasonly_users_df,
                                      id_vars=['season'],
                                      value_vars=['casual_rides', 'registered_rides'],
                                      var_name='type_of_rides',
                                      value_name='count_rides')

    seasonly_users_df['season'] = pd.Categorical(seasonly_users_df['season'],
                                             categories=['Spring', 'Summer', 'Fall', 'Winter'])

    seasonly_users_df = seasonly_users_df.sort_values('season')

    return seasonly_users_df

def create_weekday_users_df(df):
    weekday_users_df = df.groupby("weekday").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    weekday_users_df = weekday_users_df.reset_index()
    weekday_users_df.rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)

    weekday_users_df = pd.melt(weekday_users_df,
                                      id_vars=['weekday'],
                                      value_vars=['casual_rides', 'registered_rides'],
                                      var_name='type_of_rides',
                                      value_name='count_rides')

    weekday_users_df['weekday'] = pd.Categorical(weekday_users_df['weekday'],
                                             categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    weekday_users_df = weekday_users_df.sort_values('weekday')

    return weekday_users_df

def create_weatherly_users_df(df):
    weatherly_users_df = df.groupby("weathersit").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    weatherly_users_df = weatherly_users_df.reset_index()
    weatherly_users_df.rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)

    weatherly_users_df = pd.melt(weatherly_users_df,
                                      id_vars=['weathersit'],
                                      value_vars=['casual_rides', 'registered_rides'],
                                      var_name='type_of_rides',
                                      value_name='count_rides')

    weatherly_users_df['weathersit'] = pd.Categorical(weatherly_users_df['weathersit'],
                                             categories=['Clear', 'Cloudy', 'Light rain', 'Heavy rain'])

    weatherly_users_df = weatherly_users_df.sort_values('weathersit')

    return weatherly_users_df

def create_user_percentage_df(df):
    # Rename columns inside the function
    df = df.rename(
        columns={
            "cnt": "total_rides",
            "casual": "casual_rides",
            "registered": "registered_rides"
        }
    )
    
    # Calculate total rides for each user type
    user_summary = df[["casual_rides", "registered_rides"]].sum()
    user_percentage_df = user_summary.reset_index()
    user_percentage_df.columns = ['user_type', 'count']

    # Add a column for percentage
    total_count = user_percentage_df['count'].sum()
    user_percentage_df['percentage'] = (user_percentage_df['count'] / total_count) * 100

    return user_percentage_df

# filter

min_date = df["dteday"].min()
max_date = df["dteday"].max()

# SIDEBAR 

with st.sidebar:
    # add capital bikeshare logo
    st.image("https://raw.githubusercontent.com/alfiranabillah/bike-rental-project/main/image/bike.png")

    # mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label="Date Filter", min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )



main_df = df[
    (df["dteday"] >= str(start_date)) &
    (df["dteday"] <= str(end_date))
]


monthly_users_df = create_monthly_users_df(main_df)
weekday_users_df = create_weekday_users_df(main_df)
seasonly_users_df = create_seasonly_users_df(main_df)
weatherly_users_df = create_weatherly_users_df(main_df)
user_percentage_df = create_user_percentage_df(main_df)


# KPI 
st.title("Bike Rental Dashboard")
st.markdown("##")

col1, col2, col3 = st.columns(3)

with col1:
    total_all_rides = main_df['cnt'].sum()
    st.metric("Total Rides", value=total_all_rides)
with col2:
    total_casual_rides = main_df['casual'].sum()
    st.metric("Total Casual Rides", value=total_casual_rides)
with col3:
    total_registered_rides = main_df['registered'].sum()
    st.metric("Total Registered Rides", value=total_registered_rides)

st.markdown("---")

# CHART
fig = px.line(monthly_users_df,
              x='yearmonth',
              y=['casual_rides', 'registered_rides', 'total_rides'],
              color_discrete_sequence=["skyblue", "orange", "red"],
              markers=True,
              title="Monthly Count of Bikeshare Rides").update_layout(xaxis_title='', yaxis_title='Total Rides')

st.plotly_chart(fig, use_container_width=True)

fig1 = px.bar(seasonly_users_df,
              x='season',
              y=['count_rides'],
              color='type_of_rides',
              color_discrete_sequence=["skyblue", "orange", "red"],
              title='Count of bikeshare rides by season').update_layout(xaxis_title='', yaxis_title='Total Rides')

st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(weekday_users_df,
              x='weekday',
              y=['count_rides'],
              color='type_of_rides',
              barmode='group',
              color_discrete_sequence=["skyblue", "orange", "red"],
              title='Count of bikeshare rides by weekday').update_layout(xaxis_title='', yaxis_title='Total Rides')

st.plotly_chart(fig2, use_container_width=True)

fig3 = px.bar(weatherly_users_df,
              x='weathersit',
              y=['count_rides'],
              color='type_of_rides',
              color_discrete_sequence=["skyblue", "orange", "red"],
              title='Count of bikeshare rides by weathersit').update_layout(xaxis_title='', yaxis_title='Total Rides')

st.plotly_chart(fig3, use_container_width=True)

fig_pie = px.pie(
    user_percentage_df,
    names='user_type',
    values='count',
    color='user_type',
    title='Percentage of Registered vs Casual Users',
    color_discrete_map={
        'casual_rides': 'skyblue',
        'registered_rides': 'orange'
    }
)
fig_pie.update_traces(textinfo='percent+label')
st.plotly_chart(fig_pie, use_container_width=True)


st.caption('Created by Alfira Nabillah Putri')
