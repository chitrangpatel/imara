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

from kfp.registry import RegistryClient

def upload(
    project_id: str,
    region: str,
    pipeline_registry: str,
    compiled_pipeline_path: str
) -> str:
    """_summary_

    Args:
        project_id (str): _description_
        region (str): _description_
        pipeline_registry (str): _description_
        compiled_pipeline_path (str): _description_

    Returns:
        str: _description_
    """
    
    PIPELINE_REGISTRY_URI = f"https://{region}-kfp.pkg.dev/{project_id}/{pipeline_registry}" # @param {type:"string"}
    print("Vertex AI Pipeline Registry:", PIPELINE_REGISTRY_URI)

    client = RegistryClient(
        host=PIPELINE_REGISTRY_URI
    )

    PIPELINE_TEMPLATE_NAME, PIPELINE_TEMPLATE_VERSION = client.upload_pipeline(
        file_name=compiled_pipeline_path,
        tags=["latest"],
        extra_headers={"description":"This is the RLHF Pipeline Template."}
    )

    PIPELINE_TEMPLATE_URI = f"{PIPELINE_REGISTRY_URI}/{PIPELINE_TEMPLATE_NAME}/{PIPELINE_TEMPLATE_VERSION}"
    print("RLHF Pipeline Template:", PIPELINE_TEMPLATE_URI)
    
    return PIPELINE_TEMPLATE_URI
