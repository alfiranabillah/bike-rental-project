# Bike Rental Analysis
This is a final project from Dicoding in the "Belajar Analisis Data Dengan Python" course to make analysis and create a dashboard from the bike sharing dataset. See the detail of this analysis and visualization on the [notebook](bike_rental.ipynb) In the notebook file, I attached the way I did the analysis from Data Wrangling, Exploratory Data Analysis, and Data Visualization. 

## Project Work Cycle
### 1. Data Wrangling:
* Gathering data
* Assessing data
* Cleaning data
### 2. Exploratory Data Analysis (EDA):
* Create data exploration
### 3. Data Visualization:
* Create data visualization to answer business question
### 4. Dashboard:
* Set up the DataFrame which will be used
* Make filter components on the dashboard
* Complete the dashboard with various data visualizations

## Business Question
1. How is the trend in the number of bike-sharing rides in recent years?
2. What is the usage pattern of bike-sharing rides based on day of the week?
3. What are the differences in bicycle usage patterns between weekdays and weekends?
4. What season has the highest bike-sharing rides?
5. How does the number of registered and casual users compare?
6. Does weather affect bikeshare usage?

## Insights 
1. The number of bikeshare rides in 2012 was higher than in 2011. Despite the increase in overall numbers, the usage pattern remained consistent in both years. The trends reveal a seasonal behavior, where bikeshare rides peaked during the middle of the year, likely due to favorable weather or increased outdoor activities, and dropped at the beginning and end of the year, possibly because of colder weather or reduced demand.
2. Registered users predominantly used the bikes on weekdays, likely for commuting to work or school, while casual users had more rides on weekends, suggesting they used the service mainly for leisure or recreational activities.
3. Bicycle usage is significantly higher on weekdays, comprising 69.6% of total usage, while holidays account for only 30.4%. This suggests that bicycles are primarily used for commuting or work-related purposes rather than leisure activities during weekends and holidays.
4. Bikeshare rides were highest during the summer season and lowest during the winter season.
5. Registered users dominate the user base, making up 81.2% compared to 18.8% casual users. This significant difference suggests that most individuals prefer registering, likely to take advantage of benefits or additional access provided through registration.
6. Weather plays a big role in influencing bikeshare usage habits. The number of rides is significantly higher during clear weather compared to more extreme weather conditions such as rain.

## Dashboard
View the dashboard on streamlit could directly on this [link ](https://bikeshare-rental.streamlit.app/)





![Screenshot (108)](https://github.com/user-attachments/assets/deece726-40c4-4fc9-871f-66632ddc4fac)
















### Run Dashboard 
1. Download this project.
2. Install the Streamlit in your terminal or command prompt using pip install streamlit. Install another libraries like pandas, numpy, scipy, matplotlib, and seaborn if you haven't.
3. Please note, don't move the csv file because it acts a data source. keep it in one folder as app.py
4. Open your VSCode and run the file by clicking the terminal and write it streamlit run app.py.
