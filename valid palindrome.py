def check(s):
    # t = ""

    # for ch in s:
    #     if ch.isalnum():
    #         t += ch.lower()

    # j = len(t) - 1

    # for i in range(len(t) // 2):
    #     if t[i] != t[j]:
    #         return False
    #     j -= 1

    # return True
  s = "".join(char.lower() for char in s if char.isalnum())
  return s == s[::-1]


print(check("NoxinNixon"))                 # True
print(check("A man, a plan, a canal: Panama"))  # True
print(check("race a car"))                 # False
print(check("0P"))                         # False
