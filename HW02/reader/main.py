import numpy as np


if __name__ == '__main__':
	with open('/home/common/file.txt', 'r') as file:
		numbers = file.read()

	numbers = np.array(numbers.split(' '), dtype=np.int32)
	print(f'Mean of this numbers: {np.mean(numbers)}')
