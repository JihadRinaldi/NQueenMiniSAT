from math import ceil
from displaySol import displayGUI, displayNonGUI
import sys
import subprocess

file = open("N_Queen_To_SAT.cnf", mode='w')

def main():
	global file

	if len(sys.argv) == 1:
		N = int(input("Enter chess board size: "))
	else:
		N = int(sys.argv[1])


	# Printing the File header in the DIMACS CNF Format
	file.write("c N-Queen to SAT converter\n")

	printRowClauses(N)
	printColClauses(N)
	printDiagClauses(N)

	file.close()
	# Minisat INPUT OUTPUT
	subprocess.call(['minisat', 'N_Queen_To_SAT.cnf', 'N_Queen_To_SAT.sol'])

	if N <= 40:
		displayGUI(N)
	else:
		displayNonGUI(N)


def printRowClauses(N):
	# for setting the number of squares and adding one as the loop counter is (inclusive, exclusive)
	lim = N * N + 1
	global file

	for i in range(1, lim):
		file.write("{0:d} ".format(i))
		if i % N == 0:
			file.write("0\n")

	# loop to go through all the squares of the board
	for i in range(1, lim):
		row = ceil(i / N)  # determining the row number based on the square number

		# loop to print the clauses
		for j in range(i, row * N + 1):
			if j == i:  # skips if row = column, as it is meaningless as a SAT clause
				continue
			file.write("-{0:d} -{1:d} 0\n".format(i, j))


def printColClauses(N):
	# for setting the number of squares and adding one as the loop counter is (inclusive, exclusive)
	lim = N * N + 1

	# loop to go through all the squares of the board
	for i in range(1, lim):

		# loop to print the clauses
		for j in range(i, lim, N):
			if j == i:  # skips if row = column, as it is meaningless as a SAT clause
				continue
			file.write("-{0:d} -{1:d} 0\n".format(i, j))


def printDiagClauses(N):
	# for setting the number of squares and adding one as the loop counter is (inclusive, exclusive)
	lim = N * N + 1

	# loop to go through all the squares of the board
	for i in range(1, lim):
		# getting row and column
		row = ceil(i / N)
		col = i % N

		if col == 0: col = N

		# loop to print the Left to Right Diagonal clauses
		for j in range(i, min(((N - col + row) * N + 1), lim), N + 1):
			if j == i:  # skips if row = column, as it is meaningless as a SAT clause
				continue
			file.write("-{0:d} -{1:d} 0\n".format(i, j))

	# loop to go through all the squares of the board
	for i in range(1, lim):
		# loop to print the Right to Left Diagonal clauses
		for j in range(i, lim, N - 1):
			if j == i:  # skips if row = column, as it is meaningless as a SAT clause
				continue
			elif ceil((j - (N - 1)) / N) == ceil(j / N):
				break
			file.write("-{0:d} -{1:d} 0\n".format(i, j))

main()
