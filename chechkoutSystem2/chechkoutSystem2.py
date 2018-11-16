import re
import unittest

class product():

     def getName(self):
       return self.name

     def getPrice(self):
         price=self.price-self.markdown
         return price
     def getMarkdown(self):
        return self.markdown

     def getCode(self):
       return self.special_code
    
     def setcode(self,specialoffer):
       str=re.sub(r"\s+", "", specialoffer.lower())
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
   price=temp_object.getPrice()
   add_number=1
   if(temp_object.ifbyweight):
       add_number=input("enter item weight ")
       price=float(price)*float(add_number)
   item = checkout_list.get(key)
   if item is not None:
        checkout_list[key]['count']+=add_number
        checkout_list[key]['price']+=price
        
   else:
       checkout_list[key]={'product':temp_object,'count':add_number,'price':price}
def remove_item():
    remove_item=str(input("enter item you like to remove"))
    item=checkout_list.get(remove_item.lower())['product']
    if(item is None):
        print("Invalid input, please try again")
        return
    if(item.ifbyweight):
        del checkout_list[remove_item]
    else:
        checkout_list[remove_item]['count']-=1
        checkout_list[remove_item]['price']-=item.getPrice()
def get_total():
    total=0
    for item in checkout_list.values():
       curr_product=item['product']
       item_count=item['count']
     
       total+=item['price']-get_discount(curr_product,item_count)
    return total
def get_discount(curr_product,count):
    discount=0
    if(curr_product.getCode()==1):
        
        discount=int(count/2)*curr_product.getPrice()
    if(curr_product.getCode()==2):
        discount=int(count/3)*0.5*curr_product.getPrice()
    if(curr_product.getCode()==3):
        discount=int(count/3)*0.2*2*curr_product.getPrice()
    return discount
if __name__ == '__main__':
    dict={}
    checkout_list={}
    inputList=[product('beef',3.2,"buy 5 get 3 half off,limit 8",True,0.33),product('pork',2.2,"",True,0),product('Apple',2.2,"buy1get1free",False,0),product('Peach',1.5,"buy2get1halfoff",False,0.5)]
    init_productList();
    total=0
   
    checkout_item=str(input("enter item name or '0' to exit, 'c'to cancel item"))
    while(checkout_item!="0"): 
        if(checkout_item.lower()=="c"):
            remove_item()
        else:
            scan_item(checkout_item)
        checkout_item=str(input("enter item name or '0' to exit, 'c'to cancel item"))
    print(get_total())
    unittest.main(exit=False)

