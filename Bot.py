import random
from collections import defaultdict as dd
import botres as b
from itertools import combinations
import bpoker as bp
import math
"""List=[]
List1=[] 
List2=[]
List3=[]
List4=[]
#List 5 for 1 deck
List5=[]
#List6 for storing the cards of players
outspt=[0,0,0,0,0,0,0,0,0,0]


for i in range(2,15):
    if(i<10):
        List.append('0'+str(i))  
    else:
        List.append(str(i))
                                                              
for j in range(0,13):
    List1.append(str(List[j])+'H')
for k in range (0,13):
    List2.append(str(List[k])+'D')     
for q in range (0,13):
    List3.append(str(List[q])+'S')  
for m in range (0,13):
    List4.append(str(List[m])+'C')     
List5=List1+List2+List3+List4

dealer=[]
bcards=[]
def distribute(bcards, List5):
    for i in range(2):
        bcards.append(random.choice(List5))
        List5.remove(bcards[i])


def flop(dealer,List5):
    for i in range(3):
        dealer.append(random.choice(List5))
        List5.remove(dealer[i])

def turn(dealer,List5):
    dealer.append(random.choice(List5))
    List5.remove(dealer[3])

def river(dealer,List5):
    dealer.append(random.choice(List5))
    List5.remove(dealer[4])

distribute(bcards,List5)

 """   



#flop(dealer, List5)
def pre_flop(bcards,current_bet):
    values=[i[0:2] for i in bcards]
    values=list(map(int,values))
    suit=[i[2] for i in bcards]
    if(len(set(values))==1):
        return values[0]*current_bet
    elif(abs(values[0]-values[1])==5 and len(set(suit))==1):
        return (6-abs(values[0]-values[1]))*current_bet
    else:
         return 1000
    


def pre_turn(bcards,dealer,List5):
    betamount=0
    outspt=[0,0,0,0,0,0,0,0,0,0]
    avc=bcards+dealer
    twocards=combinations(List5,2)
    for tc in twocards:
        flags=[0,0,0,0,0,0,0,0,0,0]
        avcf=[]
        avcf+=tc
        avcf+=avc
        pos_hand=combinations(avcf,5)
        for h in pos_hand:
            if(b.check_royalflush(h)):
                flags[0]=1
            elif(b.check_straightflush(h)):
                flags[1]=1
            elif(b.check_fourofakind(h)):
                flags[2]=1
            elif(b.check_fullhouse(h)):
                flags[3]=1
            elif(b.check_flush(h)):
                flags[4]=1
            elif(b.check_straight(h)):
                flags[5]=1
            elif(b.check_triplet(h)):
                flags[6]=1
            elif(b.check_twopair(h)):
                flags[7]=1
            elif(b.check_pair(h)):
                flags[8]=1
            else:
                flags[9]+=1
        for i in range(10):
            if(flags[i]==1):
                outspt[i]+=1
            else:
                pass

    for i in range(10):
        betamount=betamount+round(outspt[i]*(1.2**(10-i)))
    return betamount

        

#pre_turn(bcards,dealer,List5)
#turn(dealer,List5)


def pre_river(bcards,dealer,List5):
    betamount=0
    outspr=[0,0,0,0,0,0,0,0,0,0] 
    avc=bcards+dealer
    for i in range(len(List5)):
        flags=[0,0,0,0,0,0,0,0,0,0]
        avcf=[]
        avcf.append(List5[i])
        avcf+=avc
        pos_hand=combinations(avcf,5)
        for h in pos_hand:
            if(b.check_royalflush(h)):
                flags[0]=1
            elif(b.check_straightflush(h)):
                flags[1]=1
            elif(b.check_fourofakind(h)):
                flags[2]=1
            elif(b.check_fullhouse(h)):
                flags[3]=1
            elif(b.check_flush(h)):
                flags[4]=1
            elif(b.check_straight(h)):
                flags[5]=1
            elif(b.check_triplet(h)):
                flags[6]=1
            elif(b.check_twopair(h)):
                flags[7]=1
            elif(b.check_pair(h)):
                flags[8]=1
            else:
                flags[9]+=1
        for i in range(10):
            if(flags[i]==1):
                outspr[i]+=1
            else:
                pass
        
        for i in range(10):
            betamount=betamount+round(outspr[i]*(1.4**(10-i)))

    return betamount


#pre_river(bcards,dealer,List5)
#river(dealer,List5)

def post_river(bcards,dealer,List5):
    avcf=bcards+dealer
    betamount=(9-b.find_rank(avcf,0))*random.randint(5,8)*1000
    return betamount

def head(round_no,current_bet,bcards,dealer,List5,chc,fold,n):
    if(random.randint(1,11)==5):
        bet_amount=current_bet*random.randint(2,5)
    elif(round_no==0):
        bet_amount=pre_flop(bcards,current_bet)
    elif(round_no==1):
        bet_amount=pre_turn(bcards,dealer,List5)
    elif(round_no==2):
        bet_amount=pre_river(bcards,dealer,List5)
    elif(round_no==3):
        bet_amount=post_river(bcards,dealer,List5)
    else:
        pass
    n=len(str(bet_amount))
    bet_amount=int(math.ceil(bet_amount/math.pow(10,n-1))*math.pow(10,n-1))
    print(bet_amount)
    print(chc)
    if(bet_amount<current_bet/1.25):
        bp.call_fold()    
    elif(bet_amount>current_bet*1.25):
        bp.call_bet(bet_amount)
    elif(chc==n-len(fold)-1):
        bp.call_check()
    else:
        bp.call_call()


#post_river(bcards,dealer,List5,betamount)
