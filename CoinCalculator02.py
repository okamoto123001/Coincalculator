class calculator:
  mustCoinCount = [0,0,0,0,0,0]
  myCoinCount = [8,5,1,4,0,9]
  resultCoinCount = [0,0,0,0,0,0]
  coin = [500,100,50,10,5,1]
  resultSum = 0
  sumMyMoney = 0

  def __init__(self,target):
    self.target = int(target)
    self.calculateMyMoney()

  def calculateResultCoinCount(self):
    for index, count in enumerate(self.myCoinCount):
      self.mustCoinCount[index] = self.target // self.coin[index]

      if self.mustCoinCount[index] >= count:
        self.resultCoinCount[index] = count
      else:
        self.resultCoinCount[index] = self.mustCoinCount[index]
      self.target -= self.coin[index] * self.resultCoinCount[index]

  def calculateMyMoney(self):
    for index, count in enumerate(self.myCoinCount):
      self.sumMyMoney += self.coin[index] * count

  def checkCanPay(self):
    return self.target <= self.sumMyMoney
  
  def calculateResultSum(self):
    for count in self.resultCoinCount:
      self.resultSum += count

target = input('計算したい金額を入力してください。')
result = calculator(target)

if result.checkCanPay():
  result.calculateResultCoinCount()
  result.calculateResultSum()
  print(f'合計{result.resultSum}枚です。')
  print(f'内訳\n500円（{result.resultCoinCount[0]}枚）\n100円（{result.resultCoinCount[1]}枚）\n50円（{result.resultCoinCount[2]}枚）\n10円（{result.resultCoinCount[3]}枚）\n5円（{result.resultCoinCount[4]}枚）\n1円（{result.resultCoinCount[5]}枚）')
else:
  print(f'現在の所持金では支払できません。')
