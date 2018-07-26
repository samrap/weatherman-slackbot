# Weatherman Slackbot

A Slackbot for retrieving weather information.

This bot uses [Spacy](https://spacy.io) for natural language processing and [OpenWeatherMap](https://openweathermap.org) for retrieving weather information.

NLP is used to determine the location the user wants weather information for, as well as determining if they are looking for current weather or a forecast. It allows the user to speak to the weatherman naturally, rather than requiring a specifically formatted message.

This bot uses the `en_core_web_lg` Spacy dataset.

**Note:** This is experimental

## Examples

![](https://raw.githubusercontent.com/samrap/assets/master/weatherman-slackbot/example.gif)

## Roadmap

- [x] Respond to basic weather and temperature queries
- [ ] Respond to a forecast request
- [ ] Respond to requests for weather at a future date or time
