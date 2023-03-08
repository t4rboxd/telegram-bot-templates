<?php
require_once __DIR__ . '/vendor/autoload.php';

$config = json_decode(file_get_contents(__DIR__ . '/config.json'), true);

// create an instance of the bot
$bot = new \TelegramBot\Api\Client($config['token']);

// define an example command
function hello($message) {
  global $bot;
  $bot->sendMessage($message->getChat()->getId(), "Hello " . $message->getFrom()->getFirstName());
}

$bot->command('start', function($message) {
  hello($message);
});

$bot->run();
