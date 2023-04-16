#Finding the percentage

if __name__ == '__main__':

    n = int(input())
    student_marks = {}
    
    for _ in range(n):

        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    l1 = list(student_marks[query_name]) 
    addition = sum(l1)
    result = addition/len(l1)
    print('%.2f'% result)
    
    
#String Split and Join

def split_string(string):

	list_string = string.split(' ')
	return list_string

def join_string(list_string):
    string = '-'.join(list_string)
	
    return string

if __name__ == '__main__':
	string = 'My name is Prasann'
	
	list_string = split_string(string)
	print(list_string)
 
	new_string = join_string(list_string)
	print(new_string)
 
# Enter your code here. Read input from STDIN. Print output to STDOUT

N1 = int(input())
storage1 = set(input().split());
N2 = int(input())
storage2 = set(input().split());
storage3 = storage1.union(storage2)
print(len(storage3))


#Find the Runner-Up Score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lst = list(arr)
    scores = list()

    for score in lst:
        if score not in scores:
            scores.append(score)
        else :
            continue
    ordr = sorted(scores, reverse=True)
    print(ordr[1])
    
#sWAP cASE

def swap_case(s):
    SwAp = ''
    for char in s:
        if char.upper() != char:
            SwAp += char.upper()
        elif char.lower() != char:
            SwAp += char.lower()
        else:
            SwAp += char
    
    
    return SwAp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
#Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    
#Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)    

#Python If-Else

if __name__ == '__main__':
    n = int(input().strip()) 
    oddcheck = (n % 2) != 0
    if oddcheck or (n > 100) or (n < 1) or (n >= 6 and n <= 20):
        print("Weird")
    else:
        print("Not Weird")


#Nested Lists

Result =[]
scorelist = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 

    for a,c in sorted(Result):
        if c==b:
            print(a)
            
#Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
        
#Write a function leap year

def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
year = int(input())
print(is_leap(year))

#Find a string

def count_substring(string, sub_string):
    total = 0
    for i in range(len(string)):
        if string[i:len(string)].startswith(sub_string):
            total += 1
    return total

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
#Lists

if __name__ == '__main__':

    N = int(input())

    List=[];

    for i in range(N):

        command=input().split();

        if command[0] == "insert":

            List.insert(int(command[1]),int(command[2]))

        elif command[0] == "append":

            List.append(int(command[1]))

        elif command[0] == "pop":

            List.pop();

        elif command[0] == "print":

            print(List)

        elif command[0] == "remove":

            List.remove(int(command[1]))

        elif command[0] == "sort":

            List.sort();

        else:

            List.reverse();
    
                           