from early_fish_disease_detection.config.config import ConfigurationManager
from early_fish_disease_detection.components.prepare_callbacks import PrepareCallbacks
from early_fish_disease_detection.components.training import Training
from early_fish_disease_detection import logger

STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()


        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )


if __name__ == '__main__':
    try:
        logger.info("*"*25)
        logger.info(f"Starting {STAGE_NAME}...")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed.")
    except Exception as e:
        logger.exception(e)
        raise e