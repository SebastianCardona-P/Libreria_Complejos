import libcomplex as cplx

def result(a, b, c, d):
    passed = 0
    failed = 0
    if a == b and c ==d:
        passed += 1
    else:
        failed += 1
    return "passed = "+str(passed)+" | failed = "+str(failed)
    
def result1(a, b):
    passed = 0
    failed = 0
    if a == b:
        passed += 1
    else:
        failed += 1
    return "passed = "+str(passed)+" | failed = "+str(failed)
    
# Suma:
c1 = (7,9)
c2 = (8,10)
c3 = (8,-3)
c4 = (12,9)
answer1 = cplx.sumcplx(c1,c2)
answer2 = cplx.sumcplx(c3,c4)
print("Caso 1, suma")
print(result(answer1[0],15,answer1[1],19))
print("")
print("Caso 2, suma")
print(result(answer2[0],20,answer2[1],6))
print("")

# Resta:
c1 = (17,62)
c2 = (11,-77)
c3 = (35,-9)
c4 = (-5,3)
answer1 = cplx.rescplx(c1,c2)
answer2 = cplx.rescplx(c3,c4)
print("Caso 1, resta")
print(result(answer1[0],6,answer1[1],139))
print("")
print("Caso 2, resta")
print(result(answer2[0],40,answer2[1],-12))
print("")

# Multiplicacion:
c1 = (8,13)
c2 = (8,5)
c3 = (41,-23)
c4 = (17,-19)
answer1 = cplx.multcplx(c1,c2)
answer2 = cplx.multcplx(c3,c4)
print("Caso 1, multiplicacion")
print(result(answer1[0],-1,answer1[1],144))
print("")
print("Caso 2, multiplicacion")
print(result(answer2[0],260,answer2[1],-1170))
print("")

# Division:
c1 = (24,55)
c2 = (3,4)
c3 = (8,1)
c4 = (-6,4)
answer1 = cplx.divcplx(c1,c2)
answer2 = cplx.divcplx(c3,c4)
print("Caso 1, division")
print(result(answer1[0],292/25,answer1[1],69/25))
print("")
print("Caso 2, division")
print(result(answer2[0],-11/13,answer2[1],-19/26))
print("")

# Modulo:
c1 = (3,4)
c2 = (-6,0)
answer1 = cplx.modcplx(c1)
answer2 = cplx.modcplx(c2)
print("Caso 1, modulo")
print(result1(answer1,5))
print("")
print("Caso 2, modulo")
print(result1(answer2,6))
print("")

# Conjugado:
c1 = (54,85)
c2 = (32,-34)
answer1 = cplx.conjucplx(c1)
answer2 = cplx.conjucplx(c2)
print("Caso 1, conjugado")
print(result(answer1[0],54,answer1[1],-85))
print("")
print("Caso 2, conjugado")
print(result(answer2[0],32,answer2[1],34))
print("")


# cartesiano-polar:
c1 = (64,33)
c2 = (12,42)
answer1 = cplx.polar_cartecplx(c1)
answer2 = cplx.polar_cartecplx(c2)
print("Caso 1, polar-cartesiano")
print(result(answer1[0],-0.85,answer1[1],63.99))
print("")
print("Caso 2, polar-cartesiano")
print(result(answer2[0],-4.8,answer2[1],-11))
print("")

# Fase:
c1 = (3,4)
c2 = (4,4)
answer1 = cplx.fasecplx(c1)
answer2 = cplx.fasecplx(c2)
print("Caso 1, fase")
print(result1(answer1,0.93))
print("")
print("Caso 2, fase")
print(result1(answer2,0.79))
print("")
