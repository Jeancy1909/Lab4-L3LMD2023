#1.Kukungama Kanyenge Nathan 
#2. Malu Mwanza Ariel 
#3. Makwaya Mawonda Mauricette 
#4. Senkere Afidou Jemima 
#5. Luayi Kangombo Jonas 
#6. Mubiala Kiesse Samuel 
#7. Ngamba Nkua-Mvibudulu Dave 
#8. Kabisayi Katambua Franklin 
#9. Nshole Mazana Obed 
#10. Shabani Bin Shabani Jeancy


### SECTION DE CONVERSION EN VALEUR ASCII (SUR 3 CHIFFRES)
def to_ascii_bin(p):
    p_ascii = ""
    for i in range(len(p)):
        p_ascii += '0'*(3-len(str(ord(p[i])))) + str(ord(p[i]))
# decoupage en segment de taille consecutive 
    s=[]
    i,j = int(1),int(0)
    while len(p_ascii)>j :
        s.append(p_ascii[j:j+i])
        j+=i
        i+=1
    
### SECTION DE CONVERSION EN BINAIRE (SUR 8 CHIFFRRES)

    b = []
    b.append(bin(int(s[0]))[2:])
    for i in range(1,len(s)):
        b.append('0'*(8-len(bin(int(s[i]))[2:])) + bin(int(s[i]))[2:])
    b = ''.join(map(str, b))
    return b

### SECTION DE COMPRESSION, COMPOSITION ET TRADUCTION DANS L'ALPHABET
def hashage(b):
    
    global alphabet
    global alph 
    global segment
    global taille 
    global encode 

## Mise en forme du texte(ajustement de la longueur)
    #Allonger la chaine
    while taille > len(b):     
        b = to_ascii_bin(b)

    # Compresser la chaine
    if len(b) > taille:       
        t = []
        j = int(0)
        while len(b)>j :
            t.append(b[j:j+taille])
            j+=taille

        n = len(t)
        m = taille - len(t[n-1])

        T = t0 = t[0]
        for v in range(1,n):
            i = n-v
            if i==n-1 : 
                # pourr le segment n'ayant pas la longuer voulu (taille)
                tx = str(t[i]) +str(t0[:m])
                T = bin(int(''.join(map(str, t[0])), 2) & int(''.join(map(str,  tx)), 2))[2:].zfill(4)
                T =''.join(map(str, T))
                
            else : 
                # pour les autres segments
                if i%2==0:
                    T = bin(int(''.join(map(str, T)), 2) & int(''.join(map(str,  t[i])), 2))[2:].zfill(4)
                else :
                    T = [int(bit) for bit in bin(int(''.join(map(str, T)), 2) ^ int(''.join(map(str, t[i])), 2))[2:].zfill(4)]
                T =''.join(map(str, T))
            
            if taille > len(T):
                # rajouter des 0 au debut pour garder la bonne taille
                vide = "0"*(taille-len(T))
                T =vide  + T

        T =''.join(map(str, T)) # pret pour traduction

    ## Conversion du code binaire vers l'alphabet

    # decoupage en segment de taille donnée
    k=[]
    j = int(0)
    while taille > j :
        k.append(T[j:j+segment])
        j+=segment
    # Conversion de binaire en int pour obtenir les indices
    u = []
    for i in range(encode):
        nb=0
        for j in range(segment):
            nb += (2**j)*int(k[i][j])
        u.append(int(nb))    

    # Traduction dans alphabet (valleur du segment % langueur alphabet = indice dans alphabet )
    chaine=[]
    for i in range(encode):
        chaine.append(alphabet[u[i]%alph])
    chaine = ''.join(map(str, chaine))

    return chaine


### PARAMETRAGE DE L'ALGO
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
alph = len(alphabet) # 62
segment = 7    # longueur de 62 en binaire
encode = 32 # taille de la sortie
taille = int(segment*encode*2) # taille du texte à depasser avant compression et traduction


### COODE PRINCIPAL
p=str(input('Chaine à hasher : '))    # Reception dde la chhaine
texte = hashage(to_ascii_bin(p))       # compression et traduction
print('texte hashé =',texte)
