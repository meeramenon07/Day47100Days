import os,time,random

print("Top Trump's Most Efficient Coding Teachers Simulation")
print()

card = {}
card["David"] = {"intelligence": 100, "skills":90, "clarity":90, "smartness":100}
card["Dylan"] = {"intelligence": 99, "skills":97, "clarity":95, "smartness":99}
card["Florin Pop"] = {"intelligence":100,"skills": 100, "clarity":100, "smartness": 89}
card["Tiffany"] = {"intelligence":80, "skills":75, "clarity":89, "smartness":100}

while True :
  print("Top Trumps Card Game")
  print()
  print("Best Coding Teachers")
  print()
  for key in card:
    print(key)
  player1 = input("choose your teacher > ")
  print("player1 has chosen,", player1)
  player2 = random.choice(list(card.keys()))
  print("player2 has chosen" , player2)
  print()
  print("choose your stat: intelligence,  skills, clarity, smartness")
  
  answer = input(" > ")
  print(f"{player1}: {card[player1][answer]}")
  print(f"{player2}: {card[player2][answer]}")
  if card[player1][answer] > card[player2][answer]:
    print(player1, "wins")
  elif card[player1][answer] < card[player2][answer]:
    print(player2,  "wins")
  else:
    print("It's a tie!" )

  time.sleep(4)
  os.system("clear")
  
































































































#import os, time, random
#print("Welcome to the Top Trumps 'Most Efficient Programming Teachers' Simulator")
#print()

#card = {}
#card["David"] = {"Intelligence": 200, "Skills": 190, "Clarity": 100, "Smartness": 200}
#card["Dylan Israel"] = {"Intelligence": 170, "Skills": 180, "Clarity": 150, "Smartness": 170}
#card["Florin Pop"] = {"Intelligence": 199, "Skills": 195, "Clarity": 200, "Smartness": 100}
#card["Tiffany"] = {"Intelligence": 90, "Skills": 100, "Clarity": 190, "Smartness": 200}

#while True:
  #print("TOP TRUMPS")
  #print()
  #print("Programming Teachers")
  #print()
  #for key in card:
    #print(key)
  #player1 = input("Choose your teacher  >  ")
  #print("Player1 has chosen", player1)
  #player2 = random.choice(list(card.keys()))
  #print("Player2 has chosen", player2)
  #print()
  #print("Choose your stat: Intelligence, Skills, Clarity, Smartness")

  #answer = input("> ")

  #print(f"{player1}: {card[player1][answer]}")
  #print(f"{player2}: {card[player2][answer]}")

  #if card[player1][answer] > card[player2][answer]:
    #print(player1, "wins")
  #elif card[player1][answer] < card[player2][answer]:
    #print(player2, "wins")
  #else:
    #print("It is a Draw!!!")


  #time.sleep(2)
  #os.system("clear")
    
    
