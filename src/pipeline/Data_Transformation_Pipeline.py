from src.config.configuration import ConfigurationManager
from src.components.data_Transformation import DataTransformation
from logger import logging


class DataTransformationPipeline:
    def __init__(self) -> None:
        pass
    def run(self):
        config = ConfigurationManager()
        DataTransformationConfig = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = DataTransformationConfig)
        data_transformation.transform_data()

  
STAGE_NAME = "Data Ingestion stage"


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.run()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e