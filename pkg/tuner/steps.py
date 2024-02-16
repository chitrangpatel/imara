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

import math
from pkg.tuner import metadata

def get_reward_model_train_steps() -> int:
    """Calculates the reward model train steps.

    This depends on the size of your "comparison dataset".
    Usually, the model should train over the comparison dataset for 20-30 times for best results.

    Returns:
        int:  reward model train steps
    """
    reward_model_train_steps = math.ceil(
        metadata.N_PREFERENCE_DATASET_EXAMPLES * metadata.N_REWARD_MODEL_TRAIN_EPOCHS / metadata.BATCH_SIZE
    )
    print(f"{reward_model_train_steps=}")
    return reward_model_train_steps

def get_reinforcement_learning_train_steps() -> int:
    """Calculates the reinforcement learning training steps.

    This depends on the size of your prompt dataset.
    Usually, the model should train over the prompt dataset for roughly 10-20 times, but beware,
    if given too many training steps, the policy model may figure out a way exploit the reward
    and exhibit undesired behavior (i.e. "reward hacking").

    Returns:
        int: reinforcement learning training steps
    """
    reinforcement_learning_train_steps = math.ceil(
        metadata.N_PROMPT_DATASET_EXAMPLES * metadata.N_REINFORCEMENT_LEARNING_TRAIN_EPOCHS / metadata.BATCH_SIZE
    )
    print(f"{reinforcement_learning_train_steps=}")
    return reinforcement_learning_train_steps
