# https://www.1point3acres.com/bbs/thread-921612-1-1.html

# To determine whether two passwords are similar, they take the new password, choose a set of indices and change the characters at these indices to the next cyclic character exactly once. Character 'a' is changed to "b', "b' to 'c' and so on, and '2' changes to 'a'. The password is said to be similar if after applying the operation, the old password is a subsequence of the new password.
# The developers come up with a set of n password change requests, where newPasswords denotes
# the array of new passwords and oldPasswords denotes the array of old passwords. For each pair newPasswords!] and oldPasswords!), return "YES" if the passwords are similar, that is, newPasswords[) becomes a subsequence of oldPasswords(] after performing the operations, and "No" otherwise.
# Note: A subsequence is a sequence that can be derived from the given sequence by deleting zero
# or more elements without changing the order of the remaining elements.
# Example
# The two lists of passwords are given as newPasswords = ("baacbab", "accdb", "baacba"], and
# oldPasswords = l"abdbc", "ach" "abb"].
# C‍‌‌‌‍‌‍‌‍‌‌‍‌‍‍‌‌‍‍‌onsider the first pair: newPasswords[0] = "baacbab" and oldPasswords = "abdbc". Change
# "'ac"to "'bd'" at the 3rd and 4th positions, and "b"to "c" at the last position.