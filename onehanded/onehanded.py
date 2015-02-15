import os, random, sys

RANKS = "23456789TJQKA"
SUITS = "HDCS"

# Simulate a game of one-handed solitaire.
# @return {number} The number of held cards remaining at the end of the game.
def play():
  deck = ["%s%s" % (rank, suit) for rank in RANKS for suit in SUITS]
  random.shuffle(deck)

  pos = 0
  while pos < len(deck):
    if pos > 2 and deck[pos][0] == deck[pos-3][0]:
      deck[pos-3:pos+1] = []
      pos -= 3
    elif pos > 2 and deck[pos][1] == deck[pos-3][1]:
      deck[pos-2:pos] = []
      pos -= 2
    else:
      pos += 1

  return len(deck)

TRIALS = 1000000
STEP = 100000
counts = [0]*52

sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)

for i in range(TRIALS):
  score = play()
  counts[score] += 1

  if i%STEP == 0:
    print ".",

print "Simulation done."

with open("output.txt", "w") as f:
  fmt = "| %5d | %8d | %15.2f |\n"
  line = "|" + "-"*7 + "|" + "-"*10 + "|" + "-"*17 + "|\n"

  f.write(line)
  f.write("| Score | Count    | Probability (%) |\n")
  f.write(line)
  for score, count in enumerate(counts):
    if score%2 == 0:
      probability = 100*count/float(TRIALS)
      f.write(fmt  % (score, count, probability))
  f.write(line)

print "Output done."