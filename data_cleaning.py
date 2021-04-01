import sys
from sklearn.impute import KNNImputer
import pandas as pd

def map_marital_status(num):
        if num == 'Married':
                return 1
        elif num == 'Not Married':
                return 0
        else:
                return num

binary = ['behavioral_antiviral_meds','behavioral_avoidance',
              'behavioral_face_mask', 'behavioral_wash_hands',
              'behavioral_large_gatherings','behavioral_outside_home',
              'behavioral_touch_face', 'doctor_recc_h1n1',
              'doctor_recc_seasonal', 'chronic_med_condition',
              'child_under_6_months', 'health_worker',
              'health_insurance', 'marital_status']

opinion = ['opinion_h1n1_vacc_effective','opinion_h1n1_risk',
           'opinion_h1n1_sick_from_vacc','opinion_seas_vacc_effective',
           'opinion_seas_risk','opinion_seas_sick_from_vacc']

categorical = ['age_group','education','race', 'sex',
               'income_poverty', 'marital_status', 'hhs_geo_region',
               'census_msa']

data_file = sys.argv[1]
df = pd.read_csv(data_file)

df = df.set_index('respondent_id')

print('set index to: respondent_id')


df['marital_status'] = df['marital_status'].map(lambda x:map_marital_status(x))
df = pd.get_dummies(df, columns=['employment_status','rent_or_own'])
df = df.drop(['employment_industry','employment_occupation'], axis=1)


### IMPUTATION ###
print('imputing...')

df['h1n1_concern'].fillna(value=df['h1n1_concern'].mean(), inplace=True)
df['h1n1_knowledge'].fillna(value=df['h1n1_concern'].mean(), inplace=True)
df['household_adults'].fillna(value=df['household_adults'].mean(), inplace=True)
df['household_children'].fillna(value=df['household_children'].mean(), inplace=True)
df['income_poverty'].fillna(value=df['income_poverty'].value_counts().max(), inplace=True)
df['education'].fillna(value=df['education'].value_counts().max(), inplace=True)

imputer = KNNImputer(n_neighbors=2)
df[binary+opinion] = imputer.fit_transform(df[binary+opinion])


print('changing column types')
df['h1n1_concern'] = df['h1n1_concern'].astype("category")
df['h1n1_knowledge'] = df['h1n1_knowledge'].astype("category")


for col in binary:
        df[col] = df[col].map(lambda x: True if (x == 1.0) else False)
        df[col] = df[col].astype("category")

for col in opinion:
        df[col] = df[col].astype('int8')
        df[col] = df[col].astype("category")


for category in categorical:
        df[category] = df[category].astype("category")

df['household_adults'] = df['household_adults'].astype('int8')
df['household_children'] = df['household_children'].astype('int8')

df['h1n1_vaccine'] = df['h1n1_vaccine'].map(lambda x: True if (x == 1.0) else False)
df['h1n1_vaccine'] = df['h1n1_vaccine'].astype("category")
df['seasonal_vaccine'] = df['seasonal_vaccine'].map(lambda x: True if (x == 1.0) else False)
df['seasonal_vaccine'] = df['seasonal_vaccine'].astype("category")

df.to_pickle("data/data.pkl")

print('data is ready for use')

