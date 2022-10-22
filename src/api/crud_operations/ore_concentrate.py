from src.api.crud_operations.base_crud_operations import ModelOperation
from src.api.models.ore_concentrate import OreConcentrateModel


class OreConcentrateOperation(ModelOperation):
    def __init__(self, db):
        self.model = OreConcentrateModel
        self.model_name = 'ore_concentrate'
        self.db = db
