def count_words(file):
    return len(file.split())

def count_letters(string):
  d = {}
  for l in string:
    low = l.lower()
    if low in d:
      d[low] += 1
    else:
      d[low] = 1
  return d

def sort_on(item):
  return item['num']

def sort(d):
  n = []
  for i in d:
    n.append({"char": i, "num": d[i]})
  n.sort(reverse=True, key=sort_on)
  return n