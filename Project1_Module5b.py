#Import section
from datetime import datetime
import random
from os import path

#variabels

date_time=""
quizdatafile=""
quizresultsfile=""

#grade 1 question
grade1questions={
    "Question 1":'What is the sum of #x + #y = ? ',
    "Question 2":'What is the sum of #x + #y = ? ',
    "Question 3":'What is the sum of #x + #y = ? ',
    "Question 4":'What is the sum of #x + #y = ? ',
}

#grade 2 questions
grade2questions={
    "Question 1":'The class is doing a math activity. There are  #x groups of  #y students' + 'How many student are there are in the class = ? ',
    "Question 2":'The class is doing a math activity. There are  #x groups of #y students. Each group should have #y  pairs of scissors. How many pairs of scissors are needed in total = ? ',
    "Question 3":'Students get #x stickers on their reward chart for each correct answer. If a student gets #y correct answers, how many stickers will he get = ? ',
    "Question 4":'A student started by making mini sandwiches. If he has #x  friends coming over and he made  #y sandwiches for each one of them, how many sandwiches did he make = ? '
}

#grade 3 questions
grade3questions={
    "Question 1":'#x \u00F7 #y = ? ',
    "Question 2":'#x \u00F7 #y = ? ',
    "Question 3":'#x \u00F7 #y = ? ',
    "Question 4":'#x \u00F7 #y = ? '
}
# save quiz history
def generatequizdata(sname,grade,question,answer,excepted,result):
    
    isfileexists=path.exists("data.txt")
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y%H%M%S")
    if(isfileexists==True):
        f=open("data.txt",'a')
    else:
        f=open("data.txt",'w')
        f.write('=' * 200 + "\n")
        f.write(' ' * 90   + 'UWF  Quiz Information' + '\n')
        f.write('=' * 200+ "\n")
      
        record_header = '%-25s %-15s  %5s  %10s  %10s %-15s %-100s' % ( "Quiz on","Student name", "Grade","Answer","Excepted","Results","Question",)
        f.write(record_header+ '\n')
        f.write('=' * 200 + "\n")
    record_new =  '%-25s %-15s  %5s  %10s   %10s %-15s %-100s'  % (date_time,sname, grade,answer,excepted,result,question)
    f.write(record_new+ "\n")

# save quiz resutls  
def generategradereport(sname,grade,score):
    isfileexists=path.exists("Results.txt")
    if(isfileexists==True):
        f=open("Results.txt",'a')
    else:
        f=open("Results.txt",'w')
        record_new =   ( sname + str(','), str(grade)+ str(','),str(score)+ str(','),'$')
    f.write(record_new+ "\n")

#Grade 1 Quiz
def grade1quiz(name):
    score=0
    for m, n in grade1questions.items():
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        question= (str(n).replace('#x',str(x)).replace('#y',str(y)))
        answer=input(question)
        if(answer.isnumeric() == False): answer='0'
        if(len(answer) == 0):
            answer=0
        if x+y==int(answer):
            score+=1
        generatequizdata(name,1,question,int(answer),str(x+y), (x+y==int(answer)))
    return score

#Grade 2 Quiz
def grade2quiz(name):
    score=0
    gradelevel=2
    for m, n in grade2questions.items():
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        question= (str(n).replace('#x',str(x)).replace('#y',str(y)))
        answer=input(question)
        if(answer.isnumeric() == False): answer='0'
        if(len(answer) == 0):
            answer=0
        if x*y==int(answer):
            score+=1  
        generatequizdata(name,gradelevel,question,int(answer),str(x*y),(x*y==int(answer)))
  
     
    return score

#Grade 3 Quiz
def grade3quiz(name):
    score=0
    gradelevel=2
    for m, n in grade3questions.items():
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        question= (str(n).replace('#x',str(x)).replace('#y',str(y)))
        answer=input(question)
        if(answer.isnumeric() == False): answer='0'
        if(len(answer) == 0):
            answer=0
        if round(x/y,2)==round(float(answer),2):
            score+=1  
        generatequizdata(name,gradelevel,question,float(answer), str(round(x/y,2)),(round(x/y,2)==round(float(answer),2)))
  
     
    return score

#print report
def print_report():
    f=open("Results.txt",'r')
  
    while True:
        line=f.readline().strip()
        rdata=line.split(',')
        print(rdata)

        if line == "" :
            break;
        print(line)
    f.close()

#grade results
def calculategrade(score):
    print('Total score :'+ str(score))
    earnedgrade=''
    if (score==4):
        earnedgrade= 'A'
    elif(score==3):
        earnedgrade= 'B'
    elif(score==2):
        earnedgrade= 'C'
    elif(score==1):
        earnedgrade= 'D'
    else:
        earnedgrade= 'F'
    print('earned grade :'+ str(earnedgrade))
    return earnedgrade

# main entry 
def main():
    
    
    
    quizresutls={}
    studentno=0
    
    while (studentno < 4):
        name = str(input(str(studentno+1) + ".Enter a  studnet name: "))
        gradelevel=''
        graderesults=''
        score=0
        if(len(name) != 0):
            gradelevel =int(input("Enter grade level (1,2,3): "))
            quizresutls["name"]=name
            quizresutls["gradelevel"]=gradelevel
            if(gradelevel==1):
               score=grade1quiz(name)
            elif(gradelevel==2):
                score=grade2quiz(name)
            elif(gradelevel==3):
                score=grade3quiz(name)
            studentno+=1
        else:
            break
       
        generategradereport(name,gradelevel,score)


if __name__== "__main__":
   main()
   print_report()

