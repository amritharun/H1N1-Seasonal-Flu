import sys


import pandas as pd

data_file = sys.argv[1]
df = pd.read_csv(data_file)

df = df.set_index('respondent_id')
df = df.dropna()

df['h1n1_concern'] = df['h1n1_concern'].astype("category")
df['h1n1_knowledge'] = df['h1n1_knowledge'].astype("category")

binary = ['behavioral_antiviral_meds','behavioral_avoidance',
              'behavioral_face_mask', 'behavioral_wash_hands',
              'behavioral_large_gatherings','behavioral_outside_home',
              'behavioral_touch_face', 'doctor_recc_h1n1',
              'doctor_recc_seasonal', 'chronic_med_condition',
              'child_under_6_months', 'health_worker', 'health_insurance']

for col in binary:
        df[col] = df[col].map(lambda x: True if (x == 1.0) else False)
        df[col] = df[col].astype("category")

opinion = ['opinion_h1n1_vacc_effective','opinion_h1n1_risk',
           'opinion_h1n1_sick_from_vacc','opinion_seas_vacc_effective',
           'opinion_seas_risk','opinion_seas_sick_from_vacc']
for col in opinion:
        df[col] = df[col].astype('int8')
        df[col] = df[col].astype("category")

categorical = ['age_group','education','race', 'sex',
               'income_poverty', 'marital_status',
               'rent_or_own','employment_status',
               'hhs_geo_region','census_msa','employment_industry',
               'employment_occupation']

for category in categorical:
        df[category] = df[category].astype("category")
df['household_adults'] = df['household_adults'].astype('int8')
df['household_children'] = df['household_children'].astype('int8')




df.to_pickle("data/data.pkl")

print('Successfully cleaned data')
