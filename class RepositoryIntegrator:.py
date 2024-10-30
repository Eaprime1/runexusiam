class RepositoryIntegrator:
    def __init__(self):
        self.structure_mapper = StructureMapper()
        self.path_generator = PathGenerator()
        self.format_converter = FormatConverter()
        
    def integrate_document(self, document, migration_profile):
        target_path = self.path_generator.determine_path(migration_profile)
        converted_format = self.format_converter.convert(document)
        return self.structure_mapper.place_document(
            converted_format, 
            target_path
        )