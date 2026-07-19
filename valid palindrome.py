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
  # s = "".join(char.lower() for char in s if char.isalnum())
  # return s == s[::-1]
  j = len(s)-1
  ch = 0
  while ch < j:
    if s[ch].isalnum() & s[j].isalnum():
      if s[ch].lower() == s[j].lower():
        j -= 1
        ch += 1
        continue
      else:
        print(s[ch],s[j])
        return False
    if not s[ch].isalnum():
      ch += 1
      continue
    if not s[j].isalnum():
      j -= 1
      continue
  return True


print(check("NoxinNixon"))                 # True
print(check("A man, a plan, a canal: Panama"))  # True
print(check("race a car"))                 # False
print(check("0P"))                         # False
