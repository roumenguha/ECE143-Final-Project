from functools import reduce
import pandas as pd
import os

ECO_PATH = './Data/countries.csv'
HAPPY_PATH = './Data/2016.csv'

SAVE_PATH = './Data/data.csv'

def create_dataset(save_path, eco_path, happy_path):
	"""
	This function reads the various datasets we use to construct our dataset, cleans them
	for missing values and bad characters, and saves the final dataset in a new file.
	"""
	### Import Global Ecological Footprint 2016 dataset ###
	# link: https://www.kaggle.com/footprintnetwork/ecological-footprint
	ecological = pd.read_csv(eco_path)

	### Import World Happiness Report 2016 dataset ###
	# link: https://www.kaggle.com/unsdsn/world-happiness
	happiness = pd.read_csv(happy_path)

	### Data Cleaning ###
	# Remove countries that aren't on both datasets
	# Note that I had to name Vietnam to be the same in the csv files
	data = reduce(lambda left, right: pd.merge(left, right, on='Country'), [ecological, happiness])

	# Remove countries with NaNs as any element
	# print(data.isnull().values.any()) # Check if any contain NaNs
	# data[data.isna().any(axis=1)] # Display which ones contain NaN
	data = data.dropna(how='any')

	# Remove dollar signs and comma characters
	data['GDP per Capita'] = data['GDP per Capita'].replace('[\$,]', '', regex=True).astype(float)

	data.to_csv(save_path, index = False)

def load_dataset(save_path):
	"""
	Returns a cleaned version of the final dataset
	"""
	if not os.path.exists(save_path):
		create_dataset()

	data = pd.read_csv(save_path)
	
	return data



