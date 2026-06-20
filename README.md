# Workflow Deadlock Detector

## Overview

Workflow Deadlock Detector is a web-based workflow analysis system developed using Python, Streamlit, and NetworkX. The application helps identify workflow deadlocks, structural anomalies, validation issues, and overall workflow quality. It provides graphical workflow visualization and generates analysis reports for business process evaluation.

---

## Features

### Workflow Upload

* Upload workflow files in JSON format.
* Supports workflow node and edge definitions.

### Workflow Visualization

* Generates directed workflow graphs.
* Displays workflow structure using NetworkX and Matplotlib.

### Deadlock Detection

* Detects cyclic dependencies in workflows.
* Identifies potential deadlock situations.

### Structural Analysis

* Detects unreachable nodes.
* Detects orphan nodes.
* Highlights workflow anomalies.

### Workflow Validation

* Checks for missing Start node.
* Checks for missing End node.
* Validates workflow structure before analysis.

### Workflow Quality Score

* Calculates workflow quality score out of 100.
* Deducts points for detected issues.

### Report Generation

* Generates downloadable workflow analysis reports.
* Summarizes validation and analysis results.

### Security Features

* Invalid JSON file handling.
* File size validation.
* Safe workflow processing.

---

## Technology Stack

* Python 3.11
* Streamlit
* NetworkX
* Matplotlib
* JSON

---

## Project Structure

```text
workflow-deadlock-detector/
│
├── app.py
├── workflow_parser.py
├── graph_generator.py
├── deadlock_detector.py
├── structural_analyzer.py
├── validator.py
├── README.md
│
├── uploads/
│
└── sample_workflows/
    ├── workflow1.json
    ├── deadlock.json
    ├── missing_end.json
    └── unreachable.json
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Arya2206/workflow-deadlock-detector.git
```

Navigate to the project directory:

```bash
cd workflow-deadlock-detector
```

Install dependencies:

```bash
pip install streamlit networkx matplotlib pandas
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## Sample Test Cases

### Valid Workflow

* workflow1.json

### Deadlock Workflow

* deadlock.json

### Missing End Node

* missing_end.json

### Unreachable Node

* unreachable.json

---

## Future Enhancements

* PDF Report Generation
* Advanced Workflow Analytics
* Workflow Recommendations
* Cloud Deployment
* Real-Time Monitoring Dashboard

---

## Author

Developed as an academic MVP project for workflow analysis, deadlock detection, and process validation.

