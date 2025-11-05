# RizzosAI Sales Site

This is the sales site for RizzosAI Domains, designed for deployment on Render at domain.rizzosai.com.

- Main page: Professional packages and guide details
- Thank-you page: Redirects users to the backoffice after purchase
- Built with Flask

## Deployment
- Use requirements.txt for dependencies
- Set the Render root directory to this folder
- Set the start command to: `gunicorn --bind 0.0.0.0:$PORT app:app`

## After Purchase
- Users are redirected to the backoffice login page automatically
