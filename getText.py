
def convertToText(num):

    onesPlace = ['','One ','Two ','Three ','Four ','Five ','Six ','Seven ','Eight ','Nine ']
    one_in_twosPlace= ['Ten ','Eleven ','Twelve ','Thirteen ','Fourteen ','Fifteen ','Sixteen ','Seventeen ','Eighteen ','Nineteen ']
    twosPlace =['','Ten ','Twenty ','Thirty ','Forty ','Fifty ','Sixty ','Seventy ','Eighty ','Ninety ']

    ret = ""
    n = int(num)
    while len(str(n))>=1:     
    
        splitCount=0;
    #issue 10001,10034, 12211 20000
        #print(n)        
        
        if(len(str(n))==6): # conversion for 6th place
                ret = ret + onesPlace[int(str(n)[:1])] + "Lakh "
        
        elif(len(str(n))==5): # conversion for 5th place
                if(n%10000==0): # For 5 digit numbers like 10000,20000,etc
                    ret = ret + twosPlace[int(str(n)[:1])] + "Thousand "
                elif(int(str(n)[:1])==1):   # For 5 digit numbers in range 11000 - 19999
                    ret  = ret + one_in_twosPlace[int(str(n)[1:2])] + "Thousand "
                    splitCount+=1
                else:   #   For 5 digit numbers like 20500, 23500,72080
                    ret = ret + twosPlace[int(str(n)[:1])]
                    ret = ret  + onesPlace[int(str(n)[1:2])] + "Thousand " 
                    # 80098 vs 123456
                    splitCount+=1
        elif(len(str(n))==4): # conversion for 4th place
                # Numbers like 1000,1050,4050,etc
                ret = ret + onesPlace[int(str(n)[:1])] + "Thousand "

        elif(len(str(n))==3): # conversion for 3rd place 
                if(n%100==0):   #For 3 digit numbers like 100,400,etc
                    ret = ret + onesPlace[int(str(n)[:1])] + "Hundred "
                else:   #For 3 digit numbers like 109,150,980
                    ret = ret + onesPlace[int(str(n)[:1])] + "Hundred And "
                
        elif(len(str(n))==2): # conversion for 2nd place i.e 11, 12 ,13
            if(n==10):
                ret= ret+"Ten "
                return ret
            if(int(str(n)[:1])==1):
                ret  = ret + one_in_twosPlace[int(str(n)[1:])]
                return ret
            else:
                ret = ret + twosPlace[int(str(n)[:1])]
                
        elif(len(str(n))==1): # conversion for ones place 
            ret = ret + onesPlace[int(str(n)[:1])]
   
        if(len(str(n))==1):
            break
        else:
            splitCount+=1
            n = int(str(n)[splitCount:])
        
    return ret

def getDecimal(num):
    if num=="":
        return ""
    den = 10**len(num)
    return str(num)+"/"+str(den)+" "
    
def processInput(n):
    #print(type(n))
    try :  
        float(n) 
    except : 
        return "The entered string cannot be converted to float"
        
    if(float(n)<0.0 or float(n)>999999.99):
        print("Please enter a value between 0 and 999999.99")
        return
        
    if '.' not in n:
        n+='.'
        
    wholePart = n.split('.')[0]
    decimalPart = n.split('.')[1]
    result = "Rs. "
    
    result +=  convertToText(wholePart)
    result += getDecimal(decimalPart) + "ONLY"
    
    return result
    
n =input("Enter number: ")
print(processInput(n))
