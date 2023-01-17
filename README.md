## Demographic Data Analyzer

*This project is part of "Data Analyst with Python" course provided by freecodecamp and is required as the accomplishment criteria.*

> Link to course : https://www.freecodecamp.org/learn/data-analysis-with-python/
#
### Overview
Data source will be extracted from the 1994 Census database. The dataset will contain informations as shown in table below.

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |

#
### Objective :

The result will cover the following index:
<p> 1. Number of each race represented in the dataset.
<p> 2. Average age of men.
<p> 3. Percentage of people with Bachelor's degree.
<p> 4. Percentage of people with advanced education (Bachelors, Masters, or Doctorate) with more than 50K salary.
<p> 5. Percentage of people without advanced education with more than 50K salary.
<p> 6. Minimum number of hours a person works per week.
<p> 7. Percentage of the people who work the minimum number of hours per week have a salary of more than 50K.
<p> 8. Country with highest percentage of people that earn >50K and the percentage
<p> 9. Most popular occupation for those who earn >50K in India.
