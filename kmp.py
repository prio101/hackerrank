def kmp(pat, text):
  length_pat = len(pat)
  length_text = len(text)

  # to hold longest prefix suffix
  lps = [0]*length_pat

  # initial pattern index
  pat_index = 0

  computeLPSArray(pat, length_pat, lps)

  text_index = 0

  while text_index < length_text:
    if pat[pat_index] == text[text_index]:
      text_index += 1
      pat_index += 1
    
    if pat_index == length_pat:
      print("Found Pattern at index: "+str(text_index-pat_index))
      pat_index = lps[ pat_index-1 ]

    elif text_index < length_text and pat[pat_index] != text[text_index]:
      if pat_index != 0:
         pat_index = lps[pat_index-1]
      else:
        text_index +=1


def computeLPSArray(pat, length_pat, lps):
  # length of the prev lognest prefix suffix
  longest_prefix_suffix_len = 0

  # lps[0] is always 0
  lps[0]

  index = 1


  # loop to calculate the lps[index] for the index=1 to length_pat - 1

  while index < length_pat:
    if pat[index] == pat[longest_prefix_suffix_len]:
      longest_prefix_suffix_len += 1
      lps[index] = longest_prefix_suffix_len
      index += 1
    else:
      if longest_prefix_suffix_len != 0:
        longest_prefix_suffix_len = lps[longest_prefix_suffix_len-1]
      else:
        lps[index] = 0
        index += 1


def count_substring(string, sub_string):
    kmp(string, sub_string)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)