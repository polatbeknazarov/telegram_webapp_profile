# Telegram Web App

## Project Overview
This project is a Telegram WebApp that allows users to interact with a Telegram bot, enter their birthdate, and view relevant personal information. The application provides a seamless user experience by integrating a backend with FastAPI and Aiogram, and a frontend built with Vue 3 and TailwindCSS. The app also enables users to share their profile data with others.

## Tech Stack
- **Backend**: FastAPI, Aiogram, TortoiseORM
- **Frontend**: VueJS, Pinia, TailwindCSS
- **Database**: PostgreSQL

## TMA Screenshots
<p align="center">
    <img src="screenshots/BirthDatePicker.jpg" width="45%">
    <img src="screenshots/Profile.jpg" width="45%">
</p>

## Installation

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/polatbeknazarov/telegram_webapp_profile.git
   cd coffee_order_api
   ```
2. Set up environment variables in `backend/app/.env` (example `.env` file):
   ```env
   APP_CONFIG__BOT__TOKEN=123456789:AbCdEfGhIj-k1L2m3N
   APP_CONFIG__BOT__WEB_APP_URL=https://example.com
   APP_CONFIG__BOT__WEBHOOK_URL=https://example.com/api/v1/webhook
   APP_CONFIG__DB__URL=postgres://user:password@localhost:5432/app
   ```
3. Running with docker:
   ```bash
   docker-compose up --build
   ```

## API Endpoints 
- `POST /api/v1/users` - Create a new user
- `GET /api/v1/users/{telegram_id}` - Get user by telegram_id
- `PATCH /api/v1/users/set_birth_date` - Update user birth_date field
- `GET /api/v1/users` - Get all users

## API Documentation
Swagger documentation available at: `http://localhost:8000/docs`