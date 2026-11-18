# Smart Public Grievance Management System

### AI-Powered Public Grievance Classification Using Multinomial Naive Bayes

The **Smart Public Grievance Management System** is a full-stack,
machine-learning-based platform designed to help citizens submit public
grievances and help government administrators, department
administrators, and government officers manage and resolve them.

The system is designed to use Natural Language Processing (NLP) and a
genuinely trained **Multinomial Naive Bayes** model to classify
complaint descriptions, recommend the responsible government department,
and provide an estimated classification confidence. It also provides
grievance tracking, priority management, duplicate detection, geographic
analytics, and interactive dashboards.

> **Project note:** This repository describes the intended system and
> its technical design. Update the feature checklist and screenshots to
> reflect what is implemented and tested in the current version. Do not
> present planned functionality, demonstration records, or
> synthetic-data results as live government services or real-world
> outcomes.

## Objectives

-   Make it easier for citizens to submit and track public grievances.
-   Automatically classify complaint descriptions using a trained
    machine-learning model.
-   Recommend the government department responsible for each grievance.
-   Show prediction probabilities and indicate when a prediction needs
    manual review.
-   Help officials assign, monitor, prioritize, and resolve grievances.
-   Provide administrators with data-driven dashboards and reports.
-   Improve transparency, accountability, and the organization of
    public-service complaints.

## Main Modules and Intended Features

### 1. Citizen Portal

-   Citizen registration and login.
-   Submit grievances with title, description, location, and supporting
    attachments.
-   View the predicted category, recommended department, and
    classification confidence.
-   Track grievance ID, status, assignment, and status history.
-   Receive in-app updates and submit feedback after resolution.

### 2. Machine Learning and Dataset Management

-   Upload CSV datasets and map the complaint-text and category columns.
-   Preview and validate datasets, including missing values, duplicates,
    and category distribution.
-   Preprocess complaint text while preserving meaningful words such as
    negations.
-   Convert text into numerical features using `TfidfVectorizer`.
-   Train a `MultinomialNB` classifier.
-   Persist versioned model and vectorizer artifacts.
-   Evaluate the model on held-out test data using accuracy, precision,
    recall, F1-score, classification report, and confusion matrix.
-   Test new complaint text and display predicted categories,
    probabilities, and model version.

The category classifier predicts complaint **category**. Department
recommendation is based on a configurable category-to-department
mapping. Priority is handled separately and must not be confused with
the Naive Bayes category prediction.

### 3. Grievance and Department Management

-   Search, filter, sort, and view grievance records.
-   Assign grievances to departments and officers.
-   Update grievance status and record remarks.
-   Maintain status history and assignment records.
-   Manage departments, officers, and workloads.
-   Support priority changes with a recorded reason.

### 4. Administrator and Department Dashboards

-   Grievance totals by status, category, department, and priority.
-   Submission trends and resolution performance.
-   Pending, in-progress, resolved, critical, and overdue grievance
    summaries.
-   Department-specific views and filters.
-   Interactive charts connected to application data.

### 5. Additional Management Features

-   Duplicate grievance candidate detection using TF-IDF and cosine
    similarity.
-   Geographic visualization using available, valid coordinates.
-   Configurable service-level targets and overdue escalation.
-   In-app notifications.
-   Citizen feedback and resolution reopening requests.
-   PDF, CSV, and Excel reports.
-   Audit logs for important administrative actions.
-   Dark and light themes with responsive layouts.

## User Roles

  -----------------------------------------------------------------------
  Role                                Intended access
  ----------------------------------- -----------------------------------
  Super Administrator                 System-wide access, users,
                                      departments, datasets, model
                                      training, analytics, reports,
                                      settings, and audit logs

  Department Administrator            Department grievances, officer
                                      assignment, status management,
                                      department analytics, and
                                      escalation

  Government Officer                  Assigned grievances, investigation
                                      remarks, progress updates, and
                                      resolution evidence

  Citizen                             Submit grievances, view personal
                                      grievance history, track status,
                                      receive updates, and provide
                                      feedback
  -----------------------------------------------------------------------

Access control must be enforced by backend authorization, not only by
hiding frontend navigation elements.

## Technology Stack

  Layer               Technologies
  ------------------- -----------------------------------------------
  Frontend            React, TypeScript, Tailwind CSS
  UI and navigation   React Router, Lucide React
  Charts              Recharts
  Backend             Python, FastAPI, Pydantic
  Machine Learning    Scikit-learn, TF-IDF, Multinomial Naive Bayes
  Data processing     Pandas, NumPy
  Database            PostgreSQL, SQLAlchemy
  Migrations          Alembic
  Maps                Leaflet, OpenStreetMap
  Reports             PDF, CSV, and Excel export libraries

## Machine Learning Workflow

1.  Upload a labelled grievance dataset in CSV format.
2.  Map the complaint-text and category columns.
3.  Validate and inspect the dataset.
4.  Preprocess text and inspect class distribution.
5.  Split the data into training and test sets using stratification
    where appropriate.
6.  Fit the TF-IDF vectorizer using training data only.
7.  Train the Multinomial Naive Bayes classifier.
8.  Evaluate the model on held-out test data.
9.  Save the model, vectorizer, and training metadata as a version.
10. Use the saved model to classify new complaint descriptions.

The application should calculate all evaluation metrics from the actual
test set. Prediction confidence is an estimate derived from the model's
probability output, not a guarantee that a prediction is correct. If no
trained model is available, classification should be reported as
unavailable rather than replaced with fabricated predictions.

## Grievance Categories

The initial configurable categories are:

1.  Roads and Infrastructure
2.  Water Supply
3.  Sanitation and Garbage
4.  Electricity and Streetlights
5.  Drainage and Sewage
6.  Healthcare
7.  Education
8.  Public Transport
9.  Food and Ration
10. Public Safety
11. Housing
12. Other Public Services

Categories and their corresponding government departments should be
configurable by authorized administrators.

## Repository Setup

The project specification targets a React frontend and FastAPI backend.
Exact commands and environment variables depend on the source-code
structure in this repository.

### Prerequisites

-   Python 3.10 or a compatible version selected by the project.
-   Node.js and npm.
-   PostgreSQL for the primary database configuration.
-   Git.

### Configuration

1.  Clone the repository.
2.  Install frontend and backend dependencies using the respective
    project manifests.
3.  Configure environment variables using the documented example
    environment file, if provided.
4.  Configure the database connection.
5.  Run database migrations.
6.  Start the FastAPI backend and React development server using the
    commands documented in their respective folders.

Do not commit `.env` files, database passwords, API keys, private
uploads, or other secrets. If setup scripts or environment templates are
not yet present, add and document them before publishing a runnable
release.

## Dataset Format

A minimum training CSV requires these columns:

  Column             Required   Description
  ------------------ ---------- ------------------------------------------------
  `complaint_text`   Yes        Text describing the public grievance
  `category`         Yes        Correct category label for supervised training
  `department`       Optional   Department label, if available
  `priority`         Optional   Priority label, if available
  `language`         Optional   Complaint language
  `location`         Optional   Location description

Example:

``` csv
complaint_text,category
"There are several potholes on the main road",Roads and Infrastructure
"Water supply has been interrupted for three days",Water Supply
"Garbage has not been collected from our street",Sanitation and Garbage
"Streetlights are not working in our area",Electricity and Streetlights
"Drainage water is overflowing onto the road",Drainage and Sewage
```

Use appropriately licensed data or clearly labelled synthetic examples.
Synthetic training and demonstration data must not be represented as
real government complaints.

## Privacy, Security, and Responsible Use

-   Store passwords using secure password hashing.
-   Enforce role-based authorization on backend endpoints.
-   Restrict citizens to their own private grievance records.
-   Validate uploaded files, types, and sizes.
-   Protect contact details and complaint attachments.
-   Keep secrets in environment variables.
-   Record important administrative actions in audit logs.
-   Do not publish personal citizen data in public dashboards or sample
    datasets.
-   Treat model predictions as decision support; provide manual review
    for uncertain or sensitive cases.
-   Do not automatically reject or delete complaints based only on
    similarity scores.

## Development Status

Use this checklist to communicate the actual state of the repository:

-   [ ] Authentication and role-based access
-   [ ] Citizen grievance submission and tracking
-   [ ] Dataset upload and validation
-   [ ] Naive Bayes training and model persistence
-   [ ] Model evaluation using held-out test data
-   [ ] Live classification and department recommendation
-   [ ] Grievance assignment and status history
-   [ ] Administrator and department dashboards
-   [ ] Interactive analytics and filters
-   [ ] Duplicate detection
-   [ ] Geographic analytics
-   [ ] SLA and escalation
-   [ ] Notifications and citizen feedback
-   [ ] Reports and exports
-   [ ] Audit logs
-   [ ] Dark and light themes
-   [ ] Automated tests and deployment documentation

Only mark a feature complete after it has been implemented and tested.

## Contribution

Contributions, suggestions, and bug reports are welcome. For substantial
changes, create an issue first to discuss the proposed improvement. Keep
changes focused, add or update tests, and document any new configuration
requirements.

## License

Choose and add a license before distributing or inviting reuse of this
project. No license is implied by the presence of this README.

------------------------------------------------------------------------

**Project:** Smart Public Grievance Management System\
**Subtitle:** AI-Powered Public Grievance Classification Using
Multinomial Naive Bayes\
**Domain:** Machine Learning, Natural Language Processing, and Public
Grievance Management
