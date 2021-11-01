<p align="center"><img width="40%" src="https://hacktoberfest.digitalocean.com/_nuxt/img/logo-hacktoberfest-full.f42e3b1.svg"/></p>

<p align="center">Automatically grade answer sheets!</p>
<p align="center">Consider leaving a :star: if you found the project helpful.</p>

# Auto Grader

Auto Grader helps teachers by automating the paper correction process using advanced computer vision and NLP.

## Flow

Step 1: Teacher uploads the scanned answersheet and the correct answers for the question.

<img src="https://raw.githubusercontent.com/IEEE-VIT/auto-grader/main/samples/form_scanned_2.jpg" alt="Auto-Grader Teacher Input" width="500"/>

Step 2: The boxes in the scanned image are identified and cropped out.

<img src="https://raw.githubusercontent.com/IEEE-VIT/auto-grader/main/samples/processed/img_final_bin.jpg" alt="Auto-Grader Processed" width="500"/>

Extracted Character

<img src="https://raw.githubusercontent.com/IEEE-VIT/auto-grader/main/samples/output/334.png" alt="Auto-Grader Cropped Character" width="100"/>

Step 3: Using a CNN, these characters are classified.

Step 4: Words are formed out of these classified characters.

Step 5: These words are sent through a spelling corrector to remove mistakes which the CNN model might've caused.

Step 6: Then sentences are formed which are then sent along with the correct answers through a Text Similarity NLP model.

Step 7: The similarity model gives a cosine score using which is used to determine the marks a student should get for their answer.

## Built With

- [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [TensorFlow 2](https://www.tensorflow.org/)
- [OpenCV](https://docs.opencv.org/master/index.html)

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python 3.8.10 and the latest version of pip.

### Installation

1. Fork it.

2. Clone the repo
   ```sh
   git clone https://github.com/iamyajat/auto-grader.git
   ```
3. Install `virtualenv`
   ```sh
   pip install virtualenv
   ```
4. Create a virtual environment
   ```sh
   python -m venv env
   ```
   ```sh
   .\env\Scripts\activate
   ```
5. Install all requirements
   ```sh
   pip install -r requirements.txt
   ```
6. Start the API
   ```sh
   uvicorn main:app --reload
   ```

## Contributing

To start contributing, check out [CONTRIBUTING.md](https://github.com/IEEE-VIT/auto-grader/blob/master/CONTRIBUTING.md). New contributors are always welcome to support this project. If you want something gentle to start with, check out issues labelled as `easy` or `good-first-issue`. Check out issues labelled as `hacktoberfest` if you are up for some grabs! :)

## License

This project is licensed under [MIT](https://github.com/IEEE-VIT/auto-grader/blob/master/LICENSE.md).
