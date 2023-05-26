import random
from collections import defaultdict

# 役と強さ
hand = {
    '-1': 'ヒフミ',
    '0' : '役なし',
    '1' : '1',
    '2' : '2',
    '3' : '3',
    '4' : '4',
    '5' : '5',
    '6' : '6',
    '7' : 'シゴロ',
    '8' : 'アラシ',
    '9' : 'ピンゾロ'
}

def main():
    players = int(input('何人で遊びますか:'))
    party = []
    for i in range(players):
        party.append(input(str(i+1)+'人目のプレイヤー名を入力してください:'))

    box = dict()
    for i in range(len(party)):
        dices = roll()
        box.update({party[i]:dices})
        dices = []
    print(box)
    power = defaultdict(list)
    for k,v in box.items():
        print(k + ':'+ hand.get(str(check(v))))
        power[check(v)].append(k)
    winners = power.get(max(power.keys()))
    print_winners(winners)
    

def check(dices:list[int])->int:
    if len(dices) == 0:
        return 'error'
    else:
        dices = sorted(dices)
    
    if dices[0] == dices[1] and dices[1] == dices[2]:
        if dices[0] == '1':
            return -1
        else:
            # アラシ
            return 8 
    elif dices == 4 and dices == 5 and dices == 6:
        # シゴロ
        return 7
    elif dices == 1 and dices == 2 and dices == 3:
        # ヒフミ
        return -1
    elif dices[0] == dices[1]:
        return dices[2]
    elif dices[1] == dices [2]:
        return dices[0]
    # 役なし
    return 0
    
def print_winners(winners:list[str])->None:
    print('Winner:',end="")
    counter = 0
    for winner in winners:
        if counter == 0:
            print(winner,end="")
            counter += 1
        else:
            print(","+winner, end="")
    print("")

def roll()->list[int]:
    return [random.randint(1,6),random.randint(1,6),random.randint(1,6)]

if __name__ == "__main__":
    main()