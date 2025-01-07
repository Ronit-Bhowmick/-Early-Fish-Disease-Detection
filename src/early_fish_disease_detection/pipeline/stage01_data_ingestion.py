from early_fish_disease_detection.config.config import ConfigurationManager
from early_fish_disease_detection.components.data_ingestion import DataIngestion
from early_fish_disease_detection import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_file()



if __name__ ==  '__main__':
    try:
        logger.info(f"Starting {STAGE_NAME}...")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed.")
    except Exception as e:
        logger.exception(e)
        raise e