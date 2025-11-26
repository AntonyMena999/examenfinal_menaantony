build:
	docker build -t miapp:latest .

run:
	docker run -p 5000:5000 miapp:latest
