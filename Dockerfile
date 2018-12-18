FROM openjdk:8-jdk-alpine
WORKDIR /usr/src/app
COPY . .
EXPOSE 3001
CMD alias python=python3
CMD wget https://bootstrap.pypa.io/get-pip.py
CMD python get-pip.py
CMD pip install pandas numpy datetime os calendar
CMD python prepare_data/src/process_data.py
CMD java -jar target/*.jar
