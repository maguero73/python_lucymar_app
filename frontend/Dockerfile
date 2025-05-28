# Etapa 1: build de la app
FROM node:18 AS build-stage

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Etapa 2: servidor Nginx para producción
FROM nginx:stable-alpine AS production-stage

# Copia los archivos estáticos al directorio público de Nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copia configuración personalizada si la tenés
# COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

