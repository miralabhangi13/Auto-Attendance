import streamlit as st
from PIL import Image
from io import BytesIO
import hashlib

@st.dialog("Capture or upload photos")
def add_photos_dialog():

    # 1. Initialize session states
    if "attendance_images" not in st.session_state:
        st.session_state.attendance_images = []

    if "processed_photos" not in st.session_state:
        st.session_state.processed_photos = set()

    st.write("Add classroom photos to scan for attendance")

    # 2. Use native st.tabs instead of buttons for a smoother UI without manual reruns
    tab1, tab2 = st.tabs(["Camera", "Upload photos"])

    with tab1:
        cam_photo = st.camera_input("Take Snapshot", key="dialog_cm")

        if cam_photo:
            raw = cam_photo.getvalue()
            photo_id = hashlib.md5(raw).hexdigest()

            if photo_id not in st.session_state.processed_photos:
                img = Image.open(BytesIO(raw)).convert("RGB")
                st.session_state.attendance_images.append(img)
                st.session_state.processed_photos.add(photo_id)
                st.toast("Photo captured!")
            else:
                st.info("This photo has already been added.")

    with tab2:
        uploaded_files = st.file_uploader(
            "Choose image files",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
            key="dialog_upload"
        )

        if uploaded_files:
            added = 0
            for f in uploaded_files:
                raw = f.getvalue()
                photo_id = hashlib.md5(raw).hexdigest()

                if photo_id not in st.session_state.processed_photos:
                    img = Image.open(BytesIO(raw)).convert("RGB")
                    st.session_state.attendance_images.append(img)
                    st.session_state.processed_photos.add(photo_id)
                    added += 1

            if added:
                st.toast(f"{added} photo(s) added!")
            elif len(uploaded_files) > 0:
                # Let the user know if they uploaded a duplicate image
                st.info("Selected photos are already in the list.")

    st.divider()

    st.subheader(f"Added Photos ({len(st.session_state.attendance_images)})")

    if st.session_state.attendance_images:
        cols = st.columns(3)

        for i, img in enumerate(st.session_state.attendance_images):
            with cols[i % 3]:
                # 3. FIX: Replaced width="stretch" with use_container_width=True
                st.image(
                    img,
                    caption=f"Photo {i + 1}",
                    use_container_width=True
                )
    else:
        st.info("No photos added yet.")

    st.divider()

    # 4. FIX: Replaced width="stretch" with use_container_width=True
    if st.button("Done", type="primary", use_container_width=True):
        st.session_state.pop("dialog_cm", None)
        st.session_state.pop("dialog_upload", None)
        st.rerun()