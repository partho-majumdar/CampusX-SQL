import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import numpy as np  # type: ignore

# App Title
st.title("Data Cleaning App")

# File Upload
uploaded_file = st.file_uploader(
    "Upload your dataset (CSV/Excel)", type=["csv", "xlsx"]
)

if uploaded_file:
    # Load the dataset
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Display raw data
    st.subheader("Raw Data")
    st.write(df)

    # Cleaning Options
    st.sidebar.title("Cleaning Options")

    # Handle Missing Values
    if st.sidebar.checkbox("Handle Missing Values"):
        st.write("Missing Values Info")
        st.write(df.isnull().sum())

        missing_option = st.radio(
            "Choose an option",
            [
                "Drop Rows",
                "Fill with Mean",
                "Fill with Median",
                "Fill with Custom Value",
            ],
        )
        if missing_option == "Drop Rows":
            df = df.dropna()
        elif missing_option == "Fill with Mean":
            df = df.fillna(df.mean())
        elif missing_option == "Fill with Median":
            df = df.fillna(df.median())
        elif missing_option == "Fill with Custom Value":
            custom_value = st.text_input("Enter custom value:")
            df = df.fillna(custom_value)
        st.write("Updated Data")
        st.write(df)

    # Remove Duplicates
    if st.sidebar.checkbox("Remove Duplicates"):
        df = df.drop_duplicates()
        st.write("Duplicates Removed")
        st.write(df)

    # Change Data Types
    if st.sidebar.checkbox("Change Data Types"):
        column = st.selectbox("Select Column", df.columns)
        dtype = st.radio("Select Data Type", ["int", "float", "string"])
        if dtype == "int":
            df[column] = pd.to_numeric(df[column], errors="coerce").astype("Int64")
        elif dtype == "float":
            df[column] = pd.to_numeric(df[column], errors="coerce")
        elif dtype == "string":
            df[column] = df[column].astype(str)
        st.write(f"Updated Column: {column}")
        st.write(df)

    # Handle Outliers
    if st.sidebar.checkbox("Handle Outliers"):
        column = st.selectbox(
            "Select Column for Outlier Removal",
            df.select_dtypes(include=[np.number]).columns,
        )
        method = st.radio("Choose Method", ["Remove Outliers", "Cap Values"])
        if method == "Remove Outliers":
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
        elif method == "Cap Values":
            lower_cap = st.number_input("Lower Cap")
            upper_cap = st.number_input("Upper Cap")
            df[column] = np.clip(df[column], lower_cap, upper_cap)
        st.write("Updated Data")
        st.write(df)

    # Rename Columns
    if st.sidebar.checkbox("Rename Columns"):
        column = st.selectbox("Select Column to Rename", df.columns)
        new_name = st.text_input("Enter New Column Name")
        if new_name:
            df.rename(columns={column: new_name}, inplace=True)
            st.write("Updated Columns")
            st.write(df)

    # Save Cleaned Data
    st.subheader("Save Cleaned Data")
    st.download_button(
        "Download Cleaned Data as CSV",
        df.to_csv(index=False),
        "cleaned_data.csv",
        "text/csv",
    )
