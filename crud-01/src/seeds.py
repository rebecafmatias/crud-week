def seed_dogs_breed():
    
    from databse import SessionLocal
    from models import DogsBreedModel

    dog_breed = [
        DogsBreedModel(
            breed_name= "Golden Retriever",
            origin_country= "Scotland",
            colors= "Golden, Cream",
            description= "Friendly, intelligent and devoted family dog.",
            avg_life_range= 11.0,
            avg_weight= 30.0
        ),
        DogsBreedModel(
            breed_name="French Bulldog",
            origin_country= "France",
            colors= "Fawn, Brindle, White, Cream",
            description= "Affectionate and calm, not tolerant of heat",
            avg_life_range= 11.5,
            avg_weight= 11.0
        ),
        DogsBreedModel(
            breed_name="German Shepherd",
            origin_country= "Germany",
            colors= "Black and Tan, Sable, Black",
            description= "Intelligent, protective, highly trainable working dog.",
            avg_life_range= 11.0,
            avg_weight= 32.0
        )
    ]
    session = SessionLocal()
    session.add_all(dog_breed) #add_all pois estou passando uma lista de registros pra inserir
    session.commit()