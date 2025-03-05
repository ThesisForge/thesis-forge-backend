# Thesis Forge Backend

This is the backend part of the Thesis Forge application, designed to support the functionality of the frontend application and provide an API for data access.

## Description

The backend provides the following functionalities:

* User account management and authentication.
* Storage and management of thesis and research project ideas.
* API for accessing project, user, and rating data.
* Integration with AI models for generating recommendations and suggestions.

## Technology Stack

* FastAPI
* Python
* PostgreSQL (or another database of your choice)

## Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/ThesisForge/thesis-forge-backend.git](https://github.com/ThesisForge/thesis-forge-backend.git)
    ```

2.  Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Configure the database:

    * Create a database and user.
    * Set environment variables for database connection.

5.  Start the application:

    ```bash
    uvicorn main:app --reload
    ```

## Contributing

This application is open source, and we welcome any contributions. For more information, please see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions and suggestions, please contact us at [email protected]