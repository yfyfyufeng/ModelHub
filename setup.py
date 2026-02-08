# Copyright 2021 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import find_packages, setup


extras = {}
extras["quality"] = ["ruff == 0.13.1"]

extras["docs"] = []
extras["test_prod"] = ["pytest>=7.2.0", "pytest-xdist", "pytest-subtests", "parameterized", "pytest-order"]
extras["test_dev"] = [
    "datasets",
    "diffusers",
    "evaluate",
    "torchdata>=0.8.0",
    "torchpippy>=0.2.0",
    "transformers",
    "scipy",
    "scikit-learn",
    "tqdm",
    "bitsandbytes",
    "timm",
]
extras["testing"] = extras["test_prod"] + extras["test_dev"]
extras["deepspeed"] = ["deepspeed"]
extras["rich"] = ["rich"]

extras["test_fp8"] = ["torchao"]  # note: TE for now needs to be done via pulling down the docker image directly
extras["test_trackers"] = [
    "wandb",
    "comet-ml",
    "tensorboard",
    "dvclive",
    # "mlflow", too many deps that lead to download a very old version of the lib
    "matplotlib",
    "swanlab[dashboard]",  # dashboard required for local use
    "trackio",
]
extras["dev"] = extras["quality"] + extras["testing"] + extras["rich"]

extras["sagemaker"] = [
    "sagemaker",  # boto3 is a required package in sagemaker
]

setup(
    name="accelerate",
    version="1.13.0.dev0",
    description="Accelerate",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="deep learning",
    license="Apache",
    author="The Hugging Face team",
    author_email="transformers@huggingface.co",
    url="https://github.com/huggingface/accelerate",
    package_dir={"": "src"},
    packages=find_packages("src"),
    entry_points={
        "console_scripts": [
            "accelerate=accelerate.commands.accelerat
... (truncated for brevity) ...