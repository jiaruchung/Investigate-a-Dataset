import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'tmdb_5000_credits.csv'
df = pd.read_csv(file_path)

# Display the first few rows to understand its structure
df.head()

# Display general information about the dataset
df.info()

# Check for missing values in the dataset
df.isnull().sum()

# Check for duplicate entries in the dataset
df.duplicated().sum()

# Check data types of columns to ensure they are appropriate for analysis
df.dtypes

#2. Data Cleaning
#2.1 Identify and Clean Invalid Entries
#python
#Copy code
# Convert 'movie_id' to string to handle all values, including NaNs and floats
df['movie_id'] = df['movie_id'].astype(str)

# Identify problematic entries in 'movie_id' column
invalid_movie_ids = df[~df['movie_id'].str.isdigit()]

# Display the problematic entries
invalid_movie_ids

# Drop or fix invalid entries in 'movie_id' column (Example: Drop rows with invalid movie IDs)
df_cleaned = df[df['movie_id'].str.isdigit()]

# Convert 'movie_id' back to integer for analysis
df_cleaned['movie_id'] = df_cleaned['movie_id'].astype(int)

#2.2 Handle Missing Values
#python
#Copy code
# Drop columns with too many missing values or irrelevant columns (if any)
df_cleaned = df_cleaned.drop(['Unnamed: 4', 'Unnamed: 5', ...], axis=1, errors='ignore')  # Replace ... with irrelevant column names

# Fill or drop rows with missing values as necessary
df_cleaned = df_cleaned.dropna(subset=['title'])  # Example: Drop rows where 'title' is missing

#2.3 Correct Data Types
#python
#Copy code
# Convert columns to appropriate data types
df_cleaned['cast'] = df_cleaned['cast'].astype(str)
df_cleaned['crew'] = df_cleaned['crew'].astype(str)

#2.4 Verify Cleaning
#python
#Copy code
# Verify the dataset after cleaning
df_cleaned.info()
df_cleaned.head()

#3. Exploratory Data Analysis
#3.1 Univariate Analysis
#python
#Copy code
# Univariate Analysis 1: Distribution of 'movie_id'
plt.figure(figsize=(10, 5))
plt.hist(df_cleaned['movie_id'], bins=50, edgecolor='k')
plt.title('Distribution of Movie IDs')
plt.xlabel('Movie ID')
plt.ylabel('Frequency')
plt.show()

# Univariate Analysis 2: Distribution of Movie Title Length
df_cleaned['title_length'] = df_cleaned['title'].apply(len)
plt.figure(figsize=(10, 5))
plt.hist(df_cleaned['title_length'], bins=30, edgecolor='k')
plt.title('Distribution of Movie Title Lengths')
plt.xlabel('Title Length')
plt.ylabel('Frequency')
plt.show()

#3.2 Multivariate Analysis
#python
#Copy code
# Multivariate Analysis 1: Relationship between 'cast_count' and 'crew_count'
df_cleaned['cast_count'] = df_cleaned['cast'].apply(lambda x: len(eval(x)) if pd.notnull(x) else 0)
df_cleaned['crew_count'] = df_cleaned['crew'].apply(lambda x: len(eval(x)) if pd.notnull(x) else 0)

plt.figure(figsize=(10, 5))
plt.scatter(df_cleaned['cast_count'], df_cleaned['crew_count'], alpha=0.5)
plt.title('Relationship between Number of Cast and Crew Members')
plt.xlabel('Number of Cast Members')
plt.ylabel('Number of Crew Members')
plt.show()

# Multivariate Analysis 2: Movie Title Length vs. Number of Cast Members
plt.figure(figsize=(10, 5))
plt.scatter(df_cleaned['title_length'], df_cleaned['cast_count'], alpha=0.5)
plt.title('Movie Title Length vs. Number of Cast Members')
plt.xlabel('Movie Title Length')
plt.ylabel('Number of Cast Members')
plt.show()

#4. Summary Statistics
#python
#Copy code
# Summary statistics of key numerical columns
df_cleaned[['title_length', 'cast_count', 'crew_count']].describe()


