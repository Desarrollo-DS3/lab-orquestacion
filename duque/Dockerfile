FROM node:14

WORKDIR /app

COPY . .

RUN npm init -y
RUN npm install express

EXPOSE 80

CMD ["node", "duque.js"]