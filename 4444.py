print "\"olla v6i mitte olla\" ytles ta"
word = "test text"
print word
print """
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
word = "A"+"test"
print word
print "------------------------"
###################################
arv="1234567" 
print arv[:2] #2 arv j2rjekorras
print "------------------------"
word="Python" 
print word[-1] #0 taht jarjekorras print word[-1]
print "x"+word[1:]  #taht x liidetud s6nale Python, valja arvestades P
print "------------------------"
s = "supermegaawesomeword"
print len(s)
print('{:.2f}'.format(3.1415926))	#prindib kaks kohta peale koma
print'{0:>30}'.format('paremjoondus')	#prindib teksti paremjoondusega
print "asdf\nasdf"			#tekst uuele reale
print "asdf\tasdf"			#teksti vahele tab vahe
print "tekst {tekst teksti sees} 222"
print "-------------------------"
print "Kaal: {0}{1}".format(11,"kg")	#ise tehtud format
print "-----Tunnis tehtud------"
b=20
valem= 5*b
print "kaal: {0}{1}".format(valem,"kg")
print "-------------------------"
s=5.0
m=10.0
v=15.0
summa=s+m+v
#A - 1 kuul, ja see oleks must
valem=float (m/float(s+m+v))
print valem
print "------------"

#1sinine 1must
D=(s/summa)*(m/(summa-1))
print "{:f}".format(D)

print "kahe kuuli v6tmisel k6ik erinevad kuulid"

e1=(s/summa)*(m/(summa-1))
e2=(s/summa)*(v/(summa-1))
e3=(m/summa)*(v/(summa-1))
E=e1+e2+e3
print "{:f}".format(E)



