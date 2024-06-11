print("\n***Your choices will be presented as a list. \n***Type the corresponding number and hit enter to make your selection.\n***Otherwise, you will die.")
print("\n\nYou are not welcome here")

### STAGE 0 ###
print("\n\nYou awake from a deep, dreamless sleep to find yourself laying in a pile of hay.")
stage0 = input("\n  1. Go back to sleep\n  2. Stand up and gather your surroundings\n")
if stage0 == "1": ### GAME OVER ###
  print("\nYou died")
elif stage0 == "2": ### STAGE 1 ###
  print("\nYou arise to see the sun is setting and You are in a horse stable.")
  stage1 = input("\n  1. Take a deep breath\n  2. Look around\n  3. Listen closely\n")
  if stage1 == "1": ### GAME OVER ###
    print("\nYou died")
  elif stage1 == "3": ### STAGE 2
    print("\nYou hear the clop of hooved footsteps on a cobbled road.\nThey appear to be coming from the north, but you can't see the source")
    stage2 = input("\n  1. Go north towards the sound\n  2. Go south down the road\n  3. Go east across the road, into the woods\n  4. Hide behind the stables\n  5. Do nothing\n")
    if stage2 == "1" or stage2 == "5": ### GAME OVER ###
      print("\nYou died")
    elif stage2 == "2": ### STAGE 3A ###
      stage3a = input("\n  1. Run\n  2. Walk\n  3. Sneak\n")
      if stage3a == "1" or stage3a == "2": ### GAME OVER ###
        print("\nYou died")
      elif stage3a == "3": ### STAGE 4 ###
        print("\n ### STAGE 4 ###")

      else: ### GAME OVER ###
        print("\nInvalid choice. You died") 
    elif stage2 == "3" or stage2 == "4": ### STAGE 3B ###
      print("\nYou crouch down, hiding in the shadows")

      
    else: ### GAME OVER ###
      print("\nInvalid choice. You died") 
  elif stage1 == "2": ### STAGE 1A ###
    print("\nYou look around to see that there are 3 stables in a line. \nYou are in the middle one, and the other two are empty. \nIn fact, you don't see any sign that these stables have been used in years.")
    stage1a = input("\n  1. Take a deep breath\n  2. Listen closely\n")
    if stage1a == "1": ### GAME OVER ###
      print("\nYou died")
    elif stage1a == "2": ### STAGE 2 ###
      print("\n ### STAGE 2 ###")
    
    
    else: ### GAME OVER ###
      print("\nInvalid choice. You died") 
  else: ### GAME OVER ###
    print("\nInvalid choice. You died")
else: ### GAME OVER ###
  print("\nInvalid choice. You died")




  
# stage1 = input("You come to a fork in the road.\nDo you go left or right?\n").lower()
# if stage1=="left":
#   print("You died")
# else:
#   stage2 = input("You come across a chest.\nDo you open it? Y or N.\n").lower()
#   if stage2== "y":
#     print("You died")
#   else:
#     stage3 = input("Behind the chest you see a farmer minding his own business.\nDo you attack the famer? Y or N\n").lower()
#     if stage3 == "y":
#       print("You died")
#     else:
#       print("Pussy")
#       stage4= input("Attack the farmer you pussy. Y or N\n").lower()
#       if stage4 == "y":
#         print("You died")
#       else:
#         print("Congrats, you're a pussy.\n\nGAME OVER")   
  
