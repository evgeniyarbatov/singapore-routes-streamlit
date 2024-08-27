import streamlit as st
import json

ROUTES_DIR = 'routes'

def get_distance(item):
    return float(item['distance'].replace('km', ''))

def main():
    st.title("Singapore Running Routes")

    with open(f'{ROUTES_DIR}/metadata.json') as f:
        config = json.load(f)

    config = sorted(config, key=get_distance)

    for _, route in enumerate(config):
        st.subheader(f'{route["name"]} - {route["distance"]}')
        
        gpx_path = f"{ROUTES_DIR}/{route['gpx']}"
        with open(gpx_path, 'rb') as file:
            st.download_button(
                label="GPX",
                data=file,
                file_name=gpx_path.split('/')[-1],
                mime="application/gpx+xml",
                type="primary",
                use_container_width=True
            )

        st.image(
            f"{ROUTES_DIR}/{route['map']}",
        )

if __name__ == "__main__":
    main()
