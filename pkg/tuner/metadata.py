# Copyright 2024 Google. All Rights Reserved.
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

N_PREFERENCE_DATASET_EXAMPLES = 3000

N_REWARD_MODEL_TRAIN_EPOCHS = 30

N_PROMPT_DATASET_EXAMPLES = 2000

N_REINFORCEMENT_LEARNING_TRAIN_EPOCHS = 10

BATCH_SIZE = 64

PROMPT_SEQUENCE_LENGTH = 512

TARGET_SEQUENCE_LENGTH = 64

REWARD_MODEL_LEARNING_RATE_MULTIPLIER = 1.0

REINFORCEMENT_LEARNING_RATE_MULTIPLIER = 1.0

KL_COEFF = 0.1

INSTRUCTION = "Summarize in less than 50 words"

LARGE_MODEL_REFERENCE = "text-bison@001"

MODEL_DISPLAY_NAME = "rlhf-tuned-text-bison"

COMPILED_PIPELINE_PATH = "pipeline.yaml"

PIPELINE_REGISTRY = "rlhf-pipelines"

BUCKET_URI = "gs://rlhf-artifacts"

PIPELINE_ROOT = f"{BUCKET_URI}/rlhf"

PREFERENCE_DATASET=f"{BUCKET_URI}/data/preference/*.jsonl"

PROMPT_DATASET=f"{BUCKET_URI}/data/prompt/*.jsonl"

EVALUATION_DATASET=f"{BUCKET_URI}/data/evaluation/*.jsonl"

ENDPOINT_DISPLAY_NAME = f"{MODEL_DISPLAY_NAME}-endpoint"
