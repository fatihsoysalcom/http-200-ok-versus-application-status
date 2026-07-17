# HTTP 200 OK Versus Application Status

This example demonstrates how an HTTP 200 OK status from a server does not always guarantee a successful outcome from the application's perspective. It runs a simple Python HTTP server that consistently returns a 200 OK status, yet the JSON payload within the response varies to indicate application-level success, warning, or error states. This illustrates the critical distinction between a technical HTTP success and a user/business success.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run `python main.py` in your terminal.
3. Open your browser or use `curl` to visit `http://localhost:8000/api/data` multiple times and observe the JSON responses.

## Original Article

This example accompanies the Turkish article: [HTTP 200 Durumu: Sunucunun 'Başarılı' Yanıtı Gerçekten Her Şeyin Yolunda Olduğu Anlamına Gelir mi?](https://fatihsoysal.com/blog/http-200-durumu-sunucunun-basarili-yaniti-gercekten-her-seyin-yolunda-oldugu-anlamina-gelir-mi/).

## License

MIT — see [LICENSE](LICENSE).
