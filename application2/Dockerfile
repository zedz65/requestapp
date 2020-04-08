FROM python:3.6
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]
COPY . .

#from python with version
#working directory called /app
#copy the requirements.txt . to our working directory with .
#run pip3 install -r means recursively/everything
#entrypoint is the location of the python executable and then run app.py
#copy everything into the working directory using . .
