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

from pkg.tuner import metadata

def get_values(
    preference_dataset: str,
    prompt_dataset: str,
    eval_dataset: str,
    reward_model_train_steps: int,
    reinforcement_learning_train_steps: int
) -> dict:
    """_summary_

    Args:
        preference_dataset (str): _description_
        prompt_dataset (str): _description_
        reward_model_train_steps (int): _description_
        reinforcement_learning_train_steps (int): _description_

    Returns:
        dict: _description_
    """
     
    values = {
        "preference_dataset": preference_dataset,
        "prompt_dataset": prompt_dataset,
        "eval_dataset": eval_dataset,
        "large_model_reference": metadata.LARGE_MODEL_REFERENCE,
        "model_display_name": metadata.MODEL_DISPLAY_NAME,
        "reward_model_train_steps": reward_model_train_steps,
        "reinforcement_learning_train_steps": reinforcement_learning_train_steps,
        "prompt_sequence_length": metadata.PROMPT_SEQUENCE_LENGTH,
        "target_sequence_length": metadata.TARGET_SEQUENCE_LENGTH,
        "reward_model_learning_rate_multiplier": metadata.REWARD_MODEL_LEARNING_RATE_MULTIPLIER,
        "reinforcement_learning_rate_multiplier": metadata.REINFORCEMENT_LEARNING_RATE_MULTIPLIER,
        "kl_coeff": metadata.KL_COEFF,
        "instruction": metadata.INSTRUCTION,
    }

    return values
