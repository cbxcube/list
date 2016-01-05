#!/usr/bin/python3

import sqlite3
import os

shouldExit = False

#Create database
def createTable():
	c.execute('CREATE TABLE items(name TEXT, purchased BOOLEAN)')
	db.commit()


if os.path.isfile('./list.db'):
	print('Welcome!')
	print('')
	db = sqlite3.connect('list.db')
	c = db.cursor()
else:
	db = sqlite3.connect('list.db')
	c = db.cursor()
	createTable()

shopList = []

#Get data from user
def itemInput():
	while True:
		i = input("Enter item (or Enter to stop): ")
		if not i:
			break
		t = str(i)
		shopList.append(i)
	for x in shopList: # Add items to DB
		c.execute('INSERT INTO items VALUES(?,?)', (x, 0) )

def listItems():
	c.execute('select * from items')
	items = c.fetchall()
	for x in items:
		print(x)
		print('')

#Update values
def select():
	item = input("Input an item ")
	item = item.lower()
	c.execute('SELECT name FROM items WHERE name=(?)', (item,))
	c.execute('UPDATE items SET purchased=1 WHERE name=(?)', (item,))

#removed purchased items
def remove():
	c.execute('DELETE FROM items WHERE purchased=1')

#controls
def controls():
	global shouldExit
	print("Menu:")
	print("View, Add, Select, Quit")
	option = input()
	if option.lower() == "view":
		listItems()
	elif option.lower() == "add":
		itemInput()
	elif option.lower() == "select":
		select()
	elif option.lower() == "quit":
		shouldExit = True
	else:
		print("Not a valid option") 
while not shouldExit:
	controls()

remove()
db.commit()
db.close()
