# Imara: GenAI application development in Google Cloud

The Imara project showcases GenAI application development in Google Cloud, including:
* Tuning of Google and Hugging Face foundation models using Reinforcement Learning from Human Feedback (RLHF) in Vertex AI.
* Automating Continuous Integration (CI), Continuous Training (CT) and Continuous Delivery (CD) for machine learning. This automation streamlines the development and deployment processes, ensuring efficient and reliable model updates to deliver value to users more quickly.

## Setup

Before you begin, use the [setup](/docs/SETUP.md) guide to configure your project, service account, permissions, storage and more.

## Development

In machine learning domain, Jupyter notebooks provide a highly interactive environment for model development which supports iterative refinement of machine learning models.

### Development

This project provides several notebooks:
1. [Bison Notebook](text-bison-notebook.ipynb): demonstrates fine tuning a [PaLM 2 Text Bison] model from Vertex AI [Model Garden].
2. (Coming Soon) T5 Notebook: demonstrates fine tuning the [Text-To-Text Transfer Transformer] model from [Hugging Face].

The notebooks can be executed locally or on Vertex AI through either Vertex AI [Workbench] or [Colab Enterprise].

#### Vertex AI Workbench

* [Create][vertex-wb] a Vertex AI Workbench instance.
* [Clone][vertex-wb-git] this GitHub repository in your instance. 
* Open a notebook within your Vertex AI Workbench instance and execute the steps.

#### Colab Enterprise

TBD (will add the steps after testing it out)

## Automation

This project demonstrates Continuous Integration (CI), Continuous Training (CT) and Continuous Delivery (CD) to accelerate deployment of LLMs into production and value delivery of GenAI applications. 

### Google Cloud

This project uses a suite of Google Cloud products to facilitate CI/CT/CD of the [PaLM 2 Text Bison] model, including:
* [Cloud Build] for automating the pipeline.
* [Cloud Storage] for storing data.
* [Vertex AI] for fine tuning models.
* [Artifact Registry] for storing artifacts.
* [Cloud Deploy] for deploying models. 

Upon any code or data changes in this repository, Cloud Build triggers the execution of the [workflow](.cloudbuild/cloudbuild.yaml), ensuring efficient and reliable GenAI application development and delivery.

### GitHub Actions on Google Cloud

(Coming Soon)

This project uses [GitHub Actions] to facilitate CI/CT/CD of the [Text-To-Text Transfer Transformer] model from [Hugging Face], including:
* [GitHub Actions] for automating the workflow.
* [Cloud Storage] for storing data.
* [Vertex AI] for fine tuning models.
* [Artifact Registry] for storing artifacts.

[Model Garden]: https://cloud.google.com/vertex-ai/docs/start/explore-models
[Workbench]: https://cloud.google.com/vertex-ai/docs/workbench/introduction
[Colab Enterprise]: https://cloud.google.com/vertex-ai/docs/colab/create-console-quickstart
[Hugging Face]: https://huggingface.co/
[Text-To-Text Transfer Transformer]: https://huggingface.co/google-t5/t5-small 
[vertex-wb]: https://cloud.google.com/vertex-ai/docs/workbench/instances/create#consol
[vertex-wb-git]: https://cloud.google.com/vertex-ai/docs/workbench/instances/save-to-github#clone-a-repo
[Vertex AI]: https://cloud.google.com/vertex-ai
[Artifact Registry]: https://cloud.google.com/artifact-registry
[Cloud Build]: https://cloud.google.com/build
[Cloud Deploy]: https://cloud.google.com/deploy
[Cloud Storage]: https://cloud.google.com/storage
[PaLM 2 Text Bison]: https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text
[GitHub Actions]: https://docs.github.com/en/actions
