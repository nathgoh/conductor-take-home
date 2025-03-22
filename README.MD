# Take Home Project

This is ConductorAI's take home project for engineering candidates.

## The problem

[Here is a large pdf document](https://www.saffm.hq.af.mil/Portals/84/documents/FY25/FY25%20Air%20Force%20Working%20Capital%20Fund.pdf?ver=sHG_i4Lg0IGZBCHxgPY01g%3d%3d). We want to find the largest number in this document. The unit is not important (could be dollars, years, pounds, etc), we're just looking for the greatest numerical value in the document.

For a bonus challenge if you have time, take natural language guidance from the document into consideration. For example, where the document states that values are listed in millions, a value of 3.15 would be considered to be 3,150,000 instead of 3.15.

## How to run

### Clone the repository
```
gh repo clone nathgoh/conductor-take-home
```

### Install dependencies

Assuming you have a python virtual environment installed like conda, first create the virtual environment and activate it
```
conda create -n conductor python=3.12
conda activate conductor 
```

Once you have created and activate the virtual environment, run the following command to install the necessary dependencies.
```
pip install -e .
```
### Run the code
To run the code there's a handy `Makefile` command I created so you don't need to find the right python command to run it. Just do:
```
make run
```
This will load the Streamlit app where you can interact with and upload the PDF file that you want to extract the largest number from. It should be hosted on something like `http://localhost:8501`.

