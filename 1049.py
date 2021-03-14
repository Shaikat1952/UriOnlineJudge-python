x=input()
y=input()
z=input()
main='vertebrado'
one='ave'
two='mamifero'
three='carnivoro'
four='onivoro'
five='onivoro'
six='herbivoro'
main1='invertebrado'
one1='inseto'
two2='anelideo'
three3='hematofago'
four4='herbivoro'
five5='hematofago'
six6='onivoro'
if(x==main and y==one and z==three):
    output='aguia'
elif(x==main and y==one and z==four):
    output='pomba'
elif(x==main and y==two and z==five):
    output='homem'
elif(x==main and y==two and z==six):
    output='homem'
elif(x==main1 and y==one1 and z==three3):
    output='pulga'
elif(x==main1 and y==one1 and z==four4):
    output='lagarta'
elif(x==main1 and y==two2 and z==five5):
    output='sanguessuga'
elif(x==main1 and y==two2 and z==six6):
    output='minhoca'
print(output)