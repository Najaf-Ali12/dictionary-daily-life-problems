#9. Song Organizer:
#Develop a program that stores song titles, artists, 
#and genres in a dictionary. Include functions to sort by different criteria
#(title, artist, genre) and search for specific songs.
dictionary={
    "motivational":{},
    "romantic":{},
    "sad":{}
}
def romantic():
    for i in range(5):
        roman=input(f"enter the name of  romantic song {i+1}:")
        singer=input(f"enter the name of singer of {roman}:")
        dictionary["romantic"][roman]=singer
def sad():
    for i in range(5):
        sad=input(f"enter the name of sad song {i+1}:")
        singer=input(f"enter the name of singer of {sad}:")
        dictionary["sad"][sad]=singer
def motivational():
    for i in range(5):
        moti=input(f"enter the name of motivational song {i+1}:")
        singer=input(f"enter the name of singer of {moti}:")
        dictionary["motivational"][moti]=singer
romantic()
sad()
motivational()
print(dictionary)