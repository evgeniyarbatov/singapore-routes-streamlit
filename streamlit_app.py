import streamlit as st
import json

ROUTES_DIR = 'routes'

def get_distance(item):
    return float(item['distance'].replace('km', ''))

def main():
    st.title("Singapore Running Routes")

    st.markdown("""
        I started running in Singapore in 2019.
        I explored a variety of places and I encourage you to do the same.
        These routes are meant as an inspiration for you to get started. 
    """)
    
    st.markdown("""
        How did I create the routes? 
        I used my GPX files from Strava to extract places I visit frequently.
        I then chose several landmarks in Singapore and created routes to them.
    """)

    st.markdown("""
        New to GPX? 
        See steps for [Garmin](https://support.garmin.com/en-US/?faq=wKuZXCaZRP4mWPX5aRz5h5) 
        and [Polar](https://support.polar.com/en/how-to-import-route).
    """)

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
