
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M',
          '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M',
          '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded',
          '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B',
          '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
          '91.6B', '25.1B']

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
