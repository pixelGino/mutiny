FROM nginx:alpine

# Copy website files
COPY mutiny-labs-website.html /usr/share/nginx/html/index.html
COPY mutiny_logo.png /usr/share/nginx/html/mutiny_logo.png

# Create nginx configuration for single-page app
RUN echo 'server { \n\
    listen 8080; \n\
    server_name _; \n\
    root /usr/share/nginx/html; \n\
    index index.html; \n\
    \n\
    # Enable gzip compression \n\
    gzip on; \n\
    gzip_vary on; \n\
    gzip_min_length 1024; \n\
    gzip_types text/plain text/css text/xml text/javascript application/javascript application/xml+rss application/json; \n\
    \n\
    # Security headers \n\
    add_header X-Frame-Options "SAMEORIGIN" always; \n\
    add_header X-Content-Type-Options "nosniff" always; \n\
    add_header X-XSS-Protection "1; mode=block" always; \n\
    add_header Referrer-Policy "no-referrer-when-downgrade" always; \n\
    \n\
    # Cache static assets \n\
    location ~* \.(png|jpg|jpeg|gif|ico|svg|webp)$ { \n\
        expires 1y; \n\
        add_header Cache-Control "public, immutable"; \n\
    } \n\
    \n\
    location / { \n\
        try_files $uri $uri/ /index.html; \n\
    } \n\
}' > /etc/nginx/conf.d/default.conf

# Remove default nginx config
RUN rm /etc/nginx/conf.d/default.conf.dpkg-dist 2>/dev/null || true

# Expose port 8080 (Cloud Run requirement)
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:8080/ || exit 1

# Run nginx
CMD ["nginx", "-g", "daemon off;"]
