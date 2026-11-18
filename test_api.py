import requests

base_url = "http://127.0.0.1:8000"
resp = requests.post(f"{base_url}/api/auth/login", json={"email": "admin@grievance.gov.in", "password": "Admin@123"})
if resp.status_code == 200:
    data = resp.json()
    token = data["access_token"]
    user = data["user"]
    print(f"Logged in as: {user['full_name']} ({user['role']})")
    
    # Inject demo data
    inject_resp = requests.post(f"{base_url}/api/admin/inject-demo-data", headers={"Authorization": f"Bearer {token}"})
    print("Demo Data Injection:", inject_resp.json())

    # Fetch KPIs
    kpi_resp = requests.get(f"{base_url}/api/analytics/kpis", headers={"Authorization": f"Bearer {token}"})
    print("Live KPIs:", kpi_resp.json())
else:
    print("Login failed:", resp.text)
