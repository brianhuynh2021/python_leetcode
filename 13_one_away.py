'''One Away: There are three types of edits that can be performed on strings: 
insert a character, remove a character, or replace a character. Given two strings, 
write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true pales, pale -> true pale, bale -> true pale, bake -> false'''


def one_away(str1, str2):
  """
  Checks if two strings are one edit away (or zero edits).

  Args:
      str1: The first string.
      str2: The second string.

  Returns:
      True if the strings are one edit away, False otherwise.
  """

  len1, len2 = len(str1), len(str2)

  # Check if the length difference is greater than 1
  if abs(len1 - len2) > 1:
    return False

  # If lengths are equal, check for replace operation
  if len1 == len2:
    count = 0
    for i in range(len1):
      if str1[i] != str2[i]:
        count += 1
        if count > 1:
          return False
    return True

  # If lengths differ by one, check for insert or delete operation
  longer, shorter = (str1, str2) if len1 > len2 else (str2, str1)
  i, j = 0, 0
  while i < len(shorter) and j < len(longer):
    diff_count = 0
    if shorter[i] != longer[j]:
      # check if there is only edit away
      diff_count += 1
      if diff_count > 1:
          return False
      j += 1
    
    else:
      i += 1
      j += 1
  return True

# Test cases
print(one_away('pale', 'ple'))   # True
print(one_away('pales', 'pale'))  # True
print(one_away('pale', 'bale'))  # True
print(one_away('pale', 'bake'))  # False
