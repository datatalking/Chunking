# SOURCE https://pythonspeed.com/articles/indexing-pandas-sqlite/
# FILENAME Chunking_Down

import safety
import bandit
import pandas as pd
import numpy
from menu import get_data
from filprofiler.api import profile
from dotenv import load_dotenv
from pathlib import Path



def main():
	print(pd)
	print(numpy)
	get_whole_file(filename)
	# get_voters_on_street()


def get_whole_file(filename):
	"""
	:param filename: csv file
	:return:
	"""
	voters_street = pd.read_csv(
		"voters.csv")["County"]
	print(voters_street.value_counts())


def get_data_profile(filename):
	"""
	:param filename: run_profile = full profile, pandas profile, profile on one colum or many etc
	:return:
	"""
	result = profile(lambda: get_whole_file(filename), "/tmp/fil-result")
	return result

# function for defined dataset to scan into an index
def get_voters_on_street(name):
	return pd.concat(
		df[df["county"] == name] for df in
		pd.read.csv("voters.csv", chunksize=1000))


if __name__ == '__main__':
	filename = str
	PATH_TO_ENV = str
	dotenv_path = Path(PATH_TO_ENV)
	load_dotenv(dotenv_path=dotenv_path)
	main()
    # function_a()
    # function_b()
#print("after __name__ guard")
