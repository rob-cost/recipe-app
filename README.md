# Recipe-App 🍳

A comprehensive Django-based web application for managing and discovering recipes. Users can browse, search, add, and analyze recipes with an intuitive interface and powerful filtering capabilities.
View the website here: https://stark-atoll-86571-47f58799b91f.herokuapp.com/

## Features

### 📖 Recipe Management

- Browse all available recipes
- View detailed recipe information including:
  - Ingredients
  - Cooking instructions
  - Difficulty level
  - Cooking time
  - Recipe images
- Add new recipes to the database
- Like/favorite recipes

### 🔍 Advanced Search & Filtering

- Search recipes by:
  - Recipe name
  - Ingredients
  - Difficulty level (Easy, Medium, Hard, Expert)
  - Maximum cooking time
- Visual data analysis with charts:
  - Bar chart: Recipe cooking times
  - Pie chart: Difficulty distribution
  - Line chart: Cooking time trends
- Paginated results for better navigation

### 📊 Data Analysis

- Statistical visualization using Matplotlib
- Interactive charts for recipe analysis
- Pandas DataFrame integration for data processing

## Technology Stack

- **Framework**: Django 4.x
- **Language**: Python 3.x
- **Database**: SQLite
- **Data Analysis**: Pandas, Matplotlib
- **Frontend**: HTML5, CSS3
- **Pagination**: Django Paginator

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Recipe-App.git
   cd Recipe-App
   ```

2. **Create a virtual environment**

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up your admin credentials.

6. **Collect static files**

   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### For Regular Users

1. **Register/Login**

   - Create a new account or log in with existing credentials
   - Access is required to view and add recipes

2. **Browse Recipes**

   - View all recipes on the homepage
   - See popular recipes based on likes
   - Navigate through paginated results

3. **Search Recipes**

   - Use the search feature to filter by name, ingredients, difficulty, or time
   - View statistical charts analyzing search results
   - Navigate through filtered results with pagination

4. **View Recipe Details**

   - Click on any recipe to see complete information
   - View ingredients, cooking method, and metadata
   - Like recipes to mark them as favorites

5. **Add Recipes**
   - Share your own recipes with the community
   - Include all necessary details and images

### For Administrators

- Access the admin panel at `/admin/`
- Manage users, recipes, and all database entries
- Moderate user-submitted content

### User Model

- Django's built-in User model with authentication

## Dependencies

Main dependencies (see `pyproject.toml` for complete list):

```
Django>=4.0
pandas>=1.5.0
matplotlib>=3.6.0
Pillow>=9.0.0
```

## Configuration

### Environment Variables

Create a `.env` file in the project root for sensitive information:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=your-database-url
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

Made with ❤️ and Python
