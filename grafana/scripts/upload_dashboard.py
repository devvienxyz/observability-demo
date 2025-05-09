import json
import requests
import sys

# Set Grafana API URL and your API Key (replace with your actual values)
GRAFANA_URL = "http://localhost:3000"
API_KEY = "your-grafana-api-key"  # You can generate an API key in Grafana under API Keys in the settings.

# Helper function to upload dashboard
def upload_dashboard(dashboard_file):
    # Read the dashboard JSON file
    try:
        with open(dashboard_file, 'r') as file:
            dashboard_json = json.load(file)
    except Exception as e:
        print(f"Error reading the dashboard file: {e}")
        return

    # Define the request headers
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # URL to the Grafana dashboard API
    url = f"{GRAFANA_URL}/api/dashboards/db"

    # Grafana API payload to create a new dashboard
    data = {
        "dashboard": dashboard_json,
        "overwrite": True  # Set to True if you want to overwrite the existing dashboard with the same name
    }

    # Make the API request to upload the dashboard
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Dashboard '{dashboard_file}' uploaded successfully!")
    else:
        print(f"Failed to upload dashboard: {response.status_code} - {response.text}")

# Main function to handle command-line argument
def main():
    if len(sys.argv) != 2:
        print("Usage: python upload_dashboard.py <dashboard_name>")
        sys.exit(1)

    dashboard_name = sys.argv[1]
    dashboard_file = f"grafana/dashboards/{dashboard_name}.json"

    upload_dashboard(dashboard_file)

if __name__ == "__main__":
    main()
