"""Example module for the demo package"""

from .logger_config import logger


def hello_world(message):
    """Example function to say Hello world with a message"""
    logger.debug("This is DEBUG level log message")
    logger.info("This is INFO level log message")
    logger.warning("This is WARN level log message")
    logger.error("This is ERROR level log message")
    return f"Hello world!: {message}"

def describe_numbers(numbers: list[float]) -> dict:
    """Calculate descriptive statistics for a list of numbers."""
    import statistics
    import math

    if len(numbers) < 2:
        raise ValueError("At least two numbers are required.")

    if not all(math.isfinite(x) for x in numbers):
        raise ValueError("All numbers must be finite.")

    return {
        "Count": len(numbers),
        "Mean": statistics.mean(numbers),
        "Median": statistics.median(numbers),
        "Sample Variance": statistics.variance(numbers),
        "Sample Std Dev": statistics.stdev(numbers),
        "Minimum": min(numbers),
        "Maximum": max(numbers),
        "Range": max(numbers) - min(numbers),
    }
