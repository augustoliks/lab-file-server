FROM golang:1.17.0-alpine
WORKDIR /app
ADD main.go .
RUN go build main.go
CMD [ "./main" ]
