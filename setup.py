#!/usr/bin/env python3
"""
Medical Hub - פלטפורמה רפואית ישראלית
Setup script for the Medical Hub project
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="medical-hub",
    version="1.0.0",
    author="Medical Hub Team",
    author_email="contact@medical-hub.com",
    description="פלטפורמה רפואית ישראלית - Israeli Medical Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/medical_hub_full_project",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Natural Language :: Hebrew",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "prod": [
            "gunicorn>=20.0",
            "psycopg2-binary>=2.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "medical-hub=run:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords="medical, healthcare, israel, flask, python, medical-platform",
    project_urls={
        "Bug Reports": "https://github.com/YOUR_USERNAME/medical_hub_full_project/issues",
        "Source": "https://github.com/YOUR_USERNAME/medical_hub_full_project",
        "Documentation": "https://github.com/YOUR_USERNAME/medical_hub_full_project/wiki",
    },
)


