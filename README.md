# H1N1-Seasonal-Flu

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