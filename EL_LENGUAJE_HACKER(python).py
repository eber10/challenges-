"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 """
normal="abcdefghijklmnopqrstuvwxyz0123456789"
leet=["4","8","[",")","3","v","9","#","eye","1","1<","7","[]v[]","/V","Q","?",
    "()_","[Z","$","+","(_)","|/","Щ","Ж","j",">_","o","L","Z","E","A","S","b","T","B","g"]
texto=input("Ingrese un texto: ")
resultado=" "
for c in texto:
    letra=c.lower()
    encontrado=False
    for i in range(36):
        if normal[i]==letra:
            resultado+=leet[i]
            encontrado=True
    if not encontrado:
        resultado+=letra
print(resultado)