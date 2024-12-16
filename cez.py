def cezars(text, shift, mode="encrypt"): # kādi paramteri mums nepieciešams
    """
     :parametrs text: tekts -->šifrējam vai atšifrējam
     :parametrs shift: pozitīvs skaitlis - kā veidojas nobīde M 1 L
     :parametrs mode: 'encrypt' -šifrējam (kodējam), 'decrypt' - atšifrējam
     : return: kodēts vai dekodēts teksts
    """
    if mode=='decrypt':
        shift=shift
    rezultats=''

    for char in text:
        if char.isalpha():
            # pārbaudīt, vai burts ir liels vai mazs
            start=ord('A') if char.isupper() else ord('a')
            # aprēķina jauno burtu
            jauns_burts=chr((ord(char)-start+shift)%26+start)
            rezultats+=jauns_burts
        else:
            # Ja nav burts, jāpievieno simbols nemainot!
            rezultats+=char
    return rezultats


# piemērs
org_teksts="Sveika, pasaule!"
solis=3

# šifrēsim
shifreet=cezars(org_teksts,solis,mode="encrypt")
print("\u1060ifrēts teksts: ",shifreet)

# atšifrēsim
at_shifreet=cezars(org_teksts,solis,mode="decrypt")
print("\u1060ifrēts teksts: ",at_shifreet)