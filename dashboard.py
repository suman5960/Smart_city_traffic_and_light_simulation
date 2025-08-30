import streamlit as st
import json
import matplotlib.pyplot as plt
import numpy as np

# --- Load data ---

# Traffic and Voltage optimization data
with open('traffic_data.json', 'r') as f:
    traffic_data = json.load(f)

with open('smoothed_voltage_schedule.json', 'r') as f:
    voltage_data = json.load(f)

# City Grid for zones mapping
with open('city_grid.json', 'r') as f:
    city_grid = json.load(f)

# --- Auto Build Intersection Zone Mapping ---
intersection_zone_mapping = {
    node["id"]: node["zone"] for node in city_grid["nodes"]
}

# All zones
zones = ["residential", "commercial", "industrial", "park"]

# --- Helper functions ---

def get_zone_intersections(zone):
    return [node for node, z in intersection_zone_mapping.items() if z == zone]

def aggregate_traffic_for_zone(zone):
    intersections = get_zone_intersections(zone)
    combined_traffic = {str(h): {"vehicle": 0, "pedestrian": 0} for h in range(24)}

    for node in intersections:
        node_traffic = traffic_data.get(node, {})
        for hour, counts in node_traffic.items():
            combined_traffic[hour]["vehicle"] += counts.get("vehicle", 0)
            combined_traffic[hour]["pedestrian"] += counts.get("pedestrian", 0)
    return combined_traffic

def plot_zone_traffic(combined_traffic, zone):
    hours = list(range(24))
    vehicles = [combined_traffic[str(h)]["vehicle"] for h in hours]
    pedestrians = [combined_traffic[str(h)]["pedestrian"] for h in hours]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(hours, vehicles, marker='o', label='Vehicles', color='blue')
    ax.plot(hours, pedestrians, marker='o', label='Pedestrians', color='orange')

    ax.set_title(f"Traffic Pattern for {zone.capitalize()} Zone")
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Traffic Volume")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def get_zone_roads(zone):
    intersections = get_zone_intersections(zone)
    roads = []
    for src in intersections:
        if src in voltage_data:
            for dst in voltage_data[src]:
                if dst in intersections:
                    roads.append(f"{src}→{dst}")
    return roads

def plot_road_traffic(road):
    src, dst = road.split('→')
    hours = list(range(24))
    vehicle_counts = []
    pedestrian_counts = []

    for hour in hours:
        src_data = traffic_data.get(src, {}).get(str(hour), {})
        dst_data = traffic_data.get(dst, {}).get(str(hour), {})

        vehicles = src_data.get("vehicle", 0) + dst_data.get("vehicle", 0)
        pedestrians = src_data.get("pedestrian", 0) + dst_data.get("pedestrian", 0)

        vehicle_counts.append(vehicles)
        pedestrian_counts.append(pedestrians)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(hours, vehicle_counts, label="Vehicles", marker='o', color='blue')
    ax.plot(hours, pedestrian_counts, label="Pedestrians", marker='o', color='orange')

    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Traffic Volume")
    ax.set_title(f"Traffic Pattern for Road {road}")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def plot_voltage_for_road(road):
    src, dst = road.split('→')
    voltage_for_road = voltage_data.get(src, {}).get(dst, {})

    if not voltage_for_road:
        st.warning(f"No voltage optimization data found for {road}.")
        return

    # Only take hours 19-23 and 0-6
    night_hours = list(range(19, 24)) + list(range(0, 7))
    voltages = [voltage_for_road.get(str(h), 0) for h in night_hours]

    # Create proper labels
    hour_labels = [str(h) for h in night_hours]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(hour_labels, voltages, marker='o', color='green')

    ax.set_title(f"Voltage Optimization for {road} (Night Only)")
    ax.set_xlabel("Hour of Day")
    ax.set_ylabel("Voltage Optimization (%)")
    ax.grid(True)
    st.pyplot(fig)

# --- Streamlit Layout ---

st.title("🚦 Smart City Traffic & Voltage Optimization Dashboard")

# --- Select Zone ---
selected_zone = st.selectbox("Select Zone", zones)

if selected_zone:
    combined_traffic = aggregate_traffic_for_zone(selected_zone)
    st.subheader(f"Traffic Pattern for {selected_zone.capitalize()} Zone")
    plot_zone_traffic(combined_traffic, selected_zone)

    available_roads = get_zone_roads(selected_zone)

    if available_roads:
        selected_road = st.selectbox("Select Road in Zone", available_roads)

        if selected_road:
            st.subheader(f"Traffic Pattern for Road {selected_road}")
            plot_road_traffic(selected_road)

            st.subheader(f"Voltage Optimization for {selected_road}")
            plot_voltage_for_road(selected_road)
    else:
        st.warning("No roads available for this zone.")
