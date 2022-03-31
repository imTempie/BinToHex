#Binary and Hexadecimal converter
#Github.com/imTempie

print("Binary to Hexadecimal")
print("---------------------")

#Binary to Hexadecimal
def binary():
  binary = input("\nEnter The Binary:  ")
  hex = f'{int(binary, 2):X}'
  print("\nThe Hex is:",hex,"\n")

#Hexadecimal to binary
def hex():
  hex1 = input("\nEnter the Hex:  ")
  hex1 = f'{0xABC123EFFF:0>42b}'
  print("\nIn binary is:",hex1,"\n")

#infinite loop of converter
while True:  
  print("[A] Binary to Hex")
  print("[B] Hex to Binary\n")
  
  choice = input("")
  
  if choice == "A" or choice == "a":
    binary()
  elif choice == "B" or choice == "b":
    hex()
  else:
    print("Menu option not available")
