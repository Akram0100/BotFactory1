# Chatbot Factory AI

## Overview

Chatbot Factory AI is a Telegram AI chatbot platform designed for Uzbek language users. It enables users to create and manage AI-powered chatbots with subscription-based features and multi-language support. The platform integrates with Google Gemini AI for natural language processing and offers a tiered subscription model with varying functionalities. The business vision is to provide an accessible and powerful AI chatbot solution for the Uzbek market, with ambitions for broader regional reach.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend
-   **Framework**: Flask with MVC architecture
-   **Database**: SQLAlchemy ORM supporting PostgreSQL and SQLite
-   **Authentication**: Flask-Login with bcrypt hashing
-   **AI Integration**: Google Gemini API (gemini-2.5-flash)
-   **Telegram Integration**: `python-telegram-bot` library

### Frontend
-   **Template Engine**: Jinja2
-   **UI Framework**: Bootstrap 5
-   **Icons**: Font Awesome
-   **Styling**: Custom CSS with variables
-   **JavaScript**: Vanilla JavaScript

### Database Design
Key entities include User (with subscription types), Bot (individual instances), KnowledgeBase (document uploads), Payment, and ChatHistory.

### Authentication & Authorization
Features user registration, session-based login, role-based access for admins, and subscription-based feature access.

### Subscription Model
A four-tier system: Free/Test (14 days), Starter, Basic, and Premium, offering different bot limits, platform support, languages, and technical support levels.

### AI Response System
Includes language detection, knowledge base context management, plain text response formatting (no Markdown), and localized fallback handling.

### File Upload System
Supports .txt and .docx files (up to 16MB) for knowledge base, with content extraction for AI training.

### UI/UX Decisions
The platform uses Bootstrap 5 for a responsive design, Font Awesome for consistent iconography, and custom CSS for theming. The overall design aims for a clean, user-friendly interface.

### System Design Choices
The architecture emphasizes modularity (MVC), scalability (PostgreSQL option), and robust error handling, particularly for database connections and AI interactions. Webhooks are implemented for efficient Telegram integration.

## External Dependencies

### AI Services
-   **Google Gemini API**: For natural language processing and chatbot responses.

### Messaging Platforms
-   **Telegram Bot API**: Primary integration for bot functionality.
-   **Instagram & WhatsApp**: Supported across all subscription tiers.

### Payment Processors
-   **PayMe**
-   **Click**
-   **Uzum**
-   **Paynet**: Integrated for local Uzbek payments.

### Python Libraries
-   **Flask**: Core web framework and extensions (Flask-SQLAlchemy, Flask-Login).
-   **python-telegram-bot**: Telegram API wrapper.
-   **google-genai**: Google Gemini AI client library.
-   **python-docx**: For processing .docx files in the knowledge base.
-   **Werkzeug**: Security and WSGI utilities.
-   **Gunicorn**: Production WSGI server.

### Frontend Dependencies
-   **Bootstrap 5**: UI framework (via CDN).
-   **Font Awesome**: Icon library (via CDN).

### Database Options
-   **SQLite**: Used for development environments.
-   **PostgreSQL**: Recommended for production environments.

## Recent Import Status

**September 18, 2025**: ✅ **FRESH REPLIT IMPORT COMPLETED** - Successfully set up GitHub import in Replit environment:
- **Dependencies**: All Python packages installed from requirements.txt using pip
- **Database**: PostgreSQL connection established with SQLite fallback for development  
- **Workflow**: Flask application configured on port 5000 with webview output
- **Environment**: Required secrets (SESSION_SECRET, DATABASE_URL) properly configured
- **Application**: Flask app running successfully with HTTP 200 responses
- **Deployment**: Production deployment configured with autoscale and gunicorn
- **Code Quality**: Fixed LSP errors and pandas DataFrame type issues
- **Status**: ✅ FULLY OPERATIONAL - Fresh GitHub clone running perfectly