# docker run -d --name mykinesis -p 4567:4567 instructure/kinesalite
docker start -a mykinesis
python3 ../python/producer.py