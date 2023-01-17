import pandas as pd


def calculate(print_data=True):
  url = 'https://raw.githubusercontent.com/a-mt/fcc-demographic-data-analyzer/master/adult.data.csv'
  df = pd.read_csv(url)

  #Question_1 : How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
  q1_race = df['race'].value_counts()

  #Question_2 : What is the average age of men?
  q2_avg_men = q2_avg_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

  # Question 3 : What is the percentage of people who have a Bachelor's degree?
  # number of people with Bachelors degree
  bachelor = df.loc[df['education'] == 'Bachelors', 'education'].count()
  # percentage of people who have a Bachelor's degree
  q3_percentage_bachelors = round(bachelor / df['education'].count() * 100, 1)

  # Question 4 : What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
  # people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K
  filtered_data = df[
    df['education'].isin(['Doctorate', 'Bachelors', 'Masters'])
    & df['salary'].str.startswith('>')]
  # percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K
  q4_adv_more50k = round(
    filtered_data['education'].count() / df['education'].count() * 100, 1)

  # Question 5 : What percentage of people without advanced education make more than 50K?
  # number of people without advanced education make more than 50K?
  filtered_data2 = df[
    -df['education'].isin(['Doctorate', 'Bachelors', 'Masters'])
    & df['salary'].str.startswith('>')]
  # percentage of people without advanced education make more than 50K?
  q5_noadvedu_more50k = round(
    filtered_data2['education'].count() / df['education'].count() * 100, 1)

  # Question 6 : What is the minimum number of hours a person works per week?
  q6_min_hours = df['hours-per-week'].min()

  # Question 7 : What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
  # number of the people who work the minimum number of hours per week have a salary of more than 50K
  filtered_data3 = df[(df['hours-per-week'] == df['hours-per-week'].min())
                      & (df['salary'].str.startswith('>'))]
  #percentage
  q7_minhr_more50k = round(
    filtered_data3['salary'].count() / df['salary'].count() * 100, 1)

  # Question 8 : What country has the highest percentage of people that earn >50K and what is that percentage?
  highest_country = df.loc[df['salary'].str.startswith('>'),
                           'native-country'].value_counts()
  q8_highest_country = highest_country.index[0]
  q8_percentage = round(
    highest_country[0] / df['native-country'].count() * 100, 1)

  # Question 9 : Identify the most popular occupation for those who earn >50K in India.
  q9_pop_occupation = df.loc[df['salary'].str.startswith('>'),
                             'occupation'].value_counts().index[0]

  if print_data:
    print("Number of each race represents:", q1_race)
    print("Average age of men:", q2_avg_men)
    print(
      f"Percentage of people with Bachelors degrees:  {q3_percentage_bachelors}%"
    )
    print(
      f"Percentage of people with advanced education that earn >50K: {q4_adv_more50k}%"
    )
    print(
      f"Percentage of people without advanced education that earn >50K: {q5_noadvedu_more50k}%"
    )
    print(f"Min working hours: {q6_min_hours} hours/week")
    print(
      f"Percentage of people who work the minimum number of hours per week with >50K salary: {q7_minhr_more50k}%"
    )
    print("Country with highest percentage of people with >50k salary:",
          q8_highest_country)
    print(f"Highest percentage of people with >50k salary: {q8_percentage}%")
    print("Most popular occupation with >50k salary:", q9_pop_occupation)
  return {
    'q1_race': q1_race,
    'q2_avg_men': q2_avg_men,
    'q3_percentage_bachelors': q3_percentage_bachelors,
    'q4_adv_more50k': q4_adv_more50k,
    'q5_noadvedu_more50k': q5_noadvedu_more50k,
    'q6_min_hours': q6_min_hours,
    'q7_minhr_more50k': q7_minhr_more50k,
    'q8_highest_country': q8_highest_country,
    'q8_percentage': q8_percentage,
    'q9_pop_occupation': q9_pop_occupation
  }
