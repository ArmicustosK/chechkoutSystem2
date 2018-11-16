import re
import unittest
class Discount ():
    def getApplyPosition(self):
        return self.position
    def getLimit(self):
        return self.limit
    def getValue(self):
        return self.value
    def __init__(self, position, value,limit):
        self.position=position
        self.value=value
        self.limit=limit if limit is not None else 0
class product():

     def getName(self):
       return self.name

     def getPrice(self):
         price=self.price-self.markdown
         return price
     def getMarkdown(self):
        return self.markdown

     def getDiscount(self):
        return self.discount
    
     def setDiscount(self,specialoffer):
       str=re.sub(r"\s+", "", specialoffer.lower())
       if ( str== "buy1get1free"):
           return Discount(2,1,None)
       if(str=="buy2get1halfoff"):
           return Discount(3,0.5,None)
       if(str=="buy3get220%off"):
          return Discount(5,0.4,None)
       if(str=="3for$5"):
           return 4
       if(str=="2for$2.5"):
           return 5
       if(str=="buy3lbsget1lbhalfoff"):
           return 6
       if(str=="buy1get1free,limit6"):
           return Discount(2,1,6)
       if(str=="buy2get1halfoff,limit8"):
           return Discount(3,0.5,8)
       if(str=="buy3get220%off,limit10"):
          return Discount(5,0.4,10)
       if(str=="buy3.5lbget1.5lbhalfoff"):
           return 9
       
     def __init__(self,name, price, specialoffer , ifbyweight, markdown):
       self.name = name.lower()
       self.price = price
       self.markdown=markdown
       self.discount=None
       if(specialoffer is not None):
        self.discount=self.setDiscount(specialoffer)
      
       self.ifbyweight = ifbyweight
class test(unittest.TestCase):
    
     #def test_Dictionary(self):
        
     #    object = product('beef',3.2,"buy 5 get 3 half off,limit 8")
     #    dict[object.getName()] = object
     #    self.assertEquals(dict['beefs'],object)
    
     #def test_inputNullcode(self):
     #    object = product('beef',3.2,"",True)
     #    dict[object.getName()] = object
     #    object2=dict['beef']
     #    assert object2.getCode() is  None
     def test_dictionaryInputList(self):
         for input in inputList:
             self.assertEqual(dict[input.getName()],input)
            
     def test_properdiscount(self):
         item=product('banana',3.2,"buy 1 get 1 free",True,0.33)
         self.assertEqual(item.discount.getApplyPosition(),2)
         self.assertEqual(item.discount.getValue(),1)
         self.assertEqual(item.discount.getLimit(),0)   
         item1=product('kiwa',4.2,"buy 1 get 1 free, limit 6",True,0.33)
         self.assertEqual(item1.discount.getApplyPosition(),2)
         self.assertEqual(item1.discount.getValue(),1)
         self.assertEqual(item1.discount.getLimit(),6) 
     def test_discount(self):
          checkout_list={}
         #test discount item cal by unit without limit 
         #apple*4+peach*4
         #total=8*2.2-(4*2.2)+1*4-(1*1*0.5)=
          checkout_items=["apple","peach","apple","peach","apple","apple","apple","peach","peach","apple","apple","apple"]
          for item in checkout_items:
              scan_item(item)
          self.assertEqual(round(get_total(), 2),12.3)
     def test_discountWithLimit(self):
         #test discount item cal by unit without limit 
         #kiwi*8+banana*9
         #total=8*2.2-(3*2.2)+1*9-(1*2*0.5)=19
          checkout_list.clear()
          checkout_items=["kiwi","banana","kiwi","banana","kiwi","banana","banana","banana","kiwi","banana","banana","banana","kiwi","banana","kiwi","kiwi","kiwi"]
          for item in checkout_items:
              scan_item(item)
          self.assertEqual(round(get_total(), 2),19)
def init_productList():
   for input in inputList:

      dict[input.getName()] = input

def scan_item(checkout_product):
   temp_object=dict.get(checkout_product.lower())
   if (temp_object is None):
       print("The item is not scannable")
       return
   discount = temp_object.getDiscount()
   key=temp_object.getName()
   price=temp_object.getPrice()
   total=price
   add_number=1
   if(temp_object.ifbyweight):
       add_number=input("enter item weight ")
       total=float(price)*float(add_number)
       #add discount here:
   item = checkout_list.get(key)
   if item is not None:
        position=checkout_list[key]['count']
        position +=add_number
        checkout_list[key]['count']=position
        if (discount is not None):
            if(position%discount.getApplyPosition()==0):
                if(discount.getLimit()==0 or (discount.getLimit()!=0 and position<=discount.getLimit())):
                    total=total-discount.getValue()*price
        checkout_list[key]['total']+=total    
   else:
       checkout_list[key]={'product':temp_object,'count':add_number,'total':total}

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
        checkout_list[remove_item]['total']-=item.getPrice()
def get_total():
    total=0
    for item in checkout_list.values():
        total+=item['total']
    return total
#def get_discount(curr_product,count):
#    discount=0
#    if(curr_product.getCode()==1 or curr_product.getCode()==7):
#        count=6 if count>6 else count
#        discount=int(count/2)*curr_product.getPrice()
#    if(curr_product.getCode()==2 or curr_product.getCode()==8):
#        count=8 if count>8 else count
#        discount=int(count/3)*0.5*curr_product.getPrice()
#    if(curr_product.getCode()==3 or curr_product.getCode()==10):
#        count=10 if count>10 else count
#        discount=int(count/3)*0.2*2*curr_product.getPrice()
#      #if(str=="3for$5"):
#      #     return 4
#      # if(str=="2for$2.5"):
#      #     return 5
    
#    return discount
if __name__ == '__main__':
    dict={}
    checkout_list={}
    inputList=[product('beef',3.2,"buy 5 get 3 half off,limit 8",True,0.33),product('pork',2.2,"",True,0),product('Apple',2.2,"buy1get1free",False,0),product('kiwi',2.2,"buy1get1free,limit6",False,0),product('Peach',1.5,"buy2get1halfoff",False,0.5),product('banana',1.5,"buy2get1halfoff,limit8",False,0.5)]
    init_productList();
    total=0
   
    checkout_item=str(input("enter item name or '0' to exit, 'c'to cancel item"))
    while(checkout_item!="0"): 
        if(checkout_item.lower()=="c"):
            remove_item()
        else:
            scan_item(checkout_item)
        checkout_item=str(input("enter item name or '0' to exit, 'c'to cancel item"))
    
    unittest.main(exit=False)

