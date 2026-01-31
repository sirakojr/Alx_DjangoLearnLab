# HTTPS Configuration

This project enforces HTTPS using Django security settings.

## Django Settings
- SECURE_SSL_REDIRECT forces all HTTP traffic to HTTPS
- HSTS headers instruct browsers to use HTTPS only
- Secure cookies ensure session and CSRF data are transmitted safely

## Deployment Notes
In production, HTTPS would be enabled using:
- Nginx or Apache
- SSL/TLS certificates (e.g., Let's Encrypt)

Example Nginx configuration:
- Redirect HTTP to HTTPS
- Configure ssl_certificate and ssl_certificate_key
