import streamlit as st  # type: ignore
from dbhelper import DB
import plotly.express as px # type: ignore

st.sidebar.title("Flight Dashboard")
user_option = st.sidebar.selectbox("Menu", ["Select one", "Check Flights", "Analytics"])

db = DB()

if user_option == "Check Flights":
    st.title("Check flights")

    col1, col2 = st.columns(2)
    with col1:
        city = db.fetch_city_name()
        source = st.selectbox("Source", city)

    with col2:
        city = db.fetch_city_name()
        destination = st.selectbox("Destination", city)

    if st.button("Search"):
        results = db.fetch_all_flights(source, destination)
        st.dataframe(results)

elif user_option == "Analytics":
    st.title("Analytics")
    airline, frequency = db.fetch_airline_frequency()

    data = {
        "Airline": airline,
        "Frequency": frequency,
    }

    # Create a pie chart
    fig = px.pie(
        data,
        names="Airline",
        values="Frequency",
        title="Airline Frequency Distribution",
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)

    city, frequency = db.busy_airport()

    data = {
        "City": city,
        "Frequency": frequency,
    }

    # Create a pie chart
    fig = px.bar(
        x=data["City"],
        y=data["Frequency"],
        title="City Frequency Distribution",
        labels={"x": "City", "y": "Frequency"},  # Label the axes
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)

    date, frequency = db.daily_frequency()
    data = {
        "Date": date,
        "Frequency": frequency,
    }

    # Create a pie chart
    fig = px.line(
        x=data["Date"],
        y=data["Frequency"],
        title="Date Frequency Distribution",
        labels={"x": "Date", "y": "Frequency"},  # Label the axes
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)


else:
    st.title("Tell about the project")
