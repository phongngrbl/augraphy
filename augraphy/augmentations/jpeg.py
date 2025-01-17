import random
from typing import Tuple

import cv2
import numpy as np

from augraphy.base.augmentation import Augmentation


class Jpeg(Augmentation):
    """Uses JPEG encoding to create compression artifacts in the image.

    :param quality_range: Pair of ints determining the range from which to
           sample the compression quality.
    :param p: The probability that this Augmentation will be applied.
    """

    def __init__(
        self,
        quality_range: Tuple[int, int] = (25, 95),
        p: float = 1,
    ):
        """Constructor method"""
        super().__init__(p=p)
        self.quality_range = quality_range

    # Constructs a string representation of this Augmentation.
    def __repr__(self):
        return f"Jpeg(quality_range={self.quality_range}, p={self.p})"

    # Applies the Augmentation to input data.
    def __call__(self, image: np.ndarray, force: bool = False) -> np.ndarray:
        if force or self.should_run():
            image = image.copy()
            encode_param = [
                int(cv2.IMWRITE_JPEG_QUALITY),
                random.randint(self.quality_range[0], self.quality_range[1]),
            ]
            result, encimg = cv2.imencode(".jpg", image, encode_param)
            image = cv2.imdecode(encimg, 1)
            return image
