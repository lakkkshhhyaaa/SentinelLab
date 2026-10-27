# SentinelLab — AI Agent Security Lab

A local AI security lab for experimenting with AI agent security, prompt-injection detection, policy enforcement, simulated tools, and audit logging.

## Overview

SentinelLab combines a locally running language model with a FastAPI backend and a React frontend to explore how an AI agent can interact with simulated data while remaining subject to explicit security policies.

The project is designed for cybersecurity learning, experimentation, and portfolio demonstration. It does not require a paid AI API or cloud service for its core functionality.

## Key Features

- **Local AI analysis:** Uses Ollama with the `llama3.2:3b` model.
- **Prompt-injection analysis:** Analyzes untrusted text for suspicious instructions and potential security threats.
- **Policy enforcement:** Evaluates proposed actions before tool execution.
- **Simulated tools:** Provides fictional email inbox and calendar data for controlled experiments.
- **Read-only agent actions:** Supports simulated data inspection and email reading.
- **Action restrictions:** Blocks prohibited actions, including simulated email deletion.
- **Audit logging:** Records agent decisions, policy decisions, and tool execution events in JSONL format.
- **Security dashboard:** Provides an interface for exploring the simulator, security tests, and audit events.
- **Automated tests:** Includes a Python test suite for API behavior, policy enforcement, and simulated tool workflows.

## Architecture


## Architecture

```text
Project-AI_Agent_Security_Lab/
├── README.md
├── index.html
├── index-backup.html
├── backend/
│   ├── main.py
│   ├── policy.py
│   ├── tools_simulator.py
│   ├── audit_log.py
│   ├── requirements.txt
│   ├── test_agent.py
│   └── test_policy.py
└── frontend/
    ├── index.html
    ├── package.json
    ├── package-lock.json
    ├── src/
    │   └── App.jsx
    └── public/
```

The frontend communicates with the FastAPI backend over HTTP.
The backend communicates with the local Ollama API.
Audit events are stored locally in JSON Lines (JSONL) format.


The backend communicates with the local Ollama API. The frontend communicates with the backend API.

## Technology Stack

- **Frontend:** React, Vite, JavaScript, CSS
- **Backend:** Python, FastAPI
- **Local AI runtime:** Ollama
- **Language model:** Llama 3.2 3B
- **Testing:** pytest and pytest-cov
- **Audit storage:** JSON Lines (JSONL)

## Prerequisites

Install the following before running the project:

- Windows with PowerShell
- Python and the project's existing backend virtual environment
- Node.js and npm
- Ollama
- The `llama3.2:3b` model

## Running Locally

### 1. Start Ollama

Ensure Ollama is installed and running. Verify that the configured model is available:

```powershell
ollama list
```

If the model is not installed, pull it:

```powershell
ollama pull llama3.2:3b
```


### 2. Start the backend

Open PowerShell in the backend directory:

```powershell
cd F:\Projects\Project-AI_Agent_Security_Lab\backend
```

Create a Python virtual environment if one does not already exist:

```powershell
py -m venv .venv
```

Install the backend dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Start the FastAPI server:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

Check the API health endpoint:

http://127.0.0.1:8000/health

Interactive API documentation:

http://127.0.0.1:8000/docs

Keep the backend running while using the frontend.



### 3. Start the frontend

Open a second PowerShell terminal in the project root and navigate to the frontend directory:

```powershell
cd F:\Projects\Project-AI_Agent_Security_Lab\frontend
```

Install the frontend dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

Open the local URL printed by Vite, expected to be:

```text
http://localhost:5173
```

Keep Ollama, the backend, and the frontend running while using the application.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Root service status |
| GET | `/health` | Backend and local model health check |
| POST | `/api/policy/check` | Evaluate a proposed action against policy |
| GET | `/api/simulated/inbox` | Inspect the fictional inbox |
| GET | `/api/simulated/inbox/{email_id}` | Read a simulated email |
| GET | `/api/simulated/calendar` | View the simulated calendar |
| POST | `/api/analyze` | Analyze untrusted text using the local model |
| POST | `/api/agent/run` | Run the simulated agent workflow |
| GET | `/api/audit/logs` | Retrieve recorded audit events |

## Security Controls

### Untrusted input and prompt injection

The simulated inbox includes an example of a malicious email containing instructions to ignore security rules and disclose saved passwords. The agent can analyze this content as untrusted evidence.

### Policy enforcement

Proposed actions are evaluated by the policy layer. Prohibited actions remain blocked even when an approval flag is supplied. A successful policy check does not itself execute an action.

### Simulated execution

The email and calendar tools operate on fictional lab data. This project is not connected to a real mailbox or calendar.

### Audit logging

The backend records events locally in JSONL format, allowing decisions and simulated tool executions to be inspected.

## Validation and Test Results

The following checks were manually observed during development on October 26, 2026:

- The backend health endpoint reported the API and Ollama as online, with `llama3.2:3b` available.
- A malicious simulated email was classified as malicious by the local model.
- A benign meeting-related message was classified as benign in a separate manual example.
- An attempted simulated email-deletion request was rejected without executing the requested action.
- The policy layer blocked the prohibited deletion action, including when approval was supplied.
- Inbox inspection and valid simulated email-reading workflows were exercised.
- An invalid email ID returned a clarification response without executing a tool action.
- The automated test suite previously reported **42 passing tests**, with approximately 99% coverage.

These manual examples demonstrate basic functionality, not comprehensive security effectiveness. The automated prompt-injection test uses a mocked analysis response and does not establish real-model detection accuracy.

## Limitations

- The local model may misclassify malicious or benign content.
- Prompt-injection resistance has not been established through a large, systematic benchmark.
- The simulated tools do not demonstrate the security of integrations with real email, calendar, or enterprise systems.
- Local JSONL audit logs are not tamper-proof and do not provide an independent audit authority.
- A development server is used for local experimentation; production deployment hardening is outside the current scope.
- The project should not be treated as a production security product or as proof that an AI agent is safe.

## Future Improvements

- Build a repeatable evaluation dataset containing benign, malicious, and ambiguous inputs.
- Measure detection performance and document false positives and false negatives.
- Improve audit coverage for rejected and invalid requests.
- Add reproducible setup and clean-start verification.
- Document the threat model, policy assumptions, and evaluation methodology.
- Prepare a recorded demonstration showing both normal behavior and security failures.

## Project Goal

SentinelLab is intended to be a practical, local-first learning environment for understanding AI agent security controls, prompt injection, policy enforcement, and auditability.
