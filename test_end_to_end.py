import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_full_pipeline():
    print("--- 1. Testing Citizen Registration ---")
    reg_payload = {
        "full_name": "Priya Verma",
        "email": "priya.verma@example.com",
        "phone": "+91 9123456789",
        "password": "Password@123",
        "role": "citizen"
    }
    # Register or login
    resp = requests.post(f"{BASE_URL}/api/auth/register", json=reg_payload)
    if resp.status_code == 200:
        citizen_token = resp.json()["access_token"]
        print("Citizen registered successfully!")
    else:
        # Try login
        login_resp = requests.post(f"{BASE_URL}/api/auth/login", json={"email": reg_payload["email"], "password": reg_payload["password"]})
        citizen_token = login_resp.json()["access_token"]
        print("Citizen logged in successfully!")

    print("\n--- 2. Testing ML Category & Priority Prediction ---")
    complaint_data = {
        "title": "Severe road craters and accident hazard",
        "description": "Massive potholes on the ring road flyover causing severe bike skids and two fatal accidents yesterday night.",
        "district": "South Delhi",
        "city": "Delhi NCR",
        "locality": "Lajpat Nagar Ring Road",
        "state": "National Capital Region"
    }
    submit_res = requests.post(
        f"{BASE_URL}/api/grievances",
        json=complaint_data,
        headers={"Authorization": f"Bearer {citizen_token}"}
    )
    assert submit_res.status_code == 200, f"Submit failed: {submit_res.text}"
    grv_data = submit_res.json()
    grv_id = grv_data["grievance_id"]
    tracking_id = grv_data["tracking_id"]
    print(f"Complaint Lodged: {tracking_id}")
    print(f"AI Category: {grv_data['predicted_category']}")
    print(f"Assigned Dept: {grv_data['department']}")
    print(f"Priority Level: {grv_data['priority']}")
    print(f"ML Confidence: {grv_data['confidence']}")

    print("\n--- 3. Testing Administrator Operations ---")
    admin_login = requests.post(f"{BASE_URL}/api/auth/login", json={"email": "admin@grievance.gov.in", "password": "Admin@123"})
    admin_token = admin_login.json()["access_token"]

    # Assign officer
    assign_res = requests.patch(
        f"{BASE_URL}/api/grievances/{grv_id}/status",
        json={"status": "Under Investigation", "remarks": "Engineer dispatched to survey pothole craters."},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert assign_res.status_code == 200
    print(f"Status updated to: Under Investigation")

    # Resolve complaint
    resolve_res = requests.patch(
        f"{BASE_URL}/api/grievances/{grv_id}/status",
        json={"status": "Resolved", "remarks": "Road cold mix patch work completed and bitumen repaved."},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert resolve_res.status_code == 200
    print(f"Status updated to: Resolved")

    print("\n--- 4. Testing Citizen Feedback ---")
    fb_res = requests.post(
        f"{BASE_URL}/api/grievances/{grv_id}/feedback",
        json={"rating": 5, "comments": "Excellent rapid road repaving! Very satisfied.", "is_satisfied": True, "request_reopen": False},
        headers={"Authorization": f"Bearer {citizen_token}"}
    )
    assert fb_res.status_code == 200
    print("Citizen feedback recorded!")

    print("\n--- 5. Testing Executive Report Generation ---")
    for fmt in ["pdf", "excel", "csv"]:
        rep = requests.get(f"{BASE_URL}/api/reports/download?format={fmt}", headers={"Authorization": f"Bearer {admin_token}"})
        assert rep.status_code == 200, f"Report {fmt} failed"
        print(f"Report [{fmt.upper()}] successfully generated ({len(rep.content)} bytes)")

    print("\n=== ALL END-TO-END WORKFLOW INTEGRATION TESTS PASSED! ===")

if __name__ == "__main__":
    test_full_pipeline()
