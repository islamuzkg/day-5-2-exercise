# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
#78 65 89 86 55 91 64 89


# Think about how you would do this manually.
# If you had a list like this:
# [10, 6, 8, 2, 4, 12, 3]
# To find the max manually, you would start with the first number, 10, and that would be the max. Then you move to the next number, 6:
#  M
# [10, 6, 8, 2, 4, 12, 3]
#      ^
# Is it bigger than 10? No, then move to the next number:
#  M
# [10, 6, 8, 2, 4, 12, 3]
#         ^
#  M
# [10, 6, 8, 2, 4, 12, 3]
#            ^
#  M
# [10, 6, 8, 2, 4, 12, 3]
#               ^
#  M
# [10, 6, 8, 2, 4, 12, 3]
#                  ^
# Now we come to a number that IS bigger than our max of 10. So then we move the max point:
#                  M
# [10, 6, 8, 2, 4, 12, 3]
#                  ^
# Then continue:
#                  M
# [10, 6, 8, 2, 4, 12, 3]
#                      ^
# The list is finished now, and M points at 12.
# Now you just need to code it up!

max = 0
for score in student_scores:
  if score > max:
    max = score
  else:
    max = max
print(max)

#Write your code below this row 👇




