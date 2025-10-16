```http
  GET https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ua
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
| `appid`   | `string` | **Required**. Your OpenWeather API key   |
| `q`       | `string` | **Required**. City name (e.g., Kyiv)     |
| `units`   | `string` | Optional. Measurement units (`metric`)   |
| `lang`    | `string` | Optional. Language of description (`ua`) |
