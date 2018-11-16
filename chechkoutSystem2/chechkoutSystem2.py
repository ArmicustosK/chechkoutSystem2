import re
import unittest

class product():

     def getName(self):
       return self.name

     def getPrice(self):
       return self.price
     
     def getCode(self):
       return self.special_code
   
     def setcode(self):
       str=re.sub(r"\s+", "", self.specialoffer.lower())
       if ( str== "buy1get1free"):
           return 1
       if(str=="buy2get1halfoff"):
           return 2
       if(str=="buy3get220%off"):
           return 3
       if(str=="3for$5"):
           return 4
       if(str=="2for$2.5"):
           return 5
       if(str=="buy3lbsget1lbhalfoff"):
           return 6
       if(str=="buy2get1free,limit6"):
           return 7
       
       if(str=="buy5get3halfoff,limit8"):
           return 8
       if(str=="buy3.5lbget1.5lbhalfoff"):
           return 9
     def __init__(self,name, price, specialoffer , ifbyweight):
       self.name = name
       self.price = price
       if(specialoffer is not None):
            self.specialoffer=specialoffer
       
            self.special_code=self.setcode()
       self.ifbyweight = ifbyweight
class test(unittest.TestCase):
    
     #def test_Dictionary(self):
        
     #    object = product('beef',3.2,"buy 5 get 3 half off,limit 8")
     #    dict[object.getName()] = object
     #    self.assertEquals(dict['beefs'],object)
    
     def test_inputNullcode(self):
         object = product('beef',3.2,"",True)
         dict[object.getName()] = object
         object2=dict['beef']
         assert object2.getCode() is  None
     def test_dictionaryInputList(self):
         for input in inputList:
             self.assertEqual(dict[input.getName()],input)
            

     #def test_loop(self):
     #    while checkout_product!="0":
             



dict={}
checkout_list={'apple':{'count':0,'price':0}}
inputList=[product('beef',3.2,"buy 5 get 3 half off,limit 8",True),product('pork',2.2,"",False)]
def init_productList():
       for input in inputList:

            dict[input.getName()] = input
def discountProcessor():
    return 1;
def scan_item(checkout_product):
   temp_object=dict.get(checkout_product.lower())
   key=temp_object.getName()
   price=temp_object.getPrice()
   if key in checkout_list:
        checkout_list[key]["count"]+=1
   else:
       checkout_list[key]={'count':1,'price':price}
    
    
init_productList();
total=0
checkout_item=str(input("enter item name or '0' to exit "))
while(checkout_item!="0"):   
 scan_item(checkout_item)
 checkout_item=str(input("enter item name or '0' to exit "))
   
 
if __name__ == '__main__':
    unittest.main(exit=False)

