from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/logs")
def get_logs():
    # Fake log entries
    logs = [
        {"timestamp": "2025-08-18T10:00:00Z", "level": "INFO", "message": "User login success", "user": "alice"},
        {"timestamp": "2025-08-18T10:05:12Z", "level": "WARN", "message": "Multiple failed login attempts", "user": "bob"},
        {"timestamp": "2025-08-18T10:07:45Z", "level": "ERROR", "message": "SQL error near 'DROP TABLE'", "user": "eve"},
    ]
    return {"logs": logs}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000) # Render requires listening on 0.0.0.0 and a specific port.