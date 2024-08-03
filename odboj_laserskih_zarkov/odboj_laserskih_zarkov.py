import math
def laser(koef, d, tocka, vektor):
    tocke = []
    zelja = tocka
    odboji=0
    while True:
        if math.sqrt(sum([(a-b)**2 for (a,b) in zip(tocka, zelja)])) < 0.101:
            if odboji != 0:
                odboji-=1
                break
            
        a = sum([k*v**2 for v,k in zip(vektor,koef)])
        b = sum([k*2*v*b for v,b,k in zip(vektor,tocka,koef)])
        c = sum([k*b**2 for b,k in zip(tocka,koef)]) - d
        t1 = ( -b + (b**2-4*a*c)**0.5 )/(2*a)
        t2 = ( -b - (b**2-4*a*c)**0.5 )/(2*a)
   
        if abs(t1)<0.0001:
            tocka =  [t2*v+b for v,b in zip(vektor,tocka)]
        else:
            tocka = [t1*v+b for v,b in zip(vektor,tocka)] 
        
        gradient = [2*k*x for x,k in zip(tocka,koef)]
        proj = ( sum([v*g for v,g in zip(vektor,gradient)])/sum([g**2 for g in gradient]) )
        proj = [proj*g for g in gradient]
            
        vektor = [2*p - v for p,v in zip(proj, vektor)]
        #print(f"t:{[round(t,3) for t in tocka]}, v: {[round(v,3) for v in vektor]}")
        tocke.append([round(t,3) for t in tocka])       
        odboji+=1
        
    return odboji, tocke[:15]

# dot(koeficienti, X) = d, da enačbo elipsoida, kjer X = (x1**2, ..., xn**2)
# laser(koeficienti, d, točka na elipsoidu od koder streljamo, smer strela) 

#primera uporabe:
  
#print(laser([4,2], 100, [0,7.071],[-1.4,-19.7]))       
#print(laser([1,2,1], 25, [0,0,5],[-1,-2,-1]))       

