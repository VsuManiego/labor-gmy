
# Construction Labor Cost Calculator

print("_________________________________________________________________________________________")
title= "CONSTRUCTION LABOR COST CALCULATOR"
x = title.center(75)
print(x)
print("_________________________________________________________________________________________")


print("Hello, what do you want to estimate? Please enter your selection from the following:")
print("\nLABOR COSTING OPTIONS")
print("1-  Painting Labor\n"
      "2-  Plastering Labor\n"
      "3-  Excavation Labor\n"
      "4-  Slab Forms Labor\n"
      "5-  Rebars Labor\n"
      "6-  TotalAll\n"
      "0-  EXIT")
print("\n")


def PaLC():
        area1= float(input ('Enter Area to Paint (Sq.m.): '))
        costpersqm1= float(input ('Enter Cost per Sq.m.: '))
        laborcost1= area1*costpersqm1
        formatted1 = f"{laborcost1:.2f}"
        print(f"The Total Painting Laborcost will be: PhP {formatted1}\n")


def PlLC ():
        area2= float(input ('Enter Area to Plaster (Sq.m.): '))
        costpersqm2= float(input ('Enter Cost per Sq.m.: '))
        laborcost2= area2*costpersqm2
        formatted2 = f"{laborcost2:.2f}"
        print(f"The Total Plastering Labor Cost will be: PhP {formatted2}\n")


def ExLC ():
        length= float(input("Enter length to be Excavated (m): "))
        Width= float(input("Enter Width to be Escavated (m): "))
        Height= float(input("Enter the Height to be Escavated (m): "))
        Footings= int(input("Enter no. of Footings: "))
        t_volume= length*Width*Height*Footings
        
        productivity_rate = 6
        total_Manhour= productivity_rate*t_volume 
    
        Labor = 8 

        No_of_days= total_Manhour/ Labor
        SalaryperDay= float(input("Enter Salary of Labor per Day: "))
        laborcost3= SalaryperDay*No_of_days
        formatted3= f"{laborcost3:.2f}"
        print(f"The Total Escavation Labor Cost will be: PhP {formatted3}\n")


def SfLC ():
        length= float(input("Enter length of Slab (m): "))
        Width= float(input("Enter Width of Slab (m): "))

        Slabs= int(input("Enter no. of Slabs: "))
        t_area= length*Width*Slabs

        productivity_rate1 = 3.34
        total_Manhour= productivity_rate1*t_area 
        print("\n")

        labor= 16 
        No_of_days1= total_Manhour/ labor
        SalaryperDay1= float(input("Enter Salary of Labor per Day: "))
        laborcost4= SalaryperDay1*No_of_days1
        formatted4= f"{laborcost4:.2f}"
        print(f"The Total Slab Forms Labor Cost will be: PhP {formatted4}\n")
        

def ReLC ():
        steels_shortside= int(input("Enter no. of Steels from the short side: "))
        steel_length1= float(input("Enter steel length: "))
        steels_longerside= int(input("Enter no. of Steels from the longer side: "))
        steel_length2= float(input("Enter steel length: "))
        diameter = float(input("Enter Diameter of the Rebar: "))
        weight_meter = 0.888

        l1= steels_shortside *steel_length1
        l2= steels_longerside*steel_length2
        t_l= l1 + l2

        t_weight= t_l*weight_meter

        productivity_rate2= 0.07

        t_MH= t_weight*productivity_rate2
        
        labor2=8
        No_of_days2= t_MH/labor2

        SalaryperDay2= float(input("Enter Salary of Labor per Day: "))
        laborcost5= SalaryperDay2*No_of_days2
        formatted5= f"{laborcost5:.2f}"
        print(f"The Total Rebar Labor Cost will be: PhP {formatted5}\n")

def total ():
     sum = 0.0
     no_count = 0

     while True:
       value = float(input("Enter cost value: "))
       sum += value
       no_count += 1
       
       selection = input("Add another value? ( y/n ) : ")
       if selection.casefold() == 'n':
           break
       elif selection.casefold()== 'y':
          if selection == 'n':
               break  
       else:
          print("Invalid input. Please try again.")
          selection = input("Add another value? ( y/n ) : ")
          if selection == 'n':
               break

     print(f"The total labor cost is : Php {sum}")
     print("_______________________________")
         
     
start_over = "true"
while start_over == "true":
    selection = int(input("SELECTION: "))
    print("_______________________________")
    if selection == 1:
        PaLC ()

    elif selection == 2:
        PlLC ()
    
    elif selection == 3:
         ExLC ()
    
    elif selection == 4:
         SfLC ()

    elif selection == 5:
         ReLC ()
         
    elif selection == 6:
         total ()

    elif selection == 0:
          break    

    else:
          print("Invalid input. Please try again.")

          redo_program = input("To restart type R: ")
          if redo_program == 'R':
               start_over = "true" 
          else:
               start_over = "null"
               print("Invalid input. Please try again.")
               redo_program = input("To restart type R: ")
               if redo_program == 'R':
                    start_over = "true"


end = "THANK YOU FOR USING CLC CALCULATOR!"                                    
y = end.center (75)                                                 
print(y)                                  
print("_________________________________________________________________________________________")            

        
  
        


        
    
    

        