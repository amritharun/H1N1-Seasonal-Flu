# H1N1-Seasonal-Flu

### Setup
1. Activate virtual environment using your preferred package. (optional)
2. Install packages required to run code:
```console
foo@bar:~$ pip install -r requirements.txt
```
3. Run data cleaning script
```console
foo@bar:~$ python3 data_cleaning.py
```
4. Now to access the cleaned data for visualization/analysis use:
```python
df = pd.read_pickle('data.pkl')
```
5. Enjoy!