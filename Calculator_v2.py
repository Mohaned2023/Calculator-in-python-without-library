#####################################################################
#             Written By Mohaned Mohammed Sherhan                   #
#####################################################################
#                                                                   #
# Attention: This project was built without                         #
# the need to use any external library or included library in Python#
#                                                                   #
#####################################################################
#                           MR.(X)                                  #
#####################################################################
#                                                                   #
# Here , you will find a practical application on the idea of       #
# ​​a calculator in python and how it is built. Of course,            #
# this idea is too small to build an integrated calculator,         #
# but here there are the basics of the calculator such as addition, #
# subtraction, multiplication, division,                            #
# rank or exponential and square root                               #
#                                                                   #
#####################################################################

# The OOP in Python 
class Mathl:
    # The main def 
    def __init__(self,liste):
        self.__arge = liste

    # Of course, this function{square_s} is not from my think.
    # I admit that I used AI ,
    # but I understood the general concept of it.
    def square_s(self,num):
        if num < 1:
            return 0
        else:
            epsilon = 0.01
            num_guesses = 0
            low = 0.0
            high = max(1.0,num)
            ans = (high + low)/2.0
            while abs(ans**2 - num) >= epsilon:
                if ans**2 < num :
                    low = ans 
                else:
                    high = ans
                ans = (high +low )/2.0
            return ans 

    # def to sutract the numbers 
    def sub_num(self):
        numbers = []
        sub_num = 0
        x = 0
        for num in self.__arge:
            numbers.append(num)
        if numbers[0]>0:
            sub_num += numbers[0]
        elif numbers[0]<0:
            sub_num += numbers[0]
        for num in numbers:
            if num == numbers[0] and x == 0:
                pass
            else:
                sub_num -= num
            x += 1
        return sub_num

    # def to sum the numbers 
    def sum_num(self):
        numbers = []
        
        sum_num = 0
        for num in self.__arge:
            numbers.append(num)
        for num in numbers:
            sum_num += num
        return sum_num
    
    # def to multiply the numbers 
    def mul_num (self):
        numbers = []
        mul_num = 1
        for num in self.__arge:
            numbers.append(num)
        for num in numbers:
            mul_num *= num
        return mul_num

    # def to divide the numbers 
    def div_num (self):
        try:
            numbers = []
            div_num = 0
            x = 0
            for num in self.__arge:
                numbers.append(num)
            if numbers[0]>0:
                div_num += numbers[0]
            elif numbers[0]<0:
                div_num += numbers[0]
            for num in numbers:
                if numbers[0] == num and x == 0 :
                    pass
                else:
                    div_num /= num
                x += 1
            return div_num
        except ZeroDivisionError:
            return "\nError : You can't division by zero...! \n"
    
    # def to up numbers 
    def up_num (self,x):
        """
        It is necessary to enter the value of x ,
        x == base .
        For example;
        >>> num = Mathl(2,3) # arge = 2+3=5
        >>> print (num.up_num(2)) # x = 2
        # 2^5 = 32 
        # if x == 0 up_num == 0

        """
        try:
            numbers = []
            up_num = 0
            for num in self.__arge:
                numbers.append(num)
            if x == 0:
                return 0

            for num in numbers :
                up_num += num 
                return x ** up_num
        except OverflowError:
            print (f"\nThis number is over kill..! ; {up_num}\n")
        

    # def to square 
    def square_num(self ,Process='+'):
        """
        This function bring the square root closer to the closest possible image . For example;
        >>> num = Mathl(32)
        >>> print (num.square_num(Process='+'))
        # 5.65625 ~ 6

        """
        if Process == '+':
            num = Mathl.sum_num(self)
            return Mathl.square_s(self,num)

        elif Process == '-':
            num = Mathl.sub_num(self)
            return Mathl.square_s(self,num)

        elif Process == '*':
            num = Mathl.mul_num(self)
            return Mathl.square_s(self,num)
        elif Process == "/":
            num = Mathl.mul_num(self)
            return Mathl.square_s(self,num)


## The Project ###############

def for_a():
    nums = []
    print ("\nTo stop Enter { . } Dot.\n")
    for choose_num in range(100000000):
        choose = input(f"Enter a number {choose_num+1}: ")
        try:
            if choose == '.':
                break
            else:
                nums.append(float (choose))
        except ValueError:
            print (f"could not convert string to float: {choose}")
    return nums

def User ():
    print ("""
    
    # To perform an operation, you must choose the code for 
        the operation .
    => To sum numbers use ======>{ + }
    => To sutract numbers use ==>{ - }
    => To multiply numbers use =>{ * }
    => To divide numbers use ===>{ / }
    => To up numbers use =======>{ ^ }
    => To square numbers use ===>{ ~ }
    => To Go oute of the tool ==>{ 0 }
    
    """)
    Process = input("Enter a Process :  ")
    if Process == "+":
        nums = for_a()
        num = Mathl(nums)
        print ("\nThe sum is : ",num.sum_num())
        User()
    elif Process == "-":
        nums = for_a()
        num = Mathl(nums)
        print ("\nThe sutract is : ",num.sub_num())
        User()
    elif Process == "*":
        nums = for_a()
        num = Mathl(nums)
        print ("\nThe multiply is : ",num.mul_num())
        User()
    elif Process == "/":
        nums = for_a()
        num = Mathl(nums)
        print ("\nThe divide is : ",num.div_num())
        User()
    elif Process == "^":
        
        try:
            base = float (input("Enter a number For base : "))
            nums = for_a()
            num = Mathl(nums)
            print ("\nThe up is : ",num.up_num(base))
            User()
        except:
            print ("\nError input...!\n")
            User()
    elif Process == "~":
        print ("""

        If you like to do a specific process before you take the square root,
        such as adding or subtracting, you must enter the process,
        if you want to get the square root for one number, enter a Dot { . },
        The Process you can do is { + } and { - } and { / } nad { * } .
        
        """)
        Process = input("==> ")
        if Process == "+" or Process =="-" or Process == "*" or Process == "/" :
            nums = for_a()
            num = Mathl(nums)
            print ("\nThe square is : ",num.square_num(Process))
        elif Process == ".":
            nums = for_a()
            num = Mathl(nums)
            print ("\nThe square is : ",num.square_num())          
        else:
            print ("\nError input ==>",Process)
        
        User()
    elif Process == '0':
        print ("\nSee you soon ... \n")

    else:
        print ("\nErorr Tupy ..!\n")
        User()

if __name__=='__main__':
    User()
