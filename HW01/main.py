import numpy as np


if __name__ == '__main__':
	print('Print numbers:')
	numbers = input()
	numbers = np.array(numbers.split(' '), dtype=np.int32)
	print(f'Mean of this numbers: {np.mean(numbers)}')
