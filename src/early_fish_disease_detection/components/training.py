from early_fish_disease_detection.entity.configuration_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )


    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1./255,
        )

        # The size of images and batch size
        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        # Create the ImageDataGenerator for validation and training data
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        # Load the validation data from the 'test' directory
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data / 'test',  # Path to your 'test' folder
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            # Apply augmentation to training data
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            # If no augmentation, use same as validation
            train_datagenerator = valid_datagenerator

        # Load the training data from the 'train' directory
        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data / 'train',  # Path to your 'train' folder
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)


    def convert_to_tflite(self):
        converter = tf.lite.TFLiteConverter.from_keras_model(self.model)

        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        
        tflite_model = converter.convert()

        tflite_model_path = self.config.trained_model_path.with_suffix(".tflite")
        with open(tflite_model_path, 'wb') as f:
            f.write(tflite_model)
        print(f"Model successfully converted to TFLite and saved at {tflite_model_path}")


    
    def train(self, callback_list: list):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        # Save the trained model
        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )

        # Convert the model to TFLite after training
        self.convert_to_tflite()
