# voting_system

This is a Flask web application that allows users to upload an image of a Voter ID card. The application uses the Gemini API to extract the Voter ID number from the uploaded image and updates the voting status in a CSV file.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload a Voter ID image in JPG format.
- Extract Voter ID number using the Gemini API.
- Update voting status in a CSV file.
- View a list of voters who have voted.

## Technologies Used

- Python
- Flask
- Pandas
- Google Generative AI (Gemini API)
- HTML/CSS for the frontend
- dotenv for environment variable management

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PDey-203/voting_system.git