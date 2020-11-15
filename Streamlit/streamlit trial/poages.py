import streamlit as st

def main():
    # Register your pages
    pages = {
        "First page": page_first,
        "Second page": page_second,
    }

    st.sidebar.title("App with pages")

    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.sidebar.radio("Select your page", tuple(pages.keys()))
    #page = st.sidebar.selectbox("Select your page", tuple(pages.keys()))

    # Display the selected page
    pages[page]()

def page_first():
    st.title("This is my first page")
    # ...

def page_second():
    st.title("This second page")
    # ...

if __name__ == "__main__":
    main()