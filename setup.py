from setuptools import setup, find_packages

setup(
    name="image-sanitizer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tensorflow",
        "numpy",
        "Pillow",
        "requests",
    ],
    author="Your Name",
    description="Image moderation tool to filter NSFW and violent images",
    url="https://github.com/yourusername/image-sanitizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
