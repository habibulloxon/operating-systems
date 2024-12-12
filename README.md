# Timetable Application

This is a simple Flask web application that displays a timetable retrieved from a PostgreSQL database. Users can filter the timetable by level.

## Features

- Displays a list of courses with their day, time, room, and level.
- Allows users to filter the timetable by level using a dropdown menu.

## Technical Details

- **Backend:** Python with Flask framework
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, and Jinja templating engine

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/timetable-app.git
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and set the following variables with your PostgreSQL database credentials:

   ```
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=your_database_host
   DB_PORT=your_database_port
   ```

## Running the Application

1. **Run the Flask app:**

   ```bash
   flask run
   ```

2. **Open your web browser and navigate to `http://127.0.0.1:5000/` to access the timetable.**

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)