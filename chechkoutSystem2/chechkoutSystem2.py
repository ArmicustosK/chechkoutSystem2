import re
import unittest
import math

class product():

     def getName(self):
       return self.name

     def getPrice(self):
       return self.price
     def getMarkdown(self):
        return self.markdown
     def getCode(self):
       return self.special_code
    
     def setcode(self,specialoffer):
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
     def __init__(self,name, price, specialoffer , ifbyweight, markdown):
       self.name = name.lower()
       self.price = price
       self.markdown=markdown

       self.special_code=0 if specialoffer is None else self.setcode(specialoffer)
       #if(specialoffer is not None):
       #     self.specialoffer=specialoffer.lower()
       #     self.special_code=self.setcode()
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
            

     
             



def init_productList():
       for input in inputList:

            dict[input.getName()] = input

def scan_item(checkout_product):
   temp_object=dict.get(checkout_product.lower())
   if (temp_object is None):
       print("The item is not scannable")
       return
   key=temp_object.getName()
   price=temp_object.getPrice()-temp_object.getMarkdown()
   add_number=1
   if(temp_object.ifbyweight):
       add_number=input("enter item weight ")
       price=float(price)*float(add_number)
   item = checkout_list.get(key)
   if item is not None:
        checkout_list[key]['count']+=add_number
        checkout_list[key]['price']+=price
        
   else:
       checkout_list[key]={'count':add_number,'price':price,}

if __name__ == '__main__':
    dict={}
    checkout_list={}
    inputList=[product('beef',3.2,"buy 5 get 3 half off,limit 8",True,0.33),product('pork',2.2,"",True,0),product('Apple',2.2,"",False,0),product('Peach',1.5,"",False,0.5)]
    init_productList();
    total=0
   
    checkout_item=str(input("enter item name or '0' to exit "))
    while(checkout_item!="0"):   
        scan_item(checkout_item)
        checkout_item=str(input("enter item name or '0' to exit "))
  
    unittest.main(exit=False)

