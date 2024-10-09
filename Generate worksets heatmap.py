import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Worksets and Revit Models Heatmap')

# Allow the user to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Strip leading/trailing spaces from the columns
    df['Revit Model Name'] = df['Revit Model Name'].str.strip()
    df['Workset Name'] = df['Workset Name'].str.strip()

    # Separate the data into two groups: worksets starting with a letter (A-Z) and those starting with '*'
    df_no_star = df[~df['Workset Name'].str.startswith('*')]
    df_star = df[df['Workset Name'].str.startswith('*')]

    # Sort each group alphabetically by 'Workset Name'
    df_no_star_sorted = df_no_star.sort_values(by=['Workset Name', 'Revit Model Name'])
    df_star_sorted = df_star.sort_values(by=['Workset Name', 'Revit Model Name'])

    # Create pivot tables for each group
    pivot_table_no_star = pd.crosstab(df_no_star_sorted['Workset Name'], df_no_star_sorted['Revit Model Name'])
    pivot_table_star = pd.crosstab(df_star_sorted['Workset Name'], df_star_sorted['Revit Model Name'])

    # Concatenate the pivot tables, ensuring that the worksets with '*' come after the A-Z worksets
    pivot_table_combined = pd.concat([pivot_table_no_star, pivot_table_star])

    # Calculate dynamic figure size based on number of rows and columns
    n_rows, n_cols = pivot_table_combined.shape
    square_size = 1.4
    fig_width = square_size * n_cols
    fig_height = square_size * n_rows

    # Cap the figure size to prevent it from getting too large
    max_width = 20  # Adjusted for more reasonable display on Streamlit
    max_height = 10  # Adjusted for Streamlit app height
    fig_width = min(fig_width, max_width)
    fig_height = min(fig_height, max_height)

    # Plot setting
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    sns.heatmap(pivot_table_combined, cmap="Blues", cbar=False, linewidths=0.5, linecolor='black', square=True, ax=ax)
    ax.xaxis.set_label_position('top')
    ax.xaxis.tick_top()

    # Rotate x-axis labels to ensure they fit within the image
    plt.xticks(rotation=90, ha='center', fontsize=8)  # Adjust font size if necessary
    plt.title('Worksets and Revit Models\n', fontsize=16, fontweight='bold')
    plt.xlabel('Revit Models', fontsize=14, fontweight='bold')
    plt.ylabel('Worksets', fontsize=14, fontweight='bold')

    # Display the plot in the Streamlit app
    st.pyplot(fig)

