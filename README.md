# Medicine Recommendation Dashboard

An interactive Shiny dashboard designed to explore fever patterns, vital signs, environmental conditions, lifestyle factors, and medicine recommendations through dynamic visual analysis.

This project transforms a healthcare-style recommendation dataset into an interactive visual application that helps users examine how patient symptoms, demographics, blood pressure, air quality, and lifestyle variables relate to medication suggestions and health indicators.

---

## Project Summary

**Built an interactive healthcare analytics dashboard** by creating a Shiny app for fever, vitals, and medicine recommendation exploration.

**Enabled users to analyze patient patterns dynamically** across symptoms, demographics, environmental conditions, and treatment suggestions.

**Did this by** designing a multi-tab Shiny dashboard with reactive filters, interactive visualizations, demographic controls, and a light/dark theme toggle for improved usability. :contentReference[oaicite:1]{index=1}

---

## Objective

**Improved interpretability of patient-level recommendation data** by presenting it through an interactive dashboard.

**Created a visual exploration tool** to help users understand how heart rate, fever severity, blood pressure, air quality, age, and lifestyle choices interact with recommended medication.

**Did this by** combining a structured healthcare dataset with Shiny-based filtering, tabbed analysis views, and responsive plot updates. :contentReference[oaicite:2]{index=2}

---

## Dataset Overview

The dashboard uses a dataset built for medicine recommendation analysis based on patient health, symptoms, medical background, environmental factors, and lifestyle characteristics.

### Dataset characteristics
- **Total samples:** 1000
- **Features:** 19 input features + 1 target column
- **File format:** CSV

### Example variables
- Temperature
- Fever Severity
- Age
- Gender
- BMI
- Headache
- Body Ache
- Fatigue
- Chronic Conditions
- Allergies
- Smoking History
- Alcohol Consumption
- Humidity
- AQI
- Physical Activity
- Diet Type
- Heartrate
- Blood Pressure
- Previous Medication
- Recommended Medication

The target variable represents the recommended medicine for the patient. :contentReference[oaicite:3]{index=3}

---

## Dashboard Features

**Delivered a structured interactive exploration experience** by dividing the app into clear analytical sections.

**Designed the dashboard with a header, sidebar, and tabbed content area** so users can explore multiple health relationships in one place.

**Did this by** creating a Shiny layout with:
- a top header with project title and theme toggle
- a left sidebar for symptom and demographic filters
- a main panel with multiple chart tabs that update automatically based on selections. :contentReference[oaicite:4]{index=4}

---

## Interactive Views

### 1. HR vs Fever
**Revealed how heart rate changes across fever severity levels** by comparing distributions for Normal, Mild Fever, and High Fever cases.

**Built a heart-rate comparison view** to help users inspect spread and average values across fever categories.

**Did this by** using filtered visual summaries that update in real time based on the selected patient group. :contentReference[oaicite:5]{index=5}

### 2. HR vs Age
**Showed how heart rate varies across life stages** by grouping patients into age-based categories.

**Created an age-focused comparison view** to examine heart-rate behavior across children, adolescents, adults, and seniors.

**Did this by** categorizing age groups and visualizing comparative distributions within the Shiny app. :contentReference[oaicite:6]{index=6}

### 3. BP vs Medication
**Connected treatment patterns with blood pressure categories** by comparing recommended medication across blood pressure groups.

**Built a medication analysis view** to help users understand how recommendation patterns differ for Normal, High, and Low BP patients.

**Did this by** aggregating category counts and presenting them as an interactive comparison chart. :contentReference[oaicite:7]{index=7}

### 4. AQI vs Fever
**Linked environmental conditions with fever severity** by comparing average AQI values across fever categories.

**Created an air-quality analysis view** to explore whether fever severity aligns with different AQI levels in the dataset.

**Did this by** summarizing AQI by fever group and rendering the results through reactive Shiny plots. :contentReference[oaicite:8]{index=8}

### 5. Alcohol vs Age
**Highlighted lifestyle patterns across demographic groups** by showing how alcohol use is distributed across life stages.

**Built a lifestyle analysis view** to identify which age groups contribute most to alcohol consumption.

**Did this by** grouping users by life stage and calculating the distribution of alcohol consumption visually. :contentReference[oaicite:9]{index=9}

---

## Filtering and Interactivity

**Improved exploratory power** by allowing users to focus on highly specific patient groups.

**Added interactive filtering across symptoms, habits, and demographics** so charts respond instantly to user selections.

**Did this by** implementing:
- symptom and lifestyle checkboxes
- age range slider
- gender dropdown
- diet type dropdown
- automatic plot refresh for all tabs when filters change. :contentReference[oaicite:10]{index=10}

---

## Night Mode

**Enhanced readability and presentation quality** by adding a dark-theme viewing option.

**Implemented a Night mode toggle** to switch the dashboard between light and dark appearance.

**Did this by** applying a theme control that changes the overall app styling without affecting the underlying data or filters. :contentReference[oaicite:11]{index=11}

---

## Business and Analytical Value

**Turned a synthetic medicine recommendation dataset into a decision-support dashboard** that is easier to interpret than raw tables.

**Made healthcare pattern exploration more accessible** by presenting patient, symptom, and environmental relationships in an interactive format.

**Did this by** combining Shiny interactivity, visual storytelling, and filter-driven analysis into a single dashboard interface. :contentReference[oaicite:12]{index=12}

---

## Tech Stack

- R
- Shiny
- ggplot2
- dplyr
- CSV dataset
- Interactive dashboard design

---

## Repository Structure

```text
Medicine_Recommendation/
│
├── app.R
├── enhanced_fever_medicine_recommendation.csv
├── Final Report.pdf
└── README.md
