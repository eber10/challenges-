/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
#include<iostream>
#include<string>
using namespace std;
int main()
{
    string texto, resultado=" ";
    char normal[]="abcdefghijklmnopqrstuvwxyz0123456789";
    string leet[]={"4","8","[",")","3","v","9","#","eye","1","1<","7","[]v[]","/V","Q","?",
    "()_","[Z","$","+","(_)","|/","Щ","Ж","j",">_","o","L","Z","E","A","S","b","T","B","g"};
    cout<<"Ingrese un texto: "; getline(cin,texto);
    for(char c:texto)
    {
        char letra=tolower(c);
        bool encontrado=false;
        for(int i=0; i<36; i++)
        {
            if(normal[i]==letra)
            {
                resultado+=leet[i];
                encontrado=true;
            }
        }
        if(!encontrado)
        {
            resultado+=letra;
        }
    }
    cout<<resultado<<endl;
    return 0;
}