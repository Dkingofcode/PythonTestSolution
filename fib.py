
# Write a program to sum the first 50 fibonacci numbers

def FirstFib(n):
    if(n <= 2):
      return 1
    else:
      return FirstFib(n - 1) + FirstFib(n - 2) 
    