from .generic_repository import GenericRepository
from src.abstract_types.object_types import Animal, Thing

class InventoryRepository(GenericRepository[Animal | Thing]):
    pass
