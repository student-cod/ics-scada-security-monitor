## TrafficRecord (sent from replay script → backend)
{
  "deviceId": "PLC-01",
  "timestamp": "2026-08-05T10:15:00",
  "features": { "FIT101": 2.4, "LIT101": 80.1, ... }
}

## RiskScore (returned from ML service → backend)
{
  "riskScore": 92,
  "riskLevel": "High",
  "reason": "Unexpected deviation in LIT101 sensor reading"
}

## Alert (backend → frontend)
{
  "id": 15,
  "deviceId": "PLC-01",
  "riskScore": 92,
  "riskLevel": "High",
  "reason": "Unexpected deviation in LIT101 sensor reading",
  "timestamp": "2026-08-05T10:15:02"
}