from pathlib import Path
from early_fish_disease_detection.entity.configuration_entity import EvaluationConfig
from early_fish_disease_detection.utils.common import save_json
import tensorflow as tf


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1./255,
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )


        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=Path(self.config.training_data) /'test',  # Path to the 'test' folder
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)


    def evaluation(self):
        self.model = self.load_model(self.config.model_path)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)


    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(Path("scores.json"), data=scores)