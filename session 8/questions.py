# This example responds to a question about cases
# where a variable is required to meaningfully deal
# with some data. For example, why can't I create a
# list, add something to it, and print that list all
# on one line?

x=[5,4,3,2,1].append(6)
print(x)
# a problem above: the .append() method has no return value;
# x will be none. This is a result resolving the = operator
# right to left. We don't resolve the new list, assign it to x,
# then append(6)—that's not what we've asked for here.
# We've asked for the result of appending(6) to the list.
# To do that:
x2 = [5,4,3,2,1]
x2.append(6)
print(x2)
