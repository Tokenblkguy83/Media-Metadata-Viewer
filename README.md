# Media-Metadata-Viewer
Media Metadata Viewer

## Project Description

Media Metadata Viewer is a web application that allows users to upload media files and view their metadata. The application is built using Flask for the backend and plain HTML, CSS, and JavaScript for the frontend. The metadata is extracted using the `mutagen` library and stored in an SQLite database.

## Setup Instructions

### Prerequisites

- Python 3.x
- Flask
- mutagen
- SQLite

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/Tokenblkguy83/Media-Metadata-Viewer.git
   cd Media-Metadata-Viewer
   ```

2. Set up a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install Flask mutagen
   ```

4. Run the Flask application:
   ```
   cd backend
   flask run
   ```

5. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

1. On the main page, use the file upload form to select a media file.
2. Click the "Upload" button to upload the file.
3. The metadata of the uploaded file will be displayed on the page.

## Project Structure

```
Media-Metadata-Viewer/
├── backend/
│   ├── app.py         # Your Flask application
│   ├── mydatabase.db  # Your SQLite database (might be ignored by git)
│   └── uploads/       # Folder for uploaded media (should be ignored by git)
├── frontend/
│   ├── index.html     # Your main HTML file
│   ├── css/
│   │   └── style.css  # Your CSS file for the Matrix look
│   └── js/
│       └── script.js  # Your JavaScript file for frontend logic
├── .gitignore         # File to tell Git what files/folders to ignore
└── README.md          # Information about your project
```

## Dependency Management

This project uses [Renovate](https://docs.renovatebot.com/) for automated dependency updates. Renovate will:

- Monitor GitHub Actions workflows for updates to actions
- Check Python dependencies in `requirements.txt` for updates
- Create pull requests for outdated dependencies
- Automatically merge minor and patch updates for stable dependencies
- Group related dependencies to minimize PR noise

The Dependency Dashboard is available in the Issues tab, providing an overview of all pending updates and detected dependencies.

### Configuration

The Renovate configuration is split between:
- `.renovaterc.json` - Main configuration file with all settings

### Schedule

By default, Renovate runs every weekend to check for updates, minimizing disruption during the work week.

## License

This project is licensed under the MIT License.
