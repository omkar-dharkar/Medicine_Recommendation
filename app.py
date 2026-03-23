from shiny import reactive
from shiny.express import input, render, ui, session
import pandas as pd
import plotnine as p9

df = pd.read_csv("enhanced_fever_medicine_recommendation.csv")
df["Blood_Pressure"] = df["Blood_Pressure"].astype("category")

age_min = int(df["Age"].min())
age_max = int(df["Age"].max())

gender_values = ["All"] + sorted(df["Gender"].dropna().unique().tolist())
diet_values = ["All"] + sorted(df["Diet_Type"].dropna().unique().tolist())

def add_life_stage(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.copy()
    life_bins = [0, 4, 9, 14, 17, 24, 64, 120]
    life_labels = [
        "Young (0–4)",
        "Older kids (5–9)",
        """Young adolescents 
           (10–14)""",
        """Older adolescents 
           (15–17)""",
        "Young adults (18–24)",
        "Adults (25–64)",
        "Seniors (65+)",
    ]
    out["Life_Stage"] = pd.cut(
        out["Age"],
        bins=life_bins,
        labels=life_labels,
        include_lowest=True,
    )
    return out

ui.tags.head(
    ui.tags.meta(
        name="viewport",
        content="width=device-width, initial-scale=1, maximum-scale=1",
    )
)

ui.tags.style(
    """
    body {
        margin: 0;
        padding-top: 96px;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    .container-fluid {
        padding-left: 8px;
        padding-right: 8px;
    }
    .top-bar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1100;
    }
    .top-bar-inner {
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 0.75rem;
        flex-wrap: wrap;
    }
    body[data-theme="light"] {
        background-color: #e5e7eb;
        color: #111827;
        margin-top: 96px;
    }
    body[data-theme="light"] .top-bar {
        padding: 0.9rem 1.2rem;
        background: linear-gradient(135deg, #0f766e, #2563eb);
        color: #f9fafb;
        box-shadow: 0 10px 26px rgba(15, 23, 42, 0.35);
    }
    body[data-theme="light"] .top-title {
        margin: 0;
        font-weight: 650;
        letter-spacing: 0.02em;
    }
    body[data-theme="light"] .top-subtitle {
        margin: 0.3rem 0 0;
        color: #e5e7eb;
        font-size: 0.95rem;
    }
    body[data-theme="light"] .sidebar-panel {
        background-color: #f9fafb;
        border-radius: 0.6rem;
        padding: 0.5rem 0.75rem 0.6rem;
        border: 1px solid #e5e7eb;
    }
    body[data-theme="light"] .main-card {
        background-color: #ffffff;
        border-radius: 0.6rem;
        padding: 0.4rem 0.6rem 0.8rem;
        border: 1px solid #e5e7eb;
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.18);
    }
    body[data-theme="light"] .filter-section-title {
        color: #374151;
    }
    body[data-theme="light"] .nav-tabs {
        border-bottom: 1px solid #e5e7eb;
    }
    body[data-theme="light"] .nav-tabs > li > a {
        color: #4b5563;
    }
    body[data-theme="light"] .nav-tabs > li > a:hover {
        background-color: #eff6ff;
        border-color: transparent transparent #e5e7eb;
        color: #1d4ed8;
    }
    body[data-theme="light"] .nav-tabs > li.active > a,
    body[data-theme="light"] .nav-tabs > li.active > a:focus,
    body[data-theme="light"] .nav-tabs > li.active > a:hover {
        color: #111827;
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-bottom-color: #ffffff;
    }
    body[data-theme="dark"] {
        background-color: #020617;
        color: #e5e7eb;
        margin-top: 96px;
    }
    body[data-theme="dark"] .top-bar {
        padding: 0.9rem 1.2rem;
        background: linear-gradient(135deg, #020617, #0f172a);
        color: #e5e7eb;
        box-shadow: 0 10px 32px rgba(15, 23, 42, 0.7);
    }
    body[data-theme="dark"] .top-title {
        margin: 0;
        font-weight: 650;
        letter-spacing: 0.02em;
        color: #f9fafb;
    }
    body[data-theme="dark"] .top-subtitle {
        margin: 0.3rem 0 0;
        color: #9ca3af;
        font-size: 0.95rem;
    }
    body[data-theme="dark"] .sidebar-panel {
        background-color: #020617;
        border-radius: 0.6rem;
        padding: 0.5rem 0.75rem 0.6rem;
        border: 1px solid #111827;
    }
    body[data-theme="dark"] .sidebar-panel .filter-section-title,
    body[data-theme="dark"] .sidebar-panel label,
    body[data-theme="dark"] .sidebar-panel .form-check-label,
    body[data-theme="dark"] .sidebar-panel .form-label,
    body[data-theme="dark"] .sidebar-panel .control-label {
        color: #ffffff !important;
    }
    body[data-theme="dark"] .sidebar-panel .irs-single,
    body[data-theme="dark"] .sidebar-panel .irs-min,
    body[data-theme="dark"] .sidebar-panel .irs-max,
    body[data-theme="dark"] .sidebar-panel .irs-grid-text {
        color: #ffffff !important;
    }
    body[data-theme="dark"] .main-card {
        background-color: #020617;
        border-radius: 0.6rem;
        padding: 0.4rem 0.6rem 0.8rem;
        border: 1px solid #111827;
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.9);
    }
    body[data-theme="dark"] .filter-section-title {
        color: #9ca3af;
    }
    body[data-theme="dark"] .nav-tabs {
        border-bottom: 1px solid #111827;
    }
    body[data-theme="dark"] .nav-tabs > li > a {
        color: #9ca3af;
        background-color: transparent;
        border-color: transparent;
    }
    body[data-theme="dark"] .nav-tabs > li > a:hover {
        background-color: #020617;
        border-color: transparent transparent #111827;
        color: #e5e7eb;
    }
    body[data-theme="dark"] .nav-tabs > li.active > a,
    body[data-theme="dark"] .nav-tabs > li.active > a:focus,
    body[data-theme="dark"] .nav-tabs > li.active > a:hover {
        color: #f9fafb;
        background-color: #020617;
        border: 1px solid #111827;
        border-bottom-color: #020617;
    }
    .sidebar-scroll {
        max-height: 80vh;
        overflow-y: auto;
        padding-right: 0.25rem;
    }
    .sidebar-scroll::-webkit-scrollbar {
        width: 6px;
    }
    .sidebar-scroll::-webkit-scrollbar-thumb {
        background-color: #6b7280;
        border-radius: 999px;
    }
    .filter-section-title {
        margin-top: 0.25rem;
        margin-bottom: 0.4rem;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }
    .tab-content {
        padding: 0.6rem 0.25rem 0.2rem;
    }
    @media (max-width: 768px) {
        .container-fluid {
            padding-left: 4px;
            padding-right: 4px;
        }
        .top-bar-inner {
            flex-direction: column;
            align-items: flex-start;
            gap: 0.4rem;
        }
        .top-subtitle {
            font-size: 0.85rem !important;
        }
        .sidebar-panel {
            margin-top: 0.4rem;
            margin-bottom: 0.4rem;
        }
        .main-card {
            padding: 0.3rem 0.35rem 0.6rem;
        }
        .nav-tabs > li > a {
            padding: 0.35rem 0.55rem;
            font-size: 0.8rem;
        }
    }
    """
)

ui.tags.script(
    """
    document.addEventListener('DOMContentLoaded', function() {
        document.body.setAttribute('data-theme', 'light');
    });
    Shiny.addCustomMessageHandler('set-theme', function(message) {
        var mode = message.mode || 'light';
        document.body.setAttribute('data-theme', mode);
    });
    """
)

ui.div(
    {"class": "top-bar"},
    ui.div(
        {"class": "top-bar-inner"},
        ui.div(
            [
                ui.h2("Fever & Vital Signs Explorer", class_="top-title"),
                ui.p(
                    "Explore how fever severity, heart rate, air quality, and lifestyle factors interact in this patient dataset.",
                    class_="top-subtitle",
                ),
            ]
        ),
        ui.div(
            {"style": "display:flex; align-items:center; gap:0.4rem;"},
            ui.tags.span("Night mode", style="font-size:0.9rem;"),
            ui.input_switch("dark_mode", None, value=False),
        ),
    ),
)

with ui.sidebar():
    ui.div(
        {"class": "sidebar-panel"},
        ui.div(
            {"class": "sidebar-scroll"},
            ui.p("SYMPTOMS & LIFESTYLE", class_="filter-section-title"),
            ui.input_checkbox_group(
                "flags",
                "Include only patients with:",
                choices=[
                    "Headache",
                    "Body_Ache",
                    "Fatigue",
                    "Chronic_Conditions",
                    "Allergies",
                    "Smoking_History",
                    "Alcohol_Consumption",
                ],
            ),
            ui.hr(),
            ui.p("DEMOGRAPHIC FILTERS", class_="filter-section-title"),
            ui.input_slider(
                "age",
                "Age range:",
                min=age_min,
                max=age_max,
                value=[age_min, age_max],
            ),
            ui.input_select(
                "gender",
                "Gender:",
                choices=gender_values,
                selected="All",
            ),
            ui.input_select(
                "diet",
                "Diet type:",
                choices=diet_values,
                selected="All",
            ),
        ),
    )

@reactive.effect
async def _sync_theme():
    mode = "dark" if input.dark_mode() else "light"
    await session.send_custom_message("set-theme", {"mode": mode})

@reactive.calc
def filtered_df():
    data = df.copy()
    age_lo, age_hi = input.age()
    data = data[(data["Age"] >= age_lo) & (data["Age"] <= age_hi)]
    gender_choice = input.gender()
    if gender_choice != "All":
        data = data[data["Gender"] == gender_choice]
    diet_choice = input.diet()
    if diet_choice != "All":
        data = data[data["Diet_Type"] == diet_choice]
    for col in input.flags():
        data = data[data[col] == "Yes"]
    return data

with ui.div({"class": "main-card"}):
    with ui.navset_tab():
        with ui.nav_panel("HR vs Fever"):

            @render.plot
            def plot_hr_severity():
                data = filtered_df()
                if data.empty:
                    return p9.ggplot() + p9.theme_void()

                hr_summary = (
                    data.groupby("Fever_Severity", as_index=False)["Heart_Rate"]
                    .mean()
                    .rename(columns={"Heart_Rate": "Mean_HR"})
                )
                hr_summary["Mean_Label"] = hr_summary["Mean_HR"].round(1)

                g = (
                    p9.ggplot(data, p9.aes(x="Fever_Severity", y="Heart_Rate"))
                    + p9.geom_boxplot(fill="#7fb3ff", alpha=0.7)
                    + p9.geom_point(
                        p9.aes(x="Fever_Severity", y="Mean_HR"),
                        data=hr_summary,
                        color="red",
                        size=3,
                    )
                    + p9.geom_text(
                        p9.aes(x="Fever_Severity", y="Mean_HR", label="Mean_Label"),
                        data=hr_summary,
                        nudge_y=2,
                        size=8,
                    )
                    + p9.theme_minimal()
                    + p9.labs(
                        title="Heart rate by fever severity",
                        x="Fever severity",
                        y="Heart rate (bpm)",
                    )
                )
                return g

        with ui.nav_panel("HR vs Age"):

            @render.plot
            def plot_hr_age():
                data = filtered_df()
                if data.empty:
                    return p9.ggplot() + p9.theme_void()

                with_stages = add_life_stage(data)
                with_stages = with_stages.dropna(subset=["Life_Stage"])
                if with_stages.empty:
                    return p9.ggplot() + p9.theme_void()

                age_summary = (
                    with_stages.groupby("Life_Stage", as_index=False)["Heart_Rate"]
                    .mean()
                    .rename(columns={"Heart_Rate": "Mean_HR"})
                )
                age_summary["Mean_Label"] = age_summary["Mean_HR"].round(1)

                g = (
                    p9.ggplot(with_stages, p9.aes(x="Life_Stage", y="Heart_Rate"))
                    + p9.geom_boxplot(fill="#9ad9b5", alpha=0.7)
                    + p9.geom_point(
                        p9.aes(x="Life_Stage", y="Mean_HR"),
                        data=age_summary,
                        color="red",
                        size=3,
                    )
                    + p9.geom_text(
                        p9.aes(x="Life_Stage", y="Mean_HR", label="Mean_Label"),
                        data=age_summary,
                        nudge_y=2,
                        size=8,
                    )
                    + p9.theme_minimal()
                    + p9.labs(
                        title="Heart rate across life stages",
                        x="Life stage",
                        y="Heart rate (bpm)",
                    )
                )
                return g

        with ui.nav_panel("BP vs Medication"):

            @render.plot
            def plot_bp_med():
                data = filtered_df()
                if data.empty:
                    return p9.ggplot() + p9.theme_void()

                g = (
                    p9.ggplot(
                        data,
                        p9.aes(x="Recommended_Medication", fill="Blood_Pressure"),
                    )
                    + p9.geom_bar(position="dodge")
                    + p9.theme_minimal()
                    + p9.labs(
                        title="Blood pressure category vs recommended medication",
                        x="Medication",
                        y="Number of patients",
                        fill="BP category",
                    )
                )
                return g

        with ui.nav_panel("AQI vs Fever"):

            @render.plot
            def plot_aqi_bar():
                data = filtered_df()
                if data.empty:
                    return p9.ggplot() + p9.theme_void()

                aqi_summary = (
                    data.groupby("Fever_Severity", as_index=False)["AQI"]
                    .mean()
                    .rename(columns={"AQI": "Mean_AQI"})
                )
                aqi_summary["Midpoint"] = aqi_summary["Mean_AQI"] / 2.0
                aqi_summary["Label"] = aqi_summary["Mean_AQI"].round(1)

                g = (
                    p9.ggplot(aqi_summary, p9.aes(x="Fever_Severity", y="Mean_AQI"))
                    + p9.geom_col(fill="#8ecae6")
                    + p9.geom_text(
                        p9.aes(y="Midpoint", label="Label"),
                        size=9,
                    )
                    + p9.coord_flip()
                    + p9.theme_minimal()
                    + p9.labs(
                        title="Average AQI by fever severity",
                        x="Fever severity",
                        y="Mean AQI",
                    )
                )
                return g

        with ui.nav_panel("Alcohol vs Age"):

            @render.plot
            def plot_alcohol_age():
                data = filtered_df()
                data = data[data["Alcohol_Consumption"] == "Yes"]
                if data.empty:
                    return p9.ggplot() + p9.theme_void()

                with_stages = add_life_stage(data)
                with_stages = with_stages.dropna(subset=["Life_Stage"])
                if with_stages.empty:
                    return p9.ggplot() + p9.theme_void()

                life_summary = (
                    with_stages
                    .groupby("Life_Stage", as_index=False)
                    .agg(Alcohol_Users=("Alcohol_Consumption", "size"))
                )

                total_alcohol_users = life_summary["Alcohol_Users"].sum()
                life_summary["Percent"] = (
                    life_summary["Alcohol_Users"] / total_alcohol_users * 100
                )
                life_summary["Label"] = life_summary["Percent"].round(1)

                g = (
                    p9.ggplot(life_summary, p9.aes(x="Life_Stage", y="Percent"))
                    + p9.geom_col(fill="#f97316")
                    + p9.geom_text(
                        p9.aes(label="Label"),
                        va="bottom",
                        nudge_y=1,
                        size=8,
                    )
                    + p9.theme_minimal()
                    + p9.labs(
                        title="Share of all alcohol users by life stage",
                        x="Life stage",
                        y="Percentage of all alcohol users (%)",
                    )
                )
                return g
