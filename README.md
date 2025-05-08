# AIOps Observability PoC

Esta PoC (Prova de Conceito) demonstra como implementar uma arquitetura de Observabilidade com Inteligência Artificial (AIOps) utilizando ferramentas open source.

## Objetivo

Integrar logs, métricas e traces com machine learning para:
- Detectar anomalias
- Visualizar dados em tempo real
- Automatizar respostas com scripts

---

## 🔧 Requisitos

Certifique-se de ter instalado:

- [Docker e Docker Compose](https://docs.docker.com/get-docker/)
- Python 3.10+
- Java 11+ (para Logstash)
- Elasticsearch e Grafana (podem rodar via Docker)

---

## 🚀 Subindo o Ambiente

1. **Clone o repositório**
```bash
git clone https://github.com/seuusuario/aiops-observability-poc.git
cd aiops-observability-poc
```

2. **Suba Elasticsearch e Grafana via Docker**
Crie um arquivo `docker-compose.yml` com:

```yaml
version: '3.7'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.12.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports:
      - 9200:9200

  grafana:
    image: grafana/grafana
    ports:
      - 3000:3000
```

```bash
docker-compose up -d
```

3. **Execute o OpenTelemetry Collector**
```bash
cd collector
otelcol-contrib --config otel-collector-config.yaml
```

4. **Execute o Logstash**
```bash
cd ../ingestion
logstash -f logstash-pipeline.conf
```

---

## 🧠 Aplicando a PoC

1. **Treine e rode o modelo de detecção de anomalias**
```bash
cd ../ml-model
pip install scikit-learn joblib pandas
python anomaly_detection.py
```

2. **Importe o dashboard no Grafana**
- Acesse: http://localhost:3000 (login padrão: admin/admin)
- Vá até **Dashboards > Import** e cole o conteúdo de `dashboards/grafana-dashboard.json`

3. **Execute a automação**
```bash
cd ../automation
chmod +x alert-handler.sh
./alert-handler.sh "Anomaly detected on CPU"
```

---

## 📂 Estrutura do Projeto

```
aiops-observability-poc/
├── collector/                  # Config do OpenTelemetry Collector
├── ingestion/                  # Pipeline do Logstash
├── ml-model/                   # Modelo ML com Isolation Forest
├── dashboards/                 # Dashboard para Grafana
├── automation/                 # Scripts de automação para alertas
└── README.md                   # Este arquivo
```

---

## 📌 Notas Finais

Essa PoC é modular e facilmente adaptável. Pode ser expandida com:
- Alertas automáticos do Elasticsearch
- Conexão com sistemas de incidentes (ex: ServiceNow)
- Modelos de ML mais avançados com timeseries

Contribuições são bem-vindas!

## 📝 Licença

MIT
