from typing import List
from typing import Tuple

import numpy as np

from augraphy.base.augmentation import Augmentation


class AugmentationSequence(Augmentation):
    """A list of Augmentations to be applied sequentially.

    :param augmentations: A list of Augmentation objects to be applied.
    :param p: The probability that this Augmentation will be applied.
    """

    def __init__(self, augmentations: List[Augmentation], p: float = 1):
        """Constructor method"""
        self.augmentations = augmentations
        self.p = p
        self.results = []

    def __repr__(self):
        output = "AugmentationSequence([\n"
        for aug in self.augmentations:
            output += f"\t{repr(aug)},\n"

        output += "])"
        return output

    def __call__(self, image: np.ndarray, force: bool = False) -> Tuple[np.ndarray, List[Augmentation]]:
        if force or self.should_run():
            result = image
            for augmentation in self.augmentations:
                if isinstance(result, tuple):
                    result = result[0]
                current_result = augmentation(result)
                self.results.append(current_result)
                result = current_result

            return result, self.augmentations
