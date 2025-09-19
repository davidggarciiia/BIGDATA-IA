class Pelicula:
    def __init__(self, nombre: str, edad: int, genero: str, ano_lanzamiento: int, plataforma: str, clasificacion: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ano_lanzamiento = ano_lanzamiento
        self.plataforma = plataforma
        self.clasificacion = clasificacion


def clasificadorEdadPelicula():
    pelicula1 = Pelicula("Inception", 13, "Ciencia Ficción", 2010, "Netflix")
    pelicula2 = Pelicula("Toy Story", 0, "Animación", 1995, "Disney+")
    pelicula3 = Pelicula("The Godfather", 18, "Crimen", 1972, "Amazon Prime")
    pelicula4 = Pelicula("Parasite", 16, "Drama", 2019, "HBO Max")
    pelicula5 = Pelicula("Spider-Man: No Way Home", 12, "Acción", 2021, "Disney+")

    for peli in peliculas:
            if peli.edad >= 0:
                peli.clasificacion = "infantil"
            elif peli.edad >= 7:
                peli.clasificacion = "familiar"
            elif peli.edad >= 13:
                peli.clasificacion = "acción"
            elif peli.edad >= 18:
                peli.clasificacion = "comedia"




                 
    #Crear lista de peliculas
    peliculas = [pelicula1, pelicula2, pelicula3, pelicula4, pelicula5]

    edad_persona=int(input("Por favor, introduce tu edad en años:"))

    #Si la edad de la persona
    if edad_persona >=0:
        print("Puedes ver las siguientes peliculas: ")
        #Recorres la lista peliculas y comparas si la edad minima de la pelicula es <= edad de la persona, que la imprima
        for peli in peliculas:
            if peli.edad <= edad_persona:
                print(peli.nombre)
