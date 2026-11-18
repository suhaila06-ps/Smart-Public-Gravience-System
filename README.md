# SMART PUBLIC GRIEVANCE CLASSIFICATION AND MANAGEMENT SYSTEM
### AI-Powered Public Grievance Classification Using Multinomial Naive Bayes

A full-stack, production-quality, civic administration and grievance management web application powered by a genuinely trained **Multinomial Naive Bayes** machine learning model.

---

## 1. Key Features

- **Genuine Machine Learning Engine**:
  - Multinomial Naive Bayes classification with TF-IDF Vectorization (`ngram_range=(1,2)`).
  - Preserved negation tokens (`not`, `no`, `never`, `without`) to maintain complaint context.
  - Stratified train/test holdout split with evaluation metrics (Accuracy, Macro F1, Precision, Recall).
  - Versioned model artifact persistence using `joblib`.
  - Live interactive classification playground with top 5 posterior probabilities.
  - Duplicate grievance detection using TF-IDF cosine similarity.

- **Role-Based Portals & RBAC**:
  - **Super Administrator**: Complete visibility over all grievances, ML model retraining, department configurations, staff management, audit trails, and PDF/Excel report exports.
  - **Department Administrator**: Department-filtered complaints, officer assignment, SLA escalation management, and staff performance tracking.
  - **Government Officer**: Assigned tasks, investigation remarks, evidence upload, and complaint resolution.
  - **Citizen**: Grievance lodgement with real-time ML classification preview, image/document upload, live status tracking timeline, and post-resolution 5-star feedback.

- **Enterprise Analytics & UI/UX**:
  - Interactive Recharts graphs: Inflow Trends, Category Distribution Donut, Department Workload Bar Chart.
  - OpenStreetMap + Leaflet interactive geographic map with NCR district hotspot density.
  - Full system-wide Dark Navy / Clean Light theme toggle with local persistence.

---

## 2. Technology Stack

- **Frontend**: React 19, TypeScript, Vite, Tailwind CSS, Recharts, Lucide React, React-Leaflet, React Router.
- **Backend**: Python 3.13, FastAPI, Pydantic, SQLAlchemy ORM, SQLite / PostgreSQL, ReportLab (PDF), OpenPyXL (Excel).
- **Machine Learning**: Scikit-Learn (MultinomialNB, TfidfVectorizer), Pandas, NumPy.

---

## 3. Demo Credentials

| Role | Email | Password | Access Level |
| :--- | :--- | :--- | :--- |
| **Super Administrator** | `admin@grievance.gov.in` | `Admin@123` | Full System Access |
| **Dept Administrator** | `deptadmin@pwd.gov.in` | `Admin@123` | Public Works Dept |
| **Government Officer** | `officer@pwd.gov.in` | `Admin@123` | Assigned Tasks |
| **Citizen** | `citizen@example.com` | `Admin@123` | Citizen Portal |

*(Quick-fill buttons for each role are available on the login page).*

---

## 4. Running the Application Locally

### Backend Server:
```bash
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```
Interactive API Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Frontend Server:
```bash
cd frontend
npm run dev -- --host 127.0.0.1 --port 5173
```
Access the Web Application: [http://127.0.0.1:5173](http://127.0.0.1:5173)

---

## 5. Automated Verification Test Suite

Run the full end-to-end integration test:
```bash
python test_end_to_end.py
```
This tests:
1. Citizen Registration & Login
2. Grievance Lodgement & Live Naive Bayes Category/Priority Inference
3. Department Routing & SLA Calculation
4. Administrator Investigation & Officer Resolution
5. Citizen Post-Resolution Feedback
6. PDF, Excel, and CSV Executive Report Generation
