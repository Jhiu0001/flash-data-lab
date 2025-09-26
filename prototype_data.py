from faker import Faker
import pandas as pd
import random

class PrototypeData:
    """
    A helper class for generating mock datasets using Faker.
    Extend with new methods as needed.
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

    def fake_name(self) -> str:
        """Generate a fake full name."""
        return self.faker.name()

    def fake_address(self) -> str:
        """Generate a fake address."""
        return self.faker.address()
 
    def fake_email(self) -> str:
        """Generate a fake email address."""
        return self.faker.email()

