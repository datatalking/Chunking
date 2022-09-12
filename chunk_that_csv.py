# SOURCE https://pythonspeed.com/articles/indexing-pandas-sqlite/
# FILENAME Chunking_Down

import safety
import bandit
import pandas as pd
import numpy


def main():
	print(pd)
	print(numpy)
	get_whole_file()


def get_whole_file():
	voters_street = pd.read_csv(
		"voters.csv")["County"]
	print(voters_street.value_counts())


# function for defined dataset to scan into an index
def get_voters_on_street(name):
	return pd.concat(
		df[df["county"] == name] for df in
		pd.read.csv("voters.csv", chunksize = 1000))


if __name__ == '__main__':
	main()
    #function_a()
    #function_b()
#print("after __name__ guard")