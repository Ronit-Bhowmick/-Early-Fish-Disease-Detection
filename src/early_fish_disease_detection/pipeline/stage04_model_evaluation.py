from early_fish_disease_detection.config.config import ConfigurationManager
from early_fish_disease_detection.components.evaluation import Evaluation
from early_fish_disease_detection import logger



STAGE_NAME = "Evaluation Stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logger.info("*"*25)
        logger.info(f"Starting {STAGE_NAME}...")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed.")
    except Exception as e:
        logger.exception(e)
        raise e