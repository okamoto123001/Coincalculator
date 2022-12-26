class calculator:
  mustCoinCount = [0,0,0,0,0,0]
  coin = [500,100,50,10,5,1]
  sum = 0

  def __init__(self,target):
    self.target = int(target)
    self.calculate500()
    self.calculate100()
    self.calculate50()
    self.calculate10()
    self.calculate5()
    self.calculate1()
    self.calculateSum()

  def calculate500(self):
    self.mustCoinCount[0] = self.target // 500
    self.target %= 500

  def calculate100(self):
    self.mustCoinCount[1] = self.target // 100
    self.target %= 100

  def calculate50(self):
    self.mustCoinCount[2] = self.target // 50
    self.target %= 50

  def calculate10(self):
    self.mustCoinCount[3] = self.target // 10
    self.target %= 10

  def calculate5(self):
    self.mustCoinCount[4] = self.target // 5
    self.target %= 5

  def calculate1(self):
    self.mustCoinCount[5] = self.target // 1
    self.target %= 1

  def calculateSum(self):
    for count in self.mustCoinCount:
      self.sum += count

target = input('計算したい金額を入力してください。')
result = calculator(target)
print(f'最小{result.sum}枚です。')
print(f'内訳\n500円（{result.mustCoinCount[0]}枚）\n100円（{result.mustCoinCount[1]}枚）\n50円（{result.mustCoinCount[2]}枚）\n10円（{result.mustCoinCount[3]}枚）\n5円（{result.mustCoinCount[4]}枚）\n1円（{result.mustCoinCount[5]}枚）')