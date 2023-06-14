Local Setup

docker run -d --name mykinesis -p 4567:4567 instructure/kinesalite

pip install awscli-local

awslocal kinesis create-stream --stream-name test_stream --shard-count 1 --endpoint-url http://localhost:4567

awslocal kinesis put-record --stream-name test_stream --partition-key samplepartitionkey --data sampledatarecord --endpoint-url http://localhost:4567/
