from early_fish_disease_detection import logger
from early_fish_disease_detection.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from early_fish_disease_detection.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from early_fish_disease_detection.pipeline.stage03_training import ModelTrainingPipeline
from early_fish_disease_detection.pipeline.stage04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info("*"*25)
    logger.info(f"Starting {STAGE_NAME}...")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training Stage"
try:
    logger.info("*"*25)
    logger.info(f"Starting {STAGE_NAME}...")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info("*"*25)
    logger.info(f"Starting {STAGE_NAME}...")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e