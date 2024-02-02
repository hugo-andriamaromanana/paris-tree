# paris-tree

## Data Science Challenge - "Greening the City" - Paris

The NGO 'Data is for good' offered a data science project called "Greening the city." This challenge focuses on route optimization for the maintenance of trees in the city. The city's urban greening program aims to find a more optimal way for their employees to cover the maximum number of trees in the least amount of time.

## Project Context

The city of Paris wants to determine the most efficient route for its employees to care for and feed the city's trees as part of its urban greening program.

## Presentation of Data

Upon quick examination of the dataset, we find information on trees, including their position (x, y), internal ID, species, growth stage, etc.

## Data Processing and Analysis

We will detail the data processing steps below:

### Step 1: Merge 

- The feature 'type_emplacement' has only one unique value, so it was dropped.
- The idea of merging the two features 'geo_points' into one tuple and the two measurement features into one tuple was considered. 
  However, Power BI doesn't accept tuple types, making it currently impractical, so we left it as is.

### Step 2: Fill Nulls 

- We renamed 'stade_developpement' with complete words and filled null values with "Inconnu" (Unknown).
- We dropped the column 'numero' since it didn't have any relevant values.
- We added a "Complement_adress" column full of empty strings to potentialy try to combine the full adress with the place.
- Null values in 'genre,' 'variete,' and all other information about trees will be filled with "Inconnu."
- Null values in 'remarquable' will be considered as 0, as trees wouldn't be marked as non-remarkable if the data were available.
- There is only one missing value in 'domanialite,' which can be replaced by other instances with the same 'lieu.'

