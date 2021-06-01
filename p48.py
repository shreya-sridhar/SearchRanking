def PlusMinus(num:int):
  str_num = str(num) 
  num_operations = len(str_num)-1 
  for i in range(2^num_operations):
    # i = 0101 
    print(i)
    if convertToSum(i,str_num)[0] == 0:
      # return sum, list of operations
      return convertToSum(i,str_num)[1].join("")
  return 'not possible'
  # code goes here

def convertToSum(i:int,str_num:str):
  #  i = 0101, str_num = 26712 
  #  0 -> -, 1-> +
  operations = ["-"]*(len(str_num)-1)
  sum = 0
  # i & (i-1) -> 0101 & 0100 -> 0100 -> returns i without last 1
  # i ^ (i-1) -> 0101 ^ 0100 -> 0001 -> returns 
  while i:
    print(i,"i")
    if i & 1 == 1:
      operations.append('+') 
      print(operations)
    else:
      operations.append('-')
    i >> 1
  # operations = [0,0,1,1]
  for index in range(len(str_num)-1):
    # 26712
    if operations[index] == '-':
      sum += int(str_num[index]) - int(str_num[index+1])
    else:
      sum += int(str_num[index]) + int(str_num[index+1])
  return sum, operations 

# def convertToOperations(i:int) -> str:


# keep this function call here 
print('Test 1 passing: ' + str(PlusMinus(199) == 'not possible'))
print('Test 2 passing: ' + str(PlusMinus(26712) == '-+--'))

# 2-6+7-1-2 = 0
# 0000,0001,...,1111 


