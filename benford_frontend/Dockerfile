FROM node:14.5.0-alpine as builder
RUN mkdir /app
WORKDIR /app
COPY benford/package.json benford/package-lock.json /app/benford/
RUN npm install --prefix benford
COPY . /app
RUN npm run build --prefix benford -- --output-path=./dist/out

FROM nginx:1.15.7-alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/benford/dist/out /usr/share/nginx/html
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
