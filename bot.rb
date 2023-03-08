require 'telegram/bot'
require 'json'

# parse config.json
config = JSON.parse(File.read('config.json'))

# define an example command
def hello(message)
  Telegram::Bot::Client.run(config['token']) do |bot|
    bot.api.send_message(chat_id: message.chat.id, text: "Hello #{message.from.first_name}")
  end
end

# start the bot
Telegram::Bot::Client.run(config['token']) do |bot|
  bot.listen do |message|
    case message.text
    when '/start'
      hello(message)
    end
  end
end
