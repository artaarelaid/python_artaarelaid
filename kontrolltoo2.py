#1
tekst1 = raw_input()
tekst2 = raw_input()
tekst3 = raw_input()

print tekst1.upper(), len(tekst2), tekst3.lower()

#2
tekst4 = raw_input()

if len(tekst4) > 4:
	print "tekst pikem kui 4 t2hte"
else:
	print "tekst lyhem kui 4 t2hte"
	
if "a" in tekst4:
	print "leidsin t2he a"
else:
	print "ei leidnud t2hte a"
	
if tekst4.islower():
	print "tekst on kirjas ainult v2iket2htedega"
else:
	print "tekstis on suurt2hti"

#3
print "Equation of derivation"

r0=2
v0t=3
a=4
t=5

r=r0+v0t+(a*t*t)/2

print "{:.2f}".format(r)

#4
tekst5 = raw_input()
print "vahetasin k6ik a t2hed # m2rgiga"
print tekst5.replace("a", "#")
