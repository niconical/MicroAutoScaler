#
#nohup python3 workload_manager.py >/dev/null 2>&1 &
# The -a means address of API server, 0.0.0.0 is necessary, or server can't be accessed outside.

while true
do
    echo "开始发送流量"
    nohup locust -f ./load_generator_boutique.py --headless > ./logs/sendFlow.log 2>&1 &
    wait
    echo "结束流量"
done
# while true
# do
#     echo "开始发送流量"
#     nohup locust -f ./load_generator_train.py --headless > .logs/sendFlow.log2 2>&1 &
#     wait
#     echo "结束流量"
# done
