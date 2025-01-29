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
            "Signs Point to Yes"]


  #Answer question randomly with one of the options from your earlier list.

num = random.random()
num = num * 1000
num = int(num)


question = input("Ask me a yes or no question: ")
print(answers[num])
if __name__ == '__main__':
  main()
