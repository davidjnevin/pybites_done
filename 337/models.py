from pydantic import BaseModel
from typing import Union

# write a Food pydantic model
class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: Union[float, None] = 0
