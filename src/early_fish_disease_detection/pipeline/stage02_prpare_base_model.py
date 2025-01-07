from early_fish_disease_detection.config.config import ConfigurationManager
from early_fish_disease_detection.components.base_model import PrepareBaseModel
from early_fish_disease_detection import logger


STAGE_NAME = 'Prepare Base Model'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info("*"*25)
        logger.info(f"Starting {STAGE_NAME}...")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed.")
    except Exception as e:
        logger.exception(e)
        raise e
