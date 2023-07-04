import base64
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

import streamlit as st


selected = option_menu(
    menu_title=None,
    options=['Home','Wholesale','Fertilizers','Model'],
    icons = ['house','book','book','book'],
    orientation='horizontal'
)

if selected == 'Wholesale':
    st.title('Contacts of Wholesalers')
    select_season = st.selectbox("Select Season: ",['Summer','Rainy','Winter']) 

    if select_season == 'Summer':
        select_crop = st.selectbox("Select Crop: ",['Moong Dal','Tomatoes','Watermelons'])
        if select_crop == 'Moong Dal':          
            st.title('Contact Details of Wholesalers-->')
            st.write('Here you will get wholesaler details according to the season and crop you have selected.')
            
            data = {
                "Name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Lee", "Tom Brown"],
                "Email": ["johndoe@example.com", "janesmith@example.com", "bobjohnson@example.com", "alicelee@example.com", "tombrown@example.com"],
                "Contact": ["123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234"],
                "Address": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "202 Maple St"],
                "Image": ["https://i.imgur.com/6sdREfC.jpg", "https://i.imgur.com/gwOdcgK.jpg", "https://i.imgur.com/W6U5EN6.jpg", "https://i.imgur.com/1kfM2JF.jpg", "https://i.imgur.com/cX9hvtA.jpg"]
                }

            
            df = pd.DataFrame(data)

            image_style = """
            <style>
            img {
                border-radius: 80%;
                object-fir: cover;
                width: 150px;
                height: 200px;
                margin: 10px;
            }
            </style>
            """
            st.write(image_style, unsafe_allow_html=True)
            for i in range(len(df)):
                st.image(df["Image"][i], width=250)
                st.write("Name:", df["Name"][i])
                st.write("Email:", df["Email"][i])
                st.write("Contact:", df["Contact"][i])
                st.write("Address:", df["Address"][i])
                st.write("---")
        
        elif select_crop == 'Tomatoes':
            st.title('Contact Details of Wholesalers-->')
            st.write('Here you will get wholesaler details according to the season and crop you have selected.')
            
            data = {
                "Name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Lee", "Tom Brown"],
                "Email": ["johndoe@example.com", "janesmith@example.com", "bobjohnson@example.com", "alicelee@example.com", "tombrown@example.com"],
                "Contact": ["123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234"],
                "Address": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "202 Maple St"],
                "Image": ["https://i.imgur.com/6sdREfC.jpg", "https://i.imgur.com/gwOdcgK.jpg", "https://i.imgur.com/W6U5EN6.jpg", "https://i.imgur.com/1kfM2JF.jpg", "https://i.imgur.com/cX9hvtA.jpg"]
                }

            
            df = pd.DataFrame(data)

            image_style = """
            <style>
            img {
                border-radius: 80%;
                object-fir: cover;
                width: 150px;
                height: 200px;
                margin: 10px;
            }
            </style>
            """
            st.write(image_style, unsafe_allow_html=True)
            for i in range(len(df)):
                st.image(df["Image"][i], width=250)
                st.write("Name:", df["Name"][i])
                st.write("Email:", df["Email"][i])
                st.write("Contact:", df["Contact"][i])
                st.write("Address:", df["Address"][i])
                st.write("---")

        else:
            st.title('Contact Details of Wholesalers-->')
            st.write('Here you will get wholesaler details according to the season and crop you have selected.')
            
            data = {
                "Name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Lee", "Tom Brown"],
                "Email": ["johndoe@example.com", "janesmith@example.com", "bobjohnson@example.com", "alicelee@example.com", "tombrown@example.com"],
                "Contact": ["123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234"],
                "Address": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "202 Maple St"],
                "Image": ["https://i.imgur.com/6sdREfC.jpg", "https://i.imgur.com/gwOdcgK.jpg", "https://i.imgur.com/W6U5EN6.jpg", "https://i.imgur.com/1kfM2JF.jpg", "https://i.imgur.com/cX9hvtA.jpg"]
                }

            
            df = pd.DataFrame(data)

            image_style = """
            <style>
            img {
                border-radius: 80%;
                object-fir: cover;
                width: 150px;
                height: 200px;
                margin: 10px;
            }
            </style>
            """
            st.write(image_style, unsafe_allow_html=True)
            for i in range(len(df)):
                st.image(df["Image"][i], width=250)
                st.write("Name:", df["Name"][i])
                st.write("Email:", df["Email"][i])
                st.write("Contact:", df["Contact"][i])
                st.write("Address:", df["Address"][i])
                st.write("---")

    elif select_season == 'Rainy':
        select_crop = st.selectbox("Select Crop: ",['Sugarcane','Pulses','Cotton'])
        if select_crop == 'Suagrcane':          
            st.title('Contact Details of Wholesalers-->')
            st.write('Here you will get wholesaler details according to the season and crop you have selected.')
            
            data = {
                "Name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Lee", "Tom Brown"],
                "Email": ["johndoe@example.com", "janesmith@example.com", "bobjohnson@example.com", "alicelee@example.com", "tombrown@example.com"],
                "Contact": ["123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234"],
                "Address": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "202 Maple St"],
                "Image": ["https://i.imgur.com/6sdREfC.jpg", "https://i.imgur.com/gwOdcgK.jpg", "https://i.imgur.com/W6U5EN6.jpg", "https://i.imgur.com/1kfM2JF.jpg", "https://i.imgur.com/cX9hvtA.jpg"]
                }

            
            df = pd.DataFrame(data)

            image_style = """
            <style>
            img {
                border-radius: 80%;
                object-fir: cover;
                width: 150px;
                height: 200px;
                margin: 10px;
            }
            </style>
            """
            st.write(image_style, unsafe_allow_html=True)
            for i in range(len(df)):
                st.image(df["Image"][i], width=250)
                st.write("Name:", df["Name"][i])
                st.write("Email:", df["Email"][i])
                st.write("Contact:", df["Contact"][i])
                st.write("Address:", df["Address"][i])
                st.write("---")
        
        elif select_crop == 'Pulses':
            st.title('Contact Details of Wholesalers-->')
            st.write('Here you will get wholesaler details according to the season and crop you have selected.')
            
            data = {
                "Name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Lee", "Tom Brown"],
                "Email": ["johndoe@example.com", "janesmith@example.com", "bobjohnson@example.com", "alicelee@example.com", "tombrown@example.com"],
                "Contact": ["123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234"],
                "Address": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "202 Maple St"],
                "Image": ["https://i.imgur.com/6sdREfC.jpg", "https://i.imgur.com/gwOdcgK.jpg", "https://i.imgur.com/W6U5EN6.jpg", "https://i.imgur.com/1kfM2JF.jpg", "https://i.imgur.com/cX9hvtA.jpg"]
                }

            
            df = pd.DataFrame(data)

            image_style = """
            <style>
            img {
                border-radius: 80%;
                object-fir: cover;
                width: 150px;
                height: 200px;
                margin: 10px;
            }
            </style>
            """
            st.write(image_style, unsafe_allow_html=True)
            for i in range(len(df)):
                st.image(df["Image"][i], width=250)
                st.write("Name:", df["Name"][i])
                st.write("Email:", df["Email"][i])
                st.write("Contact:", df["Contact"][i])
                st.write("Address:", df["Address"][i])
                st.write("---")

        else:
            st.title('Contact Details of Wholesalers-->')
            st.write('Here you will get wholesaler details according to the season and crop you have selected.')
            
            data = {
                "Name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Lee", "Tom Brown"],
                "Email": ["johndoe@example.com", "janesmith@example.com", "bobjohnson@example.com", "alicelee@example.com", "tombrown@example.com"],
                "Contact": ["123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234"],
                "Address": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "202 Maple St"],
                "Image": ["https://i.imgur.com/6sdREfC.jpg", "https://i.imgur.com/gwOdcgK.jpg", "https://i.imgur.com/W6U5EN6.jpg", "https://i.imgur.com/1kfM2JF.jpg", "https://i.imgur.com/cX9hvtA.jpg"]
                }

            
            df = pd.DataFrame(data)

            image_style = """
            <style>
            img {
                border-radius: 80%;
                object-fir: cover;
                width: 150px;
                height: 200px;
                margin: 10px;
            }
            </style>
            """
            st.write(image_style, unsafe_allow_html=True)
            for i in range(len(df)):
                st.image(df["Image"][i], width=250)
                st.write("Name:", df["Name"][i])
                st.write("Email:", df["Email"][i])
                st.write("Contact:", df["Contact"][i])
                st.write("Address:", df["Address"][i])
                st.write("---")
    else:
        select_crop = st.selectbox("Select Crop: ",['Wheat','Oats','Potato','Onion']) 
        if select_crop == 'Wheat':          
            st.title('Contact Details of Wholesalers-->')
            st.write('Here you will get wholesaler details according to the season and crop you have selected.')
            
            data = {
                "Name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Lee", "Tom Brown"],
                "Email": ["johndoe@example.com", "janesmith@example.com", "bobjohnson@example.com", "alicelee@example.com", "tombrown@example.com"],
                "Contact": ["123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234"],
                "Address": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "202 Maple St"],
                "Image": ["https://i.imgur.com/6sdREfC.jpg", "https://i.imgur.com/gwOdcgK.jpg", "https://i.imgur.com/W6U5EN6.jpg", "https://i.imgur.com/1kfM2JF.jpg", "https://i.imgur.com/cX9hvtA.jpg"]
                }

            
            df = pd.DataFrame(data)

            image_style = """
            <style>
            img {
                border-radius: 80%;
                object-fir: cover;
                width: 150px;
                height: 200px;
                margin: 10px;
            }
            </style>
            """
            st.write(image_style, unsafe_allow_html=True)
            for i in range(len(df)):
                st.image(df["Image"][i], width=250)
                st.write("Name:", df["Name"][i])
                st.write("Email:", df["Email"][i])
                st.write("Contact:", df["Contact"][i])
                st.write("Address:", df["Address"][i])
                st.write("---")
        
        elif select_crop == 'Oats':
            st.title('Contact Details of Wholesalers-->')
            st.write('Here you will get wholesaler details according to the season and crop you have selected.')
            
            data = {
                "Name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Lee", "Tom Brown"],
                "Email": ["johndoe@example.com", "janesmith@example.com", "bobjohnson@example.com", "alicelee@example.com", "tombrown@example.com"],
                "Contact": ["123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234"],
                "Address": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "202 Maple St"],
                "Image": ["https://i.imgur.com/6sdREfC.jpg", "https://i.imgur.com/gwOdcgK.jpg", "https://i.imgur.com/W6U5EN6.jpg", "https://i.imgur.com/1kfM2JF.jpg", "https://i.imgur.com/cX9hvtA.jpg"]
                }

            
            df = pd.DataFrame(data)

            image_style = """
            <style>
            img {
                border-radius: 80%;
                object-fir: cover;
                width: 150px;
                height: 200px;
                margin: 10px;
            }
            </style>
            """
            st.write(image_style, unsafe_allow_html=True)
            for i in range(len(df)):
                st.image(df["Image"][i], width=250)
                st.write("Name:", df["Name"][i])
                st.write("Email:", df["Email"][i])
                st.write("Contact:", df["Contact"][i])
                st.write("Address:", df["Address"][i])
                st.write("---")

        elif select_crop == 'Potato':
            st.title('Contact Details of Wholesalers-->')
            st.write('Here you will get wholesaler details according to the season and crop you have selected.')
            
            data = {
                "Name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Lee", "Tom Brown"],
                "Email": ["johndoe@example.com", "janesmith@example.com", "bobjohnson@example.com", "alicelee@example.com", "tombrown@example.com"],
                "Contact": ["123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234"],
                "Address": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "202 Maple St"],
                "Image": ["https://i.imgur.com/6sdREfC.jpg", "https://i.imgur.com/gwOdcgK.jpg", "https://i.imgur.com/W6U5EN6.jpg", "https://i.imgur.com/1kfM2JF.jpg", "https://i.imgur.com/cX9hvtA.jpg"]
                }

            
            df = pd.DataFrame(data)

            image_style = """
            <style>
            img {
                border-radius: 80%;
                object-fir: cover;
                width: 150px;
                height: 200px;
                margin: 10px;
            }
            </style>
            """
            st.write(image_style, unsafe_allow_html=True)
            for i in range(len(df)):
                st.image(df["Image"][i], width=250)
                st.write("Name:", df["Name"][i])
                st.write("Email:", df["Email"][i])
                st.write("Contact:", df["Contact"][i])
                st.write("Address:", df["Address"][i])
                st.write("---")
        else:
            st.title('Contact Details of Wholesalers-->')
            st.write('Here you will get wholesaler details according to the season and crop you have selected.')
            
            data = {
                "Name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Lee", "Tom Brown"],
                "Email": ["johndoe@example.com", "janesmith@example.com", "bobjohnson@example.com", "alicelee@example.com", "tombrown@example.com"],
                "Contact": ["123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234"],
                "Address": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "202 Maple St"],
                "Image": ["https://i.imgur.com/6sdREfC.jpg", "https://i.imgur.com/gwOdcgK.jpg", "https://i.imgur.com/W6U5EN6.jpg", "https://i.imgur.com/1kfM2JF.jpg", "https://i.imgur.com/cX9hvtA.jpg"]
                }

            
            df = pd.DataFrame(data)

            image_style = """
            <style>
            img {
                border-radius: 80%;
                object-fir: cover;
                width: 150px;
                height: 200px;
                margin: 10px;
            }
            </style>
            """
            st.write(image_style, unsafe_allow_html=True)
            for i in range(len(df)):
                st.image(df["Image"][i], width=250)
                st.write("Name:", df["Name"][i])
                st.write("Email:", df["Email"][i])
                st.write("Contact:", df["Contact"][i])
                st.write("Address:", df["Address"][i])
                st.write("---")
