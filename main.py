import fiftyone as fo
import os

#This program load dastaset from directory, and open fiftyone app program

def load_dataset(load_dir: str, dataset_name: str, dataset_type=None, max_samples=None) -> fo.Dataset:
    dataset_path = os.path.join(load_dir, dataset_name)
    if not dataset_type:
        dataset_type = fo.types.COCODetectionDataset

    try:
        print(f"Loading dataset: {dataset_name} from dir: {dataset_name}")
        dataset = fo.Dataset.from_dir(
            dataset_path,
            max_samples=max_samples,
            dataset_type=dataset_type,
        )
    except:
        print(f"Unable load dataset from: {dataset_path}")
        return None
    return dataset


if __name__ == "__main__":
    main_dir = os.curdir
    name = "scenes_dataset"
    max_samples = 1000
    dataset = load_dataset(load_dir=main_dir, dataset_name=name, max_samples=max_samples)

    if dataset:
        session = fo.launch_app(dataset)
        session.wait()
