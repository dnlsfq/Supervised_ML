




# Supervised_ML
Classification Algorithm

## K-Nearest Neighbors

Case Study : Telecommunications 

Telecommunications provider has segmented its customer base by service usage patterns, categorizing the customers into four groups. If demographic data can be used to predict group membership, the company can customize offers for individual prospective customers. It is a classification problem. That is, given the dataset, with predefined labels, we need to build a model to be used to predict class of a new or unknown case.

Demographic data

* Region
* Age
* Marital
* Address
* Income
* Ed
* Employ
* Retire
* Gender
* Reside

Customer 

* Tenure
* Custcat

custcat has four possible values that correspond to the four customer groups, as follows: 
* 1 - Basic Service 
* 2 - E-Service 
* 3 - Plus Service 
* 4 - Total Service
  
Demographic data (independent) is used to predict usage patterns.
Customer data (dependent) is used as label
Our objective is to build a classifier, to predict the class of unknown cases. 

---

## Components

```
import streamlit as st 
import streamlit.components.v1 as components

components.html()

components.iframe()

components.declare_component()
```

## Static Components
stateless and only send data to the browser

```st.markdown```

```
def github_gist(gist_creator, gist_id, height=600, scrolling=True):
    components.html(
        f"""
        <script src="https://gist.github.com/{gist_creator}/{gist_id}.js">

        </script>
        """,
        height = height,
        scrolling = scrolling
    )
```

## Bidirectional Components 
internal state and send back from the browser 

```components.declare_components(...)```

