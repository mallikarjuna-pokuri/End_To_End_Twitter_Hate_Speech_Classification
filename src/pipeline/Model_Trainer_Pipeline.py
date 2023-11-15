import sys
from config.configuration import ConfigurationManager
from components.model_trainer import ModelTrainer
import logger




STAGE_NAME = "Model Trainer stage"

class MOdelTrainerPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        model_trainer_config = config.model_trainer_config()
        model_trainer_params = config.model_trainer_params()
        model_trainer = ModelTrainer(config=model_trainer_config,params=model_trainer_params)
        model_trainer.run()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = MOdelTrainerPipeline()
        obj.run()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e