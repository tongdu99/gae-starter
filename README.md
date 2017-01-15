# gae-starter
A starter project for google app engine based on python and flask

# install packages into lib folder
pip install -t lib -r requirements.txt
# install packages to current virtual environment
pip install -r requirements.txt

# setup/run selenium server
java -jar selenium-server-standalone-3.0.1.jar 

# mv chromedriver
mv chromedriver /usr/local/bin

# set default google cloud project
gcloud config set project [project-id]
