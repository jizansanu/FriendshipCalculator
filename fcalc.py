name1 = input("Enter Your Name:")
print(name1)
name2 = input("Enter Your Friends Name:")
print(name2)
fcount = 0

def friend(x):
 print("""
     FRIENDSHIP METER:
                ___    ___
               (   \__/   )
                \ {0}%    /
                 \      /
                  \____/
""".format(x))

def fchecker():
   consonants = 'qwrtypsdfghjklzxcvbnm'
   vowels = 'ueioa'
   fcount = 0
   for vowels in name1:
     for vowels in name2:
        if vowels in name1 and vowels in name2:
              fcount += 2
   for consonants in name1:
     for consonants in name2:
        if consonants in name1 and consonants in name2:
           fcount + 1
   if len(name1) + len(name2) >= 25:
      fcount -= fcount
      print('Error:\n Dont type in surnames or random input')
   if fcount > 100:
      fcount = 100
   impossible = (1,9,17,25,33,41,49,57,65,73,81,89,97)
   enemies = (2,10,18,26,34,42,50,58,66,74,82,90,98)
   Notfriends = (3,11,19,27,35,43,51,59,67,75,83,91,99)
   knoweachother= (4,12,20,28,36,44,52,60,68,76,84,92,100)
   Justfriends = (5,13,21,29,37,45,53,61,69,77,85,93)
   Normalfriends = (6,14,22,30,38,46,54,62,70,78,86,94)
   Bestfriends = (7,15,23,31,39,47,55,63,71,79,87,95)
   Soulmates = (8,16,24,32,40,48,56,64,72,80,88,96)
   if fcount in impossible:
      print('\t there is no chance for friendship!!!')
      print("""
        \tIMPOSSIBLE
      {0} and {1} two will never be together\n
      NEVER!!!
      """.format(name1,name2))
      fcount = -100
   if fcount in enemies:
      print("""
        \tENEMIES
       With {0} and {1} there is no chance for even the slightest bit of love, only hatred.
       """.format(name1, name2))
      fcount = -5
   if fcount in Notfriends:
      print("""
           \tNotfriends
       {0} and {1} atleast have a chance, but its being hindered by both of them being shy.
       """.format(name1, name2))
      fcount = 15
   if fcount in Normalfriends:
      print("""
           \tNormalfriends
       {0} and {1} are meant to be Normalfriends.
       """.format(name1, name2))
      fcount = 20
   if fcount in Bestfriends:
      print("""
           \tBestfriends
       With {0} and {1} there is a chance this two will be Bestfriends.
       """.format(name1, name2))
      fcount = 30
   if fcount in Soulmates:
      print("""
           \tSoulmates
       {0} and {1} will probably last long, and are Soulmates.
       """.format(name1, name2))
      fcount = 60
   if fcount in Soulmates:
      print("""
               \tSoulmates
             {0} and {1} will probably last long, and are Soulmates.
           """.format(name1, name2))
           
      fcount = 99
      

   elif fcount == 0:
      print("""
               \tUNKNOWN
          It is impossible to determine if {0} and {1} are compatible.
          TOO BAD!
      
      """.format(name1, name2))
 
   friend(fcount)
      

fchecker()
