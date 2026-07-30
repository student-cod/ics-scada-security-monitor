CREATE TABLE devices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(100),
    ip_address VARCHAR(50),
    device_type VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Online'
);

CREATE TABLE traffic_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    device_id INT,
    timestamp DATETIME,
    raw_data JSON,
    FOREIGN KEY (device_id) REFERENCES devices(id)
);

CREATE TABLE alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    traffic_log_id INT,
    risk_score INT,
    risk_level VARCHAR(20),
    reason VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (traffic_log_id) REFERENCES traffic_logs(id)
);