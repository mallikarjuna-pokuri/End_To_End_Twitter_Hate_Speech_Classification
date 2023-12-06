# End_To_End_Twitter_Hate_Speech_Classification
This repository contains the source code and configurations for the continuous integration and continuous deployment (CI/CD) pipeline of the Twitter Hate Speech Detection project. The pipeline is built using Amazon Elastic Container Registry (ECR), Amazon EC2, and GitHub Actions.



## Continuous Integration

The continuous integration process is triggered whenever changes are pushed to the main branch of this repository. GitHub Actions is used to build, test, and package the application into a Docker image.

### GitHub Actions Workflow

The GitHub Actions workflow file (`./.github/workflows/main.yml`) defines the steps of the CI process:

- **Build**: The application code is built inside a Docker container.
- **Test**: Unit tests and integration tests are executed to ensure code quality.
- **Package**: The application is packaged into a Docker image.

## Continuous Deployment

The continuous deployment process is triggered when a new Docker image is pushed to the Amazon ECR repository. An Amazon EC2 instance is used to deploy the application from the Docker image.

### Deployment Workflow

The deployment process is defined in the deployment workflow file (`./.github/workflows/main.yml`):

- **Push to ECR**: The Docker image is pushed to the Amazon ECR repository.
- **Deploy to EC2**: An Amazon EC2 instance is updated with the latest Docker image.

## Setup Instructions

To set up the CI/CD pipeline for your environment, follow these steps:

1. **GitHub Actions Secrets**: Add the necessary secrets to your GitHub repository for AWS access.
2. **Amazon ECR**: Create an Amazon ECR repository to store your Docker images.
3. **Amazon EC2**: Set up an Amazon EC2 instance for deployment and configure it to pull the Docker image from the ECR repository.

## Configuration

Adjust the configuration files and scripts in the repository based on your project's specific requirements.
## Project Overview

Welcome to the Twitter Hate Speech Classification project! This project aims to build a robust and efficient system for identifying hate speech on Twitter. Hate speech detection is crucial for maintaining a safe and inclusive online environment.

## Introduction
Hate speech on social media platforms, especially Twitter, is a growing concern. This project focuses on developing a machine learning model to automatically classify tweets into categories like hate speech, offensive language, or non-offensive. The end-to-end process includes data preprocessing, model training, and evaluation.

## Project Structure

- **Data Ingestion**: In this module, data is collected and ingested into the system for further processing.

- **Data Transformation**: The ingested data undergoes preprocessing and transformation to prepare it for model training. This step ensures the data is in a suitable format for the machine learning pipeline.

- **Model Training**: TensorFlow is utilized to train a hate speech classification model. The model is trained on the preprocessed data, techniques in natural language processing.

- **Model Evaluation**: Once trained, the model is evaluated using a separate dataset to assess its performance and accuracy in classifying hate speech on Twitter.

- **FastAPI Backend**: The backend is built with FastAPI, providing a robust and efficient server for handling requests and interacting with the machine learning model.

- **Web Application (HTML, CSS, JavaScript)**: The frontend provides a user-friendly interface for interacting with the hate speech classification system. Users can input tweets, and the system will classify them using the trained model.

- **Docker Integration**: The entire system is containerized using Docker, ensuring easy deployment and scalability.


## Installation
To set up the project locally, follow these steps:

```bash
git clone https://github.com/mallikarjuna-pokuri/End_To_End_Twitter_Hate_Speech_Classification.git
cd End_To_End_Twitter_Hate_Speech_Classification
python -m venv .venv # create virtual environment
pip install -r requirements.txt
```

You can run the project using the below command
```bash
uvicorn app:app --reload
```
## Access the Application:

Open your web browser and navigate to http://localhost:8000 to interact with the hate speech classification system.

## Contributing
Contributions are welcome! Follow these steps to contribute:


1. Fork the repository
2. Create a new branch (git checkout -b feature/improvement)
3. Make changes and commit (git commit -am 'Add feature')
4. Push to the branch (git push origin feature/improvement)
5. Create a pull request

### Note: You can change the configuration of the project using config.yaml
## License
This project is licensed under the MIT License.

Feel free to reach out to mallikarjunapokuri595@gmail.com for any questions or concerns.

Happy coding! 🚀
