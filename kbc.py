print("Welcome to kaun Banega Crorepathi")

def KBC(): 
 print("So, for every question you will be having 4 options out of which only one answer will be correct, you have to answer only in \"a \",\"b\",\"c\",\"d\"")
 print("So here goes your question")
 questions=["1. What is the capital of china?  a) Beijing b) Sydney c)Shangai d)Hong Kong",
            "2.Which team has won the first IPL trophy: a) deccan chargers b)Rajasthan Royales c) kolkata night riders d)mumbai indians",
            "3. Who was the first president of India: a)Jawaharlal Nehru b)APJ Abdul Kalam c) Dr BR Ambedkar d)Rajendrad",
            "4.Who is the current CEO of Microsoft? a) Bill Gates b)Satya Nadella c)Steve Jobs d)Sundar Pitchai",
            "5.What is the real name of the youtuber CarryMinati? a)Abhyuday b)Ajey Nagar c) Bhuvan Bam d) harshal mehta",
            "6.By whome was the film Inception directed by? a)Cristopher Nolan b)Sidhard Anand c)Farahd Samji d)James Cameron",
            "7. Who were known as the Wright Brothers a) Hrithik and Sharukh b)Wilbur and Orville c)Thomas and Jemis d) Albert and Newton",
            "8.What was the most sold console by the year 2023? a) PS5 b)Xbox360 c)PS2 d)PS4",
            "9.Who invented PayPal? a)PeterQuill b)Peter Theil c)RobertSteve d)Scot Parker",
            "10. Which College in India has got Rank 1 in NIRF ranking 2023? a)IIT Bombay b)IIT Madras c)IIT Kharagpur d)VIT Vellore",
            "11.What is the name of the actor who acted in the role of Scott Lang in the AntMan movie series? a)Michael Douglas b)Anthony Mackie c)Paul Rudd d)Tom Holand",
            "12.Which Youtube channel has most subscribers after T-Series? a)Pewdiepie b)SonyEntertainmentIndia c)Cocomelon d)MrBeast"]
 
 answers = ["a","b", "d" , "b","b", "a" , "b", "c","b","b", "c", "d"]
 prize_money_amount = [1000, 5000, 10000, 25000, 50000, 100000, 300000, 700000, 1500000, 2500000, 5000000, 10000000 ]

 for i in range(len(questions)):
    print(questions[i])
    x=input("enter the option which you think is the correct answer:")
    if x == answers[i]:
        if prize_money_amount[i] == 10000000:
           print("Congratulations you became crorepathi")
           print("you have won:",  prize_money_amount[i])
           return
        else:
         prize_money=prize_money_amount[i]
         print(" that is the right answer,\n congratulations you have won: ", prize_money)
    else:
        print("oops, we are sorry, the answer given by you is wrong, \n You are out of the game.")
        print("So, you have won a sum total of:",prize_money)
        print("Well Played")
        print("Thanks for participating")
        return
    





while True:
   print("So, are you interested to continue\n type \"y\" if yes and \"n\" for no")
   ans=input()
   if ans=="y":
      KBC()
      break
   elif ans=="n":
      print("GetLost")
      break
   else:
      print("enter a valid input")