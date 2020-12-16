import re;
import math;


problem = input("What would you like to do?(Add, Subtract, Multiply, Divide)");

#wrongDiv = False;

# Redo the function
def redoFunc():
     if problem == "multiply":
          doMultiple();
     
     if problem == "Multiply":
          doMultiple();

     elif problem == "Add":
          doAdd();
     elif problem == "add":
          doAdd();

     elif problem == "Subtract":
          doSubtract();
     elif problem == "subtract":
          doSubtract();

     elif problem == "divide":
          doDivide();
     elif problem == "Divide":
          doDivide();
     return;

def multiplyList(myList):

     result = 1;

     for x in myList: 
          result = result * x;

     return result;

def addList(myList):

     result = 0;

     for x in myList: 
          result = result + x;

     return result;

def subtractList(myList):

     result = 0;

     for x in myList: 
          result = abs(x - result);

     return result;



def doMultiple():

     print("You chose to multiply.")
     multiplyArr = [];
     subStrMul = "*";

     multiplyPushArr = input("What numbers would you like to multiply?");

     multiplyArr.append(multiplyPushArr);
     mulResult = multiplyArr[0];

     #nameResMul = int(mulResult);
     endResMul =  [int(s) for s in re.findall(r'\b\d+\b', mulResult)];

     print(multiplyList(endResMul));

     problem = input("What would you like to do?(Add, Subtract, Multiply, Divide)");
     redoFunc();

     return;


def doAdd():

     print("You chose to add.")
     addArr = [];
     subStrAdd = "+";

     addPushArr = input("What numbers would you like to add?");

     addArr.append(addPushArr);
     addResult = addArr[0];

     #nameResMul = int(mulResult);
     endResAdd = [int(s) for s in re.findall(r'\b\d+\b', addResult)];

     print(addList(endResAdd));

     problem = input("What would you like to do?(Add, Subtract, Multiply, Divide)");

     redoFunc();

     return;

def doSubtract():

     print("You chose to subtract.")
     subArr = [];
     subStrsub = "-";

     subPushArr = input("What numbers would you like to subtract?");

     subArr.append(subPushArr);
     subResult = subArr[0];

     #nameResMul = int(mulResult);
     endResSub = [int(s) for s in re.findall(r'\b\d+\b', subResult)];

     print(subtractList(endResSub));

     problem = input("What would you like to do?(Add, Subtract, Multiply, Divide)");
     
     redoFunc();


     return;



def doDivide():

     #if wrongDiv == False:
     print("You chose to divide.")

     divArr = [];
     #subStrDiv = "/";

     divPushArr = input("What numbers would you like to divide?");

     divArr.append(divPushArr);
     divResult = divArr[0];

     #nameResMul = int(mulResult);
     endResDiv = [int(s) for s in re.findall(r'\b\d+\b', divResult)];
     endingDiv = math.trunc(endResDiv[0] / endResDiv[1]);

     print(endingDiv);

     if endingDiv == 0 :

          print("Something went wrong. Try Again");
          doDivide();
          #wrongDiv = True;

     elif endingDiv != 0:
          problem = input("What would you like to do?(Add, Subtract, Multiply, Divide)");
          redoFunc();
          #wrongDiv = False;
          #break;

     return;



# Multiply
if problem == "multiply":
     doMultiple();
     
if problem == "Multipliy":
     doMultiple();
# Add
elif problem == "Add":
     doAdd();
elif problem == "add":
     doAdd();
# Subtract
elif problem == "Subtract":
     doSubtract();
elif problem == "subtract":
     doSubtract();
# Divide
elif problem == "divide":
     doDivide();
elif problem == "Divide":
     doDivide();



