database_main=[ {"NAME":'Kumar',"MARKS":55,"SUBJECT":"EGD","ROLL_NO":1}
               ,{"NAME":'Ajay',"MARKS":32,"SUBJECT":"physics","ROLL_NO":2}
               ,{"NAME":"sai","MARKS":67,"SUBJECT":"english","ROLL_NO":3}
               ,{"NAME":"pranav","MARKS":100,"SUBJECT":"math","ROLL_NO":4}
               ,{"NAME":"sanjay","MARKS":79,"SUBJECT":"chemistry","ROLL_NO":5}]
def add_students():
 marks=int(input("enter the marks of the student"))
 name=input("enter the name of the student")
 subject=input("enter the subject")
 roll_no=int(input("enter the roll_no of the student"))
 database_structure={"NAME":name,"MARKS":marks,"SUBJECT":subject,"ROLL_NO":roll_no}
 database_main.append(database_structure) 
def all_students():
    
   print("\n All Student Records:")
   print("    Roll No | Name     | Subject    | Marks")
   print("---------------------------------------")
   for i in database_main:
    print(f"{i["ROLL_NO"]:10} | {i['NAME']:10} | {i['SUBJECT']:10} | {i['MARKS']}")  
def highest_mark():
   topper=database_main[0] 
   for i in database_main :
      if i["MARKS"] > topper["MARKS"] :
         topper = i
   print(f"the highest marks is {topper["MARKS"]} and it is scored by {topper["NAME"]} and roll no is {topper['ROLL_NO']} and the subject is {topper['SUBJECT']}")
def average_marks():
     total_marks=sum(i["MARKS"] for i in database_main)
     total_no_of_students=len(database_main)   
     average=total_marks/total_no_of_students
     print(f"the average marks of the given studnets list is {average}")  
all_students()
highest_mark()
average_marks()     