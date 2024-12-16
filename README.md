Here’s a concise README file for your Django-based `CourseGenie` project that includes instructions for setting up and running the Streamlit application. It assumes that the dependencies are listed in `requirements.txt` and provides clear instructions for running the project.

---

# CourseGenie Project

CourseGenie is a course recommendation system that leverages machine learning models to suggest relevant courses based on user input. The project is structured using Django with a Streamlit-based front end for easy interaction.

## Folder Structure

```
Course-Recommendation-system/
│
├── Services/
│   └── ml_course_recommendation_model.py  # Machine learning model for course recommendations
│
├──── course_recommendation.py  # Streamlit application for course recommendation
│
└── requirements.txt  # Python dependencies
```

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Shaik-mohd-huzaifa/Course-Recommendation-system.git
   cd Course-Recommendation-system
   ```

2. **Create a Virtual Environment:**

   It's recommended to use a virtual environment for the project.

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies:**

   Install the required dependencies using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit Application:**

   To start the Streamlit application for course recommendations, run:

   ```bash
   streamlit run course_recommendation.py
   ```

   This will launch the Streamlit app, where you can input details and get course recommendations.

## Notes

- Ensure all dependencies are properly installed by checking `requirements.txt` for required packages.
- The model file `ml_course_recommendation_model.py` is used for course recommendations and should be in place for the system to work properly.

## License

MIT License
