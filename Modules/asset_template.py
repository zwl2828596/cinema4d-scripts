"""
Name-US: Asset's Name
Description-US: Asset's Description

Note: Create an image file 64x64 pixel resolution tiff-format with transparent background
and give it same name as the asset script.
"""

# Libraries
import ar_shelf_tool as st

# Functions
def main():
    # File path of the asset
    assetPath = ""

    # Import the asset
    st.Import(path=assetPath, # Asset path
              icon=__file__,  # Icon path
              color=None,     # Icon color in c4d.Vector() format
              matsOnly=False) # If 'True' imports only materials from asset file

# Execute main()
if __name__=='__main__':
    main()