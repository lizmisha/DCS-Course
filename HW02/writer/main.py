import numpy as np


if __name__ == '__main__':
	array = np.random.randint(100, size=10)
	with open('/home/common/file.txt', 'w') as file:
		res_to_file = ' '.join(array.astype(str))
		file.write(res_to_file)
