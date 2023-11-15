from src.constants import *
import os
from src.utils.common import read_yaml,create_directories
from src.entity.config_entity import DataIngestionConfig,DataTransformationConfig,\
                                    ModelTrainerConfig,ModelTrainerParmas,ModelEvaluateConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        data_ingestion_config = DataTransformationConfig(
            root_dir=config.root_dir,
            preprocessed_data_path=config.preprocessed_data_path,
            local_data_file=config.local_data_file,
        )

        return data_ingestion_config
    def model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            model_path = config.model_path
        )
        return model_trainer_config
    def model_trainer_params(self) ->ModelTrainerParmas:
        params = self.params.model_trainer_params
        model_trainer_params = ModelTrainerParmas(
            maxlen = params.maxlen,
            vocab_size= params.vocab_size
        )
        return model_trainer_params
    def model_evaluate_config(self) -> ModelEvaluateConfig:
        config = self.config.model_evaluate
        model_evaluate_config = ModelEvaluateConfig(
            model_path = config.model_path,
            root_dir= config.root_dir,
            test_data_path= config.test_data_path
        )
