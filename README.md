# Recipe App

## Introduction

The Recipe App is a Django-based web application that allows users to browse and explore a collection of recipes.
The app provides a clean and user-friendly interface to view recipe details, making it easy to discover new dishes and get inspired in the kitchen.

## Features

- Display a list of recipes with their main attributes
- Automatically calculate the difficulty of recipes
- Show recipe details
- Admin interface for managing recipes easily
- Validation to ensure proper formatting of recipe data

## Technology Stack

- **Backend:** Django
- **Database:** SQLite (default, can be configured to PostgreSQL or other)
- **Frontend:** Django templates
- **Image Handling:** Django ImageField (optional)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies
