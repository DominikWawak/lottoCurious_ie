
# Lotto Checker 

from os import name
import random
import urllib.request
import xml.etree.ElementTree as ET
import re





userNumberSet={1,2}
lotto={}
lotto_plus1={}
lotto_plus2={}
bonus_lotto= False
bonus_lottoPlus1 = False
bonus_lottoPlus2 = False

# This method is a method I added which pulls data from the past lotto draws in the Irish lotto
# The api call returns a xml document whick needs to be correctly parsed and the numbers are take using regex.
# The user lotto numbers ant the nuber of draws the user wants to check are passed in as arguments.
# the data is taken out into arrays of the matching/ intersecting values and are returned by the function.

def realLottoNumbers(userNumbers,n):
    size = 7
    bonus= False
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = "https://resultsservice.lottery.ie/rest/GetResults?drawType=Lotto&lastNumberOfDraws="+str(n)
    headers={'User-Agent':user_agent,} 

    request=urllib.request.Request(url,None,headers) #Th
    response = urllib.request.urlopen(request)
    data = response.read().decode('utf-8') # The data u need

    # tree = ET.parse(response)
    # root = tree.getroot()

    p=re.findall("<Number>(.*?)</Number>", data, re.DOTALL)
    
    track = 0
    allArrays= []
    lottoResults =[]
    bonusArr=[]
    print("Real irish lotto Numbers")
    while track < len(p):
        arr = p[track:size+track]
        allArrays.append(arr)
        print(arr)
        track=track+size
  

    un = set(map(str,userNumbers))
    for a in allArrays:
        i = un.intersection(a)
        if(a[6] in un):
            bonusArr.append(True)
        else: bonusArr.append(False)
        lottoResults.append(i)
   

    return lottoResults,bonusArr


# Validate Input function checks the choice the user gave in a menu and checks if it is in a certain range
#
#The return is a boolean
#

def validateInput(choice,min,max):
    if(choice in range(min,max)):
        return True
    else: 
        return False


# enterLottoNumbers function gives the user the option to generate numbers or make the user enter the numbers manually.
#The numbers are not repeated as the user input variable is a set and cannot contain double values. Therefore the user can fill the set until-
# The set is size 6
#
def enterLottoNumbers():
    print()
    print()
    print()
    print()
    global userNumberSet
    userNumberSet.clear()
    print("1) Auto generate Numbers")
    print("2) Manually Enter Numbers")
    opt =int(input("Enter your choice -->"))
    while(not validateInput(opt,1,3)):
        opt =input("Enter your choice -->")
    if opt ==1:
        userNumberSet=set(random.sample(range(1,46),6))
        print(userNumberSet)
    if opt == 2:
        print("Please enter the numbers for the lotto")

        while(len(userNumberSet)<6):
            num = int(input("Enter Number -->"))
            while(not validateInput(num,1,46)):
                num = int(input("Enter Number -->"))
            
            userNumberSet.add(num)

        print(userNumberSet)
    print()
    print()
    print()
    print()
    main()


# Random number Generatpr function generates 7 sample numbers that are not repeated from a range.
# This sampling is done 3 times for the different types of lotto.
#
#
def randomLottoNumbersGenerator():
    print()
    print()
    print()
    print()
    global lotto,lotto_plus1,lotto_plus2
    print("Generating random numbers")
    lotto = random.sample(range(1,46),7)
    print(lotto)
    lotto_plus1= random.sample(range(1,46),7)
    print(lotto_plus1)
    lotto_plus2= random.sample(range(1,46),7)
    print(lotto_plus2)
    
    print()
    print()
    print()
    print()
    main()


# lottoCheck function checks the bunus of each lotto ie the last number of the lotto checking if the user has that number.
# The matching elements are found by using the intersection function on the user numbers set.
# The results are returned.
#
def lottoCheck():
    global bonus_lotto,bonus_lottoPlus1,bonus_lottoPlus2,lotto,lotto_plus1,lotto_plus2
    

    if(lotto[6] in userNumberSet):
       # print("BONUS LOTTO")
        bonus_lotto = True
    
    if(lotto_plus1[6] in userNumberSet):
        #print("BONUS LOTTOPLUS1")
        bonus_lottoPlus1 = True

    if(lotto_plus2[6] in userNumberSet):
       # print("BONUS LOTTOPLUS2")
        bonus_lottoPlus2 = True

    # print(set(userNumberSet).intersection(lotto))
    # set(userNumberSet).intersection(lotto_plus1)
    # set(userNumberSet).intersection(lotto_plus2)
   
    lotto_Result = userNumberSet.intersection(lotto)
    lotto_plus1Result=userNumberSet.intersection(lotto_plus1)
    lotto_plus2Result=userNumberSet.intersection(lotto_plus2)

    # print(lotto_Result)
    # print(lotto_plus1Result)
    # print(lotto_plus2Result)

    #Lotto results
    
    return lotto_Result,lotto_plus1Result,lotto_plus2Result


# the winning output function gives the user the output on a specific lotto draw
#
#
#
def winningsOutput(lottoResult,bonus):
    print()
    print()
    print()
    print()
    print("These are your lotto Results")
    if len(lottoResult) == 6:
        print()
        print("YOU WIN JACKPOT")
        print()
    elif len(lottoResult) == 5 and bonus:
        print()
        print("YOU WIN CASH PRIZE MATCH 5 + BONUS")
        print()
    elif len(lottoResult) == 4 and bonus:
        print()
        print("YOU WIN CASH PRIZE MATCH 4 + BONUS")
        print()
    elif len(lottoResult) == 3 and bonus:
        print()
        print("YOU WIN CASH PRIZE MATCH 3 + BONUS")
        print()
    elif len(lottoResult) == 5:
        print()
        print("YOU WIN CASH PRIZE MATCH 5")
        print()
    elif len(lottoResult) == 4:
        print()
        print("YOU WIN CASH PRIZE MATCH 4")
        print()
    elif len(lottoResult) == 3:
        print()
        print("YOU WIN A SCRATCH CARD")
        print()
    else: 
        print("NOT A WINNER")

    print()
    print()
    print()
    print()


# View winnings output allows the user to pick what lotto they want to view the output off.
#
#
#
def viewWinningOutput():
    print()
    print()
    print()
    print()
    global bonus_lotto,bonus_lottoPlus1,bonus_lottoPlus2
    print("What winnings would you like to check")
    print("1) Lotto")
    print("2) Lotto Plus 1")
    print("3) Lotto Plus 2")
    r1,r2,r3 = lottoCheck()

    choice = int(input("Please enter your choice --> "))
    while(not validateInput(choice,1,4)):
        choice = int(input("Please enter your choice --> "))
    if choice ==1:
        winningsOutput(r1,bonus_lotto)
        main()
    elif choice == 2:
        winningsOutput(r2,bonus_lottoPlus1)
        main()
    elif choice == 3:
        winningsOutput(r3,bonus_lottoPlus2)
        main()



def main():
    global bonus_lotto
    print("LOTTO PROGRAM")
    print("1) Generate Random lotto numbers")
    print("2) Enter lotto numbers")
    print("3) Check your results")
    print("4) Check real lotto results")
    print("5) Exit the program")
    choice = int(input("Please enter your choice --> "))
    while(not validateInput(choice,1,5)):
        choice = int(input("Please enter your choice --> "))
    if choice==1:
        randomLottoNumbersGenerator()
    elif choice==2:
        enterLottoNumbers()
    elif choice==3:
        viewWinningOutput()
    elif choice==4:

        choiceNum = int(input("how many lotto results from the most recent would you like to see -->"))
        while(not validateInput(choiceNum,1,51)):
            choiceNum = int(input("how many lotto results from the most recent would you like to see -->"))

        lottoRes, bonus = realLottoNumbers(userNumberSet,choiceNum)

        i=0
        print(len(lottoRes))
        while(i<len(lottoRes)):
             winningsOutput(lottoRes[i],bonus[i])
             i = i+1
        main()
    elif choice==5:
        exit()
    




if __name__ =="__main__":
    main()

