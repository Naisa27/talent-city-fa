

class DataMapper:
    db_model = None
    schema = None

    # превращение модели в схему
    @classmethod
    def map_to_domain_entity( cls, data ):
        return cls.schema.model_validate(data, from_attributes=True)

    # превращение схемы в модель
    @classmethod
    def map_to_persistence_entity( cls, data ):
        return cls.db_model(**data.model_dump())
