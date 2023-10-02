class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def sub(self, num1, num2):
        return num1 - num2
    
    def mul(self, num1, num2):
        return num1 * num2
    
    def div(self, num1, num2):
        return num1 / num2

class Factorial:
    def fact(self, num):
        factorial = 1    
        if (num == 0):    
            return 1
        else:    
            for i in range(1,num+ 1):    
                factorial = factorial*i 
        return factorial

class Square:
    def get_square(self, num):
        return num * num



class Math:
    def __init__(self, calc:Calculator, facto:Factorial,squ :Square):
        self.calc = calc
        self.factor = facto
        self.squ = squ
    
    def get_add(self, num1, num2):
        return self.calc.add(num1, num2)

    def get_sub(self, num1, num2):
        return self.calc.sub(num1, num2)

    def get_mul(self, num1, num2):
        return self.calc.mul(num1, num2)

    def get_div(self, num1, num2):
        return self.calc.div(num1, num2)
    
    def get_factor(self, num):
        return self.factor.fact(num)
    
    def get_square(self, num):
        return self.square.get_square(num)

if __name__=="__main__":
    c = Calculator()
    f = Factorial()
    s= Square()
    m = Math(c,f, s)

    num = int(input("Enter the number\n"))
    num1 = int(input("Enter the first number\n"))
    num2 = int(input("Enter the second number\n"))
    choice = 1

    while(choice != 0):
        print("The different operations are\n 1. addition\n 2.subtraction\n 3. Multiplication\n 4. Division\n 5. factorial\n 6.square\n")
        choice = int(input("Enter the choice\n"))
        if(choice == 1):
            print("The addition of two numbers is\n")
            print(m.get_add(num1, num2))
        elif(choice == 2):
            print("The subtraction of two numbers is\n")
            print(m.get_sub(num1, num2))
        elif(choice == 3):
            print("The multiplication of two numbers is\n")
            print(m.get_mul(num1, num2))
        elif(choice == 4):
            print("The division of two numbers is\n")
            print(m.get_div(num1, num2))
        elif (choice == 5):
            print("The factorial of a number is\n")
            print(m.get_factor(num))
        elif(choice == 6):
            print("The square of a number is\n")
            print(m.get_square(num))
        else:
            print("Invalid number")
            
            

