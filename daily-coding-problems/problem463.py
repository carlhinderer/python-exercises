# Problem 463
#   Easy
#   Asked by Facebook
#
# On a mysterious island there are creatures known as Quxes which come in three 
#   colors: red, green, and blue. One power of the Qux is that if two of them are 
#   standing next to each other, they can transform into a single creature of the 
#   third color.
#
# Given N Quxes standing in a line, determine the smallest number of them remaining 
#   after any possible sequence of such transformations.
#
# For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up 
#   with a single Qux through the following steps:
#
#           Arrangement       |   Change
#    ----------------------------------------
#    ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
#    ['B', 'B', 'G', 'B']      | (B, G) -> R
#    ['B', 'R', 'B']           | (R, B) -> G
#    ['B', 'G']                | (B, G) -> R
#    ['R']                     |
#
# Upgrade to premium and get in-depth solutions to every problem, including this one.
#
# If you liked this problem, feel free to forward it along so they can subscribe here! 
#   As always, shoot us an email if there's anything we can help with!
#
# Master algorithms together on Binary Search. Create a room, invite your friends, and 
#   race to finish the problem!
#
# No more? Snooze or unsubscribe.
#