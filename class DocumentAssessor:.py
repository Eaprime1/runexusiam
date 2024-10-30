class DocumentAssessor:
    def __init__(self):
        self.pattern_matrix = PatternMatrix()
        self.essence_extractor = EssenceExtractor()
        self.legacy_analyzer = LegacyAnalyzer()
        
    def assess_document(self, document):
        patterns = self.pattern_matrix.analyze(document)
        essence = self.essence_extractor.extract(document)
        legacy_value = self.legacy_analyzer.evaluate(document)
        
        return MigrationProfile(
            patterns=patterns,
            essence=essence,
            legacy_value=legacy_value
        )