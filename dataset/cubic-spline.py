#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
	h = []; alpha = []; ell = []; mu = []; z = []
	x = []; y = []; b = []; d = []
	size = int(input('Enter size (n) of data set(x,y): '))
	n = size - 1
	
	for i in range(0, size):
		x.append(float(input('Enter value for x_{}: '.format(i))))
		y.append(float(input('Enter value for y_{}: '.format(i))))
	
	c = list(x)

	for i in range(0, n):
		h.append(x[i + 1] - x[i])

	for i in range(1, n):
		alpha.append(((3 / h[i]) * (y[i + 1] - y[i])) - ((3 / h[i-1]) * (y[i] - y[i - 1])))

	ell.append(1); mu.append(0); z.append(0);
	
	for i in range(1, n):
		ell.append((2 * (x[i + 1] - x[i - 1])) - (h[i - 1] * mu[i - 1]))
		mu.append(h[i] / ell[i])
		z.append((alpha[i-1] - (h[i - 1] * z[i - 1])) / ell[i])

	ell.append(1); z.append(0); c[-1] = 0

	for j in range((n - 1), -1, -1):
		c[j] = (z[j] - (mu[j] * c[j + 1]))
		b.append((y[j + 1] - y[j] / h[j]) - ((h[j] * (c[j + 1] + (2 * c[j]))) / 3))
		d.append((c[j + 1] - c[j]) / (3 * h[j]))

	
	for i in range(0, n):
		print('S_{}(x) = {} + {}x + {}x^2 + {}x^3 for x ∈ [{}, {}]'.format(i, y[i], b[n - 1 - i], c[i], d[n - 1 - i], x[i], x[i + 1]))


if __name__ == '__main__':
	main()