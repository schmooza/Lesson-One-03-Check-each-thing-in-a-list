# if you need to restart, copy this code into myCode.py


from colored import fg, bg, attr

def listomatic():

	myList = ["pig", "dog","chicken","tiger", "elephant"]
	print("My old list", myList)
	# comment
	for n in myList:
		print(n, "debug")
		if n == "bee":
			
			
			print ('%s%s A tiger !!! %s' % (fg('black'), bg('yellow'), attr('reset')))

			
			# comment
			myList.remove(n)
		
		else:
			pass
	# comment
	
	
	#-----------------------------------------------------
	myNeWList = myList
	print("My new List", myNeWList)
	lenMyNewList = len(myNeWList)
	print (lenMyNewList, "debug")
