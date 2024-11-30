# Step 1: Use an official Node.js image to build the app
FROM node:18 AS build

# Set the working directory
WORKDIR /app


# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy package.json and package-lock.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the Angular app
COPY . .

# Build the Angular app
RUN npm run build --prod

# Step 2: Use a lightweight web server to serve the built app
FROM nginx:alpine

# Copy the built Angular app from the previous step into the Nginx server's directory
COPY --from=build /app/dist/czumper-search/browser /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
