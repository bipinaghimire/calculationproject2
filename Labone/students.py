'''
3. N students takes K apples and distribute them among each other them among each other evenly. The remaining (the undivisible) part remains in the basket. How
many apples will each student get? How many apples will remain in the basket? The program reads the number N and K. It should print the two answers for the
question above.
'''
N = int(input("enter the number of students : "))
K = int(input("enter the number of apples : "))
distribution = K//N
remaining = K%N
print (f"Each student will get{distribution}")
print (f"The remaining apple in the basket are{remaining}")