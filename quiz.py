from guizero import App, Text, PushButton
from question import Question
from qnumandrights import *
from time import sleep



stringforcsv = input('enter csv name: ') # ASKS FOR NAME (test feature)

csv = open(stringforcsv + '.csv', 'r')  # opens file

lines = csv.readlines() # creats a list of lines    list --> array

questions = []

def toQuestion(place):
    i = 0
    char = ''
    string = ""
    # step 1:  create array
    arr = []
    # step 2: get things into string
    while(char != '~'):
        char = ''
        
        while(char != '|' and char != '~'):
            
            
            if i != len(place):
                char = place[i]
            else:
                break
            
            
            if(char != '|' and char != '~' ):
                string = string + char
                
            i+=1
            
        string.replace('|', '')
        
        
        
        arr.append(string)
        
        string = ''
        
    string.replace('~', '')
    
    arr.append(string)
    
    
    
    arrprompt = arr[0]
    ans = arr[len(arr) - 1]
    arr.pop(0)
    arr.pop(len(arr) - 1)
    
    return Question(arrprompt, arr, ans)
        
    

    

    




for j in range(len(lines)):
    questions.append(  toQuestion( lines[j] )  )
    
# graphics

# Method to call when button pressed

# Set up the app
qandr = qnumandrights()

def rightsplus(num):
    qandr.
    
def afteraction():
    global qnum
    qnum+=1
    button1.disable()
    button2.disable()
    button3.disable()
    button4.disable()

    sleep(2)
    textshow.text = '?'

    try:
        button1.text = questions[qnum].answers[0]
        button2.text = questions[qnum].answers[1]
        button3.text = questions[qnum].answers[2]
        button4.text = questions[qnum].answers[3]
        button1.enable()
        button2.enable()
        button3.enable()
        button4.enable()
    except:
        prompt.text = "you got " + str(rights) + '/' + str(qnum) + "or " + str((rights/qnum)*100) + " right"
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
    
    
app = App((stringforcsv + " QUIZ"))

def action1():
    if (questions[qnum].ans == 1):
        textshow.value = "Correct"
        rightsplus(1)
    else:
        textshow.value = "Wrong"
        rightsplus(-1)
    afteraction()
    
def action2():
    if (questions[qnum].ans == 2):
        textshow.value = "Correct"
        rightsplus(1)
    else:
        textshow.value = "Wrong"
        rightsplus(-1)
    afteraction()
def action3():
    if (questions[qnum].ans == 3):
        textshow.value = "Correct"
        rightsplus(1)
    else:
        textshow.value = "Wrong"
        rightsplus(-1)
    afteraction()
def action4():
    if (questions[qnum].ans == 4):
        textshow.value = "Correct"
        rightsplus(1)
    else:
        textshow.value = "Wrong"
        rightsplus(-1)
    afteraction()

def line():
    Text(app, "\n")


text = Text(app, stringforcsv + ' QUIZ')

line()

prompt = Text(app, text=questions[qnum].prompt)

button1 = PushButton(app, action1, width=30, text=questions[qnum].answers[0])


button2 = PushButton(app, action2, width=30, text=questions[qnum].answers[1])



button3 = PushButton(app, action3, width=30, text=questions[qnum].answers[2])



button4 = PushButton(app, action4, width=30, text=questions[qnum].answers[3])

line()

textshow = Text(app, text="?")

app.display()

    
    
    
    

    
    
    
    
    
