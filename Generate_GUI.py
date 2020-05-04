import tkinter as tk
master = tk.Tk()
master.title("N Queens Problem")

colour1 = 'white'
colour2 = 'black'

dummyImg = tk.PhotoImage()
queenPhoto = tk.PhotoImage('queenImg.png')
queenIco = tk.PhotoImage('queenIco.png')
master.tk.call('wm', 'iconphoto', master._w, queenIco)

def displayGUI(N):

	colour = colour1

	with open('Queen_to_SAT.sol', mode='r') as f:
		content = f.read().splitlines()
	f.close()

	solved = content[0]

	if solved=='UNSAT':
		print("This problem is unsolvable for N = %d" %N)
		return
		
	result = content[1].split()

	r = -1
	c = 0

	for i in range(N*N):

		if (i%N) == 0:
			r += 1
			c = 0

			if (N%2) == 0:
				colour = colour1 if colour == colour2 else colour2

		tile = int(result[i])

		if tile < 0:
			tk.Label(master, bg=colour, image=dummyImg, width=32, height=32, compound='center').grid(row=r,column=c)
		else:
			tk.Label(master, bg='red', image=queenPhoto, width=32, height=32, compound='center').grid(row=r,column=c)

		c += 1
		colour = colour1 if colour == colour2 else colour2
	  

	master.mainloop()

def displayNonGUI(N):

	with open('Queen_to_SAT.sol', mode='r') as f:
		content = f.read().splitlines()
	f.close()

	solved = content[0]

	if solved=='UNSAT':
		print("This problem is unsolvable for N = %d" %N)
		return

	result = content[1].split()

	r = -1
	c = 0

	for i in range(N*N):

		if (i%N) == 0:
			r += 1
			c = 0
			print('')

		tile = int(result[i])

		if tile < 0:
			print(" _ ", end="")
		else:
			print(" X ", end="")

		c += 1

	print('\n')
