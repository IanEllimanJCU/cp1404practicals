# What did you see on line 1?
# 19. An integer.
# What was the smallest number you could have seen, what was the largest?
# 5 and 20, as it is inclusive rather than inclusive.

# What did you see on line 2?
# 9. An integer.
# What was the smallest number you could have seen, what was the largest?
# Smallest possible in 3 and largest possible is 9.
# Could line 2 have produced a 4?
# No, it starts at 3 and ends at 10, with increments of 2. Meaning it only produce 3, 5, 7 or 9.


# What did you see on line 3?
# 2.559362123303291. A floating point number.
# What was the smallest number you could have seen, what was the largest?
# 2.5 and 5.5 I assume? I looked it up and it appears to be much more complicated than that.
import random
print(random.randint(0, 101))
exit()