#Magic8Ball.py
#Name: Luke Knofczynski
#Date:1/29/25
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
answers = ["Yes", "Not Likely", "Ask Again Later",
           "Don't Count on it", "My Sources Say No", "Very Likely",
           "Without a Doubt", "No", "It is Certain", "Very Doubtful",
           "Signs Point to Yes", "You May Rely on It", "Outlook not so Good",
           "Outlook Good", "Cannot Predict Right Now", "As I see it, Yes",
           "Better not Tell You Now", "Concentrate and Ask Again", "It is Decidedly So",
           "My Reply is No"]


  #Answer question randomly with one of the options from your earlier list.

num = random.random()
num = num * 100
num = int(num)
num = num//5
num = int(num)
question = input("Ask me a yes or no question: ")
print(answers[num])
if __name__ == '__main__':
  main()
