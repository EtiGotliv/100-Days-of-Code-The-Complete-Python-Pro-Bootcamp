from logo import logo


letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char.isalpha():
      position = letter.index(char)
      new_position = position + shift_amount
      end_text += letter[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

run = True
print_logo = True
while run:
  if print_logo == True:
      print(logo)
  print_logo = False
  direction = input("Please type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Please type your message:\n").lower()
  shift = int(input("Please type the shift number:\n"))

  if shift > 26:
    shift = shift % shift == 0

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  choice = input("Do you want to encode/decode again?\nType 'yes' or 'no': ")
  if choice == 'no':
    run = False
    print("Goodbye.")