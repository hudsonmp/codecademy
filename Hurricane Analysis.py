#!/usr/bin/env python
# coding: utf-8

# # Hurricane Analysis

# #### Overview

# This project is slightly different than others you have encountered thus far. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you'll be building. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

# #### Project Goals

# You will work to write several functions that organize and manipulate data about Category 5 Hurricanes, the strongest hurricanes as rated by their wind speed. Each one of these functions will use a number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements.

# #### Prerequisites

# In order to complete this project, you should have completed the Loops and Dictionaries sections of the [Learn Python 3 Course](https://www.codecademy.com/learn/learn-python-3). This content is also covered in the [Data Scientist Career Path](https://www.codecademy.com/learn/paths/data-science/).

# ## Project Requirements

# 1. Hurricanes, also known as cyclones or typhoons, are one of the most powerful forces of nature on Earth. Due to climate change caused by human activity, the number and intensity of hurricanes has risen, calling for better preparation by the many communities that are devastated by them. As a concerned environmentalist, you want to look at data about the most powerful hurricanes that have occured. 
# 
#    Begin by looking at the `damages` list. The list contains strings representing the total cost in USD(`$`) caused by `34` category 5 hurricanes (wind speeds $\ge$ 157 mph (252 km/h)) in the Atlantic region. For some of the hurricanes, damage data was not recorded (`"Damages not recorded"`), while the rest are written in the format `"Prefix-B/M"`, where `B` stands for billions (`1000000000`) and `M` stands for millions (`1000000`).
#    
#    Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as `"Damages not recorded"`.
#    
#    Test your function with the data stored in `damages`.

# In[3]:


# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M',
          '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M',
          '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded',
          '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B',
          '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
          '91.6B', '25.1B']

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
             "B": 1000000000}
damages_converted = []
def damages_conversion(damages):
    for damage in damages:
        if damage[-1] == 'M':
            damage_updated = damage[:-1]
            damage = float(damage_updated)
            damage *= conversion["M"]
            damages_converted.append(damage)
        elif damage[-1] == 'B':
            damage_updated = damage[:-1]
            damage = float(damage_updated)
            damage *= conversion["B"]
            damages_converted.append(damage)
        else:
            damages_converted.append(damage)
    return damages_converted

damages_conversion(damages)
print(damages_converted)


# test function by updating damages


# 2. Additional data collected on the `34` strongest Atlantic hurricanes are provided in a series of lists. The data includes:
#    - `names`: names of the hurricanes
#    - `months`: months in which the hurricanes occurred
#    - `years`: years in which the hurricanes occurred
#    - `max_sustained_winds`: maximum sustained winds (miles per hour) of the hurricanes
#    - `areas_affected`: list of different areas affected by each of the hurricanes
#    - `deaths`: total number of deaths caused by each of the hurricanes
#    
#    The data is organized such that the data at each index, from `0` to `33`, corresponds to the same hurricane.
#    
#    For example, `names[0]` yields the "Cuba I" hurricane, which occurred in `months[0]` (October) `years[0]` (1924).
#    
#    Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (`Name`, `Month`, `Year`, `Max Sustained Wind`, `Areas Affected`, `Damage`, `Death`) about the hurricane.
#    
#    Thus the key `"Cuba I"` would have the value: `{'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}`.
#    
#    Test your function on the lists of data provided.

# In[36]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

def hurricane_analysis_name(names, months, years, max_sustained_winds, areas_affected, damages_converted, deaths):
    data_zip_name = dict()
    num_hurricanes = len(names)
    for i in range(num_hurricanes):
        data_zip_name[names[i]] = {"Name": names[i], 
                                    "Month":  months[i], 
                                    "Year": years[i], 
                                    "Max wind speed": max_sustained_winds[i], 
                                    "Areas affected": areas_affected[i],
                                    "Damages": damages_converted[i], 
                                    "Deaths": deaths[i]}
    return data_zip_name
        
hurricanes_names = hurricane_analysis_name(names, months, years, max_sustained_winds, areas_affected, damages_converted, deaths)

print(hurricanes_names)


# 2
# Create a Table

# Create and view the hurricanes dictionary


# 3. In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year.
# 
#    Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.
#    
#    For example, the key `1932` would yield the value: `[{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United States'], 'Damage': 'Damage not recorded', 'Deaths': 16}, {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}]`.
#    
#    Test your function on your hurricane dictionary.

# 

# In[10]:


def hurricane_analysis_year(years, names, months, max_sustained_winds, areas_affected, damages, deaths):
    data_zip_year = dict()
    num_hurricane = len(years)
    for i in range(num_hurricane):
        data_zip_year[years[i]] = {"Name": names[i], 
                                    "Month":  months[i], 
                                    "Year": years[i], 
                                    "Max wind speed": max_sustained_winds[i], 
                                    "Areas affected": areas_affected[i],
                                    "Damages": damages[i], 
                                    "Deaths": deaths[i]}
    return data_zip_year
        
hurricanes_years = hurricane_analysis_year(years, names, months, max_sustained_winds, areas_affected, damages, deaths)

print(hurricanes_years)


# 4. You believe that knowing how often each of the areas of the Atlantic are affected by these strong hurricanes is important for making preparations for future hurricanes.
# 
#    Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.
#    
#    Test your function on your hurricane dictionary.

# In[16]:


areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]
def count_damaged_areas(areas_affected):
    damaged_areas = dict()
    for i in areas_affected:
        for individual in i: 
            if individual not in damaged_areas:
                damaged_areas[individual] = 1
            else: 
                damaged_areas[individual] += 1
    return damaged_areas

damaged_areas = count_damaged_areas(areas_affected)
print(damaged_areas)
# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in


# 5. Write a function that finds the area affected by the most hurricanes, and how often it was hit.
# 
#    Test your function on your affected area dictionary.

# 

# In[30]:


def damaged_areas_analysis(damaged_areas):
    most_damaged_area = dict()
    number_of_hurricanes = 0
    hurricane = None
    for key, value in damaged_areas.items():
        if value > number_of_hurricanes:
            hurricane = key
            number_of_hurricanes = value
                
    most_damaged_area = {hurricane: number_of_hurricanes}
    return most_damaged_area
most_damaged_area = damaged_areas_analysis(damaged_areas)
print(most_damaged_area)
                
        
# 5
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in


# 6. Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.
# 
#    Test your function on your hurricane dictionary.

# In[31]:


def count_deaths(names, deaths):
    death_hurricane = dict(zip(names, deaths))
    return death_hurricane
death_hurricane = count_deaths(names, deaths)

def death_analysis(death_hurricane):
    most_deadly = dict()
    number_of_deaths = 0
    hurricane = None
    for key, value in death_hurricane.items():
        if value > number_of_deaths:
            hurricane = key
            number_of_deaths = value         
    most_deadly = {hurricane: number_of_deaths}
    return most_deadly
most_deadly = death_analysis(death_hurricane)
print(most_deadly)

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths


# 7. Just as hurricanes are rated by their windspeed, you want to try rating hurricanes based on other metrics.
# 
#    Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating.
#    
#    ```py
#    mortality_scale = {0: 0,
#    1: 100,
#    2: 500,
#    3: 1000,
#    4: 10000}
#    ```
#    
#    For example, a hurricane with a `1` mortality rating would have resulted in greater than `0` but less than or equal to `100` deaths. A hurricane with a `5` mortality would have resulted in greater than `10000` deaths.
#    
#    Store the hurricanes in a new dictionary where the keys are the mortaility ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating.
#    
#    Test your function on your hurricane dictionary.

# In[35]:


# 7
# Rating Hurricanes by Mortality
def mortality_scale (death_hurricane):
    mortality_scores = dict()
    hurricanes_0 = []
    hurricanes_1 = []
    hurricanes_2 = []
    hurricanes_3 = []
    hurricanes_4 = []
    for key, value in death_hurricane.items():
        if value == 0:
           hurricanes_0.append(key)
        elif 100 >= value > 0:
            hurricanes_1.append(key)
        elif 500 >= value > 100:
            hurricanes_2.append(key)
        elif 1000 >= value > 500:
            hurricanes_3.append(key)
        else:
            hurricanes_4.append(key)
    mortality_scores['0'] = hurricanes_0
    mortality_scores['1'] = hurricanes_1
    mortality_scores['2'] = hurricanes_2
    mortality_scores['3'] = hurricanes_3
    mortality_scores['4'] = hurricanes_4
    return mortality_scores

mortality_scores = mortality_scale(death_hurricane)
print(mortality_scores)
            
# categorize hurricanes in new dictionary with mortality severity as key


# 8. Write a function that finds the hurricane that caused the greatest damage, and how costly it was.
# 
#    Test your function on your hurricane dictionary.

# In[45]:


def count_cost(names, damages_converted):
    damages_hurricane = dict(zip(names, damages_converted))
    return damages_hurricane
damages_hurricane = count_cost(names, damages_converted)

def damage_analysis(damages_hurricane):
    most_costly = dict()
    cost = 0
    hurricane = None
    for key, value in damages_hurricane.items():
        if isinstance(value, float) and value > cost:
            hurricane = key
            cost = value         
    most_costly = {hurricane: cost}
    return most_costly
most_costly = damage_analysis(damages_hurricane)
print(most_costly)


# 9. Lastly, you want to rate hurricanes according to how much damage they cause.
# 
#    Write a function that rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating.
#    ```py
#    damage_scale = {0: 0,
#    1: 100000000,
#    2: 1000000000,
#    3: 10000000000,
#    4: 50000000000}
#    ```
#    
#    For example, a hurricane with a `1` damage rating would have resulted in damages greater than `0` USD but less than or equal to `100000000` USD. A hurricane with a `5` damage rating would have resulted in damages greater than `50000000000` USD (talk about a lot of money).
#    
#    Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating.
#    
#    Test your function on your hurricane dictionary.

# In[46]:


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# 7
# Rating Hurricanes by Mortality
def damage_scale (damages_hurricane):
    damage_scores = dict()
    hurricanes_0 = []
    hurricanes_1 = []
    hurricanes_2 = []
    hurricanes_3 = []
    hurricanes_4 = []
    for key, value in damages_hurricane.items():
        if value == 0:
           hurricanes_0.append(key)
        elif 100000000 >= value > 0:
            hurricanes_1.append(key)
        elif 1000000000 >= value > 100000000:
            hurricanes_2.append(key)
        elif 50000000000 >= value > 1000000000:
            hurricanes_3.append(key)
        else:
            hurricanes_4.append(key)
    damage_scores['0'] = hurricanes_0
    damage_scores['1'] = hurricanes_1
    damage_scores['2'] = hurricanes_2
    damage_scores['3'] = hurricanes_3
    damage_scores['4'] = hurricanes_4
    return damage_scores

damage_scores = mortality_scale(death_hurricane)
print(damage_scores)
            
# categorize hurricanes in new dictionary with mortality severity as key


# categorize hurricanes in new dictionary with damage severity as key


# ## Solution

# Great work! View the **Hurricane Analysis_Solution.ipynb** file or visit [our forums](https://discuss.codecademy.com/t/hurricane-analysis-challenge-project-python/462363) to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different than ours, and that's okay! There are multiple ways to solve these projects, and you'll learn more by seeing others' code.

# In[9]:




