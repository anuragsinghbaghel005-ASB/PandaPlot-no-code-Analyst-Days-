import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
from wordcloud  import  WordCloud
from wordcloud import STOPWORDS
from collections import Counter
from datetime import datetime
import streamlit as st
import base64 
import csv
import re
import io
import os
import random
from fpdf import FPDF
import google.generativeai as genai
from matplotlib.axes import Axes
import seaborn as sns





# <script>
# window.addEventListener("message", (event) => {
#   if (event.data.type === "house_slider") {
#     const params = new URLSearchParams(window.location.search);
#     params.set("slider_value", event.data.value);
#     window.history.replaceState({}, "", `${location.pathname}?${params}`);
#   }
# });
# </script>


st.set_page_config(layout="wide")

st.title("📊 Pandaplot🧹")

st.sidebar.title("Sidebar")
st.sidebar.markdown("Streamlit's Sidebar ")


st.sidebar.subheader("System")

if "shows_ai" not in st.session_state:
    st.session_state.shows_ai = False
if "Chats" not in st.session_state:
    st.session_state.Chats=None


if st.sidebar.button("🤖  AI Tools"):
    st.session_state.shows_ai = True



    st.session_state.ai_box_color=random.choice([
                                                # Basic Colors
                                                "#FF0000",  # Red
                                                "#0000FF",  # Blue
                                                "#FFFF00",  # Yellow
                                                "#00FF00",  # Green
                                                "#000000",  # Black
                                                
                                                # Standard Colors
                                                "#1C2526",  # Navy Blue
                                                "#4A7043",  # Olive Green
                                                "#F7C7D2",  # Soft Pink
                                                "#8C8C8C",  # Warm Gray
                                                "#E07B39",  # Deep Orange
                                                
                                                # Extreme, Rare, Elegant, Beautiful, Yet Scary Colors
                                                "#2E1A47",  # Midnight Amethyst
                                                "#0B3D3D",  # Phantom Teal
                                                "#8B1E3F",  # Blood Amber
                                                "#E8E3D6",  # Spectral Ivory
                                                "#1A2249",  # Abyss Indigo
                                                "#A68A1B",  # Wraith Gold
                                                "#3B7B8C",  # Frostbite Cyan
                                                "#4A0F1B",  # Crimson Veil
                                                "#7B6E8C",  # Ghastly Lilac
                                                "#0F3D2E"   # Obsidian Emerald
                                            ])

if st.session_state.shows_ai:
    bck_grd=st.session_state.get("ai_box_color","#4f92d4")
    border_color=bck_grd

    with st.container():
        st.markdown(
            f"""
            <div style="
                border: 3px solid {border_color};
                padding: 20px;
                border-radius: 15px;
                background-color: {bck_grd};
                box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                margin-top: 15px;">
            """,
            unsafe_allow_html=True
        )

        st.subheader("Gem_AI Chat")
        st.write("Have Convo with Gemini")

        if st.button("❌ Close"):
            st.session_state.shows_ai = False

        st.markdown("</div>", unsafe_allow_html=True)

        

        apikey="AIzaSyCksEwIljDsUOFyz6tgjb4unT8ntYS2TX4"
        genai.configure(api_key=apikey)
        model=genai.GenerativeModel("gemini-2.0-flash")

        if st.session_state.Chats is None :
            st.session_state.Chats=model.start_chat()
        
        user_input=st.chat_input("Ask Anything.......")
        if user_input:
            st.chat_message("user").write(user_input)
            response = st.session_state.Chats.send_message(user_input)
            st.chat_message("assistant").write(response.text)


if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

if "Home" not in st.session_state:
    st.session_state.Home = {}

if "Dashboard_gallery" not in st.session_state :
    st.session_state.Dashboard_gallery=[]

if "lasst_figu" not in st.session_state:
    st.session_state.lasst_figu = None

# Navigation functions
def go_to_step1():
    st.session_state.step = 1
    st.query_params.clear()  # Clear query params to avoid conflicts

def go_to_step2():
    st.session_state.step = 2
    st.query_params.clear()

def go_to_step3():
    st.session_state.step = 3
    st.query_params.clear()

def go_to_step4():
    st.session_state.step= 4
    st.query_params.clear()

# Function to encode image to base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"Image file not found: {image_path}")
        return ""

# Check for query parameters to trigger navigation
query_params = st.query_params
if "go_to" in query_params:
    if query_params["go_to"] == "step2":
        go_to_step2()
    elif query_params["go_to"] == "step3":
        go_to_step3()

# Step 1: Home Page
if st.session_state.step == 1:
    st.header("🏠 Home Page")
    st.subheader("✨ A warm welcome to Pandaplot! Let's work together on your Data")
    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col_gap, col2 = st.columns([1, 0.4, 2])
    
    with col1:
        img_base64 = get_base64_image("D:\\python.1\\puru\\panda cleaner.jpeg")
        if img_base64:
            st.markdown(
                f"""
                <style>
                .clickable-image {{
                    cursor: pointer;
                    transition: transform 0.2s;
                }}
                .clickable-image:hover {{
                    transform: scale(1.05);
                }}
                </style>
                <a href="?go_to=step2">
                    <img src="data:image/jpeg;base64,{img_base64}" 
                         class="clickable-image" width="400">
                </a>
                """,
                unsafe_allow_html=True
            )

    with col2:
        img_base64 = get_base64_image("D:\\python.1\\puru\\panda.jpeg")
        if img_base64:
            st.markdown(
                f"""
                <style>
                .clickable-image {{
                    cursor: pointer;
                    transition: transform 0.2s;
                }}
                .clickable-image:hover {{
                    transform: scale(1.05);
                }}
                </style>
                <a href="?go_to=step3">
                    <img src="data:image/jpeg;base64,{img_base64}" 
                         class="clickable-image" width="400">
                </a>
                """,
                unsafe_allow_html=True
            )

    st.markdown("--------")

    # feedback section
    if st.button("Give Feedback ❤️"):
        st.session_state.show_feedback_form=True


    if st.session_state.get("show_feedback_form",False):

        cols1,col_gaps,cols2=st.columns([1,0.2,2])

        with cols1 :

            st.subheader("⭐ Rate PandaPlot")

            cols = st.columns(5)
            rating = st.session_state.get("rating", 0)

            for i, col in enumerate(cols, start=1):
                if col.button("⭐", key=f"star_{i}"):
                        st.session_state.rating = i
                        rating = i

            if rating > 0:
                st.success(f"You rated: {'⭐' * rating}")
    
        with cols2:
            st.subheader("📝 Give Feedback ")

            with st.form("Feedback_form"):
                user=st.text_input("Your name","")


                feedback=st.text_area("Write your feedback here.....")
                submitted=st.form_submit_button("Submit Feedback")

                if submitted :
                    with open("feedback.csv","a",newline="",encoding="utf-8") as f:
                        writer=csv.writer(f)
                        writer.writerow([datetime.now(),user, rating, feedback])
                        # st.markdown("❤️ Thank you for your feedback!")


                        st.success("Your Feedback makes us better,❤️ Thank you for your feedback")
                        st.markdown("--------")

                        st.markdown("### Recent FeedBack")
                        st.write(f"**Name** :{user}")
                        st.write(f"**Rating :** :{rating}")
                        st.write(f"***Feedback :** :{feedback}")

                        # reset button 
        if st.button("Reset"):      
            st.rerun()

            

# Step 2: Cleaner Page
elif st.session_state.step == 2:
    st.header("PandaPlot Cleaner 🧹")

    st.subheader("Welcome to Pandaplot Cleaning section")

    st.markdown("<br><br>", unsafe_allow_html=True)
    

    st.image(r"D:\\python.1\\puru\\panda cleaner.jpeg",width=500)
    st.markdown("<br><br>", unsafe_allow_html=True)

    def init_state():
        if "dirty_df" not in st.session_state:
            st.session_state["dirty_df"] = None
        if "cleaned_df" not in st.session_state:
            st.session_state["cleaned_df"] = None
        if "last_uploaded_name" not in st.session_state:
            st.session_state["last_uploaded_name"] = None


    # ----------------------- Utilities -----------------------
    
    def read_csv(file) -> pd.DataFrame:
        try:
            return pd.read_csv(file)
        except Exception:
            # try with io buffer
            file.seek(0)
            return pd.read_csv(io.StringIO(file.getvalue().decode("utf-8")))
    
    
    def df_info_as_text(df: pd.DataFrame) -> str:
        buf = io.StringIO()
        df.info(buf=buf)
        return buf.getvalue()
    
    
    # ----------------------- Smart Check -----------------------
    
    def smart_check(df:pd.DataFrame):
        st.subheader("👀 Preview")
        st.dataframe(df.head(20))
    
        st.subheader("📊 Info")
        st.text(df_info_as_text(df))
    
        st.subheader("📈 Description (numeric)")
        st.dataframe(df.describe())
    
        st.subheader("🧹 Nulls & Duplicates")
        st.write(df.isnull().sum())
        st.write("Duplicate rows present?", df.duplicated().any())
    
        null_percentage = df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100
        dup_percentage = df.duplicated().sum() / len(df) * 100
        st.write(f" - Null percentage: {null_percentage:.2f}%")
        st.write(f" - Duplicate percentage: {dup_percentage:.2f}%")
    
        if null_percentage > 2 or dup_percentage > 2:
            st.warning("⚠️ Null/duplicate values exceed 2%. Consider filling rather than dropping.")
        else:
            st.success("✅ Data looks OK (nulls & duplicates under control).")
    
        # outliers
        Outlier_reports = []
        for col in df.select_dtypes(include=[np.number]).columns:
            Q1, Q3 = df[col].quantile([0.25, 0.75])
            IQR = Q3 - Q1
            lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
            outliers = ((df[col] < lower) | (df[col] > upper)).sum()
            if outliers > 0:
                
                Outlier_reports.append((col, int(outliers), round(outliers / len(df) * 100, 2)))
    
        st.write(f"Outlier columns: {len(Outlier_reports)}")
        if Outlier_reports:
            st.dataframe(pd.DataFrame(Outlier_reports, columns=["Column", "Outlier Count", "Outlier %"]))
    
    
        st.markdown("---")
        st.download_button(
            "📥 Download this dataset (after Smart Check)",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="smart_checked.csv",
            mime="text/csv"
        )
    
    
    # ----------------------- Interactive Cleaning (persistent) -----------------------



    def handle_nan():
        df = st.session_state["cleaned_df"]
        null_percentage = df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100
        st.write(f"Dataset null percentage: {null_percentage:.2f}%")

        column_with_null = [c for c in df.columns if df[c].isnull().sum() > 0]
        if not column_with_null:
            st.success("✅ No missing values found.")
            return   # fixed

        st.info(f"Columns with missing values: {column_with_null}")

        with st.form("NaN_form"):
            choices = {}
            custom_value = {}
            for col in column_with_null:
                st.write(f"---\nColumn: {col} (missing: {int(df[col].isnull().sum())})")
                if pd.api.types.is_numeric_dtype(df[col]):
                    method = st.selectbox(
                        f"Method for {col}",
                        ["Mean", "Median", "Mode", "Interpolation", "Custom", "Skip"],
                        key=f"NaN_methods_{col}"
                    )
                    choices[col] = method
                    if method == "Custom":
                        custom_value[col] = st.text_input(f"Custom numeric value for {col}", key=f"NaN_custom_{col}")
                else:
                    method = st.selectbox(
                        f"Method for {col}",
                        ["Mode", "Unknown", "Forward Fill", "Backward Fill", "Custom", "Skip"],
                        key=f"NaN_methods_{col}"
                    )
                    choices[col] = method
                    if method == "Custom":
                        custom_value[col] = st.text_input(f"Custom value for {col}", key=f"NaN_custom_{col}")

            submit = st.form_submit_button("Apply NaN Handling")

        if submit:
            for col, method in choices.items():
                try:
                    if method == "Mean":
                        st.session_state["cleaned_df"][col] = st.session_state["cleaned_df"][col].fillna(
                            st.session_state["cleaned_df"][col].mean()
                        )
                    elif method == "Median":
                        st.session_state["cleaned_df"][col] = st.session_state["cleaned_df"][col].fillna(
                            st.session_state["cleaned_df"][col].median()
                        )
                    elif method == "Mode":
                        st.session_state["cleaned_df"][col] = st.session_state["cleaned_df"][col].fillna(
                            st.session_state["cleaned_df"][col].mode()[0]
                        )
                    elif method == "Interpolation":
                        st.session_state["cleaned_df"][col] = st.session_state["cleaned_df"][col].interpolate()
                    elif method == "Custom":
                        val = custom_value.get(col)
                        if val is not None and val != "":
                            if pd.api.types.is_numeric_dtype(st.session_state["cleaned_df"][col]):
                                st.session_state["cleaned_df"][col] = st.session_state["cleaned_df"][col].fillna(float(val))
                            else:
                                st.session_state["cleaned_df"][col] = st.session_state["cleaned_df"][col].fillna(val)
                    elif method == "Unknown":
                        st.session_state["cleaned_df"][col] = st.session_state["cleaned_df"][col].fillna("Unknown")
                    elif method == "Forward Fill":
                        st.session_state["cleaned_df"][col] = st.session_state["cleaned_df"][col].ffill()
                    elif method == "Backward Fill":
                        st.session_state["cleaned_df"][col] = st.session_state["cleaned_df"][col].bfill()
                    # Skip does nothing
                except Exception as e:
                    st.error(f"Error applying NaN method for {col}: {e}")
            st.success("✅ NaN handling applied to cleaned_df (persistent).")


    def handle_duplicates():
        df = st.session_state["cleaned_df"]
        dup_pct = df.duplicated().sum() / len(df) * 100
        st.write(f"Duplicate rows: {dup_pct:.2f}%")

        with st.form("dup_form"):
            method = st.selectbox(
                "Method",
                ["Show duplicates", "Drop all (keep first)", "Drop all (keep last)", "Drop by columns", "Ignore"],
                key="dup_method"
            )
            cols = None
            if method == "Drop by columns":
                cols = st.text_input("Columns (comma separated)")
            submit = st.form_submit_button("Apply Duplicate Action")

        if submit:
            if method == "Show duplicates":
                st.dataframe(df[df.duplicated(keep=False)])
            elif method == "Drop all (keep first)":
                st.session_state["cleaned_df"] = df.drop_duplicates(keep="first").reset_index(drop=True)
                st.success("✅ Duplicates dropped (kept first).")
            elif method == "Drop all (keep last)":
                st.session_state["cleaned_df"] = df.drop_duplicates(keep="last").reset_index(drop=True)
                st.success("✅ Duplicates dropped (kept last).")
            elif method == "Drop by columns" and cols:
                col_list = [c.strip() for c in cols.split(",")]
                st.session_state["cleaned_df"] = df.drop_duplicates(subset=col_list, keep="first").reset_index(drop=True)
                st.success(f"✅ Duplicates dropped using columns {col_list}.")
            else:
                st.info("No action taken.")


    def handle_dtypes():
        df = st.session_state["cleaned_df"]
        st.write(df.dtypes)

        with st.form("dtype_form"):
            conversions = {}
            for col in df.columns:
                st.write("---")
                st.write(f"Column: {col} (current: {df[col].dtype})")
                choice = st.selectbox(
                    f"Target type for {col}",
                    ["No change", "int", "float", "datetime", "category", "string", "boolean"],
                    key=f"dtype_choice_{col}"
                )
                conversions[col] = choice
            submit = st.form_submit_button("Apply Type Conversions")

        if submit:
            for col, choice in conversions.items():
                try:
                    if choice == "int":
                        cast = pd.to_numeric(st.session_state["cleaned_df"][col], errors="coerce")
                        st.session_state["cleaned_df"][col] = cast.astype("Int64")
                    elif choice == "float":
                        cast = pd.to_numeric(st.session_state["cleaned_df"][col], errors="coerce")
                        st.session_state["cleaned_df"][col] = cast.astype("float64")
                    elif choice == "datetime":
                        cast = pd.to_datetime(st.session_state["cleaned_df"][col], errors="coerce")
                        st.session_state["cleaned_df"][col] = cast
                    elif choice == "category":
                        st.session_state["cleaned_df"][col] = st.session_state["cleaned_df"][col].astype("category")
                    elif choice == "string":
                        st.session_state["cleaned_df"][col] = st.session_state["cleaned_df"][col].astype("string")
                    elif choice == "boolean":
                        boolean_map = {"true": True, "false": False, "1": True, "0": False, "yes": True, "no": False, "y": True, "n": False}
                        cast = st.session_state["cleaned_df"][col].astype(str).str.lower().map(boolean_map)
                        st.session_state["cleaned_df"][col] = cast.astype("boolean")
                except Exception as e:
                    st.error(f"Could not convert {col}: {e}")
            st.success("✅ Data type conversions applied (persistent).")


    def handle_column_names():
        df = st.session_state["cleaned_df"]
        st.write(df.columns.tolist())
        choice = st.selectbox("Column cleaning method", ["No change", "lowercase + underscores", "Titlecase + underscores"])
        if st.button("Apply column name cleaning"):
            if choice == "lowercase + underscores":
                st.session_state["cleaned_df"].columns = (
                    st.session_state["cleaned_df"].columns.str.lower().str.strip().str.replace(" ", "_", regex=False)
                )
                st.success("✅ Columns cleaned to lowercase + underscores")
            elif choice == "Titlecase + underscores":
                st.session_state["cleaned_df"].columns = (
                    st.session_state["cleaned_df"].columns.str.title().str.strip().str.replace(" ", "_", regex=False)
                )
                st.success("✅ Columns cleaned to Titlecase + underscores")


    def handle_row_filtering():
        df = st.session_state["cleaned_df"]
        st.info("Build a filter to reduce rows. This tool applies filters in sequence.")

        with st.form("filter_form"):
            filters = []
            col = st.selectbox("Column to filter", df.columns)
            if pd.api.types.is_numeric_dtype(df[col]):
                op = st.selectbox("Operation", ["==", ">", "<", "between"])
                if op == "between":
                    lo = st.number_input("Low", value=float(df[col].min()))
                    hi = st.number_input("High", value=float(df[col].max()))
                    filters.append((col, op, lo, hi))
                else:
                    val = st.number_input("Value", value=0.0)
                    filters.append((col, op, val))
            else:
                op = st.selectbox("Operation", ["equals", "contains", "startswith", "endswith", "in_list"])
                if op == "in_list":
                    vals = st.text_input("Comma-separated values")
                    vals = [v.strip() for v in vals.split(",")]
                    filters.append((col, op, vals))
                else:
                    val = st.text_input("Value")
                    filters.append((col, op, val))
            submit = st.form_submit_button("Apply filter")

        if submit:
            new_df = df.copy()
            for f in filters:
                if f[1] == "==":
                    new_df = new_df[new_df[f[0]] == f[2]]
                elif f[1] == ">":
                    new_df = new_df[new_df[f[0]] > f[2]]
                elif f[1] == "<":
                    new_df = new_df[new_df[f[0]] < f[2]]
                elif f[1] == "between":
                    new_df = new_df[(new_df[f[0]] >= f[2]) & (new_df[f[0]] <= f[3])]
                elif f[1] == "equals":
                    new_df = new_df[new_df[f[0]] == f[2]]
                elif f[1] == "contains":
                    new_df = new_df[new_df[f[0]].astype(str).str.contains(f[2], na=False)]
                elif f[1] == "startswith":
                    new_df = new_df[new_df[f[0]].astype(str).str.startswith(f[2], na=False)]
                elif f[1] == "endswith":
                    new_df = new_df[new_df[f[0]].astype(str).str.endswith(f[2], na=False)]
                elif f[1] == "in_list":
                    new_df = new_df[new_df[f[0]].isin(f[2])]
            st.session_state["cleaned_df"] = new_df.reset_index(drop=True)
            st.success("✅ Filter applied and saved to cleaned_df")


    def comparison_reports(dirty_df: pd.DataFrame, cleaned_df: pd.DataFrame) -> pd.DataFrame:
        memory_usage_dirty_df = dirty_df.memory_usage(deep=True).sum()
        memory_usage_cleaned_df = cleaned_df.memory_usage(deep=True).sum()
        reports = pd.DataFrame({
            "Before Cleaning": [
                dirty_df.shape[0],
                dirty_df.shape[1],
                dirty_df.isnull().sum().sum(),
                dirty_df.duplicated().sum(),
                dirty_df.isnull().sum().sum() / (dirty_df.shape[0] * dirty_df.shape[1]) * 100,
                dirty_df.duplicated().sum() / len(dirty_df) * 100,
                memory_usage_dirty_df / (1024 * 1024),
            ],
            "After Cleaning": [
                cleaned_df.shape[0],
                cleaned_df.shape[1],
                cleaned_df.isnull().sum().sum(),
                cleaned_df.duplicated().sum(),
                cleaned_df.isnull().sum().sum() / (cleaned_df.shape[0] * cleaned_df.shape[1]) * 100,
                cleaned_df.duplicated().sum() / len(cleaned_df) * 100,
                memory_usage_cleaned_df / (1024 * 1024),
            ],
        }, index=["Rows", "Columns", "Null Values", "Duplicate Rows", "Null percentage", "Duplicate percentage", "Memory usage (MB)"])
        return reports


    def app():
        st.set_page_config(page_title="Pandaplot's Cleaner", layout="wide")
        init_state()

        st.title("🐼🔹 Pandaplot's Cleaner 🔹🐼")

        tab_load, tab_check, tab_clean, tab_report = st.tabs(["Load", "Smart Check", "Interactive Cleaning", "Reports & Export"])

        with tab_load:
            uploaded_file = st.file_uploader("Upload CSV file", type=["csv"], key="file_uploader")
            if uploaded_file is not None:
                name = getattr(uploaded_file, "name", "uploaded.csv")
                if st.session_state["last_uploaded_name"] != name:
                    with st.spinner("Reading file..."):
                        df = read_csv(uploaded_file)
                        st.session_state["dirty_df"] = df.copy()
                        st.session_state["cleaned_df"] = df.copy()
                        st.session_state["last_uploaded_name"] = name
                        st.success("✅ File loaded into dirty_df and cleaned_df")
            if st.session_state["cleaned_df"] is not None:
                st.download_button(
                    "Download current cleaned_df (CSV)",
                    data=st.session_state["cleaned_df"].to_csv(index=False).encode("utf-8"),
                    file_name="cleaned.csv"
                )

        with tab_check:
            if st.session_state["cleaned_df"] is None:
                st.info("Upload a CSV in the Load tab first.")
            else:
                smart_check(st.session_state["cleaned_df"])

        with tab_clean:
            if st.session_state["cleaned_df"] is None:
                st.info("Upload a CSV in the Load tab first.")
            else:
                st.subheader("✨ Interactive Cleaning (changes are saved to cleaned_df)")
        
                with st.expander("🧩 Handle Missing Values (NaN)"):
                    handle_nan()
        
                with st.expander("📑 Handle Duplicates"):
                    handle_duplicates()
        
                with st.expander("🔠 Clean Column Names"):
                    handle_column_names()
        
                with st.expander("📊 Convert Data Types"):
                    handle_dtypes()
        
                with st.expander("🔎 Filter Rows"):
                    handle_row_filtering()
        
                st.subheader("Current cleaned_df preview")
                st.dataframe(st.session_state["cleaned_df"].head(200))


        with tab_report:
            if st.session_state["dirty_df"] is None:
                st.info("Upload a CSV in the Load tab first.")
            else:
                if st.session_state["dirty_df"].equals(st.session_state["cleaned_df"]):
                    st.info("No cleaning has been performed.")
                else:
                    st.subheader("Comparison Report")
                    st.dataframe(comparison_reports(st.session_state["dirty_df"], st.session_state["cleaned_df"]))

                st.markdown("---")
                st.download_button(
                    "Download cleaned CSV",
                    data=st.session_state["cleaned_df"].to_csv(index=False).encode("utf-8"),
                    file_name="cleaned.csv"
                )


    if __name__ == "__main__":
        app()



    

    col1,col_gap,col2=st.columns([1,0.2,2])

    with col1:
        st.button("➡️ Visualizer", on_click=go_to_step3)

    
    with col2:
    
        st.button("⬅️ Back to Home", on_click=go_to_step1)

# Step 3: Visualizer Page
elif st.session_state.step == 3:
    st.header("Pandaplot Visualizer 📊")

    st.subheader("Welcome to Pandaplot Visualiser")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.image(r"D:\\python.1\\puru\\panda.jpeg",width=500)
    st.markdown("<br><br>", unsafe_allow_html=True)



    
    
    def Data_Frame(df:pd.DataFrame):
        st.write("**Dataframe**")
        st.dataframe(df.head(50),use_container_width=True)
        st.write("**dtypes**")
        st.write(pd.DataFrame(df.dtypes, columns=["dtype"]))
    # 
    # 
        # Main part of program
    # 
    st.subheader(" Choose Dataset type ")
    main_choice=st.radio("Enter Choice",["Text Data","Numerical & Category"],horizontal=True,label_visibility="collapsed")
    # 
        # **********************************
    # 
        #    =========================
        #         Text DataSet
        #    =========================
    # 
        # **********************************
    # 
    if main_choice=="Text Data":
    # 
        st.info("Since you uploaded a text-like dataset, **WordCloud** or **Top‑N Frequency** is most useful.",icon="ℹ️")
    # 
        text_choice = st.radio(
            "Pick a visualization",
            ["WordCloud", "Top‑N Word Frequency"],
            horizontal=True,
        )
    # 
        st.markdown("## Upload .txt or .csv (if .csv, select the text column)")
        text_file=st.file_uploader("Upload  file here",type=["txt","csv"])
        text_data=""
        text_col=None
    # 
        if text_file is not None :
            if text_file.name.lower().endswith(".txt"):
                text_data= text_file.read().decode("utf-8", errors="ignore")
                # 
    # 
            else :
                df_text=pd.read_csv(text_file)
                st.write("Columns detected:", df_text.columns.tolist())
                text_col = st.selectbox("Pick  column to analyze", df_text.columns)
                if text_col:
                    text_data = " ".join(df_text[text_col].astype(str))
    # 
        # Choose chart option :-
        if text_choice=="WordCloud":
            st.markdown("## Wordcloud options")
            bg=st.selectbox("Background color",["white", "black", "ivory", "mintcream"],index=0)
            IP=st.selectbox("interpolation types",["bilinear", "bicubic", "nearest", "lanczos"],index=0)
    # 
            stopwords=set(STOPWORDS)
    # 
            # optional custom stop words 
            custom_stopwords= st.text_input("Add custom stopwords (comma-separated)",key="wc_stopwords")
            if custom_stopwords :
                stopwords |= {w.strip().lower() for w in custom_stopwords.split(",") if w.strip()}
    # 
            if text_data:
                print(len(text_data))  
                wc = WordCloud(width=1200, height=600, background_color=bg, stopwords=stopwords).generate(text_data)
                fig = plt.figure(figsize=(12, 6))
                plt.imshow(wc, interpolation=IP)
                plt.axis("off")
                st.pyplot(fig, use_container_width=True)
    # 
            else:
                st.warning("Upload a .txt or .csv and/or pick a column to generate WordCloud.")
    # 
        elif text_choice=="Top‑N Word Frequency":
    # 
            st.markdown("## Top‑N Word Frequency options")
            N=st.slider("Top-N", min_value=5, max_value=50, value=10, step=1)
            color_mode = st.radio("Color mode", ["single", "multi"], horizontal=True, index=1)
            stopwords = set(STOPWORDS)
    # 
            # custom stopwords
    # 
            custom_sw= st.text_input("Add custom stopwords (comma-separated)",key="frequency_stopwords")
            if custom_sw :
                stopwords |= {w.strip().lower() for w in custom_sw.split(",") if w.strip()}
    # 
            if text_data:
                words = [w.lower() for w in re.findall(r"\b\w+\b", text_data) if w.lower() not in stopwords]
                freq = Counter(words).most_common(N)
                freq_df = pd.DataFrame(freq, columns=["Word", "Frequency"])
                if color_mode == "single":
                    color_options = {
                                    "turquoise 🌊": "turquoise",
                                    "violet 💜": "violet",
                                    "tomato 🍅": "tomato",
                                    "gold ✨": "gold",
                                    "deepskyblue ☁️": "deepskyblue",
                                    "seagreen 🌿": "seagreen",
                                    "orchid 🌸": "orchid",
                                    "coral 🧡": "coral",
                                    }
    # 
    # 
                    color_choice = st.selectbox(
                                                "These are solid bar colors:",
                                                options=list(color_options.keys()),  # shows with emojis
                                                index=4, #default : deep skyblue
                                                key="topn_color_choice"
                                                )
                    color_name = color_options[color_choice]
    # 
                    st.write(f"You selected: **{color_choice}** → CSS color = `{color_name}`")
                    fig = px.bar(freq_df, x="Word", y="Frequency", title=f"Top {N} Word Frequencies", text="Frequency")
                    fig.update_traces(marker_color=color_name, textposition="outside")
                    fig.update_layout(yaxis_title=None, xaxis_title=None)
                    st.plotly_chart(fig, use_container_width=True)
    # 
                else :
                    color_available={
                        "tealrose🌊🌹":"tealrose",
                        "twilight 🌌":"twilight",
                        "Viridis 🔵🟢🟡": "viridis",
                        "Plasma 🔴🟡": "plasma",
                        "Cividis 🟡🟢": "cividis",
                        "Inferno 🔥": "inferno",
                        "Magma 🌑🔥": "magma",
                        "Turbo 🌈": "turbo",
                        "Hot 🔥": "hot",
                        "Blues 🌊": "blues",
                        # "🍫 Chocolate": "#D2691E",
                        # "🌲 DeepGreen": "#006400",
                        # "🌱 SpringGreen": "#00FF7F",
                        # "🍊 DarkOrange": "#FF8C00",
                        # "🌹 Crimson": "#DC143C",
                        # "🌿 OliveDrab": "#6B8E23",
                        # "👑 RoyalBlue": "#4169E1",
                        # "💜 MediumPurple": "#9370DB",
                        # "🌊 DarkCyan": "#008B8B",
                        # "🍅 Tomato": "#FF6347",
                        # "🪵 SaddleBrown": "#8B4513",
                        # "💐 DarkMagenta": "#8B008B",
                        # "🩵 SteelBlue": "#4682B4",
                        # "🌟 GoldenRod": "#DAA520",
                        # "🔥 FireBrick": "#B22222"
    # 
                        } 
    # 
                    available_color=st.selectbox("Choose Available color",options=list(color_available.keys()))
    # 
                    selected_scale=color_available[available_color]                    
    # 
                    fig = px.bar(freq_df,
                                    x="Word",
                                    y="Frequency",
                                    title=f"Top {N} Word Frequencies",
                                    text="Frequency",
                                    color="Frequency",  # Gradient color based on frequency
                                    color_continuous_scale=selected_scale)  # Nice looking scheme
                    # 
    # 
                    fig.update_layout(yaxis_title=None, xaxis_title=None)
                    st.plotly_chart(fig, use_container_width=True)
    # 
            else :
                st.warning("Upload a .txt or .csv and/or pick a column to compute frequencies.")
    # 
    # ==============================================
    # 
    #        Numerical + Categorical Dataset
    # 
    # ==============================================
    # 
    # 
    else :
        st.markdown("## Provide Data")
        data_typess= st.radio(
            "How would you like to Upload Data?",
            ["Upload CSV", "Paste Excel"],
            horizontal=True,
        )
        df=None
    # 
        if data_typess=="Upload CSV":
            up_load = st.file_uploader("Upload .csv or .CSV", type=["csv","CSV"])
    # 
            if up_load is not None:
                df = pd.read_csv(up_load)
            else :
                st.warning("Upload a File")
    # 
        else:
            up_load = st.file_uploader("Upload .xlsx", type=["xlsx"])
            if up_load is not None:
                df = pd.read_excel(up_load)
                st.success("Excel file uploaded successfully!")
            else:
                st.warning("Upload an Excel file...........")
    # 
        if df is not None :
            Data_Frame(df)
            st.markdown("## Pick a chart type")
            chart_types = [
                "Select chart...",
                "Bar Chart",
                "Pie Chart",
                "Scatter Chart",
                "Subplots (Two Histograms)",
                "Parallel Coordinates",
                "Heatmap (Correlation)",
                "Contour (Correlation)",
                "Histogram",
                "Parallel Categories",
                "Bubble Chart",
                "Box Plot",
                "Violin Plot",
                "3D Scatter",
                "3D Surface (Correlation)",
                "Area Chart",
                "KDE Plot" , 
                "Line Plot"
            ]
            choice = st.selectbox("", chart_types)
            cols = df.columns.tolist()
            num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    # 
            # -------- Bar Chart----------
    # 
            if choice=="Bar Chart":
                with st.expander("Plotly Chart",expanded=False):
                    st.subheader("Plotly Bar")
                    x = st.selectbox("x", cols)
                    y = st.selectbox("y", cols)
                    color_opt = st.selectbox("color (optional)", [None] + cols)
                    fig = px.bar(df, x=x, y=y, color=color_opt if color_opt else None)
                    st.plotly_chart(fig, use_container_width=True)
                    st.session_state["lasst_figu"] = fig 
       

                
   

                with st.expander("Matplotlib Chart",expanded=False):    
                    st.subheader("Matplotlib Bar Chart")

                    x = st.selectbox("X axis", cols)
                    y = st.selectbox("Y axis", cols)

                    # Chart labels + title inputs
                    xlabel = st.text_input("X-label", x)
                    ylabel = st.text_input("Y-label", y)
                    legend_label = st.text_input("Legend label", y)
                    title = st.text_input("Chart Title", f"{y} by {x}")

                    # Prepare data
                    x_vals = df[x].astype(str).tolist()
                    y_vals = pd.to_numeric(df[y], errors="coerce")

                    # Plot
                    fig, ax = plt.subplots(figsize=(10, 4))
                    ax.bar(x_vals, y_vals, label=legend_label, color="C0")

                    # Labels and title
                    ax.set_xlabel(xlabel)
                    ax.set_ylabel(ylabel)
                    ax.set_title(title)
                    ax.legend()

                    plt.xticks(rotation=45, ha="right")

                    st.pyplot(fig, use_container_width=True)
                    st.session_state["lasst_figu"] = fig 

                    
                
   

                
                
                with st.expander("Seaborn Bar Chart", expanded=False):
                
                    # --- BASIC SELECTORS ---
                    x_sns = st.selectbox("X axis (seaborn)", cols, key="x_sns")
                    y_sns = st.selectbox("Y axis (seaborn)", cols, key="y_sns")
                    hue_sns = st.selectbox("Hue (optional)", [None] + cols, key="hue_sns")
                
                    # --- LABELS & TITLE ---
                    xlabel_sns = st.text_input("X-label", x_sns, key="xlabel_sns")
                    ylabel_sns = st.text_input("Y-label", y_sns, key="ylabel_sns")
                    legend_label_sns = st.text_input("Legend label", y_sns, key="legend_sns")
                    title_sns = st.text_input("Chart Title", f"{y_sns} by {x_sns}", key="title_sns")
                
                    st.markdown("### Chart Settings")

                
                    # --- ADVANCED OPTIONS ---
                    colA, colB, colC = st.columns(3)
                
                    with colA:
                        estimator_opt = st.selectbox(
                            "Estimator", 
                            ["mean", "sum", "count", "median", "None (raw values)"], 
                            key="estimator_sns"
                        )
                        orientation = st.radio("Orientation", ["Vertical", "Horizontal"], key="orient_sns")
                
                    with colB:
                        ci_opt = st.selectbox(
                            "CI (Confidence Interval)", 
                            ["auto", 95, 68, None], 
                            key="ci_sns"
                        )
                        dodge_opt = st.checkbox("Dodge (side-by-side if Hue used)", True, key="dodge_sns")
                
                    with colC:
                        palette_opt = st.selectbox(
                            "Palette", 
                            ["deep", "pastel", "muted", "bright", "dark", "colorblind", "Set2", "Set3", "tab10"], 
                            key="palette_sns"
                        )
                        bar_width = st.slider("Bar width", 0.1, 1.0, 0.8, 0.05, key="width_sns")
                
                    # sort categories
                    order_opt = st.checkbox("Sort X values", False, key="order_sns")
                
                    # --- PREPARE DATA ---
                    data_sns = df.copy()
                
                    # SAFELY CONVERT Y COLUMN TO NUMERIC
                    col_data = data_sns[y_sns]
                
                    # If Y accidentally becomes DataFrame → STOP
                    if not isinstance(col_data, pd.Series):
                        st.error("Y axis must be **one single column**, not multiple.")
                        st.stop()
                
                    try:
                        data_sns[y_sns] = pd.to_numeric(col_data, errors="coerce")
                    except Exception as e:
                        st.error(f"Cannot convert Y to numeric: {e}")
                        st.stop()
                
                    # build x-axis order
                    if order_opt:
                        x_order = sorted(data_sns[x_sns].astype(str).unique())
                    else:
                        x_order = None
                
                    # estimator mapping
                    if estimator_opt == "mean":
                        estimator = np.mean
                    elif estimator_opt == "sum":
                        estimator = np.sum
                    elif estimator_opt == "count":
                        estimator = len
                    elif estimator_opt == "median":
                        estimator = np.median
                    else:
                        estimator = None   # raw values
                
                    # orientation
                    orient_value = "v" if orientation == "Vertical" else "h"
                
                    # --- PLOT ---
                    fig_sns, ax_sns = plt.subplots(figsize=(10, 5))
                
                    sns.barplot(
                        data=data_sns,
                        x=x_sns if orient_value == "v" else y_sns,
                        y=y_sns if orient_value == "v" else x_sns,
                        hue=hue_sns,
                        estimator=estimator,
                        ci=None if ci_opt == "auto" else ci_opt,
                        dodge=dodge_opt,
                        palette=palette_opt,
                        order=x_order,
                        width=bar_width,
                        ax=ax_sns
                    )
                
                    # LABELS
                    if orient_value == "v":
                        ax_sns.set_xlabel(xlabel_sns)
                        ax_sns.set_ylabel(ylabel_sns)
                    else:
                        ax_sns.set_xlabel(ylabel_sns)
                        ax_sns.set_ylabel(xlabel_sns)
                
                    ax_sns.set_title(title_sns)
                
                    # LEGEND
                    if hue_sns:
                        ax_sns.legend(title=hue_sns)
                    else:
                        ax_sns.legend([legend_label_sns])
                
                    plt.xticks(rotation=45, ha="right")
                
                    st.pyplot(fig_sns, use_container_width=True)
                    st.session_state["lasst_figu"] = fig 
                
                    if st.button("Save-Chart"):
                        if st.session_state.lasst_figu is None:
                            st.waring("NO Charts to save ")
                        else :
                            st.session_state.Dashboard_gallery.append(st.session_state.lasst_figu)
                            st.success("Chart saved to dashboard to queue!")

                
            # ---------- Pie chart ----------

            elif choice=="Pie Chart":
                st.title("Pie Chart Visualizer 🍰")

                st.write("# Checking Datatype...")

                for cols in df.columns:
                    st.write(f"**{cols}** : {df[cols].dtype}")

                numeric_cols=df.select_dtypes(include=['number'])

                if numeric_cols.empty:
                    st.warning("⚠️  No numeric columns found for Chart")

                else :
                    st.write("### Select Plot type..")

                    plot_type=st.radio("Select plot type :",[1, 2, 3],
                        format_func=lambda x: {1: "Subplots (Matplotlib)", 2: "Plotly Chart", 3: "Both"}[x])
                
                    if plot_type == 1:
                        st.write("### Matplotlib Subplots Pie Chart")
                        fig, ax = plt.subplots(figsize=(10, 10))
                        numeric_cols.plot(kind='pie', subplots=True, figsize=(10, 10))
                        st.pyplot(plt)
                
                    elif plot_type == 2:
                        st.write("### Plotly Pie Chart")
                        # Flatten numeric columns for plotly
                        melted_df = numeric_cols.reset_index().melt(id_vars="index", var_name="Category", value_name="Value")
                        fig = px.pie(melted_df, names="index", values="Value", color="Category", hole=0.5)
                        st.plotly_chart(fig)
                
                    else:
                        st.write("### Both Charts")
                
                        # Matplotlib
                        fig, ax = plt.subplots(figsize=(16, 13))
                        numeric_cols.plot(kind='pie', subplots=True, figsize=(16, 13))
                        st.pyplot(plt)
                
                        # Plotly
                        melted_df = numeric_cols.reset_index().melt(id_vars="index", var_name="Category", value_name="Value")
                        fig = px.pie(melted_df, names="index", values="Value", color="Category", hole=0.5)
                        st.plotly_chart(fig)

    
            # -----------Scatter Chart--------------
            elif choice=="Scatter Chart":
                x=st.selectbox("x",cols)
                y=st.selectbox("y",cols)
                color=st.selectbox("color",[None]+cols)
                fig = px.scatter(df, x=x, y=y, color=color if color else None, title="Scatter Chart")
                st.plotly_chart(fig,use_container_width=True)
    # 
            # 
            # ---------- Subplots ----------------
    # 
            elif choice=="Subplots (Two Histograms)":
                x=st.selectbox("First Numeric Column",num_cols)
                y=st.selectbox("Second Numeric Column",[ c for c in num_cols if c!=x] or num_cols)
                title=st.text_input("Title",value=f"{x} vs {y}")
                fig = make_subplots(rows=1, cols=2, subplot_titles=(x, y))
                # Add histogram of x
                fig.add_trace(go.Histogram(x=df[x], name=x), row=1, col=1)
                # Add histogram of y
                fig.add_trace(go.Histogram(x=df[y], name=y), row=1, col=2)
    # 
                fig.update_layout(title_text=title)
                st.plotly_chart(fig,use_container_width=True)
    # 
            #---------- Parallel Co-ordinates ----------------
    # 
            elif choice=="Parallel Coordinates":
    # 
                if not num_cols :
                    st.error(" No Numeric column found. .. ... ....")
    # 
                else :
                    dimension=st.multiselect("Select Multiple Dimesions",num_cols,default=num_cols[0:3])
    # 
                color=st.selectbox("Color",num_cols)
    # 
                color_opt={
                            # simple colors
                            "🍎 Red": "red",
                            "🍀 Green": "green",
                            "💧 Blue": "blue",
                            "🌕 Yellow": "yellow",
                            "⚫ Black": "black",
    # 
                            # Pretty colors
                            "tealrose🌊🌹":"tealrose",
                            "twilight 🌌":"twilight",
                            "Viridis 🔵🟢🟡": "viridis",
                            "Plasma 🔴🟡": "plasma",
                            "Cividis 🟡🟢": "cividis",
                            "Inferno 🔥": "inferno",
                            "Magma 🌑🔥": "magma",
                            "Turbo 🌈": "turbo",
                            "Hot 🔥": "hot",
                            "Blues 🌊": "blues",
    # 
                            # 15 Complex/Bold Colors
                            "🍫 Chocolate": "#D2691E",
                            "🌲 DeepGreen": "#006400",
                            "🌱 SpringGreen": "#00FF7F",
                            "🍊 DarkOrange": "#FF8C00",
                            "🌹 Crimson": "#DC143C",
                            "🌿 OliveDrab": "#6B8E23",
                            "👑 RoyalBlue": "#4169E1",
                            "💜 MediumPurple": "#9370DB",
                            "🌊 DarkCyan": "#008B8B",
                            "🍅 Tomato": "#FF6347",
                            "🪵 SaddleBrown": "#8B4513",
                            "💐 DarkMagenta": "#8B008B",
                            "🩵 SteelBlue": "#4682B4",
                            "🌟 GoldenRod": "#DAA520",
                            "🔥 FireBrick": "#B22222"
                        }
    # 
                select_color_opt = st.selectbox(
                "Pick a color",
                options=list(color_opt.keys()),index=10)
    # 
                selected_color_opt=color_opt[select_color_opt]
    # 
                if isinstance(selected_color_opt, str) and not selected_color_opt in px.colors.named_colorscales():
                    selected_color_opt = [selected_color_opt, selected_color_opt]
    # 
                if dimension:
                    fig = px.parallel_coordinates(df, dimensions=dimension, color=color, color_continuous_scale=selected_color_opt,title=f"Parallel Coordinates:{', '.join(dimension)}")
                    st.plotly_chart(fig,use_container_width=True)
                else:
                        st.warning("Pick at least one dimension.")
    # 
            # 
            # ==============================================
            # 
            #        "Heatmap (Correlation)"
            # 
            # ==============================================
    # 
            elif choice=="Heatmap (Correlation)":
                if not num_cols :
                    st.error("No numeric columns found ")
                else :
                    color_avai_={
                            # simple colors
                            "🍎 Red": "red",
                            "🍀 Green": "green",
                            "💧 Blue": "blue",
                            "🌕 Yellow": "yellow",
                            "⚫ Black": "black",
    # 
                            # Pretty colors
                            "tealrose🌊🌹":"tealrose",
                            "twilight 🌌":"twilight",
                            "Viridis 🔵🟢🟡": "viridis",
                            "Plasma 🔴🟡": "plasma",
                            "Cividis 🟡🟢": "cividis",
                            "Inferno 🔥": "inferno",
                            "Magma 🌑🔥": "magma",
                            "Turbo 🌈": "turbo",
                            "Hot 🔥": "hot",
                            "Blues 🌊": "blues",
    # 
                            # 15 Complex/Bold Colors
                            "🍫 Chocolate": "#D2691E",
                            "🌲 DeepGreen": "#006400",
                            "🌱 SpringGreen": "#00FF7F",
                            "🍊 DarkOrange": "#FF8C00",
                            "🌹 Crimson": "#DC143C",
                            "🌿 OliveDrab": "#6B8E23",
                            "👑 RoyalBlue": "#4169E1",
                            "💜 MediumPurple": "#9370DB",
                            "🌊 DarkCyan": "#008B8B",
                            "🍅 Tomato": "#FF6347",
                            "🪵 SaddleBrown": "#8B4513",
                            "💐 DarkMagenta": "#8B008B",
                            "🩵 SteelBlue": "#4682B4",
                            "🌟 GoldenRod": "#DAA520",
                            "🔥 FireBrick": "#B22222"
                        }
                    select_color_avai_=st.selectbox("🎨 Pick a color",options=list(color_avai_.keys()),index=10)
    # 
                    selected_color_avai_=color_avai_[select_color_avai_]
    # 
                    if isinstance(selected_color_avai_, str) and not selected_color_avai_ in px.colors.named_colorscales():
                        selected_color_avai_= [selected_color_avai_,selected_color_avai_]
    # 
    # 
                    cor = df[num_cols].corr()
                    fig = go.Figure(
                        go.Heatmap(
                            z=cor,
                            x=cor.columns,
                            y=cor.columns,
                            colorscale=selected_color_avai_,
                            text=cor.round(3),
                            texttemplate="%{text}",
                        )
                    )
                    fig.update_layout(title="Correlation Heatmap")
                    st.plotly_chart(fig, use_container_width=True)
    # 
            # ==============================================
            # 
            #        "Contour (Correlation)"
            # 
            # ==============================================   
    # 
            elif choice == "Contour (Correlation)":
                if not num_cols:
                    st.error("No numeric columns found.")
                else :
                    color_avai_lable={
                            # simple colors
                            "🍎 Red": "red",
                            "🍀 Green": "green",
                            "💧 Blue": "blue",
                            "🌕 Yellow": "yellow",
                            "⚫ Black": "black",
    # 
                            # Pretty colors
                            "tealrose🌊🌹":"tealrose",
                            "twilight 🌌":"twilight",
                            "Viridis 🔵🟢🟡": "viridis",
                            "Plasma 🔴🟡": "plasma",
                            "Cividis 🟡🟢": "cividis",
                            "Inferno 🔥": "inferno",
                            "Magma 🌑🔥": "magma",
                            "Turbo 🌈": "turbo",
                            "Hot 🔥": "hot",
                            "Blues 🌊": "blues",
    # 
                            # 15 Complex/Bold Colors
                            "🍫 Chocolate": "#D2691E",
                            "🌲 DeepGreen": "#006400",
                            "🌱 SpringGreen": "#00FF7F",
                            "🍊 DarkOrange": "#FF8C00",
                            "🌹 Crimson": "#DC143C",
                            "🌿 OliveDrab": "#6B8E23",
                            "👑 RoyalBlue": "#4169E1",
                            "💜 MediumPurple": "#9370DB",
                            "🌊 DarkCyan": "#008B8B",
                            "🍅 Tomato": "#FF6347",
                            "🪵 SaddleBrown": "#8B4513",
                            "💐 DarkMagenta": "#8B008B",
                            "🩵 SteelBlue": "#4682B4",
                            "🌟 GoldenRod": "#DAA520",
                            "🔥 FireBrick": "#B22222"
                        }
                    select_color_avai_lable=st.selectbox(" 🎨 Pick a color",options=list(color_avai_lable.keys()),index=13)
    # 
                    selected_select_color_avai_lable=color_avai_lable[select_color_avai_lable]
    # 
                    if isinstance(selected_select_color_avai_lable,str) and not selected_select_color_avai_lable in px.colors.named_colorscales():
                        selected_select_color_avai_lable=[selected_select_color_avai_lable,selected_select_color_avai_lable]
    # 
                    cor=df[num_cols].corr()
    # 
                    fig=go.Figure(go.Contour(
    # 
                            z=cor,
                            x=cor.columns,
                            y=cor.columns,
                            colorscale=selected_select_color_avai_lable,
                            text=cor.round(3),
                            texttemplate="%{text}",
                    ))
    # 
                    fig.update_layout(title="Contour Heatmap")
                    st.plotly_chart(fig, use_container_width=True)
    # 
            # ==============================================
            # 
            #      "Histogram"  
            # 
            # ============================================== 
    # 
            elif choice=="Histogram":
                x=st.selectbox("x",cols)
                color=st.selectbox("color(optional)",[None]+cols)
    # 
                custom_colors = {
                                "Classic Blue": "#1f77b4",
                                "Bright Orange": "#ff7f0e",
                                "Green": "#2ca02c",
                                "Red": "#d62728",
                                "Purple": "#9467bd",
    # 
                                "Cyan Teal": "#17becf",
                                "Olive Green": "#bcbd22",
                                "Pink Magenta": "#e377c2",
                                "Coffee Brown": "#8c564b",
                                "Neutral Gray": "#7f7f7f",
                                "Deep Pink": "#ff1493",
                                "Dark Turquoise": "#00ced1",
                                "Tomato": "#ff6347",
                                "Turquoise": "#40e0d0",
                                "Goldenrod": "#daa520",
                                "Slate Blue": "#6a5acd",
                                "Orange Red": "#ff4500",
                                "Light Sea Green": "#20b2aa",
                                "Pale Violet Red": "#db7093",
                                "Slate Gray": "#708090",
                                "Green Yellow": "#adff2f"
                            }
                # 
                select_name=st.selectbox("🎨 Select a color",options=list(custom_colors.keys()))
                selected_name=custom_colors[select_name]
    # 
                anime=st.selectbox("Animation(optional)",[None]+cols)
                bar_mode=st.selectbox("Bar_mode",["stack", "group", "relative", "overlay"])
                fig=px.histogram(df,x=x,color=color if color else None , color_discrete_sequence= [selected_name],animation_frame=anime if anime else  None)
                fig.update_layout(barmode=bar_mode)
                st.plotly_chart(fig,use_container_width=True)
    # 
            # ==============================================
            # 
            #        "Parallel Categories"
            # 
            # ==============================================    
    # 
    # 
            elif choice=="Parallel Categories":
                dimen_sion=st.multiselect("Dimensions (categorical or numeric)", cols, default=cols[:2])
                color=st.selectbox("Color(optional)",[None]+cols)
    # 
                color_opt_avai={
                            # simple colors
                            "🍎 Red": "red",
                            "🍀 Green": "green",
                            "💧 Blue": "blue",
                            "🌕 Yellow": "yellow",
                            "⚫ Black": "black",
    # 
                            # Pretty colors
                            "tealrose🌊🌹":"tealrose",
                            "twilight 🌌":"twilight",
                            "Viridis 🔵🟢🟡": "viridis",
                            "Plasma 🔴🟡": "plasma",
                            "Cividis 🟡🟢": "cividis",
                            "Inferno 🔥": "inferno",
                            "Magma 🌑🔥": "magma",
                            "Turbo 🌈": "turbo",
                            "Hot 🔥": "hot",
                            "Blues 🌊": "blues",
    # 
                            # 15 Complex/Bold Colors
                            "🍫 Chocolate": "#D2691E",
                            "🌲 DeepGreen": "#006400",
                            "🌱 SpringGreen": "#00FF7F",
                            "🍊 DarkOrange": "#FF8C00",
                            "🌹 Crimson": "#DC143C",
                            "🌿 OliveDrab": "#6B8E23",
                            "👑 RoyalBlue": "#4169E1",
                            "💜 MediumPurple": "#9370DB",
                            "🌊 DarkCyan": "#008B8B",
                            "🍅 Tomato": "#FF6347",
                            "🪵 SaddleBrown": "#8B4513",
                            "💐 DarkMagenta": "#8B008B",
                            "🩵 SteelBlue": "#4682B4",
                            "🌟 GoldenRod": "#DAA520",
                            "🔥 FireBrick": "#B22222"
                        } 
                select_color_opt_avai=st.selectbox( "🎨 Pick a color",options=list(color_opt_avai.keys()),index=13)
    # 
                selected_color_opt_avai=color_opt_avai[select_color_opt_avai]
    # 
                # 
    # 
                if dimen_sion:
                    if color and color in num_cols:
    # 
                        fig = px.parallel_categories(
                        df,
                        dimensions=dimen_sion,
                        color=color  ,
                        color_continuous_scale=(
                            selected_color_opt_avai
                            if selected_color_opt_avai in px.colors.named_colorscales()
                            else None
                        ))
    # 
                    else :
                        fig=px.parallel_categories(df,dimensions=dimen_sion,color=color if color else None,
                                                color_discrete_sequence=([selected_color_opt_avai] if selected_color_opt_avai not in px.colors.named_colorscales()  else None))
    # 
                    st.plotly_chart(fig, use_container_width=True)    
    # 
                else :
                    st.warning("Pick at least One Dimension")
    # 
            # ==============================================
            # 
            #        "Bubble Chart"
            # 
            # ==============================================    
    # 
            elif choice=="Bubble Chart":
                x=st.selectbox("x",cols)
                y=st.selectbox("y",[ c for c in cols if c!=x] or cols)
                size=st.selectbox("size(numeric)",num_cols)
                color=st.selectbox("color(optional)",[None]+cols)
    # 
                color_opt_avai_lable={
                            # simple colors
                            "🍎 Red": "red",
                            "🍀 Green": "green",
                            "💧 Blue": "blue",
                            "🌕 Yellow": "yellow",
                            "⚫ Black": "black",
    # 
                            # Pretty colors
                            "tealrose🌊🌹":"tealrose",
                            "twilight 🌌":"twilight",
                            "Viridis 🔵🟢🟡": "viridis",
                            "Plasma 🔴🟡": "plasma",
                            "Cividis 🟡🟢": "cividis",
                            "Inferno 🔥": "inferno",
                            "Magma 🌑🔥": "magma",
                            "Turbo 🌈": "turbo",
                            "Hot 🔥": "hot",
                            "Blues 🌊": "blues",
    # 
                            # 15 Complex/Bold Colors
                            "🍫 Chocolate": "#D2691E",
                            "🌲 DeepGreen": "#006400",
                            "🌱 SpringGreen": "#00FF7F",
                            "🍊 DarkOrange": "#FF8C00",
                            "🌹 Crimson": "#DC143C",
                            "🌿 OliveDrab": "#6B8E23",
                            "👑 RoyalBlue": "#4169E1",
                            "💜 MediumPurple": "#9370DB",
                            "🌊 DarkCyan": "#008B8B",
                            "🍅 Tomato": "#FF6347",
                            "🪵 SaddleBrown": "#8B4513",
                            "💐 DarkMagenta": "#8B008B",
                            "🩵 SteelBlue": "#4682B4",
                            "🌟 GoldenRod": "#DAA520",
                            "🔥 FireBrick": "#B22222"
                        }
                select_color_opt_avai_lable=st.selectbox( "🎨 Pick a color",options=list(color_opt_avai_lable.keys()),index=13)
    # 
                selected_color_opt_avai_lable=color_opt_avai_lable[select_color_opt_avai_lable]
    # 
                if color and color in num_cols and selected_color_opt_avai_lable in px.colors.named_colorscales():
                    # numeric column + valid colormap
                    fig = px.scatter(
                        df,
                        x=x,
                        y=y,
                        size=size,
                        color=color,
                        color_continuous_scale=selected_color_opt_avai_lable,
                        hover_data=cols
                    )
                else:
                    # categorical or no color → just use selected fixed color
                    fig = px.scatter(
                        df,
                        x=x,
                        y=y,
                        size=size,
                        color=color if color else None,
                        hover_data=cols
                    )
                    if not color:
                        # Apply fixed chosen color to all markers
                        fig.update_traces(marker=dict(color=selected_color_opt_avai_lable))
    # 
                st.plotly_chart(fig, use_container_width=True)
    # 
            # ==============================================
            # 
            #                "Box Plot" 
            # 
            # ==============================================    
            # 
            elif choice=="Box Plot":
                x=st.selectbox("x",cols)
                y=st.selectbox("y",cols)
                color=st.selectbox("color", [None]+cols)
    # 
                custom_col_ors = {
                                "Classic Blue": "#1f77b4",
                                "Bright Orange": "#ff7f0e",
                                "Green": "#2ca02c",
                                "Red": "#d62728",
                                "Purple": "#9467bd",
    # 
                                "Cyan Teal": "#17becf",
                                "Olive Green": "#bcbd22",
                                "Pink Magenta": "#e377c2",
                                "Coffee Brown": "#8c564b",
                                "Neutral Gray": "#7f7f7f",
                                "Deep Pink": "#ff1493",
                                "Dark Turquoise": "#00ced1",
                                "Tomato": "#ff6347",
                                "Turquoise": "#40e0d0",
                                "Goldenrod": "#daa520",
                                "Slate Blue": "#6a5acd",
                                "Orange Red": "#ff4500",
                                "Light Sea Green": "#20b2aa",
                                "Pale Violet Red": "#db7093",
                                "Slate Gray": "#708090",
                                "Green Yellow": "#adff2f"
                            }
                select_na_me=st.selectbox("🎨 Select a color",options=list(custom_col_ors.keys()))
                selected_na_me=custom_col_ors[select_na_me]
                # 
                # 
                if color and color in num_cols:
                    # numeric column → continuous scale
                    fig = px.box(df, x=x, y=y, color=color)
                else:
                    # no color or categorical → use selected color
                    fig = px.box(
                        df,
                        x=x,
                        y=y,
                        color=color if color else None,
                        color_discrete_sequence=[selected_na_me]
                    )
                st.plotly_chart(fig, use_container_width=True)
    # 
            # ==============================================
            # 
            #              "Violin Plot"   
            # 
            # ============================================== 
            # 
    # 
            elif choice=="Violin Plot":
                with st.expander("Plotly Chart",expanded=False):
                    st.subheader("Plotly Violin")

                    categorical_cols = [c for c in cols if c not in num_cols]
                    # 
                    ori=st.selectbox("Select orientation",["v(vertical)","h(horizontal)"])
                    if ori.startswith("v"):
                        x=st.selectbox("x(categorical)",categorical_cols)
                        y=st.selectbox("y(numerical)",num_cols)
                        orientation="v"
    #   
                    else:
                        x=st.selectbox("x(numerical)",num_cols)
                        y=st.selectbox("y(categorical)",categorical_cols)
                        orientation="h"
    #   
                    # 
                    color = st.selectbox("color (optional)", [None] + cols)
                    # 
                    fig = px.violin(df, x=x, y=y, color=color if color else None, box=True, points="all", hover_data=cols,orientation=orientation)
                    # 
                    st.plotly_chart(fig, use_container_width=True)

                with st.expander("Sns Chart",expanded=False):
                    st.subheader("Sns Violin")
                    if not num_cols:
                        st.error("No numeric columns found.")
                    else:
                        st.subheader("Violin Plot (Seaborn)")

                        # Column selector
                        col = st.selectbox("Select numeric column", num_cols)

                        # Show inner options
                        inner_opt = st.selectbox(
                            "Inner display",
                            ["box", "quartiles", "stick", None],
                            index=0
                        )

                        # ---- Color Options (same as KDE) ----
                        violin_colors = {
                            "🍎 Red": "red",
                            "🍀 Green": "green",
                            "💧 Blue": "blue",
                            "🌕 Yellow": "yellow",
                            "⚫ Black": "black",
                            "🍫 Chocolate": "#D2691E",
                            "🌲 DeepGreen": "#006400",
                            "🌱 SpringGreen": "#00FF7F",
                            "🍊 DarkOrange": "#FF8C00",
                            "🌹 Crimson": "#DC143C",
                            "🌿 OliveDrab": "#6B8E23",
                            "👑 RoyalBlue": "#4169E1",
                            "💜 MediumPurple": "#9370DB",
                            "🌊 DarkCyan": "#008B8B",
                            "🍅 Tomato": "#FF6347",
                            "🪵 SaddleBrown": "#8B4513",
                            "💐 DarkMagenta": "#8B008B",
                            "🩵 SteelBlue": "#4682B4",
                            "🌟 GoldenRod": "#DAA520",
                            "🔥 FireBrick": "#B22222"
                        }

                        selected_color = st.selectbox(
                            "🎨 Pick a color",
                            list(violin_colors.keys()),
                            index=10
                        )

                        violin_color_value = violin_colors[selected_color]

                        # ---- Plot ----
                        import matplotlib.pyplot as plt
                        import seaborn as sns

                        fig, ax = plt.subplots(figsize=(7, 4))

                        sns.violinplot(
                            data=df,
                            y=col,
                            inner=inner_opt,
                            color=violin_color_value,
                            ax=ax
                        )

                        ax.set_title(f"Violin Plot of {col}")
                        ax.set_ylabel(col)

                        st.pyplot(fig)
            # ==============================================
            # 
            #          "3D Scatter"       
            # 
            # ============================================== 
    # 
            elif choice=="3D Scatter":
                if len(num_cols) < 3:
                    st.error("Need at least three numeric columns for 3D scatter.")
                else:
                    x = st.selectbox("x", num_cols)
                    y = st.selectbox("y", [c for c in num_cols if c != x] or num_cols)
                    z = st.selectbox("z", [c for c in num_cols if c not in {x, y}] or num_cols)
                    color = st.selectbox("color (optional)", [None] + cols)
                    scale_color = {
                            # simple colors
                            "🍎 Red": "red",
                            "🍀 Green": "green",
                            "💧 Blue": "blue",
                            "🌕 Yellow": "yellow",
                            "⚫ Black": "black",
    # 
                            # Pretty colors
                            "tealrose🌊🌹":"tealrose",
                            "twilight 🌌":"twilight",
                            "Viridis 🔵🟢🟡": "viridis",
                            "Plasma 🔴🟡": "plasma",
                            "Cividis 🟡🟢": "cividis",
                            "Inferno 🔥": "inferno",
                            "Magma 🌑🔥": "magma",
                            "Turbo 🌈": "turbo",
                            "Hot 🔥": "hot",
                            "Blues 🌊": "blues",
    # 
                            # 15 Complex/Bold Colors
                            "🍫 Chocolate": "#D2691E",
                            "🌲 DeepGreen": "#006400",
                            "🌱 SpringGreen": "#00FF7F",
                            "🍊 DarkOrange": "#FF8C00",
                            "🌹 Crimson": "#C90771AB",
                            "🌿 OliveDrab": "#6B8E23",
                            "👑 RoyalBlue": "#4169E1",
                            "💜 MediumPurple": "#9370DB",
                            "🌊 DarkCyan": "#008B8B",
                            "🍅 Tomato": "#FF6347",
                            "🪵 SaddleBrown": "#8B4513",
                            "💐 DarkMagenta": "#8B008B",
                            "🩵 SteelBlue": "#4682B4",
                            "🌟 GoldenRod": "#DAA520",
                            "🔥 FireBrick": "#B22222"
                        }
                    # 
                    select_scale_color=st.selectbox( "🎨 Pick a color",options=list(scale_color.keys()),index=13)
                    selected_scale_color=scale_color[select_scale_color]
                    if isinstance(selected_scale_color,str) and not selected_scale_color in px.colors.named_colorscales():
                        selected_select_color_avai_lable=[selected_scale_color,selected_scale_color]
    # 
                    fig = px.scatter_3d(
                        df, x=x, y=y, z=z, color=color if color else None, color_continuous_scale=selected_scale_color if color and color in num_cols else None
                    )
                    st.plotly_chart(fig, use_container_width=True)
    # 
            # ==============================================
            # 
            #          "3D Surface (Correlation)"       
            # 
            # ============================================== 
    # 
            elif choice=="3D Surface (Correlation)":
    # 
                if not num_cols:
                    st.error("No Numeric columns  found")
                else :
                    scales_colors = {
                            # simple colors
                            "🍎 Red": "red",
                            "🍀 Green": "green",
                            "💧 Blue": "blue",
                            "🌕 Yellow": "yellow",
                            "⚫ Black": "black",
    # 
                            # Pretty colors
                            "tealrose🌊🌹":"tealrose",
                            "twilight 🌌":"twilight",
                            "Viridis 🔵🟢🟡": "viridis",
                            "Plasma 🔴🟡": "plasma",
                            "Cividis 🟡🟢": "cividis",
                            "Inferno 🔥": "inferno",
                            "Magma 🌑🔥": "magma",
                            "Turbo 🌈": "turbo",
                            "Hot 🔥": "hot",
                            "Blues 🌊": "blues",
    # 
                            # 15 Complex/Bold Colors
                            "🍫 Chocolate": "#D2691E",
                            "🌲 DeepGreen": "#006400",
                            "🌱 SpringGreen": "#00FF7F",
                            "🍊 DarkOrange": "#FF8C00",
                            "🌹 Crimson": "#C90771AB",
                            "🌿 OliveDrab": "#6B8E23",
                            "👑 RoyalBlue": "#4169E1",
                            "💜 MediumPurple": "#9370DB",
                            "🌊 DarkCyan": "#008B8B",
                            "🍅 Tomato": "#FF6347",
                            "🪵 SaddleBrown": "#8B4513",
                            "💐 DarkMagenta": "#8B008B",
                            "🩵 SteelBlue": "#4682B4",
                            "🌟 GoldenRod": "#DAA520",
                            "🔥 FireBrick": "#B22222"
                        }
                    # 
                    select_scales_colors=st.selectbox( "🎨 Pick a color",options=list(scales_colors.keys()),index=13)
                    selected_scales_colors=scales_colors[select_scales_colors]
                    if not selected_scales_colors in px.colors.named_colorscales():
                        selected_scales_colors = [[0, selected_scales_colors], [1, selected_scales_colors]]
    # 
    # 
                    cor = df[num_cols].corr()
                    fig=go.Figure(go.Surface(z=cor,x=cor.columns,y=cor.columns,colorscale=selected_scales_colors))
                    fig.update_layout(scene=dict(zaxis=dict(title="Correlation")))
                    st.plotly_chart(fig, use_container_width=True)
    # 
    # 
            # ==============================================
            # 
            #          "Area chart"       
            # 
            # ============================================== 
    # 
            elif choice=="Area Chart":
                x=st.selectbox("x",cols) 
                y=st.selectbox("y",cols) 
                color=st.selectbox("color",[None]+cols)
                fig=px.area(df,x=x,y=y,color=color if color else None,title=f"Area Chart of {x} & {y} ")
                st.plotly_chart(fig, use_container_width=True)

            # ==============================================
            # 
            #          "KDE Plot "       
            # 
            # ============================================== 


            elif choice == "KDE Plot":
                if not num_cols:
                    st.error("No numeric columns found.")
                else:
                    st.subheader("KDE Plot (Seaborn)")

                    col = st.selectbox("Select numeric column", num_cols)
                    fill_opt = st.checkbox("Fill KDE", value=True)
                    bw = st.slider("Bandwidth (smaller → sharper curve)", 0.1, 2.0, 0.4)

                    # ---- Color Options ----
                    kde_colors = {
                        "🍎 Red": "red",
                        "🍀 Green": "green",
                        "💧 Blue": "blue",
                        "🌕 Yellow": "yellow",
                        "⚫ Black": "black",
                        "🍫 Chocolate": "#D2691E",
                        "🌲 DeepGreen": "#006400",
                        "🌱 SpringGreen": "#00FF7F",
                        "🍊 DarkOrange": "#FF8C00",
                        "🌹 Crimson": "#DC143C",
                        "🌿 OliveDrab": "#6B8E23",
                        "👑 RoyalBlue": "#4169E1",
                        "💜 MediumPurple": "#9370DB",
                        "🌊 DarkCyan": "#008B8B",
                        "🍅 Tomato": "#FF6347",
                        "🪵 SaddleBrown": "#8B4513",
                        "💐 DarkMagenta": "#8B008B",
                        "🩵 SteelBlue": "#4682B4",
                        "🌟 GoldenRod": "#DAA520",
                        "🔥 FireBrick": "#B22222"
                    }

                    selected_color = st.selectbox("🎨 Pick a color", kde_colors.keys(), index=10)
                    kde_color_value = kde_colors[selected_color]

                    # ---- Plot KDE ----


                    fig, ax = plt.subplots(figsize=(7, 4))
                    sns.kdeplot(
                        data=df,
                        x=col,
                        fill=fill_opt,
                        bw_method=bw,
                        color=kde_color_value,
                        ax=ax
                    )

                    ax.set_title(f"KDE Plot of {col}")
                    ax.set_xlabel(col)
                    ax.set_ylabel("Density")
                    st.pyplot(fig)

            # ==============================================
            # 
            #          "Line plot "       
            # 
            # ============================================== 
            # elif choice == "Line Plot":
    
            #     with st.expander("Plotly Line plot",expanded=False):    
            #         st.subheader("Plotly Line Plot")

            #         if not num_cols:
            #             st.error("No numeric columns found for line plot.")
            #         else:
            #             st.subheader("Line Plot (Simple + Color Options)")

            #             x_col = st.selectbox("Select X-axis", df.columns)
            #             y_col = st.selectbox("Select Y-axis", num_cols)

            #             group_col = st.selectbox("Group by (Optional)", [None] + df.columns.tolist())

            #             # ---- SAME COLOR LIST YOU USED BEFORE ----
            #             color_options = {
            #                 "🍎 Red": "red",
            #                 "🍀 Green": "green",
            #                 "💧 Blue": "blue",
            #                 "🌕 Yellow": "yellow",
            #                 "⚫ Black": "black",
            #                 "🍫 Chocolate": "#D2691E",
            #                 "🌲 DeepGreen": "#006400",
            #                 "🌱 SpringGreen": "#00FF7F",
            #                 "🍊 DarkOrange": "#FF8C00",
            #                 "🌹 Crimson": "#DC143C",
            #                 "🌿 OliveDrab": "#6B8E23",
            #                 "👑 RoyalBlue": "#4169E1",
            #                 "💜 MediumPurple": "#9370DB",
            #                 "🌊 DarkCyan": "#008B8B",
            #                 "🍅 Tomato": "#FF6347",
            #                 "🪵 SaddleBrown": "#8B4513",
            #                 "💐 DarkMagenta": "#8B008B",
            #                 "🩵 SteelBlue": "#4682B4",
            #                 "🌟 GoldenRod": "#DAA520",
            #                 "🔥 FireBrick": "#B22222"
            #             }

            #             selected_color = st.selectbox("Line Color", list(color_options.keys()), index=2)
            #             chosen_color = color_options[selected_color]

            #             # ---- PLOT ----
            #             fig = px.line(
            #                 df,
            #                 x=x_col,
            #                 y=y_col,
            #                 color=group_col if group_col else None,
            #                 markers=True
            #             )

            #             # If NO grouping → apply only 1 color
            #             if group_col is None:
            #                 fig.update_traces(line=dict(color=chosen_color))
            #             else:
            #                 # If grouping is present → apply palette (repeat chosen color)
            #                 fig.update_traces(line=dict(color=chosen_color))

            #             fig.update_layout(
            #                 title=f"Line Plot: {y_col} vs {x_col}",
            #                 xaxis_title=x_col,
            #                 yaxis_title=y_col,
            #                 height=500
            #             )

            #             st.plotly_chart(fig, use_container_width=True)

            #     with st.expander("Sns Line Plot",expanded=False):    
            #         st.subheader("Sns Line Plot")

            #         if not num_cols:
            #             st.error("No numeric columns found.")
            #         else:
            #             st.subheader("Line Plot (Seaborn)")

            #             # X and Y selectors
            #             x_col = st.selectbox("Select X-axis", df.columns)
            #             y_col = st.selectbox("Select Y-axis", num_cols)

            #             # Optional grouping (hue)
            #             hue_col = st.selectbox(
            #                 "Group by (Optional)",
            #                 [None] + df.columns.tolist(),
            #                 index=0
            #             )

            #             # ---- Color Options ----
            #             sns_colors = {
            #                 "🍎 Red": "red",
            #                 "🍀 Green": "green",
            #                 "💧 Blue": "blue",
            #                 "🌕 Yellow": "yellow",
            #                 "⚫ Black": "black",
            #                 "🍫 Chocolate": "#D2691E",
            #                 "🌲 DeepGreen": "#006400",
            #                 "🌱 SpringGreen": "#00FF7F",
            #                 "🍊 DarkOrange": "#FF8C00",
            #                 "🌹 Crimson": "#DC143C",
            #                 "🌿 OliveDrab": "#6B8E23",
            #                 "👑 RoyalBlue": "#4169E1",
            #                 "💜 MediumPurple": "#9370DB",
            #                 "🌊 DarkCyan": "#008B8B",
            #                 "🍅 Tomato": "#FF6347",
            #                 "🪵 SaddleBrown": "#8B4513",
            #                 "💐 DarkMagenta": "#8B008B",
            #                 "🩵 SteelBlue": "#4682B4",
            #                 "🌟 GoldenRod": "#DAA520",
            #                 "🔥 FireBrick": "#B22222"
            #             }

            #             selected_color = st.selectbox("Line Color", list(sns_colors.keys()), index=2)
            #             chosen_color = sns_colors[selected_color]

            #             # ---- Plot ----
            #             fig, ax = plt.subplots(figsize=(7, 4))

            #             sns.lineplot(
            #                 data=df,
            #                 x=x_col,
            #                 y=y_col,
            #                 hue=hue_col if hue_col else None,
            #                 color=None if hue_col else chosen_color,  # single color only when no hue
            #                 ax=ax,
            #                 marker="o"
            #             )

            #             ax.set_title(f"Line Plot: {y_col} vs {x_col}")
            #             ax.set_xlabel(x_col)
            #             ax.set_ylabel(y_col)

            #             st.pyplot(fig)




            if st.button("Save this Chart"):
                st.session_state.Dashboard_gallery.append(fig)
                st.success("Chart saved to Dashboard queue!")

            st.markdown("-------")
            st.subheader("Dashboard View")

            if st.button("Make Dashboard"):

                col1,col2=st.columns(2)

                for i, fig in enumerate(st.session_state.Dashboard_gallery):
                    if i%2==0:
                        current_col=col1
                    else:
                        current_col=col2

                    if isinstance(fig,plt.Figure):
                        current_col.pyplot(fig)

                    elif isinstance(fig, Axes):     # Seaborn figure (sns plots return Axes)
                        seaborn_fig = fig.get_figure()   # extract the underlying Figure
                        current_col.pyplot(seaborn_fig, key=f"sns_plot_{i}")
                
                    else:
                        current_col.plotly_chart(fig,use_container_width=True,key=f"chart_{i}")

                    
            
                def generate_html_dashboard(chart_list):
                    html = """
                    <html>
                    <head>
                        <title>PandaPlot Dashboard</title>
                        <style>
                            body { font-family: sans-serif; margin: 40px; background-color: #f0f2f6; }
                            .card { background: white; padding: 20px; margin-bottom: 30px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
                            h2 { border-bottom: 1px solid #eee; padding-bottom: 10px; color: #333; }
                        </style>
                    </head>
                    <body>
                        <h1 style='text-align:center; color:#0e1117;'>📊 PandaPlot Dashboard</h1>
                    """
                    for i, fig in enumerate(chart_list):
                        html += f"<div class='card'><h2>Chart {i+1}</h2>"
                        # 1. IF PLOTLY (Interactive)
                        if hasattr(fig, 'to_html'):
                            # include_plotlyjs='cdn' keeps the file size manageable
                            html += fig.to_html(full_html=False, include_plotlyjs='cdn')
                        # 2. IF MATPLOTLIB / SEABORN (Static)
                        else:
                            # Safety Check: If it's a Seaborn 'Axes', get the 'Figure'
                            if hasattr(fig, 'get_figure'):
                                fig = fig.get_figure()
                            # Save as Base64 Image
                            buf = io.BytesIO()
                            fig.savefig(buf, format='png', bbox_inches='tight')
                            buf.seek(0)
                            img_str = base64.b64encode(buf.read()).decode()
                            html += f'<div style="text-align:center"><img src="data:image/png;base64,{img_str}" style="max-width:100%"/></div>'
                        html += "</div>"
                    html += "</body></html>"
                    return html
                
                    # ... your existing loop for displaying charts ends here ...

                st.markdown("---")
                
                # The Download Button
                if len(st.session_state.Dashboard_gallery) > 0:
                    html_data = generate_html_dashboard(st.session_state.Dashboard_gallery)
                    
                    st.download_button(
                        label="📥 Download Dashboard as HTML",
                        data=html_data,
                        file_name="My_PandaPlot_Dashboard.html",
                        mime="text/html"
                    )

        else:
            st.warning("Upload a dataset or paste CSV to continue.")
    # else:
    #        pass              
    
    

    st.markdown("<br><br>", unsafe_allow_html=True)


    col1,col_gap,col2=st.columns([1,0.2,2])

    st.markdown("<br><br>", unsafe_allow_html=True)
    with col1:

        st.button("⬅️ Back to Cleaner", on_click=go_to_step2)

    
    with col2:

        st.button("🏠 Home", on_click=go_to_step1)



# elif st.session_state.step == 4:
#     with st.container():
#         st.markdown(
#             """
#             <div style="
#                 border: 2px solid #4CAF50;
#                 padding: 20px;
#                 border-radius: 15px;
#                 background-color: #f9f9f9;
#                 box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
#                 margin-top: 15px;">
#             """,
#             unsafe_allow_html=True
#         )
#         st.subheader("🤖 AI Tools Box")
#         st.write("Here you can add your AI data cleaning, filtering, summarization, etc.")
#         st.button("❌ Close", on_click=lambda: st.session_state.update({"show_ai": False}))
#         st.markdown("</div>", unsafe_allow_html=True)
    
#     apikey= "AIzaSyCksEwIljDsUOFyz6tgjb4unT8ntYS2TX4"
#     genai.configure(api_key=apikey)
#     model=genai.GenerativeModel("gemini-2.0-flash")
#     chat=model.start_chat()
#     print("chat with GEMINI GENERATIVEAI")
#     while True:
#         user_input=input("YOU :- ")
#         if user_input.lower()=="exit":
#             break
#         response=chat.send_message(user_input)
#         print("genai:",response.text)

