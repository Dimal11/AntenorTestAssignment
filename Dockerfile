FROM python:3.13-slim

RUN apt-get update && apt-get install -y wget unzip openjdk-21-jre-headless curl gnupg && rm -rf /var/lib/apt/lists/*

ENV ALLURE_VERSION=2.35.1
RUN wget https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz && \
    tar -zxvf allure-${ALLURE_VERSION}.tgz -C /opt/ && \
    ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure && \
    rm allure-${ALLURE_VERSION}.tgz

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps

COPY . .

CMD ["bash", "-c", "pytest tests/test.py --alluredir=allure-results && allure generate allure-results --clean -o allure-report && echo 'Allure report generated: http://localhost:8080' && python3 -m http.server 8080 --directory allure-report"]
