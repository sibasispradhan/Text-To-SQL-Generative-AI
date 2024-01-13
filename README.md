# Text-To-SQL-Generative-AI
Test To SQL Generative AI

environment setup if not set the conda environment path in system
source /C/ProgramData/Anaconda3/etc/profile.d/conda.sh

## Step of running the application

conda create -p venv python=3.10 -y

conda activate venv/

pip install -r requirements.txt

python sqlite.py

streamlit run app.py

## Example for testing the app

give me the 2nd last rank student name form student table

## Deployed setup to test

https://huggingface.co/spaces/sibasispradhan/Text-To-SQL-Generative-AI
