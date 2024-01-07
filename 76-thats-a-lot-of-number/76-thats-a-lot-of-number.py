with open("/Users/alfielong/programming/ocr-challenges/76-thats-a-lot-of-number/76-thats-a-lot-of-number.txt", "r") as f:
    nums = [int(i) for i in f]

nums = sum(nums)

nums = str(nums)

print(nums[:10])
