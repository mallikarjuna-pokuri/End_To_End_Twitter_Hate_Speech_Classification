from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    preprocessed_data_path: Path
    local_data_file: Path
    root_dir: Path
@dataclass(frozen=True)
class ModelTrainerConfig:
    train_data_path: Path
    model_path: Path
    root_dir: Path
@dataclass(frozen=True)
class ModelTrainerParmas:
    maxlen: int
    vocab_size: int
@dataclass(frozen=True)
class ModelEvaluateConfig:
    model_path: Path
    root_dir: Path
    test_data_path:Path