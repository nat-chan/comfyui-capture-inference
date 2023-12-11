import numpy as np
from typing import Optional


class StatusManager:
    def __init__(self):
        self._capture_img: Optional[np.ndarray] = None
        self._result_img: Optional[np.ndarray] = None
        self._is_capturing: bool = False

    @property
    def is_capturing(self) -> bool:
        return self._is_capturing

    @property
    def capture_img(self) -> Optional[np.ndarray]:
        return self._capture_img

    @property
    def result_img(self) -> Optional[np.ndarray]:
        return self._result_img

    @capture_img.setter
    def capture_img(self, img: np.ndarray) -> None:
        self._capture_img = img

    @result_img.setter
    def result_img(self, img: np.ndarray) -> None:
        self._result_img = img

    def run_capture(self) -> None:
        self._is_capturing = True

    def stop_capture(self):
        self._is_capturing = False
