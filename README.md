# ML Zoomcamp Midterm Project: Credit Card Approval Prediction

This repository is for the ML Zoomcamp course Midterm Project by Alexey Grigorev. You can enroll in this course for free via the following link: http://mlzoomcamp.com/

## Table of Contents
* [1. About the Project](#about-project)
* [2. Directory Explained](#directory-explained)
* [3. Train the Model](#train-model)
* [4. Run the Model as Flask Web Service](#deploy-model)
* [5. Deploy Model as Docker Container](#docker-model)

<a id='about-project'></a>
## 1. About the Project

Credit card approval prediction models are used by financial institutions to assess the risk of approving a credit card application. These models typically take into account a variety of factors, including the applicant's credit history, income, employment status, and debt-to-income ratio. By predicting the likelihood of an applicant defaulting on their credit card payments, these models can help financial institutions make more informed decisions about who to approve for a credit card.

There are a number of different machine learning algorithms that can be used to build credit card approval prediction models. Some of the most popular algorithms include logistic regression, random forests, and gradient boosted trees. These algorithms work by analyzing historical data on credit card applications and defaults to identify patterns that can be used to predict the likelihood of an applicant defaulting.

Credit card approval prediction models can be a valuable tool for financial institutions. By helping to identify high-risk applicants, these models can help financial institutions reduce their risk of losses. Additionally, these models can help financial institutions make more fair and equitable credit decisions.

<a id='directory-explained'></a>
## 2. Directory Explained

**Python package dependencies**
>* For this project, I used `pipenv` for package dependencies and virtual environment.

**Data Directory**
>* `data/Credit_card_label.csv` and `data/Credit_card.csv` are the raw data before I transformed them into clean data. The dataset I used for modeling is `data/clean_data.csv`.

**Notebook Directory**
>* I placed my Jupyter notebook file in this directory. In this notebook file `notebook.ipynb`, I prototype my model, perform data cleansing and EDA.

**Model Training**
>* `train.py`: is the python file that i used for training the model and save the model as binary file.

**Deploy model with Flask**
>* `predict-flask.py`: prediction model deployed as flask web service.
>* `request-flask.py`: script to make post method in flask web service and the result of this file is predicition.
>* `randomforest.bin`: is the model that i used in this project. 

<a id='train-model'></a>
## 3. Train the Model
You can train the model by using this step:

1. Clone this repo (if you have not done already)
    ```
    git clone https://github.com/gitbarok/mlzoomcamp-midterm.git
    ```
after you clone the repo, move to the directory with:
    ```
    cd mlzoomcamp-midterm/
    ```
2. Run virtual environment:
- If you don't have `pipenv yet``, install it with this, if you already have it, you can skip this step
    ```
    pip3 install pipenv
    ```
- Run this command if you already have `pipenv`` installed on your machine to install all dependencies for this project:
    ```
    pipenv sync
    ```
- After running `pipenv sync`, activate the virtual environment:
    ```
    pipenv shell
    ```
3. Run the train script to train the model and export it as a binary file:
    ```
    python3 train.py
    ```

<a id='deploy-model'></a>
## 4. Run the Model as Flask Web Service
To run this, you need two separate terminals: one for running Flask and another for making requests to Flask.
- In terminal 1, run the following command to start the Flask Web Service:
    ```
    python3 predict-flask.py
    ```
- In another terminal, use the following command to make a prediction from the model you trained earlier:
    ```
    python3 request-flask.py
    ```
<a id='docker-model'></a>
## 5. Deploy Model as Docker Container
You can deploy Flask web server with model running inside docker container.

ps. you should have Docker installed and running on your local machine:

You can follow this steps to do this:
1. Clone this repo
2. Change the directory to this repo
3. Build docker image with this command

    ```
    docker build -t credit-card-approval
    ```
4. Create docker container from the image that you've build befor with this command
    ```
    docker run -p 9696:9696 -d credit-card-approval
    ```
5. Check whether docker container running with this command:
    ```
    docker ps -a
    ```
6. Run the script `flask-request.py` to send a request to flask web service running inside container
    ```
    python3 flask-request.py
    ```