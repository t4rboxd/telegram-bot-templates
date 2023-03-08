const TelegramBot = require('node-telegram-bot-api');
const { token } = require('./config.json');

// create a new bot instance
const bot = new TelegramBot(token, { polling: true });

// define an example command
bot.onText(/\/start/, (msg, match) => {
  const chatId = msg.chat.id;
  const firstName = msg.from.first_name;
  bot.sendMessage(chatId, `Hello ${firstName}`);
});
