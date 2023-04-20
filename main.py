import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
        {
           "command": "st.selectbox",
           "rating": 4,
           "is_widget": True,
           "icon": "🔘"
        },
        {
           "command": "st.balloons",
           "rating": 5,
           "is_widget": False,
           "icon": "🎈"
        },
        {
            "command": "st.time_input",
            "rating": 3,
            "is_widget": True,
            "icon": "⏱️"
        },
   ]
)
edited_df = st.experimental_data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
favorite_icon = edited_df.loc[edited_df["rating"].idxmax()]["icon"]
st.markdown(f"Your favorite command is **{favorite_command}** {favorite_icon}")