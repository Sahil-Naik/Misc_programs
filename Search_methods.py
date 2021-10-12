import names
import random

stu_names = []
stu_roll = []
stu_att = []
exit = False
exile = False
options = ['absent', 'present']
quote = ['Hooray!', 'We did it!', 'Not bad!', 'Getting Serious?', 'No shaddy business.']

# Function for Linear Search
def lini_srch(na_me):
    for i in range(len(stu_roll)):
        if na_me in stu_names:
            indi = stu_names.index(na_me)
            print(na_me,"was",stu_att[indi],"for the training program.\n")
            break
        else:
            print("No such name exist.")
            break

# Function for Sentinel Search
def senti_srch(lit, n, na_m):
    last = lit[n - 1]
    lit[n - 1] = na_m
    i = 0
    while (lit[i] != na_m):
        i += 1
    lit[n - 1] = last
    if ((i < n - 1) or (lit[n - 1] == na_m)):
        indi = stu_names.index(huh)
        print(na_m,"was",stu_att[indi],"for the training program.\n")
    else:
        print("Name not found!")

# Function for Binary Search
def binary_srch(arr_list, strt, end, var):
    if end >= strt:
        mid = (end + strt)//2
        if arr_list[mid] == var:
            return mid
        elif arr_list[mid] > var:
            return binary_srch(arr_list, strt, mid-1, var)
        else:
            return binary_srch(arr_list, mid+1, end, var)
    else:
        return print("No such Name found!")

# Function for Fibbonacci Series
def fibbo_srch(arr, x, n):
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1
    while (fibM > 1):
        i = min(offset+fibMMm2, n-1)
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i
    if(fibMMm1 and arr[n-1] == x):
        return n-1
    return -1

# This code returns name, roll no., and attendance of student
for k in range(random.randint(65,77)):
    name = names.get_first_name()
    stu_names.append(name)
    stu_roll.append(k+1)
    st_at = random.choice(options)
    stu_att.append(st_at)
    
gret = random.choice(quote)
print(gret,len(stu_roll),"Students joined the training program.")

# This code displays options for the user
while exit != True:
    chc = int(input("List of options available :\n1 = Show names of student.\n2 = Show student's attendance.\n3 = Exit.\nEnter your Choice : "))
    if chc == 1:
        print("\nStudents who signed up for the program are :\n\n", stu_names,"\n")
    elif chc == 2:
        while exile != True:
            huh = input("Enter the name of student : ").capitalize()
            ch1 = int(input("Search using :\n1 = Linear Search\n2 = Sentinel Search\n3 = Binary Search\n4 = Fibonacci Search\n5 = Head back\nEnter your Choice : "))
            if ch1 == 1:
                lini_srch(huh)
            elif ch1 == 2:
                senti_srch(stu_names, len(stu_roll), huh)
            elif ch1 == 3:
                res = binary_srch(stu_names, 0, len(stu_roll)-1, huh)
                indi = stu_names.index(huh)
                if res != -1:
                    print(huh,"was", stu_att[indi],"for the training program.\n")
            elif ch1 == 4:
                res = fibbo_srch(stu_names, huh, len(stu_roll))
                indi = stu_names.index(huh)
                if res <= 0:
                    print(huh,"was", stu_att[indi],"for the training program.\n")
                else:
                    print("No!")
            elif ch1 == 5:
                exile = True        
    elif chc == 3:
        print("\nSee you Soon!")
        exit = True
