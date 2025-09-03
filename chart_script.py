import plotly.graph_objects as go
import plotly.express as px
import json
import numpy as np

# Updated data with Docker infrastructure layer
data = {
  "components": [
    {"name": "Lufthansa API", "type": "external", "layer": "External", "x": 50, "y": 5},
    {"name": "Data Collector", "type": "service", "layer": "Collection", "x": 50, "y": 20},
    {"name": "MySQL", "type": "database", "layer": "Storage", "x": 30, "y": 35},
    {"name": "MongoDB", "type": "database", "layer": "Storage", "x": 70, "y": 35},
    {"name": "FastAPI", "type": "api", "layer": "API", "x": 50, "y": 50},
    {"name": "Streamlit", "type": "frontend", "layer": "Frontend", "x": 50, "y": 65},
    {"name": "Airflow", "type": "orchestrator", "layer": "Orchestration", "x": 15, "y": 20},
    {"name": "Docker", "type": "infrastructure", "layer": "Infrastructure", "x": 85, "y": 50}
  ],
  "connections": [
    {"from": "Lufthansa API", "to": "Data Collector", "type": "data_fetch"},
    {"from": "Data Collector", "to": "MySQL", "type": "store_relational"},
    {"from": "Data Collector", "to": "MongoDB", "type": "store_nosql"},
    {"from": "FastAPI", "to": "MySQL", "type": "query"},
    {"from": "FastAPI", "to": "MongoDB", "type": "query"},
    {"from": "Streamlit", "to": "FastAPI", "type": "api_calls"},
    {"from": "Airflow", "to": "Data Collector", "type": "orchestrate"}
  ]
}

# Color mapping for layers
layer_colors = {
    "External": "#1FB8CD",        # Strong cyan
    "Collection": "#DB4545",      # Bright red
    "Storage": "#2E8B57",         # Sea green
    "API": "#5D878F",             # Cyan
    "Frontend": "#D2BA4C",        # Moderate yellow
    "Orchestration": "#B4413C",   # Moderate red
    "Infrastructure": "#964325"   # Dark orange
}

# Create figure
fig = go.Figure()

# Create component lookup
comp_lookup = {comp["name"]: comp for comp in data["components"]}

# Add connections with better arrows
for conn in data["connections"]:
    from_comp = comp_lookup[conn["from"]]
    to_comp = comp_lookup[conn["to"]]
    
    # Calculate arrow position (slightly before the target node)
    dx = to_comp["x"] - from_comp["x"]
    dy = to_comp["y"] - from_comp["y"]
    length = np.sqrt(dx**2 + dy**2)
    
    # Normalize and scale to stop before node
    if length > 0:
        dx_norm = dx / length
        dy_norm = dy / length
        arrow_end_x = to_comp["x"] - dx_norm * 3
        arrow_end_y = to_comp["y"] - dy_norm * 3
    else:
        arrow_end_x = to_comp["x"]
        arrow_end_y = to_comp["y"]
    
    # Add connection line
    fig.add_trace(go.Scatter(
        x=[from_comp["x"], arrow_end_x],
        y=[from_comp["y"], arrow_end_y],
        mode='lines',
        line=dict(color='#666666', width=2),
        hoverinfo='none',
        showlegend=False
    ))
    
    # Add arrow head
    fig.add_annotation(
        x=arrow_end_x,
        y=arrow_end_y,
        ax=from_comp["x"],
        ay=from_comp["y"],
        xref='x',
        yref='y',
        axref='x',
        ayref='y',
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=3,
        arrowcolor='#666666',
        showarrow=True,
        text=""
    )

# Add components by layer for legend organization
layers = list(set(comp["layer"] for comp in data["components"]))

for layer in layers:
    layer_components = [comp for comp in data["components"] if comp["layer"] == layer]
    
    fig.add_trace(go.Scatter(
        x=[comp["x"] for comp in layer_components],
        y=[comp["y"] for comp in layer_components],
        mode='markers+text',
        marker=dict(
            size=80,  # Increased size for better readability
            color=layer_colors[layer],
            line=dict(width=3, color='white')
        ),
        text=[comp["name"] for comp in layer_components],
        textposition="middle center",
        textfont=dict(size=11, color='white', family="Arial Black"),
        name=layer,
        hovertemplate='<b>%{text}</b><br>Layer: ' + layer + '<br>Type: ' + 
                     [comp["type"] for comp in layer_components][0] + '<extra></extra>'
    ))

# Add layer background rectangles for better visual separation
layer_y_ranges = {
    "External": (0, 10),
    "Collection": (13, 27),
    "Storage": (28, 42),
    "API": (43, 57),
    "Frontend": (58, 72),
    "Orchestration": (13, 27),
    "Infrastructure": (43, 57)
}

# Update layout
fig.update_layout(
    title="DST Airlines System Architecture",
    xaxis=dict(
        range=[0, 100],
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        fixedrange=True
    ),
    yaxis=dict(
        range=[0, 75],
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        fixedrange=True
    ),
    plot_bgcolor='white',
    legend=dict(
        orientation='h', 
        yanchor='bottom', 
        y=1.02, 
        xanchor='center', 
        x=0.5
    )
)

fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("dst_airlines_architecture.png")