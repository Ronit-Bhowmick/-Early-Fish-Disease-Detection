from early_fish_disease_detection import logger
from early_fish_disease_detection.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from early_fish_disease_detection.pipeline.stage02_prpare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion"

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