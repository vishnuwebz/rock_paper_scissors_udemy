rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
🪨
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
📃
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
✂️
'''

choice = int(input("Type 0 for Rock 🪨, 1 for Paper 📃 or 2 for Scissors ✂️.: "))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice ==  2:
    print(scissors)
else:
    print("Invalid Input!")