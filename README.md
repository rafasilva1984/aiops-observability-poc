# AIOps Observability PoC

This project demonstrates a Proof of Concept (PoC) for building an AIOps-driven Observability architecture using open source tools.

## Components

- **OpenTelemetry Collector:** For collecting logs, metrics and traces.
- **Logstash:** For ingesting and enriching the data.
- **Elasticsearch:** For storing observability data.
- **Python + ML (Isolation Forest):** For detecting anomalies.
- **Grafana:** For visualizing data.
- **Automation script:** To handle alerts and trigger actions.

## Requirements

- Docker & Docker Compose
- Python 3.10+
- Java (for Logstash)
- Grafana & Elasticsearch running (can use Docker)

## Setup

### 1. Configure OpenTelemetry Collector

Edit `collector/otel-collector-config.yaml` with your endpoints.

```bash
cd collector
otelcol-contrib --config otel-collector-config.yaml
```

### 2. Setup Logstash

Configure `logstash-pipeline.conf` and start Logstash:

```bash
cd ingestion
logstash -f logstash-pipeline.conf
```

### 3. Train and Run the ML Model

Install Python dependencies and run anomaly detection:

```bash
cd ml-model
pip install -r requirements.txt
python anomaly_detection.py
```

### 4. Import Grafana Dashboard

Use the `grafana-dashboard.json` file inside Grafana UI to visualize metrics and anomalies.

### 5. Automation

Use `automation/alert-handler.sh` to act on alerts, such as sending notifications or restarting services.

## License

MIT
