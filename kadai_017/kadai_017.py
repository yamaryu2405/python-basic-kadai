people_dict ={"侍太郎":36,"侍花子":17}


class Human:
	def __init__(self,name,age):
		self.name=name
		self.age =age
	
	def check_adult(self):
		if self.age <20:
			print(f"{self.name}は20歳未満です。")
		
		else:
			print(f"{self.name}は大人です。")

for key,value in people_dict.items():
	human = Human(key,value)
	human.check_adult()


