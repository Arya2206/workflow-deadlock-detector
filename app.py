import streamlit as st
import json
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Workflow Analyzer",
    page_icon="🔍",
    layout="wide"
)

from graph_generator import build_graph
from workflow_parser import parse_workflow
from deadlock_detector import detect_deadlock
from validator import validate_workflow

from structural_analyzer import (
    find_unreachable_nodes,
    find_orphan_nodes
)

st.title("🔍 Workflow Analyzer")

st.markdown(
    "Detect Deadlocks and Structural Anomalies in Enterprise Workflows"
)
st.sidebar.title("Project Information")

st.sidebar.info(
    """
    Workflow Analyzer MVP

    Features:
    - Deadlock Detection
    - Validation
    - Structural Analysis
    - Workflow Quality Score
    """
)

uploaded_file = st.file_uploader(
    "Upload Workflow File",
    type=["json"]
)

if uploaded_file is not None:

    # Security Check - File Size
    if uploaded_file.size > 5 * 1024 * 1024:
        st.error("File size exceeds 5 MB")
        st.stop()

    # Read JSON File
    try:
        data = json.load(uploaded_file)

    except Exception:
        st.error("Invalid JSON File")
        st.stop()

    st.success("Workflow Uploaded Successfully")

    # Workflow Data
    st.subheader("Workflow Data")
    st.json(data)

    # Parse Workflow
    nodes, edges = parse_workflow(data)

    st.subheader("Nodes")
    st.write(nodes)

    st.subheader("Edges")
    st.write(edges)

    # Build Graph
    graph = build_graph(nodes, edges)

    # Graph Information
    st.subheader("Graph Information")

    st.write("Total Nodes:", graph.number_of_nodes())
    st.write("Total Edges:", graph.number_of_edges())

    # Validation
    st.subheader("Validation")

    errors = validate_workflow(nodes)

    if errors:
        for error in errors:
            st.error(error)
    else:
        st.success("Workflow Structure Valid")

    # Main Workflow Flow
    st.subheader("Main Workflow Flow")

    for edge in edges:
        st.write(f"{edge[0]} → {edge[1]}")

    # Workflow Graph
    st.subheader("Workflow Graph")

    fig, ax = plt.subplots(figsize=(8, 6))

    pos = nx.spring_layout(
        graph,
        k=2,
        seed=42
    )

    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=3000,
        font_size=10,
        ax=ax
    )

    st.pyplot(fig)

    # Deadlock Detection
    st.subheader("Deadlock Analysis")

    cycles = detect_deadlock(graph)

    if cycles:
        st.error("Deadlock Detected")
        st.write(cycles)
    else:
        st.success("No Deadlock Found")

    # Structural Analysis
    st.subheader("Structural Analysis")

    unreachable = find_unreachable_nodes(graph)

    orphans = find_orphan_nodes(graph)

    if unreachable:
        st.warning("Unreachable Nodes Found")
        st.write(unreachable)
    else:
        st.success("No Unreachable Nodes")

    if orphans:
        st.warning("Orphan Nodes Found")
        st.write(orphans)
    else:
        st.success("No Orphan Nodes")

    # Workflow Quality Score
    st.subheader("Workflow Quality Score")

    score = 100

    if cycles:
        score -= 30

    if unreachable:
        score -= 15

    if orphans:
        score -= 15

    if errors:
        score -= (20 * len(errors))

    if score < 0:
        score = 0

    st.metric(
        label="Quality Score",
        value=f"{score}/100"
    )
    report = f"""
WORKFLOW ANALYSIS REPORT

Nodes: {graph.number_of_nodes()}
Edges: {graph.number_of_edges()}

Validation Errors:
{errors}

Deadlocks:
{cycles}

Unreachable Nodes:
{unreachable}

Orphan Nodes:
{orphans}

Quality Score:
{score}/100
"""

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="workflow_report.txt",
        mime="text/plain"
    )