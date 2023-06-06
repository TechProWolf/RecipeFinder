# RecipeFinder

RecipeFinder is an application that allows users to search for recipes based on specified ingredients and dietary preferences. It provides a convenient way for users to discover new recipes and make the most out of the ingredients they have on hand.

## Installation

1. Clone the RecipeFinder repository:

   ```shell
   git clone https://github.com/TechProWolf/RecipeFinder.git

2. Navigate to the project directory:

   cd RecipeFinder

3. Install the required dependencies:

   pip install -r requirements.txt

4. Obtain API keys:

   Create an account on a recipe API provider (e.g., Spoonacular) and obtain an API key.

5. Configure the API keys:

   Create a file named .env in the root directory of the project.

   Add the following line to the .env file, replacing <YOUR_API_KEY> with your actual API key:
      
      API_KEY=<YOUR_API_KEY>

## Usage
1. Run the application:

   python app.py

2. Open your web browser and go to http://localhost:5000.

3. Enter the ingredients you have in the search box and select your dietary preferences.

4. Click the "Search" button to retrieve the recipes based on your input.

5. View the search results and click on a recipe to see its detailed information.

6. To save a recipe, click on the "Save Recipe" button.

## Folder Structure

The project follows the following folder structure:

- app.py: The main Python file that runs the Flask application and handles the routing.

- templates/: This folder contains the HTML templates used for rendering the web pages.

- static/: This folder contains static assets such as CSS stylesheets and JavaScript files.

- utils/: This folder contains utility functions used throughout the application.

- requirements.txt: This file lists the required Python packages and their versions for easy installation.

- .env: This file (not included in the repository) holds the API key and is used for environment variables.

## External APIs and Libraries

The RecipeFinder application uses the following external APIs and libraries:

- Spoonacular API: The Spoonacular API provides access to a vast collection of recipes, ingredient information, and more. Visit their website to learn more and obtain an API key.

- Flask: Flask is a lightweight web framework for Python that provides the foundation for building the RecipeFinder application.

- Jinja: Jinja is a powerful templating engine for Python, used in the application to generate dynamic HTML pages.

- Bootstrap: Bootstrap is a popular CSS framework that provides responsive and visually appealing styles for the application.

## Contributing

  Contributions to the RecipeFinder project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.
