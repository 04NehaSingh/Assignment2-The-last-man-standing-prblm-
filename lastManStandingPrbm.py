#__author__ = 'NehaS'
# date = 02-06-17

'''PROBLEM : Last Man Standing" Programming Problem
1000 people are standing in a circle, each of them numbered from 1 to 1000. Person with #1 has a gun.
He shoots person #2 and passes the gun on to person 3. Person 3 kills person 4 and passes the gun to person 5 and so on. 
Every time the person who has the gun shoots the next person in the circle and passes the gun. 
This continues till there is only one person alive. Write a program to output the number of the last man standing.
'''

''' SOLUTION:
			The problem can be solved using circular linked-list which provide an efficient way to iterate through the list_data.
			Each alternative person is killed and the gun is passed to the next person standing next the person killed.
			Ex: 1,2,3,4,5,6,7,8,9,10  	[if 10 person standing in a circle]
			sol: must be 5
'''

# Creating node structure
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Class for creating person standing in a circular
class C_LL:
    
    #Initiallizing head 
    def __init__(self):
        self.head = None
        self.tail = self.head

	# Fixing the position of persons in a circular way
    def insert(self, data):
        curr = self.head
        newnode = Node(data)
        newnode.next = newnode 
        if self.head == None:
            self.head = newnode
        else:
            while curr.next!=self.head:
                curr = curr.next
            curr.next = newnode
            newnode.next = self.head
            self.tail = newnode

    def person_standing_inCircle(self):
        curr = self.head
        list1 = []
        if self.head == None:
            return 0
                  
        list1.append(curr.data)   
        curr = curr.next
        
        while curr!=self.head:
            list1.append(curr.data)
            curr = curr.next
        return list1

    def delete_node_atvalue(self):
        curr = self.head
        next_man = None
        lastMan = 0

        while 1:
            if curr == curr.next:
                lastMan = curr.data
                break

            next_man = curr.next
            curr.next = next_man.next
            del next_man
            curr = curr.next

        return lastMan

       
def last_man_standing_problem():
    winner = None

    #Creating object
    ll = C_LL()

    # Formation of 1000 person standing in circle 
    for i in range(1,1001):
        ll.insert(i)
    list_data = ll.person_standing_inCircle()
    print "\n" +str(list_data)

    # Result of Last person standing 
    winner = ll.delete_node_atvalue()
    print "\n************ Winner is ***********    :\t # " +str(winner)

last_man_standing_problem()