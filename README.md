# H1N1-Seasonal-Flu

### DON'T USE THE PICKLE DATA, ITS MISSING IMPORTANT COLUMNS, USE THE ORIGINAL DATA.

### Setup
1. Activate virtual environment using your preferred package. (optional)
2. Install packages required to run code:
```console
foo@bar:~$ pip install -r requirements.txt
```
3. Run data cleaning script with the local csv data file location
```console
foo@bar:~$ python3 data_cleaning.py path/to/data/file
```
4. Now to access the cleaned data for visualization/analysis use:
```python
pd.read_pickle('data/data.pkl')
```
5. Enjoy! :smile:



### Tasks:
1. Garvit & Amrit: Data Cleaning, Pre-processing, Feauture Engineering.
2. Shruti: Ensemble Models (3 Models)
3. Kinjal: Linear and Tree Based Models (3 Models)
4. Abhishek: Neural Models (3 Models)
