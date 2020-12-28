import threading 
from threading import*
import time

#Global Variables
storageDict = {}
l=[]


#Update File
def updateFile():
    f = open("storage.txt",'w')
    data = str(storageDict)
    f.write(data)
    

#Creating New Key-Value File

def create():
    print("Enter the Key: ")
    key = int(input())
    
    print("Enter the Value: ")
    value = input()

    print("\nEnter the Expiration Minute(s): ")
    expiryTime = int(input())
    expiryTime *= 60
    
    if key in storageDict:
        print("Error: this key is Already exists:\n")
    else:
        if len(storageDict) < (1024*1024*1024) and key < (16*1024*1024): #Checking the memory limit
            if expiryTime == 0: l = [value, expiryTime]
            else: l = [value, time.time() + expiryTime]
            
            if len(value) <= 32:
                storageDict[key] = l
                print("\nSuccessfully Created\n")
            else:
                print("Error: Invalid Key value\n")
        else:
            print("Error: Memory Limit exceed\n")
    updateFile()


#Reading the Key-Value Pairs
            
def read():
    print("Enter key to read the pair:")
    key = int(input())
    if key not in storageDict: print("Error: Key does not Exist\n")
    else:
        data = storageDict[key]
        if time.time() < data[1] or data[1] == 0: print("\n", key, data[0])
        else: print("Error: time to live expired\n")
    updateFile()


#Deleting the Key-Value Pairs

def delete():
    print("Enter the key to delete\n")
    key = int(input())
    if key not in storageDict: print("Error: Key does not Exist\n")
    else:
        del storageDict[key]
        print("Successfully deteled\n")
    updateFile()


#Program Starts HERE

print("-------------------------------")
print("File based key-value data store")
print("-------------------------------\n")

Choice = 0
while(True):
    print("Select the operation to be performed (Enter Number):\n")
    print("1-Create\n2-Read\n3-Delete\n4-Show all\n5-Exit\n")
    
    Choice = int(input())
    if(Choice == 1): create()
    elif(Choice == 2): read()
    elif(Choice == 3): delete()
    elif (Choice == 4):
        if not storageDict: print("No Records Found!\n")
        for x in storageDict:
            print("Key:", x, "| Value:", storageDict[x][0], "| Time:", storageDict[x][1], "\n")
        updateFile()
    elif(Choice == 5):
        print("Program Ended.")
        break
    else:
        print("Invalid Operation\n")
    
    print("---------------------------------------------------\n")

#Creating Threads and Writing into the File
if Choice != 5:
    t1 = Thread(target=(create or read or delete)) 
    t1.start()
    time.sleep(1)
    t2 = Thread(target=(create or read or delete))
    t2.start()
    time.sleep(1)

    
