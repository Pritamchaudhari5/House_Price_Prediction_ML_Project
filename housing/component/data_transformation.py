from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact
import sys, os


class DataTransformation:

    def __init__(self, data_transformation_config: DataTransformationConfig,
                 data_ingestion_artifact: DataIngestionConfig,
                 data_validation_artifact: DataValidationConfig
                 ):
        try:
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e

        
