from pydantic import BaseModel

class DogsBreedSchema(BaseModel): # data validation before ingestion
    breed_name: str
    origin_country: str
    colors: str
    description: str
    avg_life_range: float
    avg_weight: float