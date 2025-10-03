from faker import Faker
import pandas as pd
import numpy as np
import random

class PrototypeData:
    """
    A helper class for generating mock datasets using Faker.
    """

    def __init__(self, locale: str = "en_US", seed: int | None = None):
        """
        Initialize the faker instance.

        Args:
            locale (str): Locale for generating data (default: en_US).
            seed (int | None): Optional seed for reproducibility.
        """
        self.faker = Faker(locale)
        if seed is not None:
            Faker.seed(seed)
            random.seed(seed)

    def fake_choice(self, choices: list[str], probs: list[float] | None = None) -> str:
        if not choices:
            raise ValueError("choices list cannot be empty.")

        if probs is not None:
            if len(probs) != len(choices):
                raise ValueError("Length of probs must match length of choices.")
            if not np.isclose(sum(probs), 1.0):
                raise ValueError("Probabilities must sum to 1.")
        else:
            # Assign equal probability if none provided
            probs = [1 / len(choices)] * len(choices)

        return np.random.choice(choices, p=probs)


    def fake_name(self, sex: str | None = None) -> str:
        if sex == "M":
            return self.faker.name_male()
        elif sex == "F":
            return self.faker.name_female()
        else:
            return self.faker.name()

    def fake_address(self) -> str:
        return self.faker.address()
 
    def fake_email(self) -> str:
        return self.faker.email()

    def generate_distribution(
        self,
        dist_type: str,
        size: int,
        mean: float | None = None,
        sigma: float = 1,
        loc: float = 0,
        scale: float = 1,
        max_value: float | None = None,
        target_mean: float | None = None,
        ) -> np.ndarray:
        """
        Generate synthetic data with different distribution shapes.

        Args:
            dist_type (str): "normal", "right-skew", or "left-skew".
            size (int): Number of samples.
            mean (float): Mean (used for lognormal).
            sigma (float): Sigma for lognormal (right-skew).
            loc (float): Mean for normal.
            scale (float): Std deviation for normal.
            max_value (float): Max value (used in left-skew).
            target_mean (float): Scale output to this mean if given.

        Returns:
            np.ndarray: Generated values.
        """
        if dist_type == "normal":
            data = np.random.normal(loc=loc, scale=scale, size=size)

        elif dist_type == "right-skew":
            data = np.random.lognormal(mean=mean, sigma=sigma, size=size)

        elif dist_type == "left-skew":
            raw = np.random.lognormal(mean=mean, sigma=sigma, size=size)
            if max_value is None:
                raise ValueError("max_value must be provided for left-skew")
            data = max_value - (raw / raw.max() * max_value)

        else:
            raise ValueError("dist_type must be 'normal', 'right-skew', or 'left-skew'")

        if target_mean is not None:
            data = data / data.mean() * target_mean

        return data