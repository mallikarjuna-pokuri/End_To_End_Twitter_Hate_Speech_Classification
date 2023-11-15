from src.components.model_evaluate import ModelEvaluate
import logger
from config.configuration import ConfigurationManager

STAGE_NAME = "Model Trainer stage"

class MOdelEvaluatePipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        model_evaluate_config = config.model_evaluate_config()
        model_evaluate = ModelEvaluate(config=model_evaluate_config)
        model_evaluate.run()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = MOdelEvaluatePipeline()
        obj.run()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e