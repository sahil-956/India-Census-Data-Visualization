
# India Census Data Visualizer

An interactive web application to **visualize India's census data** based on different parameters like **Population** and **Literacy Rate** across **States** and **Districts**.  
Built using **Streamlit** and **Plotly**, it provides dynamic scatter map visualizations with zoom and hover functionality.

---

## 📷 Screenshot

Here is the final visualisation created:

![Screenshot](https://github.com/Ritik250/Data-Visualization-miniProject/blob/main/website%20snippet.png)
## Features

- Select any **State** or view data for **Overall India**.
- Choose **Primary Parameter** (for bubble size) and **Secondary Parameter** (for bubble color).
- Interactive **Mapbox-based** scatter plots.
- Hover on bubbles to view **State/District-specific** details (Population, Literacy Rate, Coordinates).
- Zoom and pan across the map for detailed exploration.

---

## Tech Stack

- [Streamlit](https://streamlit.io/) — for building the web app interface
- [Plotly Express](https://plotly.com/python/plotly-express/) — for creating interactive scatter maps
- [Pandas](https://pandas.pydata.org/) — for data manipulation
- [NumPy](https://numpy.org/) — for numerical operations

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/india-census-visualizer.git
   cd india-census-visualizer
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Ensure the dataset `India.csv` is present in the project root.**

2. **Run the Streamlit app:**
   ```bash
   streamlit run webapp.py
   ```

3. **App Interface:**
   - Use the **left sidebar** to select:
     - State: Overall India / Specific state
     - Primary parameter (bubble size)
     - Secondary parameter (bubble color)
   - Click **"Plot Graph"** to generate the visualization.

4. **Interact with the map:**
   - Zoom, pan, and hover to view detailed district/state information.

---

## Dataset

The dataset (`India.csv`) contains:
- District and State Names
- Latitude and Longitude
- Population
- Literacy Rate
- Other census parameters

---

## Folder Structure

```
.
├── India.csv            # Dataset file
├── requirements.txt     # List of dependencies
├── webapp.py            # Main Streamlit application
└── README.md            # Project documentation
```

---

## Future Improvements

- Add more parameters (e.g., sex ratio, area).
- Implement filters for year-wise data if available.
- Enable downloading of plots as images.
- Add time-based animations if historic data is available.

---


## Author

- Sahil Takshak

---

## Acknowledgements

- Mapbox and OpenStreetMap for base maps.
- Plotly for interactive plotting.
- Streamlit for rapid app deployment.

