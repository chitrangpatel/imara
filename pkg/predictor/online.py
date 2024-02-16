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

import json
from pkg.predictor import configuration
from google.cloud import aiplatform

def send(
    resource: str,
    prompt: str
):
    """_summary_

    Args:
        resource (str): _description_
        prompt (str): _description_

    Returns:
        str: _description_
    """    
    endpoint = aiplatform.Endpoint(resource)
    prediction = endpoint.predict(
        instances=[
            {"content": prompt}
        ],
        parameters=configuration.PARAMETERS
    )
    print(json.dumps(prediction[0][0], sort_keys=True, indent=4))
