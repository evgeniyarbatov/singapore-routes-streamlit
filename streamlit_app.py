import streamlit as st
import json

def main():
    st.title("Singapore Running Routes")

    st.markdown(
        """
        <div style='text-align: center;'>
            <h1>Welcome to My Streamlit App</h1>
            <p>This is an introduction to the app. Here, you can find various features and functionalities.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with open('routes/metadata.json') as f:
        config = json.load(f)

    num_cols = 1
    cols = st.columns(num_cols)

    for i, route in enumerate(config):
        col = cols[i % num_cols]
        with col:
            st.subheader(route["distance"])
            st.image(
                f"routes/{route['map']}", 
                use_column_width = True,
            )
            
            gpx_path = f"routes/{route['gpx']}"
            with open(gpx_path, 'rb') as file:
                btn = st.download_button(
                    label="GPX",
                    data=file,
                    file_name=gpx_path.split('/')[-1],
                    mime="application/gpx+xml"
                )

if __name__ == "__main__":
    main()
