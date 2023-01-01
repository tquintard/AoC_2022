import copy

decryp_key = 811589153

def encrypted_data(part):
    with open('AoC_2022\Day_20\Day20.txt', "r") as f:
        inputs = f.read().splitlines()
    numbers = [int(input) * decryp_key ** (part - 1) for input in inputs]
    return [input for input in enumerate(numbers)], (numbers.index(0), 0)
    
def decrypt_grove(part):
  rounds = 10
  encrypted_groves, tuple_0 = encrypted_data(part)
  len_grove = len(encrypted_groves) - 1
  decrypted_groves = copy.deepcopy(encrypted_groves)
  for _ in range(rounds ** (part - 1)):
      for grove in encrypted_groves:
          pos_init = decrypted_groves.index(grove)
          decrypted_groves.remove(grove)
          pos_target = (pos_init + grove[1] + len_grove) % len_grove
          if pos_target == 0 and grove[1] != 0:
              pos_target = len_grove
          decrypted_groves.insert(pos_target, grove)
  idx_tuple_0 = decrypted_groves.index(tuple_0)
  print(sum([decrypted_groves[(idx_tuple_0 + i) % (len_grove + 1)][1] for i in [1000, 2000, 3000]]))

if __name__ == "__main__":
    for part in [1, 2]: 
        decrypt_grove(part)